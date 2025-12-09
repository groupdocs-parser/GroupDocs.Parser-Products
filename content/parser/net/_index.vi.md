---
############################# Static ############################
layout: "landing"
date: 2025-12-09T14:10:41
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
    # supported_platforms loop
    - title: "Python"
      tag: "python-net"

############################# Head ############################
head_title: "GroupDocs.Parser for .NET Document Parser SDK cho .NET"
head_description: "Document Parser SDK hiệu năng cao cho .NET. Trích xuất văn bản, hình ảnh, siêu dữ liệu, mã vạch, bảng và các dữ liệu khác từ PDF, Word, Excel, email và hơn 50 định dạng tài liệu."

############################# Header ############################
title: "Document Parser SDK cho .NET"
description: "Thêm khả năng phân tích tài liệu nhanh, chính xác vào các ứng dụng .NET của bạn và trích xuất văn bản, hình ảnh, siêu dữ liệu và dữ liệu có cấu trúc từ tài liệu và hình ảnh."
words:
  for: "cho"

actions:
  main: "Nuget Tải xuống"
  main_link: "https://www.nuget.org/packages/GroupDocs.Parser"
  alt: "Cấp phép"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/net/"
  title: "Sẵn sàng bắt đầu?"
  description: "Dùng thử các tính năng của GroupDocs.Parser miễn phí hoặc yêu cầu giấy phép"

release:
  title: "Phiên bản {0} đã phát hành"
  notes: "Xem những gì mới"
  downloads: "Tải xuống"

code:
  title: "Phân tích nhanh nội dung tài liệu bằng SDK"
  more: "Thêm ví dụ"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
  install: "dotnet add package GroupDocs.Parser"
  content: |
    ```csharp {style=abap}   
    // Đưa tệp nguồn vào thể hiện Parser
    using (var parser = new Parser("source.pdf"))
    {
        // Đưa văn bản tài liệu vào TextReader
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
  title: "GroupDocs.Parser trong một cái nhìn tổng quan"
  description: "Document Parser SDK để thực hiện việc phân tích tài liệu độ chính xác cao trong các ứng dụng .NET"
  features:
    # feature loop
    - title: "Trích xuất dữ liệu từ tài liệu"
      content: "GroupDocs.Parser for .NET API cho phép bạn lấy văn bản, siêu dữ liệu và hình ảnh từ nhiều định dạng tệp khác nhau như tài liệu Office, email, tệp đính kèm và lưu trữ. Công cụ mạnh mẽ này giúp bạn truy cập và xử lý thông tin quý giá trong các tệp một cách hiệu quả cho các ứng dụng như phân tích dữ liệu, lập chỉ mục công cụ tìm kiếm hoặc hệ thống quản lý nội dung."

    # feature loop
    - title: "Phân tích tài liệu"
      content: "Trích xuất các thành phần khác nhau như siêu liên kết, bảng, mã QR, mã vạch và dữ liệu từ các biểu mẫu PDF. Đồng thời phân tích bất kỳ thông tin mong muốn nào từ tài liệu bằng cách sử dụng mẫu tùy chỉnh."

    # feature loop
    - title: "Tùy chỉnh kết quả"
      content: ".NET API cho phép bạn lấy dữ liệu ở nhiều định dạng như thô, có cấu trúc, HTML hoặc Markdown. Ngoài ra, API cung cấp chức năng tìm kiếm để xác định các từ hoặc cụm từ cụ thể trong văn bản tài liệu."

############################# Platforms ############################
platforms:
  enable: true
  title: "Độc lập nền tảng"
  description: "GroupDocs.Parser for .NET hỗ trợ các hệ điều hành, framework và trình quản lý gói sau đây"
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
    GroupDocs.Parser for .NET hỗ trợ thao tác với các [định dạng tệp](https://docs.groupdocs.com/parser/net/supported-document-formats/) sau đây.
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
        * **Các định dạng Office khác:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### Các định dạng khác
        * **Web:** HTML, MHTML 
        * **Lưu trữ:** ZIP, TAR, 7Z 
        * **Sách điện tử:** CHM, EPUB, FB2, MOBI 
        
        

############################# Features ############################
features:
  enable: true
  title: "Các tính năng của GroupDocs.Parser for .NET"
  description: "Trích xuất dữ liệu từ PDF, tài liệu Office, hình ảnh và các định dạng khác một cách nhanh chóng và chính xác với Document Parser SDK .NET của chúng tôi"

  items:
    # feature loop
    - icon: "text"
      title: "Trích xuất văn bản"
      content: "Trích xuất thông tin văn bản từ các định dạng tệp khác nhau như tài liệu Office, tệp PDF và hình ảnh để dễ đọc và phân tích."

    # feature loop
    - icon: "image"
      title: "Trích xuất hình ảnh"
      content: "Lấy nội dung hình ảnh từ các nguồn đa dạng như tài liệu Office, tệp PDF để truy cập và sử dụng thuận tiện."

    # feature loop
    - icon: "qr"
      title: "Quét mã QR"
      content: "Phát hiện và giải mã mã QR có trong tài liệu Office, tệp PDF hoặc nội dung hình ảnh để truy xuất thông tin một cách hiệu quả."

    # feature loop
    - icon: "email"
      title: "Trích xuất dữ liệu từ tệp đính kèm email và lưu trữ"
      content: "Thu thập thông tin giá trị từ tin nhắn email, tệp đính kèm và nguồn dữ liệu nén để phân tích và sử dụng hiệu quả."

    # feature loop
    - icon: "table"
      title: "Trích xuất bảng"
      content: "Xác định và trích xuất dữ liệu dạng bảng từ tài liệu PDF để phân tích và sử dụng có tổ chức."

    # feature loop
    - icon: "hyperlink"
      title: "Trích xuất siêu liên kết"
      content: "Xác định và trích xuất siêu liên kết và địa chỉ email trong tài liệu Office hoặc tệp PDF để truy cập hiệu quả."

    # feature loop
    - icon: "pdf"
      title: "Phân tích biểu mẫu PDF"
      content: "Biểu mẫu PDF là tài liệu kỹ thuật số có các trường có thể điền để người dùng tương tác, cho phép họ nhập thông tin điện tử. API .NET có thể được sử dụng để trích xuất dữ liệu từ các biểu mẫu này nhằm xử lý hiệu quả."

    # feature loop
    - icon: "template"
      title: "Phân tích dữ liệu theo mẫu"
      content: "Tạo mẫu tùy chỉnh và sử dụng chúng cùng API .NET để phân tích thông tin cụ thể từ tệp PDF, đơn giản hóa quá trình trích xuất dữ liệu."

    # feature loop
    - icon: "search"
      title: "Tìm kiếm văn bản trong tài liệu"
      content: "Nhanh chóng xác định các từ hoặc mẫu cụ thể trong tài liệu."


############################# Code samples ############################
code_samples:
  enable: true
  title: "Mẫu code"
  description: "Một số ví dụ về các thao tác điển hình của GroupDocs.Parser for .NET"
  items:
    # code sample loop
    - title: "Trích xuất hình ảnh từ tài liệu PDF"
      content: |
        GroupDocs.Parser for .NET giúp các nhà phát triển C# dễ dàng trích xuất hình ảnh từ [tài liệu](https://docs.groupdocs.com/parser/net/extract-images-from-documents/):
        {{< landing/code title="Trích xuất hình ảnh từ tài liệu PDF trong C#">}}
        ```csharp {style=abap}
        // Tạo một thể hiện của lớp Parser
        using (var parser = new Parser("source.pptx"))
        {
            // Trích xuất hình ảnh
            var images = parser.GetImages();

            // Kiểm tra xem có gì được trích xuất không
            if (images == null)
            {
                return;
            }
            // Duyệt qua hình ảnh
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

                // Duyệt qua các mã vạch
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
