// <% "{steps.code.header}" %>
        // <% "{steps.code.instance}" %>
        using (Parser parser = new Parser(Constants.SamplePdfWithBarcodes)) {
            // <% "{steps.code.check}" %>
            if (!parser.Features.Barcodes) {
                Console.WriteLine("<% "{steps.code.not_supported}" %>");
                return;
            }

            // <% "{steps.code.scan}" %>
            IEnumerable<PageBarcodeArea> barcodes = parser.GetBarcodes();

            // <% "{steps.code.iterate}" %>
            foreach (PageBarcodeArea barcode in barcodes) {
                // <% "{steps.code.print_page_index}" %>
                Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                // <% "{steps.code.print_value}" %>
                Console.WriteLine("Value: " + barcode.Value);
            }
        }