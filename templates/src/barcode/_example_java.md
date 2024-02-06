// <% "{steps.code.header}" %>
        // <% "{steps.code.instance}" %>
        try (Parser parser = new Parser(Constants.SamplePdfWithBarcodes)) {
            // // <% "{steps.code.check}" %>
            if (!parser.getFeatures().isBarcodes()) {
                System.out.println("<% "{steps.code.not_supported}" %>");
                return;
            }

            // <% "{steps.code.scan}" %>
            Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();

            // <% "{steps.code.iterate}" %>
            for (PageBarcodeArea barcode : barcodes) {
                // <% "{steps.code.print_page_index}" %>
                System.out.println("Page: " + barcode.getPage().getIndex());
                // <% "{steps.code.print_value}" %>
                System.out.println("Value: " + barcode.getValue());
            }
        }