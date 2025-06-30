


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:38
draft: false
lang: vi
format: Pptx
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Trích xuất bảng từ tài liệu PPTX trong ứng dụng Java"
head_description: "Trích xuất dữ liệu bảng có cấu trúc từ các tập tin PPTX trong các ứng dụng Java bằng cách sử dụng GroupDocs.Parser—không cần công cụ bên ngoài."

############################# Header ############################
title: "Trích xuất dữ liệu bảng từ PPTX bằng Java" 
description: "Phát hiện và trích xuất bảng từ các định dạng như PDF, DOCX, và XLSX một cách liền mạch với GroupDocs.Parser trong quy trình Java của bạn."
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Tải phiên bản dùng thử miễn phí"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "Giới thiệu về API GroupDocs.Parser for Java"
    link: "/parser/java/"
    link_title: "Tìm hiểu thêm"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) là một API trích xuất nội dung phong phú tính năng dành cho các nền tảng Java. Nó cho phép các nhà phát triển phân tích chính xác bảng, văn bản, đồ họa, liên kết và dữ liệu có cấu trúc từ các tài liệu PDF, các tài liệu Word, bảng tính Excel, bài thuyết trình PowerPoint, và nhiều định dạng khác—mà không cần các plugin bên thứ ba.

############################# Steps ############################
steps:
    enable: true
    title: "Cách trích xuất bảng từ Pptx trong Java"
    content: |
      Để phân tích bảng từ tài liệu PPTX bằng [GroupDocs.Parser](/parser/java/), hãy làm theo các bước sau trong môi trường Java của bạn:
      
      1. Tạo một thể hiện Parser và tải tập tin PPTX mục tiêu.
      2. Xác nhận rằng tập tin hỗ trợ việc trích xuất bảng có cấu trúc.
      3. Sử dụng API để lấy các phần tử bảng từ tài liệu.
      4. Sử dụng dữ liệu đã trích xuất trong phân tích, báo cáo, hoặc hệ thống tự động hóa.
   
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
        // Tải tài liệu đầu vào với Parser bao gồm các phần tử bảng
        try (Parser parser = new Parser("input.pptx"))
        {
            // Xác nhận rằng loại tài liệu cho phép nhận diện bảng
            if (!parser.getFeatures().isTables()) {
                System.out.println("Thêm logic cho các tệp không hỗ trợ bảng");
                return;
            }

            // Định nghĩa quy tắc để diễn giải cấu trúc bảng
            TemplateTableLayout layout = new TemplateTableLayout(
                    java.util.Arrays.asList(new Double[]{50.0, 95.0, 275.0, 415.0, 485.0, 545.0}),
                    java.util.Arrays.asList(new Double[]{325.0, 340.0, 365.0, 395.0}));

            // Đặt tham số để trích xuất bảng
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            //  Chạy trích xuất bảng trên tài liệu đã tải
            Iterable<PageTableArea> tables = parser.getTables(options);

            //  Xử lý từng bảng được trích xuất từ kết quả
            for (PageTableArea t : tables) 
            {
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "Công cụ trích xuất nội dung nâng cao"
  description: "Ngoài việc đọc bảng, GroupDocs.Parser còn hỗ trợ việc khôi phục văn bản thuần, các yếu tố hình ảnh, siêu dữ liệu nhúng, và các đối tượng có cấu trúc để nâng cao các nhiệm vụ xử lý tài liệu."
  image: "/img/parser/features_extract-table.webp" # 500x500 px
  image_description: "Trích xuất nội dung có cấu trúc và dữ liệu bảng"
  features:
    # feature loop
    - title: "Phân tích bảng chính xác qua nhiều định dạng"
      content: "Hỗ trợ trích xuất bảng từ các loại tài liệu tiêu chuẩn như PDF, Word, Excel, và HTML với độ chính xác cao."

    # feature loop
    - title: "Đọc cấu trúc bảng từ nhiều nguồn khác nhau"
      content: "Khôi phục dữ liệu bảng từ bảng tính, tài liệu, và báo cáo trong khi vẫn bảo tồn cấu trúc và bố cục."

    # feature loop
    - title: "Thiết lập trích xuất bảng tùy chỉnh"
      content: "Kiểm soát việc phát hiện bố cục, quản lý tiêu đề và chân trang, cũng như tùy chỉnh việc trích xuất với các tùy chọn cấu hình linh hoạt."
      
  code_samples:
    # code sample loop
    - title: "Mẫu: trích xuất bảng từ tài liệu Excel"
      content: |
        Ví dụ này cho thấy cách trích xuất và lặp qua nội dung bảng trong tập tin Excel (XLSX) bằng cách sử dụng GroupDocs.Parser.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Khởi tạo Parser với tệp Excel
        try (Parser parser = new Parser("input.pdf"))
        {
            // Thoát nếu việc trích xuất bảng không được hỗ trợ cho tài liệu này
            if (!parser.getFeatures().isTables())
            {
                return;
            }

            // Áp dụng quy tắc để xác định bố cục bảng
            TemplateTableLayout layout = new TemplateTableLayout(
                    java.util.Arrays.asList(new Double[]{50.0, 95.0, 275.0, 415.0, 485.0, 545.0}),
                    java.util.Arrays.asList(new Double[]{325.0, 340.0, 365.0, 395.0}));

            // Cấu hình môi trường cho việc trích xuất bảng
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            // Kích hoạt quy trình trích xuất
            Iterable<PageTableArea> tables = parser.getTables(options);

            // Lặp qua tất cả các cấu trúc bảng đã phân tích
            for (PageTableArea t : tables)
            {
                // Lặp qua từng hàng trong bảng
                for (int row = 0; row < t.getRowCount(); row++)
                {
                    // Xử lý từng ô trong hàng hiện tại
                    for (int column = 0; column < t.getColumnCount(); column++) 
                    {
                        // Truy cập và đọc nội dung của ô hiện tại
                        PageTableAreaCell cell = t.getCell(row, column);
                        if (cell != null)
                        {
                            // Xuất giá trị văn bản của từng ô bảng
                            System.out.print(cell.getText());
                            System.out.print(" | ");
                        }
                    }
                }
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
    title: "Các loại tài liệu được hỗ trợ cho việc trích xuất bảng"
    exclude: "PPTX"
    description: "GroupDocs.Parser cung cấp phát hiện bảng đáng tin cậy trên nhiều loại tệp. Dưới đây là danh sách các định dạng tài liệu được hỗ trợ rộng rãi nhất cho việc trích xuất bảng."
    items: 
        # format loop 1
        - name: "Phân tích PDF"
          format: "PDF"
          link: "/parser/java/extract-table/pdf/"
          description: "(Định dạng tài liệu di động)"
          
        # format loop 2
        - name: "Phân tích DOCX"
          format: "DOCX"
          link: "/parser/java/extract-table/docx/"
          description: "(Tài liệu Microsoft Word 2007+)"
          
        # format loop 3
        - name: "Phân tích PPTX"
          format: "PPTX"
          link: "/parser/java/extract-table/pptx/"
          description: "(Định dạng trình bày Open XML)"
          
        # format loop 4
        - name: "Phân tích XLSX"
          format: "XLSX"
          link: "/parser/java/extract-table/xlsx/"
          description: "(Sổ làm việc Open XML)"
          
        # format loop 5
        - name: "Phân tích TXT"
          format: "TXT"
          link: "/parser/java/extract-table/txt/"
          description: "(Tập tin văn bản)"
          
        # format loop 6
        - name: "Phân tích RTF"
          format: "RTF"
          link: "/parser/java/extract-table/rtf/"
          description: "(Định dạng văn bản phong phú)"
          
        # format loop 7
        - name: "Phân tích XML"
          format: "XML"
          link: "/parser/java/extract-table/xml/"
          description: "(Ngôn ngữ đánh dấu mở rộng)"
          
        # format loop 8
        - name: "Phân tích EPUB"
          format: "EPUB"
          link: "/parser/java/extract-table/epub/"
          description: "(Tập tin eBook mở)"
         
          

---