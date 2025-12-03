#!/usr/bin/env python3
import argparse
import logging
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

try:
    from openai import OpenAI
except Exception as exc:  # pragma: no cover
    print("ERROR: openai package is not installed. Please run: pip install -r tools/llm-translator/requirements.txt", file=sys.stderr)
    raise


# Environment configuration (matches provided example)
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-oss")
PROFESSIONALIZE_API_URL = os.getenv("PROFESSIONALIZE_API_URL", "https://llm.professionalize.com/v1")
AI_API_KEY = os.getenv("PROFESSIONALIZE_API_KEY")

_client = None


def get_client() -> OpenAI:
    global _client
    if _client is None:
        if not AI_API_KEY:
            print("ERROR: PROFESSIONALIZE_API_KEY environment variable is not set.", file=sys.stderr)
            sys.exit(2)
        _client = OpenAI(api_key=AI_API_KEY, base_url=PROFESSIONALIZE_API_URL)
    return _client


# Language code to human-readable language for prompts
LANG_CODE_TO_NAME: Dict[str, str] = {
    "en": "English",
    "de": "German",
    "es": "Spanish",
    "fa": "Persian",
    "fr": "French",
    "id": "Indonesian",
    "it": "Italian",
    "ja": "Japanese",
    "ko": "Korean",
    "pt": "Portuguese",
    "ru": "Russian",
    "th": "Thai",
    "uk": "Ukrainian",
    "vi": "Vietnamese",
    "zh": "Chinese",
}


def read_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: Path, data: Dict[str, Any]) -> None:
    # Use 2-space indent to match existing localized files
    text = json.dumps(data, ensure_ascii=False, indent=2)
    # Ensure trailing newline
    if not text.endswith("\n"):
        text += "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        f.write(text)


def is_leaf_value(value: Any) -> bool:
    return isinstance(value, str)


def flatten(obj: Dict[str, Any], parent_key: str = "") -> Dict[str, str]:
    flat: Dict[str, str] = {}
    for k, v in obj.items():
        key_path = f"{parent_key}.{k}" if parent_key else k
        if isinstance(v, dict):
            flat.update(flatten(v, key_path))
        elif is_leaf_value(v):
            flat[key_path] = v
        else:
            # Non-string leafs are skipped
            pass
    return flat


def unflatten(flat: Dict[str, str]) -> Dict[str, Any]:
    root: Dict[str, Any] = {}
    for dotted_key, value in flat.items():
        parts = dotted_key.split(".")
        cur = root
        for part in parts[:-1]:
            if part not in cur or not isinstance(cur[part], dict):
                cur[part] = {}
            cur = cur[part]
        cur[parts[-1]] = value
    return root


def merge_preserving_structure(base_structure: Dict[str, Any], current: Dict[str, Any]) -> Dict[str, Any]:
    # Rebuild a nested dict shaped like base_structure, filling from current when available
    def _merge(b: Any, c: Any) -> Any:
        if isinstance(b, dict):
            out: Dict[str, Any] = {}
            for k, v in b.items():
                out[k] = _merge(v, (c or {}).get(k) if isinstance(c, dict) else None)
            return out
        return c if c is not None else b

    return _merge(base_structure, current)


def strip_code_fences(s: str) -> str:
    # Remove surrounding ```json ... ``` or ``` ... ``` fences if present
    fence_re = re.compile(r"^```[a-zA-Z]*\n([\s\S]*?)\n```\s*$", re.MULTILINE)
    m = fence_re.match(s.strip())
    if m:
        return m.group(1).strip()
    return s


def load_context_file(start_from: Path) -> Optional[str]:
    # Look for scripts/translation_context.md starting from the source path upwards
    for ancestor in [start_from] + list(start_from.parents):
        candidate = ancestor / "scripts" / "translation_context.md"
        if candidate.exists() and candidate.is_file():
            try:
                return candidate.read_text(encoding="utf-8")
            except Exception:
                return None
    return None


def translate_batch(pairs: Dict[str, str], target_lang_code: str, project_context: Optional[str], retries: int = 2) -> Dict[str, str]:
    if not pairs:
        return {}

    target_lang_name = LANG_CODE_TO_NAME.get(target_lang_code, target_lang_code)

    # Build a compact JSON payload for the model
    payload = json.dumps(pairs, ensure_ascii=False)

    system_msg = (
        "You are a professional technical translator for software localization. "
        "Use the provided project context to resolve domain-specific terminology and product names. "
        "Translate the provided JSON values into the target language while strictly preserving: "
        "- placeholders like {0}, {name}, {link} "
        "- markdown links [text](url) (keep URL intact) "
        "- inline/backtick code, HTML tags like <br>, and HTML entities like &nbsp; "
        "- product and brand names such as GroupDocs, GroupDocs.Total (do not translate) "
        "Return a pure JSON object with the same keys and translated string values only. "
        "Do not add extra keys, comments, explanations, or formatting."
    )

    context_section = f"\n\nProject context:\n{project_context}" if project_context else ""

    user_msg = (
        f"Target language: {target_lang_name}.{context_section}\n\n"
        f"JSON to translate (values only):\n{payload}"
    )

    client = get_client()

    # Prefer Responses API; fall back to Chat Completions if unavailable
    translated_map: Dict[str, str] = {}
    last_error: Optional[Exception] = None
    for attempt in range(1, max(1, retries) + 1):
        response_text: str = ""
        try:
            logging.debug("Attempt %d: responses.create for %d keys", attempt, len(pairs))
            t0 = time.time()
            resp = client.responses.create(
                model=MODEL_NAME,
                input=[
                    {"role": "system", "content": system_msg},
                    {"role": "user", "content": user_msg},
                ],
            )
            dt = time.time() - t0
            logging.info("LLM responses.create completed in %.2fs", dt)
            # openai>=1.44 has output_text; otherwise extract best-effort
            response_text = getattr(resp, "output_text", None) or json.dumps(resp.model_dump(), ensure_ascii=False)
            if not getattr(resp, "output_text", None):
                try:
                    out = resp.model_dump()
                    candidates = []
                    for item in out.get("output", []):
                        for c in item.get("content", []):
                            if c.get("type") == "output_text" and c.get("text"):
                                candidates.append(c.get("text"))
                    if candidates:
                        response_text = candidates[0]
                except Exception:
                    pass
        except Exception as exc:
            logging.warning("responses.create failed on attempt %d: %s", attempt, exc)
            last_error = exc
        if not response_text and last_error is None:
            # Unexpected empty response without exception — try chat fallback
            try:
                logging.debug("Attempt %d: chat.completions.create fallback", attempt)
                t0 = time.time()
                chat = client.chat.completions.create(
                    model=MODEL_NAME,
                    messages=[
                        {"role": "system", "content": system_msg},
                        {"role": "user", "content": user_msg},
                    ],
                    temperature=0.2,
                )
                dt = time.time() - t0
                logging.info("LLM chat.completions.create completed in %.2fs", dt)
                response_text = chat.choices[0].message.content or ""
            except Exception as exc:
                logging.warning("chat.completions.create failed on attempt %d: %s", attempt, exc)
                last_error = exc

        if response_text:
            cleaned = strip_code_fences(response_text)
            try:
                translated_map = json.loads(cleaned)
                break
            except Exception as exc:
                logging.warning("Model returned non-JSON on attempt %d; will retry.", attempt)
                last_error = exc

        if attempt < max(1, retries):
            sleep_s = min(8, 2 ** attempt)
            logging.info("Retrying in %ds...", sleep_s)
            time.sleep(sleep_s)

    if not translated_map:
        # Surface the last error with context
        if last_error is not None:
            raise RuntimeError("LLM translation failed after retries") from last_error
        raise RuntimeError("LLM translation failed with empty response after retries")

    # Ensure only requested keys are present
    return {k: str(v) for k, v in translated_map.items() if k in pairs}


def batch_items(d: Dict[str, str], size: int) -> List[Dict[str, str]]:
    items = list(d.items())
    batches: List[Dict[str, str]] = []
    for i in range(0, len(items), size):
        batch = dict(items[i : i + size])
        batches.append(batch)
    return batches


def build_target_structure(
    english: Dict[str, Any],
    existing_target: Dict[str, Any],
    updates: Dict[str, str],
) -> Dict[str, Any]:
    # Start from existing target; overlay updates; ensure it follows english structure
    target_flat = flatten(existing_target) if existing_target else {}
    target_flat.update(updates)
    target_nest = unflatten(target_flat)
    # Align to english structure (preserve key order/shape where possible)
    return merge_preserving_structure(english, target_nest)


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(description="LLM-based JSON translator (drop-in for Res.Translator.exe)")
    parser.add_argument("-r", "--resource", required=True, help="Path to source English JSON (e.g., templates/data/index/en.json)")
    parser.add_argument("-d", "--dest", required=True, help="Destination language code (e.g., de, es, fr, ...)")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing translations instead of filling only missing keys")
    parser.add_argument("--batch-size", type=int, default=30, help="Number of entries per LLM request batch")
    parser.add_argument("-c", "--context", help="Path to a translation context file (markdown/text). Overrides auto-detection.")
    parser.add_argument("--retries", type=int, default=2, help="Retries per LLM request on failure (default 2)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose logging")

    args = parser.parse_args(argv)

    # Logging setup
    logging.basicConfig(level=(logging.DEBUG if args.verbose else logging.INFO), format='[%(levelname)s] %(message)s')

    source_path = Path(args.resource).resolve()
    if not source_path.exists():
        logging.error("Source file not found: %s", source_path)
        return 2

    try:
        english_data = read_json(source_path)
    except Exception as exc:
        logging.error("Failed to read or parse JSON: %s: %s", source_path, exc)
        return 2

    target_lang = args.dest.lower()
    out_path = source_path.parent / f"{target_lang}.json"
    logging.info("Starting translation: src=%s -> lang=%s, output=%s", source_path, target_lang, out_path)
    logging.info("Options: overwrite=%s, batch_size=%d, retries=%d, verbose=%s", args.overwrite, args.batch_size, args.retries, args.verbose)

    # If dest is English, just write English out (copy behavior)
    if target_lang == "en":
        write_json(out_path, english_data)
        print(f"Wrote {out_path}")
        return 0

    # Load existing target translations if present
    existing_target: Dict[str, Any] = {}
    if out_path.exists() and not args.overwrite:
        try:
            existing_target = read_json(out_path)
        except Exception:
            existing_target = {}

    # Load optional project context (explicit path takes precedence; otherwise auto-detect scripts/translation_context.md)
    project_context: Optional[str] = None
    if args.context:
        context_path = Path(args.context).resolve()
        if not context_path.exists():
            logging.error("Context file not found: %s", context_path)
            return 2
        try:
            project_context = context_path.read_text(encoding="utf-8")
        except Exception as exc:
            logging.error("Failed to read context file: %s: %s", context_path, exc)
            return 2
    else:
        project_context = load_context_file(source_path)
    if project_context:
        logging.info("Using translation context (length=%d chars)", len(project_context))
    else:
        logging.info("No translation context provided or detected.")

    english_flat = flatten(english_data)
    target_flat_existing = flatten(existing_target) if existing_target else {}

    # Determine which keys require translation
    to_translate: Dict[str, str] = {}
    if args.overwrite:
        to_translate = english_flat.copy()
    else:
        for k, v in english_flat.items():
            if k not in target_flat_existing or target_flat_existing.get(k) in (None, ""):
                to_translate[k] = v
    logging.info("English keys: %d, already translated: %d, to translate: %d", len(english_flat), len(target_flat_existing), len(to_translate))

    if not to_translate:
        # Nothing to do; still write to ensure structure alignment
        final = build_target_structure(english_data, existing_target, {})
        write_json(out_path, final)
        print(f"Up-to-date: {out_path}")
        return 0

    # Process in batches
    updates: Dict[str, str] = {}
    batches = batch_items(to_translate, args.batch_size)
    total_batches = len(batches)
    for idx, batch in enumerate(batches, start=1):
        logging.info("Batch %d/%d: translating %d keys...", idx, total_batches, len(batch))
        t0 = time.time()
        translated_map = translate_batch(batch, target_lang, project_context, retries=args.retries)
        dt = time.time() - t0
        logging.info("Batch %d/%d completed in %.2fs", idx, total_batches, dt)
        # Basic sanity: ensure all keys returned
        missing = [k for k in batch.keys() if k not in translated_map]
        if missing:
            print(f"WARNING: Model response missing {len(missing)} keys; reusing English for those.")
            for m in missing:
                translated_map[m] = batch[m]
        updates.update(translated_map)

    final = build_target_structure(english_data, existing_target, updates)
    write_json(out_path, final)
    logging.info("Wrote %s", out_path)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))


