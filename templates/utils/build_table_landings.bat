HugoMarkupGenerator\Bin\net6.0\MarkupGenerator.Shell.exe -s ..\src\table -o ..\..\content\parser\

ren "..\..\content\parser\net\extract\table\*.en*" "*."
copy "..\..\content\parser\net\extract\table\*.en" "..\..\content\parser\net\extract\table\*.md"
del  "..\..\content\parser\net\extract\table\*.en"

ren "..\..\content\parser\java\extract\table\*.en*" "*."
copy "..\..\content\parser\java\extract\table\*.en" "..\..\content\parser\java\extract\table\*.md"
del "..\..\content\parser\java\extract\table\*.en"