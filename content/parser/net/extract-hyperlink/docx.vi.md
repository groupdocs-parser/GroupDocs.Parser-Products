


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:26
draft: false
lang: vi
format: Docx
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "Trích xuất liên kết từ các tệp DOCX trong ứng dụng C#"
head_description: "Sử dụng GroupDocs.Parser để phát hiện và trích xuất liên kết từ các tệp DOCX trong C# mà không cần công cụ hoặc phần mềm bổ sung."

############################# Header ############################
title: "Trích xuất liên kết từ DOCX bằng C#" 
description: "Xác định và trích xuất URL và liên kết từ PDF, Word, Excel và các loại tài liệu khác bằng GroupDocs.Parser trong các ứng dụng .NET của bạn."
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Tải xuống Bản Dùng Thử Miễn Phí"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "Giới thiệu về API GroupDocs.Parser for .NET"
    link: "/parser/net/"
    link_title: "Tìm hiểu thêm"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/) là một API phân tích tài liệu linh hoạt dành cho các nhà phát triển .NET. Nó hỗ trợ trích xuất liên kết, văn bản, hình ảnh và nội dung có cấu trúc từ nhiều định dạng tệp khác nhau như PDF, Word, Excel, HTML và hơn thế nữa — mà không cần dựa vào phần mềm bên ngoài.

############################# Steps ############################
steps:
    enable: true
    title: "Các bước để trích xuất liên kết từ Docx trong C#"
    content: |
      [GroupDocs.Parser](/parser/net/) cho phép các nhà phát triển .NET trích xuất liên kết từ các tệp DOCX bằng cách làm theo các bước đơn giản sau:
      
      1. Tải tệp DOCX bằng cách sử dụng một thể hiện Parser.
      2. Kiểm tra xem tài liệu có hỗ trợ trích xuất liên kết không.
      3. Lấy danh sách các liên kết từ tài liệu.
      4. Lặp qua các kết quả và làm việc với các URL đã được trích xuất.
   
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
        // Tải tài liệu chứa liên kết bằng lớp Parser
        using (Parser parser = new Parser("input.docx")) {

            // Xác minh rằng tệp hỗ trợ trích xuất liên kết
            if (!parser.Features.Hyperlinks)
            {
                Console.WriteLine("Không có khả năng trích xuất liên kết cho tệp này");
                return;
            }

            // Lấy và xử lý các liên kết đã được trích xuất
            IEnumerable<PageHyperlinkArea> hyperlinks = parser.GetHyperlinks();

            foreach (PageHyperlinkArea h in hyperlinks)
            {
                Console.WriteLine(h.Text);
                Console.WriteLine(h.Url);
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "Khả năng phân tích tài liệu nâng cao"
  description: "Ngoài việc trích xuất liên kết, GroupDocs.Parser còn cho phép bạn trích xuất văn bản, siêu dữ liệu, hình ảnh và dữ liệu có cấu trúc — hỗ trợ các quy trình xử lý dữ liệu mạnh mẽ."
  image: "/img/parser/features_extract-hyperlink.webp" # 500x500 px
  image_description: "Phát hiện liên kết và phân tích tài liệu"
  features:
    # feature loop
    - title: "Phát hiện liên kết từ tài liệu"
      content: "Nhanh chóng trích xuất URL và chú thích liên kết từ các tài liệu như PDF, tệp Word, bảng tính và nhiều hơn nữa."

    # feature loop
    - title: "Hỗ trợ liên kết web và nhúng"
      content: "Phát hiện và trích xuất cả URL web tiêu chuẩn và liên kết tài liệu nhúng trên nhiều định dạng."

    # feature loop
    - title: "Tùy chọn phân tích linh hoạt"
      content: "Tùy chỉnh cài đặt trích xuất để quét các phần hoặc trang cụ thể nhằm cải thiện hiệu suất và độ chính xác."
      
  code_samples:
    # code sample loop
    - title: "Cách trích xuất liên kết từ PDF bằng tùy chọn liên kết"
      content: |
        Ví dụ mã này cho thấy cách trích xuất tất cả liên kết từ tệp PDF bằng cách sử dụng các tùy chọn tùy chỉnh.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Khởi tạo Parser với tài liệu PDF
        using (Parser parser = new Parser("input.docx"))
        {
            // Kiểm tra xem trích xuất liên kết có được hỗ trợ không
            if (!parser.Features.Hyperlinks)
            {
                return;
            }

            // Đặt tùy chọn trích xuất liên kết để thu hẹp kết quả
            PageAreaOptions options = new PageAreaOptions(new Rectangle(new Point(380, 90), new Size(150, 50)));

            // Trích xuất dữ liệu liên kết từ tài liệu
            IEnumerable<PageHyperlinkArea> hyperlinks = parser.GetHyperlinks(options);

            // Xử lý danh sách các liên kết đã được trích xuất
            foreach (PageHyperlinkArea h in hyperlinks)
            {
                Console.WriteLine(h.Text);
                Console.WriteLine(h.Url);
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
    title: "Các định dạng được hỗ trợ cho việc trích xuất liên kết"
    exclude: "DOCX"
    description: "GroupDocs.Parser có thể trích xuất liên kết từ nhiều loại tài liệu khác nhau. Dưới đây là các định dạng thường được hỗ trợ."
    items: 
        # format loop 1
        - name: "Phân tích PDF"
          format: "PDF"
          link: "/parser/net/extract-hyperlink/pdf/"
          description: "(Định dạng tài liệu di động)"
          
        # format loop 2
        - name: "Phân tích DOCX"
          format: "DOCX"
          link: "/parser/net/extract-hyperlink/docx/"
          description: "(Tài liệu Microsoft Word 2007+)"
          
        # format loop 3
        - name: "Phân tích PPTX"
          format: "PPTX"
          link: "/parser/net/extract-hyperlink/pptx/"
          description: "(Định dạng trình bày Open XML)"
          
        # format loop 4
        - name: "Phân tích XLSX"
          format: "XLSX"
          link: "/parser/net/extract-hyperlink/xlsx/"
          description: "(Sổ làm việc Open XML)"
          
        # format loop 5
        - name: "Phân tích TXT"
          format: "TXT"
          link: "/parser/net/extract-hyperlink/txt/"
          description: "(Tập tin văn bản)"
          
        # format loop 6
        - name: "Phân tích RTF"
          format: "RTF"
          link: "/parser/net/extract-hyperlink/rtf/"
          description: "(Định dạng văn bản phong phú)"
          
        # format loop 7
        - name: "Phân tích XML"
          format: "XML"
          link: "/parser/net/extract-hyperlink/xml/"
          description: "(Ngôn ngữ đánh dấu mở rộng)"
          
        # format loop 8
        - name: "Phân tích EPUB"
          format: "EPUB"
          link: "/parser/net/extract-hyperlink/epub/"
          description: "(Tập tin eBook mở)"
         
          

---