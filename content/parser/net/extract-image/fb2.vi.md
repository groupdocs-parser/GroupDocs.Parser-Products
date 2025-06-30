


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:34
draft: false
lang: vi
format: Fb2
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "Trích xuất hình ảnh từ các tệp FB2 trong các ứng dụng C#"
head_description: "Sử dụng GroupDocs.Parser để phát hiện và trích xuất hình ảnh từ các tệp FB2 trong C# mà không cần công cụ bổ sung."

############################# Header ############################
title: "Trích xuất hình ảnh từ FB2 sử dụng C#" 
description: "Xác định và trích xuất hình ảnh nhúng từ các tệp PDF, tài liệu Word, trang tính Excel và các loại tệp khác bằng GroupDocs.Parser trong các ứng dụng .NET của bạn."
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Tải xuống Bản dùng thử miễn phí"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "Giới thiệu về API GroupDocs.Parser for .NET"
    link: "/parser/net/"
    link_title: "Tìm hiểu thêm"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/) là một thư viện phân tích tài liệu mạnh mẽ dành cho các nhà phát triển .NET. Nó cho phép bạn trích xuất hình ảnh, văn bản, liên kết và dữ liệu có cấu trúc từ các định dạng tệp phổ biến như PDF, DOCX, XLSX, PPTX và các định dạng khác — tất cả đều không cần ứng dụng bên thứ ba.

############################# Steps ############################
steps:
    enable: true
    title: "Các bước để trích xuất hình ảnh từ Fb2 trong C#"
    content: |
      Với [GroupDocs.Parser](/parser/net/), bạn có thể trích xuất hình ảnh từ tài liệu FB2 trong các dự án .NET của bạn chỉ trong vài bước:
      
      1. Khởi tạo Parser với tệp FB2.
      2. Lấy các phần tử hình ảnh từ tài liệu.
      3. Sử dụng các hình ảnh đã trích xuất theo nhu cầu trong quy trình làm việc của bạn.
   
    code:
      platform: "net"
      copy_title: "Sao chép"
      install:
        command: |
        command: "dotnet add package GroupDocs.Parser"
        copy_tip: "nhấp để sao chép"
        copy_done: "đã sao chép"
      links:
        #  loop
        - title: "Nhiều ví dụ hơn"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
        #  loop
        - title: "Tài liệu"
          link: "https://docs.groupdocs.com/parser/net/"
          
      content: |
        ```csharp {style=abap}
        // Mở tài liệu chứa hình ảnh bằng Parser
        using (Parser parser = new Parser("input.fb2")) {

            // Trích xuất tất cả hình ảnh nhúng từ tệp
            IEnumerable<PageImageArea> images = parser.GetImages();

            // Xử lý các trường hợp không có hình ảnh được tìm thấy
            if (images == null)
            {
                return;
            }

            // Xử lý hoặc lưu hình ảnh đã thu được
            foreach (PageImageArea image in images)
            {
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Type: {2}", 
                    image.Page.Index, image.Rectangle, image.FileType));
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "Trích xuất nội dung tài liệu toàn diện"
  description: "GroupDocs.Parser cung cấp nhiều hơn cả việc trích xuất hình ảnh — bạn cũng có thể trích xuất văn bản thô, liên kết, siêu dữ liệu và nội dung có cấu trúc cho các kịch bản tự động hóa nâng cao."
  image: "/img/parser/features_extract-image.webp" # 500x500 px
  image_description: "Quy trình làm việc trích xuất hình ảnh và phân tích tài liệu"
  features:
    # feature loop
    - title: "Trích xuất hình ảnh từ nhiều định dạng"
      content: "Trích xuất hình ảnh nhúng từ nhiều định dạng tệp, bao gồm DOCX, PDF, PPTX, XLSX và các tệp hình ảnh như PNG, JPG và TIFF."

    # feature loop
    - title: "Giữ nguyên chất lượng hình ảnh gốc"
      content: "Hình ảnh được trích xuất với độ trung thực cao, giữ nguyên độ phân giải, định dạng và hồ sơ màu sắc gốc."

    # feature loop
    - title: "Tùy chọn trích xuất nâng cao"
      content: "Tùy chỉnh việc trích xuất hình ảnh với lọc theo trang, định dạng hoặc độ phân giải, và hỗ trợ cho các tài liệu nhiều trang."
      
  code_samples:
    # code sample loop
    - title: "Cách trích xuất và lưu hình ảnh từ tài liệu PDF"
      content: |
        Ví dụ này minh họa cách trích xuất tất cả tài sản hình ảnh từ một tệp PDF và lưu chúng vào hệ thống tệp cục bộ.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Tải tệp PDF bằng lớp Parser
        using (Parser parser = new Parser("input.pdf"))
        {
            // Trích xuất hình ảnh nhúng từ tệp
            IEnumerable<PageImageArea> images = parser.GetImages();

            // Đặt định dạng đầu ra và các tùy chọn hình ảnh (ví dụ: PNG)
            ImageOptions options = new ImageOptions(ImageFormat.Png);

            // Ghi các hình ảnh đã trích xuất vào đĩa
            int imageNumber = 0;
            foreach (PageImageArea image in images)
            {
                image.Save(imageNumber.ToString() + ".png", options);
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
    - title: "Tải xuống Nuget"
      link: "https://releases.groupdocs.com/parser/net/"
      color: "red"
        #  loop
    - title: "Cấp phép"
      link: "https://purchase.groupdocs.com/pricing/parser/net/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "Định dạng được hỗ trợ cho việc trích xuất hình ảnh"
    exclude: "FB2"
    description: "GroupDocs.Parser cho phép trích xuất hình ảnh chính xác từ nhiều định dạng tài liệu và hình ảnh khác nhau. Kiểm tra danh sách dưới đây để biết các loại định dạng hỗ trợ phổ biến."
    items: 
        # format loop 1
        - name: "Phân tích PDF"
          format: "PDF"
          link: "/parser/net/extract-image/pdf/"
          description: "(Định dạng tài liệu di động)"
          
        # format loop 2
        - name: "Phân tích DOCX"
          format: "DOCX"
          link: "/parser/net/extract-image/docx/"
          description: "(Tài liệu Microsoft Word 2007+)"
          
        # format loop 3
        - name: "Phân tích PPTX"
          format: "PPTX"
          link: "/parser/net/extract-image/pptx/"
          description: "(Định dạng trình bày Open XML)"
          
        # format loop 4
        - name: "Phân tích XLSX"
          format: "XLSX"
          link: "/parser/net/extract-image/xlsx/"
          description: "(Sổ làm việc Open XML)"
          
        # format loop 5
        - name: "Phân tích ODT"
          format: "ODT"
          link: "/parser/net/extract-image/odt/"
          description: "(Tài liệu văn bản OpenDocument)"
          
        # format loop 6
        - name: "Phân tích ODS"
          format: "ODS"
          link: "/parser/net/extract-image/ods/"
          description: "(Bảng tính OpenDocument)"
          
        # format loop 7
        - name: "Phân tích ODP"
          format: "ODP"
          link: "/parser/net/extract-image/odp/"
          description: "(Trình bày OpenDocument)"
          
        # format loop 8
        - name: "Phân tích EPUB"
          format: "EPUB"
          link: "/parser/net/extract-image/epub/"
          description: "(Tập tin eBook mở)"
          
        # format loop 9
        - name: "Phân tích FB2"
          format: "FB2"
          link: "/parser/net/extract-image/fb2/"
          description: "(eBook FictionBook)"
         
          

---