HugoMarkupGenerator\Bin\net6.0\MarkupGenerator.Shell.exe -s ..\src\text -o ..\..\content\parser\

ren "..\..\content\parser\net\extract\text\*.en*" "*."
copy "..\..\content\parser\net\extract\text\*.en" "..\..\content\parser\net\extract\text\*.md"
del  "..\..\content\parser\net\extract\text\*.en"

ren "..\..\content\parser\java\extract\text\*.en*" "*."
copy "..\..\content\parser\java\extract\text\*.en" "..\..\content\parser\java\extract\text\*.md"
del "..\..\content\parser\java\extract\text\*.en"