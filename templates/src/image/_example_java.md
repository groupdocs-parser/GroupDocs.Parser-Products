// <% "{steps.code.header}" %>
        // <% "{steps.code.instance}" %>
        try (Parser parser = new Parser(Constants.SampleImagesPdf)) {
            // <% "{steps.code.extract}" %>
            Iterable<PageImageArea> images = parser.getImages();
            // <% "{steps.code.check_null}" %>
            if (images == null) {
                System.out.println("<% "{steps.code.not_supported}" %>");
                return;
            }
            // <% "{steps.code.iterate}" %>
            for (PageImageArea image : images) {
                // <% "{steps.code.print}" %>
                System.out.println(String.format("Page: %d, R: %s, Type: %s", image.getPage().getIndex(), image.getRectangle(), image.getFileType()));
            }
        }