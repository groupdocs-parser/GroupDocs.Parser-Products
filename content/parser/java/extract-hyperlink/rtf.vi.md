


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:24
draft: false
lang: vi
format: Rtf
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Trích xuất liên kết từ các tệp RTF trong các ứng dụng Java"
head_description: "Sử dụng GroupDocs.Parser để tìm và trích xuất các liên kết URL từ tài liệu RTF trong các dự án Java—không cần phần mềm bổ sung."

############################# Header ############################
title: "Trích xuất liên kết từ RTF với Java" 
description: "Trích xuất các liên kết và liên kết web từ PDF, tài liệu Word, bảng tính Excel và các tài liệu khác bằng GroupDocs.Parser trong môi trường Java của bạn."
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Tải xuống bản dùng thử miễn phí"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "Giới thiệu về API GroupDocs.Parser for Java"
    link: "/parser/java/"
    link_title: "Tìm hiểu thêm"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) là một API trích xuất nội dung mạnh mẽ được thiết kế cho các nhà phát triển Java. Nó cung cấp các công cụ để trích xuất liên kết, dữ liệu cấu trúc, hình ảnh và văn bản từ các định dạng phổ biến như DOCX, XLSX, PDF, HTML và nhiều hơn nữa—tất cả mà không cần bất kỳ plugin bên ngoài nào.

############################# Steps ############################
steps:
    enable: true
    title: "Cách trích xuất liên kết từ Rtf trong Java"
    content: |
      [GroupDocs.Parser](/parser/java/) đơn giản hóa việc trích xuất liên kết từ các tệp RTF trong các ứng dụng Java với các bước cơ bản sau:
      
      1. Mở tệp RTF bằng một thể hiện của Parser.
      2. Đảm bảo khả năng trích xuất liên kết có sẵn cho định dạng tệp.
      3. Trích xuất tất cả các liên kết bằng cách sử dụng phương thức phù hợp.
      4. Lặp qua các kết quả và xử lý từng liên kết theo nhu cầu.
   
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
        // Tải tệp có thể chứa các liên kết bằng cách sử dụng Parser
        try (Parser parser = new Parser("input.rtf")) {

            // Kiểm tra xem định dạng tài liệu có hỗ trợ phân tích liên kết không
            if (!parser.getFeatures().isHyperlinks()) {
                System.out.println("Không có khả năng trích xuất liên kết cho tệp này");
                return;
            }

            // Trích xuất và sử dụng dữ liệu liên kết từ tài liệu
            Iterable<PageHyperlinkArea> hyperlinks = parser.getHyperlinks();

            for (PageHyperlinkArea h : hyperlinks) {
                System.out.println(h.getText());
                System.out.println(h.getUrl());
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "Công cụ phân tích tài liệu toàn diện"
  description: "Ngoài việc trích xuất liên kết, GroupDocs.Parser cho phép bạn thu thập các nội dung hữu ích khác như văn bản thuần, phương tiện nhúng và dữ liệu cấu trúc để sử dụng trong các quy trình tự động."
  image: "/img/parser/features_extract-hyperlink.webp" # 500x500 px
  image_description: "Trích xuất liên kết và phân tích tài liệu"
  features:
    # feature loop
    - title: "Phát hiện liên kết chính xác"
      content: "Ghi lại tất cả các loại liên kết từ các bố cục tài liệu khác nhau, bao gồm văn bản có thể nhấp và URL ẩn."

    # feature loop
    - title: "Làm việc với tài liệu và nội dung web"
      content: "Kéo các liên kết từ PDF, DOCX, XLSX, HTML và các tệp hình ảnh chứa liên kết nhúng."

    # feature loop
    - title: "Hành vi trích xuất tùy chỉnh"
      content: "Tinh chỉnh cách các liên kết được trích xuất bằng cách sử dụng các tùy chọn như khoảng trang, loại liên kết hoặc bộ lọc nội dung."
      
  code_samples:
    # code sample loop
    - title: "Ví dụ: trích xuất liên kết từ PDF với các tùy chọn tùy chỉnh"
      content: |
        Mẫu này minh họa cách trích xuất tất cả các liên kết từ một tệp PDF bằng cách sử dụng các thiết lập trích xuất liên kết.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Mở PDF bằng lớp Parser
        try (Parser parser = new Parser("input.docx"))
        {
            // Xác minh rằng hỗ trợ liên kết đã được bật cho tài liệu này
            if (!parser.getFeatures().isHyperlinks()) {
                return;
            }

            // Áp dụng các tùy chọn để lọc các liên kết
            PageAreaOptions options = new PageAreaOptions(new Rectangle(new Point(380, 90), new Size(150, 50)));

            // Sử dụng trình phân tích để lấy dữ liệu liên kết
            Iterable<PageHyperlinkArea> hyperlinks = parser.getHyperlinks(options);

            // Lặp qua các liên kết và xử lý chúng theo cách cần thiết
            for (PageHyperlinkArea h : hyperlinks) {
                System.out.println(h.getText());
                System.out.println(h.getUrl());
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
    title: "Các định dạng tài liệu hỗ trợ trích xuất liên kết"
    exclude: "RTF"
    description: "Với GroupDocs.Parser, bạn có thể trích xuất các liên kết từ nhiều định dạng tệp thường được sử dụng. Dưới đây là danh sách các định dạng thường được hỗ trợ."
    items: 
        # format loop 1
        - name: "Phân tích PDF"
          format: "PDF"
          link: "/parser/java/extract-hyperlink/pdf/"
          description: "(Định dạng tài liệu di động)"
          
        # format loop 2
        - name: "Phân tích DOCX"
          format: "DOCX"
          link: "/parser/java/extract-hyperlink/docx/"
          description: "(Tài liệu Microsoft Word 2007+)"
          
        # format loop 3
        - name: "Phân tích PPTX"
          format: "PPTX"
          link: "/parser/java/extract-hyperlink/pptx/"
          description: "(Định dạng trình bày Open XML)"
          
        # format loop 4
        - name: "Phân tích XLSX"
          format: "XLSX"
          link: "/parser/java/extract-hyperlink/xlsx/"
          description: "(Sổ làm việc Open XML)"
          
        # format loop 5
        - name: "Phân tích TXT"
          format: "TXT"
          link: "/parser/java/extract-hyperlink/txt/"
          description: "(Tập tin văn bản)"
          
        # format loop 6
        - name: "Phân tích RTF"
          format: "RTF"
          link: "/parser/java/extract-hyperlink/rtf/"
          description: "(Định dạng văn bản phong phú)"
          
        # format loop 7
        - name: "Phân tích XML"
          format: "XML"
          link: "/parser/java/extract-hyperlink/xml/"
          description: "(Ngôn ngữ đánh dấu mở rộng)"
          
        # format loop 8
        - name: "Phân tích EPUB"
          format: "EPUB"
          link: "/parser/java/extract-hyperlink/epub/"
          description: "(Tập tin eBook mở)"
         
          

---