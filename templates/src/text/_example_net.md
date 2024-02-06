// <% "{steps.code.header}" %>
        // <% "{steps.code.instance}" %>
        using (Parser parser = new Parser(filePath)) {
            // <% "{steps.code.extract}" %>
            using (TextReader reader = parser.GetText()) {
                // <% "{steps.code.print_1}" %>
                // <% "{steps.code.print_2}" %>
                Console.WriteLine(reader == null ? "<% "{steps.code.not_supported}" %>" : reader.ReadToEnd());
            }
        }