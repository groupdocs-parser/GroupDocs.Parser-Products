HugoMarkupGenerator\Bin\net6.0\MarkupGenerator.Shell.exe -s ..\src\barcode -o ..\..\content\parser\

ren "..\..\content\parser\net\extract\barcode\*.en*" "*."
copy "..\..\content\parser\net\extract\barcode\*.en" "..\..\content\parser\net\extract\barcode\*.md"
del  "..\..\content\parser\net\extract\barcode\*.en"

ren "..\..\content\parser\java\extract\barcode\*.en*" "*."
copy "..\..\content\parser\java\extract\barcode\*.en" "..\..\content\parser\java\extract\barcode\*.md"
del "..\..\content\parser\java\extract\barcode\*.en"