


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:17
draft: false
lang: vi
format: Ods
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Đọc mã vạch từ các tệp ODS trong ứng dụng Java"
head_description: "Với GroupDocs.Parser, trích xuất dữ liệu mã vạch từ tài liệu ODS bằng Java mà không cần công cụ bên ngoài."

############################# Header ############################
title: "Đọc mã vạch từ ODS sử dụng Java" 
description: "Trích xuất nội dung mã vạch từ các tệp PDF, Word, Excel và hình ảnh bằng GroupDocs.Parser trong các ứng dụng Java của bạn."
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Tải Xuống Phiên Bản Dùng Thử Miễn Phí"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "Tổng quan về API GroupDocs.Parser for Java"
    link: "/parser/java/"
    link_title: "Tìm hiểu thêm"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) cung cấp giải pháp toàn diện cho việc phân tích tài liệu trong Java. Nó cho phép các nhà phát triển trích xuất mã vạch, văn bản, hình ảnh và thông tin có cấu trúc từ nhiều định dạng tệp như PDF, Word, Excel, PowerPoint và các định dạng khác—không cần thư viện bên thứ ba.

############################# Steps ############################
steps:
    enable: true
    title: "Cách đọc mã vạch từ Ods trong Java"
    content: |
      Với [GroupDocs.Parser](/parser/java/), các nhà phát triển Java có thể trích xuất mã vạch từ tài liệu ODS chỉ trong vài bước:
      
      1. Tải tài liệu ODS bằng Parser.
      2. Xác minh tài liệu có hỗ trợ trích xuất mã vạch.
      3. Sử dụng API để lấy dữ liệu mã vạch.
      4. Lặp qua các kết quả mã vạch và áp dụng chúng khi cần.
   
    code:
      platform: "net"
      copy_title: "Sao chép"
      install:
        command: |
          <dependencies>
            <dependency>
              <groupId>com.groupdocs</groupId>
              <artifactId>groupdocs-parser</artifactId>
              <version>{0}</version>
            </dependency>
          </dependencies>

          <repositories>
            <repository>
              <id>repository.groupdocs.com</id>
              <name>GroupDocs Repository</name>
              <url>https://repository.groupdocs.com/repo/</url>
            </repository>
          </repositories>
        copy_tip: "nhấp để sao chép"
        copy_done: "đã sao chép"
      links:
        #  loop
        - title: "Nhiều ví dụ hơn"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java/"
        #  loop
        - title: "Tài liệu"
          link: "https://docs.groupdocs.com/parser/java/"
          
      content: |
        ```java {style=abap}
        // Mở tài liệu chứa mã vạch bằng Parser
        try (Parser parser = new Parser("input.ods"))
        {
            // Kiểm tra hỗ trợ mã vạch cho tệp
            if (!parser.getFeatures().isBarcodes())
            {
                System.out.println("Xử lý các loại tệp không được hỗ trợ");
                return;
            }

            // Trích xuất và sử dụng dữ liệu mã vạch
            Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();
            for(PageBarcodeArea barcode : barcodes)
            {
                System.out.println("Page: " + barcode.getPage().getIndex());
                System.out.println("Value: " + barcode.getValue());
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "Nhiều khả năng phân tích hơn"
  description: "GroupDocs.Parser không chỉ dừng lại ở việc trích xuất mã vạch—nó còn cho phép bạn trích xuất văn bản thuần túy, hình ảnh và các yếu tố có cấu trúc để hỗ trợ các quy trình dựa trên dữ liệu."
  image: "/img/parser/features_extract-barcode.webp" # 500x500 px
  image_description: "Các tính năng trích xuất mã vạch và dữ liệu"
  features:
    # feature loop
    - title: "Hỗ trợ nhiều định dạng mã vạch"
      content: "Phát hiện các định dạng mã vạch tiêu chuẩn bao gồm QR Code, Code 39, Data Matrix, EAN, Aztec và nhiều định dạng khác."

    # feature loop
    - title: "Đọc mã vạch từ nhiều nguồn khác nhau"
      content: "Trích xuất thông tin mã vạch từ tài liệu Office, PDF và các tệp hình ảnh như PNG, JPG và BMP."

    # feature loop
    - title: "Cấu hình đọc mã vạch tùy chỉnh"
      content: "Tinh chỉnh việc trích xuất mã vạch với các tùy chọn nhằm mục tiêu các vùng cụ thể và các tệp nhiều trang."
      
  code_samples:
    # code sample loop
    - title: "Ví dụ: trích xuất mã vạch từ PDF với tùy chọn"
      content: |
        Mẫu này trình bày việc trích xuất mã vạch từ tài liệu PDF bằng cách sử dụng các cài đặt tùy chỉnh.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Khởi tạo trình phân tích với tài liệu PDF
        try (Parser parser = new Parser("input.pdf"))
        {
            // Đảm bảo tài liệu hỗ trợ đọc mã vạch
            if (!parser.getFeatures().isBarcodes())
            {
                return;
            }

            // Áp dụng bộ lọc với các tùy chọn mã vạch
            BarcodeOptions options = new BarcodeOptions(QualityMode.Low, QualityMode.Low, "QR");

            // Trích xuất mã vạch bằng cách sử dụng trình phân tích
            Iterable<PageBarcodeArea> barcodes = parser.getBarcodes(options);

            // Xử lý từng kết quả mã vạch
            for (PageBarcodeArea barcode : barcodes)
            {
                System.out.println("Page: " + String.valueOf(barcode.getPage().getIndex()));
                System.out.println("Value: " + barcode.getValue());
            }
        }
        ```
        {{< /landing/code >}}


############################# Actions ############################

actions:
  enable: true
  title: "Bạn đã sẵn sàng bắt đầu chưa?"
  description: "Thử nghiệm các tính năng của GroupDocs.Parser miễn phí hoặc yêu cầu cấp giấy phép"
  items:
    #  loop
    - title: "Tải xuống Maven"
      link: "https://releases.groupdocs.com/parser/java/"
      color: "red"
        #  loop
    - title: "Cấp phép"
      link: "https://purchase.groupdocs.com/pricing/parser/java/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "Các định dạng tệp hỗ trợ đọc mã vạch"
    exclude: "ODS"
    description: "GroupDocs.Parser có thể đọc mã vạch từ nhiều loại tài liệu và hình ảnh khác nhau. Dưới đây là một số định dạng phổ biến được hỗ trợ."
    items: 
        # format loop 1
        - name: "Phân tích PDF"
          format: "PDF"
          link: "/parser/java/extract-barcode/pdf/"
          description: "(Định dạng tài liệu di động)"
          
        # format loop 2
        - name: "Phân tích DOCX"
          format: "DOCX"
          link: "/parser/java/extract-barcode/docx/"
          description: "(Tài liệu Microsoft Word 2007+)"
          
        # format loop 3
        - name: "Phân tích PPTX"
          format: "PPTX"
          link: "/parser/java/extract-barcode/pptx/"
          description: "(Định dạng trình bày Open XML)"
          
        # format loop 4
        - name: "Phân tích XLSX"
          format: "XLSX"
          link: "/parser/java/extract-barcode/xlsx/"
          description: "(Sổ làm việc Open XML)"
          
        # format loop 5
        - name: "Phân tích ODT"
          format: "ODT"
          link: "/parser/java/extract-barcode/odt/"
          description: "(Tài liệu văn bản OpenDocument)"
          
        # format loop 6
        - name: "Phân tích ODS"
          format: "ODS"
          link: "/parser/java/extract-barcode/ods/"
          description: "(Bảng tính OpenDocument)"
          
        # format loop 7
        - name: "Phân tích ODP"
          format: "ODP"
          link: "/parser/java/extract-barcode/odp/"
          description: "(Trình bày OpenDocument)"
          
        # format loop 8
        - name: "Phân tích EPUB"
          format: "EPUB"
          link: "/parser/java/extract-barcode/epub/"
          description: "(Tập tin eBook mở)"
          
        # format loop 9
        - name: "Phân tích FB2"
          format: "FB2"
          link: "/parser/java/extract-barcode/fb2/"
          description: "(eBook FictionBook)"
         
          

---