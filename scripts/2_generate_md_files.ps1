$sources_path = "./templates/src"
$output_path =  "./content"

# cleanup
Remove-Item -LiteralPath $output_path -Force -Recurse -ErrorAction Ignore

# run generator
.\tools\generator\MarkupGenerator.Shell.exe -s $sources_path -o $output_path