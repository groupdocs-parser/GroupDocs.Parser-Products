


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:30
draft: false
lang: vi
format: Epub
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Trích xuất hình ảnh từ tệp EPUB trong ứng dụng Java"
head_description: "Với GroupDocs.Parser, bạn có thể trích xuất hình ảnh từ tệp EPUB trong Java mà không cần công cụ bên thứ ba."

############################# Header ############################
title: "Trích xuất hình ảnh từ EPUB bằng Java" 
description: "Lấy hình ảnh nhúng từ các tệp như PDF, Word, Excel và nhiều hơn nữa bằng GroupDocs.Parser trong môi trường phát triển Java của bạn."
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Tải về bản dùng thử miễn phí"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "GroupDocs.Parser for Java là gì?"
    link: "/parser/java/"
    link_title: "Tìm hiểu thêm"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) là một API phân tích đầy đủ tính năng được thiết kế dành cho các nhà phát triển Java. Nó cho phép trích xuất hình ảnh, văn bản, liên kết và các thành phần có cấu trúc từ nhiều định dạng tệp khác nhau bao gồm DOCX, XLSX, PDF, PNG, JPG và nhiều định dạng khác — tất cả mà không cần thư viện hoặc ứng dụng bên ngoài.

############################# Steps ############################
steps:
    enable: true
    title: "Cách trích xuất hình ảnh từ Epub trong Java"
    content: |
      Thực hiện các bước sau để trích xuất hình ảnh từ tài liệu EPUB bằng [GroupDocs.Parser](/parser/java/) trong ứng dụng Java của bạn:
      
      1. Tạo một thể hiện Parser và tải tệp EPUB.
      2. Trích xuất dữ liệu hình ảnh từ tài liệu đã tải.
      3. Sử dụng hoặc xuất các hình ảnh đã trích xuất theo yêu cầu.
   
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
        // Khởi tạo parser và tải tài liệu có hình ảnh bằng Parser
        try (Parser parser = new Parser("input.epub"))
        {
            // Thu thập tất cả các phần tử hình ảnh nhúng trong tài liệu
            Iterable<PageImageArea> images = parser.getImages();

            // Bỏ qua xử lý nếu tài liệu không có hình ảnh
            if (images == null) {
                return;
            }

            // Xử lý mỗi hình ảnh theo yêu cầu
            for (PageImageArea image : images) {
                System.out.println(String.format("Page: %d, R: %s, Type: %s", image.getPage().getIndex(), 
                    image.getRectangle(), image.getFileType()));
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "Các khả năng phân tích tài liệu khác"
  description: "Ngoài việc trích xuất hình ảnh, GroupDocs.Parser còn cho phép bạn trích xuất nội dung thô như văn bản, liên kết, siêu dữ liệu, và dữ liệu có cấu trúc để xử lý và phân tích."
  image: "/img/parser/features_extract-image.webp" # 500x500 px
  image_description: "Trích xuất hình ảnh và nội dung từ các tài liệu"
  features:
    # feature loop
    - title: "Hoạt động với nhiều định dạng khác nhau"
      content: "Trích xuất hình ảnh từ các loại tài liệu khác nhau bao gồm PDF, DOCX, PPTX, XLSX và các định dạng hình ảnh như PNG, JPEG và GIF."

    # feature loop
    - title: "Bảo tồn độ rõ nét và độ phân giải của hình ảnh"
      content: "Tất cả hình ảnh được trích xuất giữ nguyên độ phân giải và kiểu tệp gốc để đảm bảo chất lượng và khả năng sử dụng nhất quán."

    # feature loop
    - title: "Tùy chọn cấu hình linh hoạt"
      content: "Tùy chỉnh quy trình trích xuất hình ảnh bằng cách lọc hình ảnh theo loại, kích thước, chỉ số trang hoặc định dạng tệp."
      
  code_samples:
    # code sample loop
    - title: "Trích xuất và lưu hình ảnh từ tệp PDF"
      content: |
        Ví dụ này cho thấy cách trích xuất hình ảnh từ một tài liệu PDF và lưu chúng riêng lẻ trên thiết bị của bạn.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Sử dụng Parser để mở tệp PDF
        try (Parser parser = new Parser("input.pdf"))
        {
            // Lấy hình ảnh từ nội dung tài liệu
            Iterable<PageImageArea> images = parser.getImages();

            // Đặt các tham số đầu ra như định dạng (ví dụ: JPEG hoặc PNG)
            ImageOptions options = new ImageOptions(ImageFormat.Png);

            // Lưu hình ảnh đã trích xuất vào một thư mục cục bộ
            int imageNumber = 0;
            for (PageImageArea image : images)
            {
                image.save(Constants.getOutputFilePath(String.format("%d.png", imageNumber)), options);
                imageNumber++;
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
    title: "Các loại tệp hỗ trợ trích xuất hình ảnh"
    exclude: "EPUB"
    description: "GroupDocs.Parser hỗ trợ trích xuất hình ảnh từ nhiều tài liệu và hình ảnh khác nhau. Khám phá các định dạng thường được hỗ trợ dưới đây."
    items: 
        # format loop 1
        - name: "Phân tích PDF"
          format: "PDF"
          link: "/parser/java/extract-image/pdf/"
          description: "(Định dạng tài liệu di động)"
          
        # format loop 2
        - name: "Phân tích DOCX"
          format: "DOCX"
          link: "/parser/java/extract-image/docx/"
          description: "(Tài liệu Microsoft Word 2007+)"
          
        # format loop 3
        - name: "Phân tích PPTX"
          format: "PPTX"
          link: "/parser/java/extract-image/pptx/"
          description: "(Định dạng trình bày Open XML)"
          
        # format loop 4
        - name: "Phân tích XLSX"
          format: "XLSX"
          link: "/parser/java/extract-image/xlsx/"
          description: "(Sổ làm việc Open XML)"
          
        # format loop 5
        - name: "Phân tích ODT"
          format: "ODT"
          link: "/parser/java/extract-image/odt/"
          description: "(Tài liệu văn bản OpenDocument)"
          
        # format loop 6
        - name: "Phân tích ODS"
          format: "ODS"
          link: "/parser/java/extract-image/ods/"
          description: "(Bảng tính OpenDocument)"
          
        # format loop 7
        - name: "Phân tích ODP"
          format: "ODP"
          link: "/parser/java/extract-image/odp/"
          description: "(Trình bày OpenDocument)"
          
        # format loop 8
        - name: "Phân tích EPUB"
          format: "EPUB"
          link: "/parser/java/extract-image/epub/"
          description: "(Tập tin eBook mở)"
          
        # format loop 9
        - name: "Phân tích FB2"
          format: "FB2"
          link: "/parser/java/extract-image/fb2/"
          description: "(eBook FictionBook)"
         
          

---