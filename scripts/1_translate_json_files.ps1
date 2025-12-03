# Full locales list without `en`
$languages = 'de', 'es', 'fa', 'fr', 'id', 'it', 'ja', 'ko', 'pt', 'ru', 'th', 'uk', 'vi', 'zh'

$operations =  'index'
#$operations =  'convert-format'
#$operations =  'index', 'convert-format'

#==============================================

# Ensure Python virtual environment exists and dependencies are installed (Windows-friendly)
$venvDir = '.\.venv'
$venvPython = Join-Path $venvDir 'Scripts\python.exe'
$requirements = '.\tools\llm-translator\requirements.txt'

if (!(Test-Path $venvPython)) {
    Write-Host "Creating Python virtual environment in $venvDir ..."
    $pyLauncher = Get-Command py -ErrorAction SilentlyContinue
    $pythonCmd = Get-Command python -ErrorAction SilentlyContinue

    if ($pyLauncher) {
        & py -3 -m venv $venvDir
    } elseif ($pythonCmd) {
        & python -m venv $venvDir
    } else {
        Write-Error 'Python not found. Please install Python 3.x and ensure "py" or "python" is in PATH.'
        exit 1
    }

    if ($LASTEXITCODE -ne 0 -or !(Test-Path $venvPython)) {
        Write-Error 'Failed to create virtual environment.'
        exit 1
    }
}

Write-Host 'Upgrading pip and installing dependencies...'
& $venvPython -m pip install --upgrade pip
if ($LASTEXITCODE -ne 0) { Write-Error 'Failed to upgrade pip.'; exit 1 }

& $venvPython -m pip install -r $requirements
if ($LASTEXITCODE -ne 0) { Write-Error "Failed to install dependencies from $requirements."; exit 1 }

Foreach ($cur_language in $languages) { 
    Foreach ($cur_operation in $operations) { 
        $cur_operation  

        # Prepare
        $source_path = '.\templates\data\' + $cur_operation + '\en.json';
        $translated_path = '.\templates\data\' + $cur_operation + '\en.' + $cur_language + '.json';
        $result_path = '.\templates\data\' + $cur_operation + '\' + $cur_language + '.json';

        # Translate using venv Python
        & $venvPython ./tools/llm-translator/llm-translator.py -r $source_path -d $cur_language -c ./scripts/translation_context.md
    }
}
