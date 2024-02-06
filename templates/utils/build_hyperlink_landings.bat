HugoMarkupGenerator\Bin\net6.0\MarkupGenerator.Shell.exe -s ..\src\hyperlink -o ..\..\content\parser\

ren "..\..\content\parser\net\extract\hyperlink\*.en*" "*."
copy "..\..\content\parser\net\extract\hyperlink\*.en" "..\..\content\parser\net\extract\hyperlink\*.md"
del  "..\..\content\parser\net\extract\hyperlink\*.en"

ren "..\..\content\parser\java\extract\hyperlink\*.en*" "*."
copy "..\..\content\parser\java\extract\hyperlink\*.en" "..\..\content\parser\java\extract\hyperlink\*.md"
del "..\..\content\parser\java\extract\hyperlink\*.en"

:: COPY HYPERLINKS TO "OLD" FOLDERS 

copy "..\..\content\parser\net\extract\hyperlink\*.md" "..\..\content\parser\net\extract\*.md"
copy "..\..\content\parser\net\extract\hyperlink\*.md" "..\..\content\parser\net\*.md"
copy "..\..\content\parser\java\extract\hyperlink\*.md" "..\..\content\parser\java\extract\*.md"
copy "..\..\content\parser\java\extract\hyperlink\*.md" "..\..\content\parser\java\*.md"