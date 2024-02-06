// <% "{steps.code.header}" %>
        // <% "{steps.code.instance}" %>
        using (Parser parser = new Parser(filePath)) {
            // <% "{steps.code.check}" %>
            if (!parser.Features.Tables) {
                Console.WriteLine("<% "{steps.code.not_supported}" %>");
                return;
            }
            // <% "{steps.code.layout}" %>
            TemplateTableLayout layout = new TemplateTableLayout(
                new double[] { 50, 95, 275, 415, 485, 545 },
                new double[] { 325, 340, 365, 395 });
            // <% "{steps.code.options}" %>
            PageTableAreaOptions options = new PageTableAreaOptions(layout);
            // <% "{steps.code.extract}" %>
            IEnumerable<PageTableArea> tables = parser.GetTables(options);
            // <% "{steps.code.iterate}" %>
            foreach (PageTableArea t in tables) {
                // <% "{steps.code.iterate_rows}" %>
                for (int row = 0; row < t.RowCount; row++) {
                    // <% "{steps.code.iterate_columns}" %>
                    for (int column = 0; column < t.ColumnCount; column++) {
                        // <% "{steps.code.cell}" %>
                        PageTableAreaCell cell = t[row, column];
                        if (cell != null) {
                            // <% "{steps.code.print_cell}" %>
                            Console.Write(cell.Text);
                            Console.Write(" | ");
                        }
                    }
                    Console.WriteLine();
                }
                Console.WriteLine();
            }
        }