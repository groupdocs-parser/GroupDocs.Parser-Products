HugoMarkupGenerator\Bin\net6.0\MarkupGenerator.Shell.exe -s ..\src\parse -o ..\..\content\parser\

ren "..\..\content\parser\net\parse\*.en*" "*."
copy "..\..\content\parser\net\parse\*.en" "..\..\content\parser\net\parse\*.md"
del  "..\..\content\parser\net\parse\*.en"

ren "..\..\content\parser\java\parse\*.en*" "*."
copy "..\..\content\parser\java\parse\*.en" "..\..\content\parser\java\parse\*.md"
del "..\..\content\parser\java\parse\*.en"