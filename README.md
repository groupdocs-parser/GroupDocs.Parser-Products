# GroupDocs.Parser - Product Pages 

![Copy Content Status](https://github.com/groupdocs-parser/GroupDocs.Parser-Products/actions/workflows/copy_content.yml/badge.svg)

This repository contains templates, configs for GroupDocs.Parser product pages. It also includes tools to translate strings in Json files and generate final Markdown files.

## Scripts

* [1_translate_json_files.ps1](scripts/1_translate_json_files.ps1) - translated json files, uses [translation_context.md](scripts/translation_context.md) to pass context to LLM
* [2_generate_md_files.ps1](scripts/2_generate_md_files.ps1) - generate final markdown files 

## Tools

* [LLM translator](tools/llm-translator/)
* [Markdown generator](tools/generator/)

## Running Hugo

Make sure to checkout `common` submodule by running

```bash
git submodule update --init --recursive
```

Navigate to the `common` directory

```bash
cd common
```

Run Hugo

```bash
hugo server --config "./config-production.toml" --contentDir ../content --disableFastRender
```
