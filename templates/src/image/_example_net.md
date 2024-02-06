// <% "{steps.code.header}" %>
        // <% "{steps.code.instance}" %>
        using (Parser parser = new Parser(filePath)) {
            // <% "{steps.code.extract}" %>
            IEnumerable<PageImageArea> images = parser.GetImages();
            // <% "{steps.code.check_null}" %>
            if (images == null) {
                Console.WriteLine("<% "{steps.code.not_supported}" %>");
                return;
            }
            // <% "{steps.code.iterate}" %>
            foreach (PageImageArea image in images) {
                // <% "{steps.code.print}" %>
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Type: {2}", image.Page.Index, image.Rectangle, image.FileType));
            }
        }