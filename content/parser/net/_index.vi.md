---
############################# Static ############################
layout: "landing"
date: 2025-06-30T10:26:00
draft: false

lang: vi
product: "Parser"
product_tag: "parser"
platform: "Net"
platform_tag: "net"

############################# Drop-down ############################
supported_platforms:
  items:
    # supported_platforms loop
    - title: ".NET"
      tag: "net"
    # supported_platforms loop
    - title: "Java"
      tag: "java"

############################# Head ############################
head_title: "GroupDocs.Parser for .NET Ứng dụng phân tích tài liệu"
head_description: "Giải pháp phân tích tài liệu toàn diện cho các ứng dụng .NET. Trích xuất dữ liệu từ các định dạng tài liệu trực tuyến bằng tính năng kéo và thả đơn giản."

############################# Header ############################
title: "Phân tích tài liệu qua API .NET"
description: "Trích xuất dữ liệu từ tài liệu và hình ảnh trên bất kỳ nền tảng nào bằng cách sử dụng API linh hoạt và giải pháp ứng dụng dựa trên lập trình cho các lập trình viên và người dùng cuối."
words:
  for: "cho"

actions:
  main: "Tải xuống từ Nuget"
  main_link: "https://www.nuget.org/packages/GroupDocs.Parser"
  alt: "Cấp phép"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/net/"
  title: "Sẵn sàng bắt đầu?"
  description: "Cố gắng sử dụng các tính năng của GroupDocs.Parser miễn phí hoặc yêu cầu giấy phép"

release:
  title: "Phiên bản {0} đã được phát hành"
  notes: "Xem những điểm mới"
  downloads: "Tải xuống"

code:
  title: "Nhanh chóng phân tích nội dung tài liệu"
  more: "Nhiều ví dụ hơn"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
  install: "dotnet add package GroupDocs.Parser"
  content: |
    ```csharp {style=abap}   
    // Truyền tệp nguồn cho đối tượng Parser
    using (var parser = new Parser("source.pdf"))
    {
        // Truyền văn bản tài liệu cho TextReader
        using (var textReader = parser.GetText())
        {
            // Xử lý văn bản tài liệu
            Console.WriteLine(textReader?.ReadToEnd());
        }
    }  
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser trong cái nhìn tổng quan"
  description: "API để thực hiện phân tích tài liệu trong các ứng dụng .NET"
  features:
    # feature loop
    - title: "Trích xuất dữ liệu từ tài liệu"
      content: "API GroupDocs.Parser for .NET cho phép bạn lấy văn bản, siêu dữ liệu và hình ảnh từ nhiều định dạng tệp như tài liệu Office, email, tệp đính kèm và lưu trữ. Công cụ mạnh mẽ này giúp bạn truy cập và xử lý thông tin giá trị nằm trong các tệp này một cách hiệu quả cho nhiều ứng dụng như phân tích dữ liệu, lập chỉ mục công cụ tìm kiếm, hoặc hệ thống quản lý nội dung."

    # feature loop
    - title: "Phân tích tài liệu"
      content: "Trích xuất các yếu tố khác nhau như siêu liên kết, bảng, mã QR, mã vạch và dữ liệu từ biểu mẫu PDF. Đồng thời phân tích bất kỳ thông tin nào mong muốn từ tài liệu bằng cách sử dụng các mẫu tùy chỉnh."

    # feature loop
    - title: "Tùy chỉnh kết quả"
      content: "API .NET cho phép bạn truy xuất dữ liệu ở nhiều định dạng khác nhau như thô, cấu trúc, HTML hoặc Markdown. Ngoài ra, API còn cung cấp chức năng tìm kiếm để xác định các từ hoặc cụm từ cụ thể trong văn bản của tài liệu."

############################# Platforms ############################
platforms:
  enable: true
  title: "Tính độc lập của nền tảng"
  description: "GroupDocs.Parser for .NET hỗ trợ các hệ điều hành, khung làm việc và trình quản lý gói sau"
  items:
    # platform loop
    - title: "Amazon"
      image: "amazon"
    # platform loop
    - title: "Docker"
      image: "docker"
    # platform loop
    - title: "Azure"
      image: "azure"
    # platform loop
    - title: "VS Code"
      image: "vs_code"
    # platform loop
    - title: "ReSharper"
      image: "resharper"
    # platform loop
    - title: "macOS"
      image: "finder"
    # platform loop
    - title: "Linux"
      image: "linux"
    # platform loop
    - title: "NuGet"
      image: "nuget"

############################# File formats ############################
formats:
  enable: true
  title: "Các định dạng tệp được hỗ trợ"
  description: |
    GroupDocs.Parser for .NET hỗ trợ các thao tác với [các định dạng tệp](https://docs.groupdocs.com/parser/net/supported-document-formats/) sau.
  groups:
    # group loop
    - color: "green"
      content: |
        ### Định dạng Microsoft Office
        * **Word:** DOCX, DOC, DOCM, DOT, DOTX, DOTM, RTF
        * **Excel:** XLSX, XLS, XLSM, XLSB, XLTM, XLT, XLTM, XLTX, XLAM, SXC, SpreadsheetML
        * **PowerPoint:** PPT, PPTX, PPS, PPSX, PPSM, POT, POTM, POTX, PPTM
    # group loop
    - color: "blue"
      content: |
        ### Hình ảnh & Các định dạng khác
        * **Di động:** PDF 
        * **Hình ảnh:** JPG, BMP, PNG, TIFF, GIF
        * **Các định dạng văn phòng khác:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### Các định dạng khác
        * **Web:** HTML, MHTML 
        * **Lưu trữ:** ZIP, TAR, 7Z 
        * **e-Books:** CHM, EPUB, FB2, MOBI 
        
        

############################# Features ############################
features:
  enable: true
  title: "GroupDocs.Parser for .NET các tính năng"
  description: "Trích xuất dữ liệu từ PDFs, tài liệu Office và hình ảnh một cách nhanh chóng và chính xác"

  items:
    # feature loop
    - icon: "text"
      title: "Trích xuất văn bản"
      content: "Trích xuất thông tin văn bản từ các định dạng tệp khác nhau như tài liệu văn phòng, tệp PDF và hình ảnh để dễ dàng đọc và phân tích."

    # feature loop
    - icon: "image"
      title: "Trích xuất hình ảnh"
      content: "Lấy nội dung hình ảnh từ nhiều nguồn như tài liệu văn phòng, tệp PDF để thuận tiện trong việc truy cập và sử dụng."

    # feature loop
    - icon: "qr"
      title: "Quét mã QR"
      content: "Phát hiện và giải mã các mã QR có trong tài liệu văn phòng, tệp PDF hoặc nội dung hình ảnh để việc truy xuất thông tin hiệu quả."

    # feature loop
    - icon: "email"
      title: "Trích xuất dữ liệu từ tệp đính kèm email và lưu trữ"
      content: "Tập hợp thông tin quý giá từ các tin nhắn email, tệp đính kèm và nguồn dữ liệu nén để phân tích và sử dụng hiệu quả."

    # feature loop
    - icon: "table"
      title: "Trích xuất bảng"
      content: "Xác định và trích xuất dữ liệu dạng bảng từ tài liệu PDF để phân tích và sử dụng có tổ chức."

    # feature loop
    - icon: "hyperlink"
      title: "Trích xuất siêu liên kết"
      content: "Xác định và trích xuất siêu liên kết và địa chỉ email trong tài liệu văn phòng hoặc tệp PDF để truy cập hiệu quả."

    # feature loop
    - icon: "pdf"
      title: "Phân tích biểu mẫu PDF"
      content: "Biểu mẫu PDF là tài liệu số có các trường có thể điền để tương tác của người dùng, cho phép họ nhập thông tin một cách điện tử. API .NET có thể được sử dụng để trích xuất dữ liệu từ các biểu mẫu này cho quy trình hiệu quả."

    # feature loop
    - icon: "template"
      title: "Phân tích dữ liệu theo mẫu"
      content: "Tạo các mẫu tùy chỉnh và sử dụng chúng với API .NET để phân tích thông tin cụ thể từ các tệp PDF, đơn giản hóa quy trình trích xuất dữ liệu."

    # feature loop
    - icon: "search"
      title: "Tìm kiếm văn bản trong tài liệu"
      content: "Nhanh chóng xác định các từ hoặc mẫu cụ thể trong tài liệu."


############################# Code samples ############################
code_samples:
  enable: true
  title: "Ví dụ mã"
  description: "Một số trường hợp sử dụng các thao tác điển hình của GroupDocs.Parser for .NET"
  items:
    # code sample loop
    - title: "Trích xuất hình ảnh từ tài liệu PDF"
      content: |
        GroupDocs.Parser for .NET giúp các nhà phát triển C# dễ dàng trích xuất hình ảnh từ [tài liệu](https://docs.groupdocs.com/parser/net/extract-images-from-documents/):
        {{< landing/code title="Trích xuất hình ảnh từ tài liệu PDF trong C#">}}
        ```csharp {style=abap}
        // Tạo một đối tượng của lớp Parser
        using (var parser = new Parser("source.pptx"))
        {
            // Trích xuất hình ảnh
            var images = parser.GetImages();

            // Kiểm tra xem đã trích xuất được không
            if (images == null)
            {
                return;
            }
            // Lặp qua các hình ảnh
            foreach (PageImageArea image in images)
            {
                // In chỉ số trang, hình chữ nhật và loại hình ảnh
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Type: {2}", 
                    image.Page.Index, image.Rectangle, image.FileType));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Trích xuất mã vạch từ hình ảnh"
      content: |
        Sử dụng API .NET của chúng tôi để trích xuất [mã vạch](https://docs.groupdocs.com/parser/net/extract-barcodes-from-document/) từ hình ảnh:
        {{< landing/code title="Trích xuất mã vạch từ hình ảnh trong C#">}}
        ```csharp {style=abap}   
        // Tải hình ảnh nguồn vào Parser
        using (var parser = new Parser("source.jpg"))
        {
            // Kiểm tra xem tệp có hỗ trợ trích xuất mã vạch không
            if (parser.Features.Barcodes)
            {
                // Trích xuất mã vạch từ tệp
                var barcodes = parser.GetBarcodes();

                // Lặp qua các mã vạch
                foreach (var barcode in barcodes)
                {
                    // In chỉ số trang
                    Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                    // In giá trị mã vạch
                    Console.WriteLine("Value: " + barcode.Value);
                }
            }
        }
        ```
        {{< /landing/code >}}

---
