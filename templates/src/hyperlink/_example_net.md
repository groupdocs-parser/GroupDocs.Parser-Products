// <% "{steps.code.header}" %>
        // <% "{steps.code.instance}" %>
        using (Parser parser = new Parser(filePath)) {
            // <% "{steps.code.check}" %>
            if (!parser.Features.Hyperlinks) {
                Console.WriteLine("<% "{steps.code.not_supported}" %>");
                return;
            }
            // <% "{steps.code.extract}" %>
            IEnumerable<PageHyperlinkArea> hyperlinks = parser.GetHyperlinks();
            // <% "{steps.code.iterate}" %>
            foreach (PageHyperlinkArea h in hyperlinks) {
                // <% "{steps.code.print_text}" %>
                Console.WriteLine(h.Text);
                // <% "{steps.code.print_url}" %>
                Console.WriteLine(h.Url);
                Console.WriteLine();
            }
        }