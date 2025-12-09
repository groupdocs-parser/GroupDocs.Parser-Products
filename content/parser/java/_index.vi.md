---
############################# Static ############################
layout: "landing"
date: 2025-12-09T14:10:41
draft: false

lang: vi
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

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
head_title: "GroupDocs.Parser for Java Document Parser SDK cho Java"
head_description: "Document Parser SDK hiệu suất cao cho Java. Trích xuất văn bản, hình ảnh, siêu dữ liệu, mã vạch, bảng và các dữ liệu khác từ PDF, Word, Excel, email và hơn 50 định dạng tài liệu."

############################# Header ############################
title: "Document Parser SDK cho Java"
description: "Thêm khả năng phân tích tài liệu nhanh chóng và chính xác vào các ứng dụng Java của bạn và trích xuất văn bản, hình ảnh, siêu dữ liệu và dữ liệu có cấu trúc từ tài liệu và hình ảnh."
words:
  for: "cho"

actions:
  main: "Maven Tải xuống"
  main_link: "https://releases.groupdocs.com/java/repo/com/groupdocs/groupdocs-parser/"
  alt: "Cấp phép"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/java/"
  title: "Sẵn sàng bắt đầu?"
  description: "Dùng thử các tính năng của GroupDocs.Parser miễn phí hoặc yêu cầu giấy phép"

release:
  title: "Phiên bản {0} đã phát hành"
  notes: "Xem những gì mới"
  downloads: "Tải xuống"

code:
  title: "Nhanh chóng phân tích nội dung tài liệu bằng SDK"
  more: "Thêm ví dụ"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java/"
  install: |
    <dependency>
      <groupId>com.groupdocs</groupId>
      <artifactId>groupdocs-parser</artifactId>
      <version>{0}</version>
    </dependency>
  content: |
    ```java {style=abap}  
    // Chuyển tệp nguồn cho đối tượng Parser
    try (Parser parser = new Parser("source.pdf"))
    {
        // Chuyển văn bản tài liệu cho TextReader
        try (TextReader reader = parser.getText())
        {
            // Xử lý văn bản tài liệu
            System.out.println(reader == null 
                ? "" 
                : reader.readToEnd());
        }
    }
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser trong một cái nhìn tổng quan"
  description: "Document Parser SDK để thực hiện phân tích tài liệu độ chính xác cao trong các ứng dụng Java"
  features:
    # feature loop
    - title: "Trích xuất dữ liệu từ tài liệu"
      content: "GroupDocs.Parser for Java API cho phép bạn lấy văn bản, siêu dữ liệu và hình ảnh từ đa dạng định dạng tệp như tài liệu Office, email, tệp đính kèm và lưu trữ. Công cụ mạnh mẽ này giúp bạn truy cập và xử lý thông tin giá trị chứa trong các tệp một cách hiệu quả cho các ứng dụng như phân tích dữ liệu, lập chỉ mục công cụ tìm kiếm hoặc hệ thống quản lý nội dung."

    # feature loop
    - title: "Phân tích tài liệu"
      content: "Trích xuất các yếu tố đa dạng như siêu liên kết, bảng, mã QR, mã vạch và dữ liệu từ biểu mẫu PDF. Ngoài ra, phân tích bất kỳ thông tin mong muốn nào từ tài liệu bằng cách sử dụng mẫu tùy chỉnh."

    # feature loop
    - title: "Tùy chỉnh kết quả"
      content: "Java API cho phép bạn lấy dữ liệu ở các định dạng khác nhau như thô, có cấu trúc, HTML hoặc Markdown. Ngoài ra, API cung cấp tính năng tìm kiếm để xác định các từ hoặc cụm từ cụ thể trong văn bản của tài liệu."

############################# Platforms ############################
platforms:
  enable: true
  title: "Độc lập nền tảng"
  description: "GroupDocs.Parser for Java hỗ trợ các hệ điều hành, framework và trình quản lý gói sau đây"
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
    - title: "Eclipse"
      image: "eclipse"
    # platform loop
    - title: "IntelliJ"
      image: "intellij"
    # platform loop
    - title: "Windows"
      image: "windows"
    # platform loop
    - title: "Linux"
      image: "linux"
    # platform loop
    - title: "Maven"
      image: "maven"

############################# File formats ############################
formats:
  enable: true
  title: "Các định dạng tệp được hỗ trợ"
  description: |
    GroupDocs.Parser for Java hỗ trợ thao tác với các [định dạng tệp](https://docs.groupdocs.com/parser/java/supported-document-formats/) sau đây.
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
  title: "Các tính năng của GroupDocs.Parser for Java"
  description: "Trích xuất dữ liệu từ PDF, tài liệu Office, hình ảnh và các định dạng khác một cách nhanh chóng và chính xác với Java Document Parser SDK của chúng tôi"

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
  description: "Một số trường hợp sử dụng điển hình của các thao tác GroupDocs.Parser for Java"
  items:
    # code sample loop
    - title: "Trích xuất hình ảnh từ tài liệu PDF"
      content: |
        GroupDocs.Parser for Java giúp các nhà phát triển Java dễ dàng trích xuất hình ảnh từ [tài liệu](https://docs.groupdocs.com/parser/java/extract-images-from-documents/):
        {{< landing/code title="Trích xuất hình ảnh từ tài liệu PDF trong Java">}}
        ```java {style=abap}
        // Tạo một thể hiện của lớp Parser
        try (Parser parser = new Parser("source.pdf"))
        {
            // Trích xuất hình ảnh
            Iterable<PageImageArea> images = parser.getImages();

            // Kiểm tra xem có gì được trích xuất không
            if (images == null) {
                return;
            }

            // Duyệt qua hình ảnh
            for (PageImageArea image : images) {
                // In chỉ số trang, hình chữ nhật và loại hình ảnh
                System.out.println(String.format("Page: %d, R: %s, Type: %s", 
                    image.getPage().getIndex(), image.getRectangle(), image.getFileType()));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Trích xuất mã vạch từ hình ảnh"
      content: |
        Sử dụng API Java của chúng tôi để trích xuất [mã vạch](https://docs.groupdocs.com/parser/java/extract-barcodes-from-document/) từ hình ảnh:
        {{< landing/code title="Trích xuất mã vạch từ hình ảnh trong Java">}}
        ```java {style=abap}   
        // Tải hình ảnh nguồn vào Parser
        try (Parser parser = new Parser("source.jpg")){

            // Kiểm tra xem tệp có hỗ trợ trích xuất mã vạch không
            if (!parser.getFeatures().isBarcodes()) {

                // Trích xuất mã vạch từ tệp
                Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();

                // Duyệt qua các mã vạch
                for (PageBarcodeArea barcode : barcodes) {
                    // In chỉ số trang
                    System.out.println("Page: " + barcode.getPage().getIndex());
                    // In giá trị mã vạch
                    System.out.println("Value: " + barcode.getValue());
                }
            }
        }
        ```
        {{< /landing/code >}}

---
