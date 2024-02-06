HugoMarkupGenerator\Bin\net6.0\MarkupGenerator.Shell.exe -s ..\src\image -o ..\..\content\parser\

ren "..\..\content\parser\net\extract\image\*.en*" "*."
copy "..\..\content\parser\net\extract\image\*.en" "..\..\content\parser\net\extract\image\*.md"
del  "..\..\content\parser\net\extract\image\*.en"

ren "..\..\content\parser\java\extract\image\*.en*" "*."
copy "..\..\content\parser\java\extract\image\*.en" "..\..\content\parser\java\extract\image\*.md"
del "..\..\content\parser\java\extract\image\*.en"