


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:45
draft: false
lang: vi
format: Xlsx
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Truy xuất văn bản từ các tệp XLSX trong ứng dụng Java"
head_description: "Sử dụng GroupDocs.Parser để trích xuất nội dung văn bản có cấu trúc hoặc không có cấu trúc từ tài liệu XLSX trong Java, mà không cần các phụ thuộc bên ngoài."

############################# Header ############################
title: "Truy xuất văn bản từ XLSX bằng Java" 
description: "Lấy văn bản có thể đọc hoặc có cấu trúc từ các tệp như PDF, Word, Excel, và nhiều hơn nữa bằng cách sử dụng GroupDocs.Parser trong các dự án phát triển Java của bạn."
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Tải xuống Phiên bản Dùng thử Miễn phí"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "Giới thiệu về API GroupDocs.Parser for Java"
    link: "/parser/java/"
    link_title: "Tìm hiểu thêm"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) là một bộ phân tích tài liệu mạnh mẽ và có thể mở rộng dành cho các nhà phát triển Java. Nó cung cấp khả năng trích xuất chính xác văn bản, bảng biểu, hình ảnh và các thành phần có cấu trúc từ nhiều định dạng khác nhau, bao gồm PDF, DOCX, XLSX, PPTX và nhiều định dạng khác—mà không cần phụ thuộc vào các tiện ích bên ngoài.

############################# Steps ############################
steps:
    enable: true
    title: "Cách truy xuất văn bản từ Xlsx bằng Java"
    content: |
      Thực hiện các bước dưới đây để trích xuất văn bản từ các tệp XLSX sử dụng [GroupDocs.Parser](/parser/java/) trong dự án Java của bạn:
      
      1. Tải tài liệu XLSX bằng lớp Parser.
      2. Thực hiện trích xuất văn bản từ nội dung tệp.
      3. Kiểm tra xem văn bản đã được truy xuất thành công chưa.
      4. Sử dụng dữ liệu văn bản trong hệ thống tìm kiếm, phân tích hoặc tự động hóa.
   
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
        // Khởi tạo Parser với tài liệu của bạn
        try (Parser parser = new Parser("input.xlsx"))
        {
            // Đọc và trích xuất toàn bộ dữ liệu văn bản
            try (TextReader reader = parser.getText())
            {
                // Trả về null nếu nội dung văn bản không có
                // Tích hợp văn bản đã trích xuất vào quy trình làm việc của bạn
                System.out.println(reader == null ? 
                    "Bỏ qua các định dạng không hỗ trợ trích xuất văn bản" : reader.readToEnd());
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "Chức năng trích xuất văn bản phong phú"
  description: "GroupDocs.Parser vượt ra ngoài việc trích xuất văn bản đơn giản—hỗ trợ việc truy xuất hình ảnh, siêu dữ liệu và dữ liệu có cấu trúc để nâng cao các tác vụ xử lý nội dung."
  image: "/img/parser/features_extract-text.webp" # 500x500 px
  image_description: "Trích xuất và cấu trúc nội dung văn bản từ các tài liệu"
  features:
    # feature loop
    - title: "Hỗ trợ nhiều định dạng tài liệu"
      content: "Trích xuất văn bản thô và có cấu trúc từ DOCX, XLSX, PPTX, PDF, HTML và nhiều định dạng khác."

    # feature loop
    - title: "Trích xuất văn bản từ nội dung hình ảnh và văn bản"
      content: "Phân tích văn bản từ các tài liệu quét, slide, bảng tính và các loại tệp khác trong khi vẫn giữ nguyên cấu trúc logic."

    # feature loop
    - title: "Kiểm soát chi tiết quá trình trích xuất"
      content: "Cấu hình phạm vi trang, vùng bố cục và các tham số độ chính xác để tối ưu hóa việc phân tích văn bản."
      
  code_samples:
    # code sample loop
    - title: "Mẫu: Trích xuất vùng văn bản từ tài liệu PPTX"
      content: |
        Mẫu này minh họa việc trích xuất các khối văn bản cùng với tọa độ không gian của chúng từ một bài thuyết trình PowerPoint bằng cách sử dụng GroupDocs.Parser.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Tải tệp PPTX của bạn với API Parser
        try (Parser parser = new Parser("input.pptx"))
        {
            // Lấy tất cả các vùng văn bản hình chữ nhật
            IEnumerable<PageTextArea> areas = parser.GetTextAreas();

            // Thoát nếu chức năng này không được hỗ trợ
            if (areas == null)
            {
                return;
            }

            // Lặp qua các khu vực văn bản theo trang
            for (PageTextArea a : areas)
            {
                // Xử lý từng khối văn bản với số trang và hình chữ nhật bao quanh
                System.out.println(String.format("Page: %d, R: %s, Text: %s", a.getPage().getIndex(), a.getRectangle(), a.getText()));
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
    title: "Các loại tệp được hỗ trợ cho việc trích xuất văn bản"
    exclude: "XLSX"
    description: "GroupDocs.Parser có khả năng trích xuất nội dung văn bản từ nhiều định dạng tệp và hình ảnh khác nhau. Dưới đây là những loại tệp thông dụng nhất mà nó hỗ trợ."
    items: 
        # format loop 1
        - name: "Phân tích PDF"
          format: "PDF"
          link: "/parser/java/extract-text/pdf/"
          description: "(Định dạng tài liệu di động)"
          
        # format loop 2
        - name: "Phân tích DOCX"
          format: "DOCX"
          link: "/parser/java/extract-text/docx/"
          description: "(Tài liệu Microsoft Word 2007+)"
          
        # format loop 3
        - name: "Phân tích PPTX"
          format: "PPTX"
          link: "/parser/java/extract-text/pptx/"
          description: "(Định dạng trình bày Open XML)"
          
        # format loop 4
        - name: "Phân tích XLSX"
          format: "XLSX"
          link: "/parser/java/extract-text/xlsx/"
          description: "(Sổ làm việc Open XML)"
          
        # format loop 5
        - name: "Phân tích TXT"
          format: "TXT"
          link: "/parser/java/extract-text/txt/"
          description: "(Tập tin văn bản)"
          
        # format loop 6
        - name: "Phân tích RTF"
          format: "RTF"
          link: "/parser/java/extract-text/rtf/"
          description: "(Định dạng văn bản phong phú)"
          
        # format loop 7
        - name: "Phân tích XML"
          format: "XML"
          link: "/parser/java/extract-text/xml/"
          description: "(Ngôn ngữ đánh dấu mở rộng)"
          
        # format loop 8
        - name: "Phân tích EPUB"
          format: "EPUB"
          link: "/parser/java/extract-text/epub/"
          description: "(Tập tin eBook mở)"
         
          

---