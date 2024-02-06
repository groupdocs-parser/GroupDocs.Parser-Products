// <% "{steps.code.header}" %>
        // <% "{steps.code.instance}" %>
        try (Parser parser = new Parser(Constants.HyperlinksPdf)) {
            // <% "{steps.code.check}" %>
            if (!parser.getFeatures().isHyperlinks()) {
                System.out.println("<% "{steps.code.not_supported}" %>");
                return;
            }
            // <% "{steps.code.extract}" %>
            Iterable<PageHyperlinkArea> hyperlinks = parser.getHyperlinks();
            // <% "{steps.code.iterate}" %>
            for (PageHyperlinkArea h : hyperlinks) {
                // <% "{steps.code.print_text}" %>
                System.out.println(h.getText());
                // <% "{steps.code.print_url}" %>
                System.out.println(h.getUrl());
                System.out.println();
            }
        }