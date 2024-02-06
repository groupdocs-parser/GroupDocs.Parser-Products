HugoMarkupGenerator\Bin\net6.0\MarkupGenerator.Shell.exe -s ..\src\extract -o ..\..\content\parser

ren "..\..\content\parser\net\extract\*.en*" "*."
copy "..\..\content\parser\net\extract\*.en" "..\..\content\parser\net\extract\*.md"
del  "..\..\content\parser\net\extract\*.en"

ren "..\..\content\parser\java\extract\*.en*" "*."
copy "..\..\content\parser\java\extract\*.en" "..\..\content\parser\java\extract\*.md"
del "..\..\content\parser\java\extract\*.en"