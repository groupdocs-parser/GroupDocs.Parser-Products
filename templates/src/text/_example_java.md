// <% "{steps.code.header}" %>
        // <% "{steps.code.instance}" %>
        try (Parser parser = new Parser(filePath)) {
            // <% "{steps.code.extract}" %>
            try (TextReader reader = parser.getText()) {
                // <% "{steps.code.print_1}" %>
                // <% "{steps.code.print_2}" %>
                System.out.println(reader == null ? "<% "{steps.code.not_supported}" %>" : reader.readToEnd());
            }
        }