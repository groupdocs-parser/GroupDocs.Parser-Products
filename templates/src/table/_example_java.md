// <% "{steps.code.header}" %>
        // <% "{steps.code.instance}" %>
        try (Parser parser = new Parser(Constants.SampleInvoicePagesPdf)) {
            // <% "{steps.code.check}" %>
            if (!parser.getFeatures().isTables()) {
                System.out.println("<% "{steps.code.not_supported}" %>");
                return;
            }
            // <% "{steps.code.layout}" %>
            TemplateTableLayout layout = new TemplateTableLayout(
                    java.util.Arrays.asList(new Double[]{50.0, 95.0, 275.0, 415.0, 485.0, 545.0}),
                    java.util.Arrays.asList(new Double[]{325.0, 340.0, 365.0, 395.0}));
            // <% "{steps.code.options}" %>
            PageTableAreaOptions options = new PageTableAreaOptions(layout);
            // <% "{steps.code.extract}" %>
            Iterable<PageTableArea> tables = parser.getTables(options);
            // <% "{steps.code.iterate}" %>
            for (PageTableArea t : tables) {
                // <% "{steps.code.iterate_rows}" %>
                for (int row = 0; row < t.getRowCount(); row++) {
                    // <% "{steps.code.iterate_columns}" %>
                    for (int column = 0; column < t.getColumnCount(); column++) {
                        // <% "{steps.code.cell}" %>
                        PageTableAreaCell cell = t.getCell(row, column);
                        if (cell != null) {
                            // <% "{steps.code.print_cell}" %>
                            System.out.print(cell.getText());
                            System.out.print(" | ");
                        }
                    }
                    System.out.println();
                }
                System.out.println();
            }
        }