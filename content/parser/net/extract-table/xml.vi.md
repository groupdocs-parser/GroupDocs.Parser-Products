


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:41
draft: false
lang: vi
format: Xml
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "Trích xuất bảng từ tệp XML trong ứng dụng C#"
head_description: "Sử dụng GroupDocs.Parser để xác định và trích xuất dữ liệu bảng có cấu trúc từ các tệp XML trong ứng dụng C# mà không cần phụ thuộc thêm."

############################# Header ############################
title: "Trích xuất bảng từ XML bằng C#" 
description: "Nhanh chóng xác định và trích xuất cấu trúc bảng từ PDF, Word, Excel và các định dạng tệp khác bằng GroupDocs.Parser trong các dự án .NET của bạn."
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Tải xuống bản dùng thử miễn phí"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "Giới thiệu về API GroupDocs.Parser for .NET"
    link: "/parser/net/"
    link_title: "Tìm hiểu thêm"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/) là một API phân tích tài liệu toàn diện, được xây dựng cho các nhà phát triển .NET. Nó cho phép trích xuất chính xác văn bản, bảng, hình ảnh, liên kết và các phần tử có cấu trúc khác từ các định dạng như PDF, DOCX, XLSX, PPTX và nhiều định dạng khác — mà không cần phần mềm bên thứ ba.

############################# Steps ############################
steps:
    enable: true
    title: "Các bước để trích xuất bảng từ Xml trong C#"
    content: |
      Thực hiện các hướng dẫn sau để trích xuất bảng từ các tệp XML bằng [GroupDocs.Parser](/parser/net/) trong môi trường .NET của bạn:
      
      1. Khởi tạo một phiên bản Parser và tải tài liệu XML của bạn.
      2. Kiểm tra xem việc trích xuất bảng có được hỗ trợ cho định dạng đầu vào không.
      3. Trích xuất nội dung bảng từ tệp.
      4. Sử dụng dữ liệu bảng có cấu trúc cho báo cáo, tự động hóa hoặc phân tích.
   
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
        // Mở tài liệu chứa dữ liệu bảng bằng Parser
        using (Parser parser = new Parser("input.xml")) {

            // Kiểm tra xem định dạng có hỗ trợ nhận diện bảng hay không
            if (!parser.Features.Tables) {
                Console.WriteLine("Xử lý các tài liệu không hỗ trợ phân tích bảng");
                return;
            }

            // Định nghĩa cách cấu trúc bảng nên được nhận diện
            TemplateTableLayout layout = new TemplateTableLayout(
                new double[] { 50, 95, 275, 415, 485, 545 },
                new double[] { 325, 340, 365, 395 });

            // Xác định các tham số trích xuất cho dữ liệu bảng
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            //  Trích xuất bảng từ nội dung tệp
            IEnumerable<PageTableArea> tables = parser.GetTables(options);

            //  Lặp qua từng bảng được phát hiện
            foreach (PageTableArea t in tables)
            {
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "Khả năng trích xuất dữ liệu mạnh mẽ"
  description: "Ngoài việc phân tích bảng, GroupDocs.Parser còn có thể trích xuất nội dung phong phú như khối văn bản, hình ảnh, metadata và các dữ liệu có cấu trúc khác để hỗ trợ tự động hóa tài liệu."
  image: "/img/parser/features_extract-table.webp" # 500x500 px
  image_description: "Nhận diện bảng và trích xuất nội dung"
  features:
    # feature loop
    - title: "Phát hiện bảng đa định dạng chính xác"
      content: "Trích xuất dữ liệu bảng từ DOCX, XLSX, PDF, HTML và các định dạng tương tự với độ chính xác cao."

    # feature loop
    - title: "Phân tích cấu trúc bảng từ các tệp"
      content: "Tìm nạp dữ liệu bảng từ tài liệu và bảng tính một cách hiệu quả mà không bị mất định dạng."

    # feature loop
    - title: "Cấu hình trích xuất bảng linh hoạt"
      content: "Điều chỉnh việc nhận diện bố cục, căn chỉnh cột và tùy chọn tiêu đề/chân cho kiểm soát chính xác đầu ra."
      
  code_samples:
    # code sample loop
    - title: "Cách trích xuất bảng từ bảng tính Excel"
      content: |
        Ví dụ mã này cho thấy cách đọc và lặp qua dữ liệu bảng trong tệp XLSX bằng cách sử dụng GroupDocs.Parser.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Mở tệp Excel bằng API Parser
        using (Parser parser = new Parser("input.xlsx"))
        {
            // Thoát nếu không thể trích xuất bảng từ tệp
            if (!parser.Features.Tables)
            {
                return;
            }

            // Sử dụng quy tắc bố cục để xác định nội dung bảng
            TemplateTableLayout layout = new TemplateTableLayout(
                    new double[] { 50, 95, 275, 415, 485, 545 },
                    new double[] { 325, 340, 365, 395 });

            // Thiết lập các tham số trích xuất cho bảng
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            // Thực hiện thao tác trích xuất bảng
            IEnumerable<PageTableArea> tables = parser.GetTables(options);

            // Đi qua từng cấu trúc bảng được phát hiện
            foreach (PageTableArea t in tables)
            {
                // Lặp qua từng hàng trong bảng
                for (int row = 0; row < t.RowCount; row++)
                {
                    // Lặp qua các ô trong mỗi hàng
                    for (int column = 0; column < t.ColumnCount; column++)
                    {
                        // Truy cập ô bảng hiện tại
                        PageTableAreaCell cell = t[row, column];
                        if (cell != null)
                        {
                            // Hiển thị nội dung văn bản của mỗi ô
                            Console.Write(cell.Text);
                            Console.Write(" | ");
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
    title: "Các định dạng được hỗ trợ cho việc trích xuất bảng"
    exclude: "XML"
    description: "GroupDocs.Parser có thể trích xuất dữ liệu bảng từ nhiều loại tài liệu. Dưới đây là những định dạng thường được sử dụng nhất cho việc phân tích bảng có cấu trúc."
    items: 
        # format loop 1
        - name: "Phân tích PDF"
          format: "PDF"
          link: "/parser/net/extract-table/pdf/"
          description: "(Định dạng tài liệu di động)"
          
        # format loop 2
        - name: "Phân tích DOCX"
          format: "DOCX"
          link: "/parser/net/extract-table/docx/"
          description: "(Tài liệu Microsoft Word 2007+)"
          
        # format loop 3
        - name: "Phân tích PPTX"
          format: "PPTX"
          link: "/parser/net/extract-table/pptx/"
          description: "(Định dạng trình bày Open XML)"
          
        # format loop 4
        - name: "Phân tích XLSX"
          format: "XLSX"
          link: "/parser/net/extract-table/xlsx/"
          description: "(Sổ làm việc Open XML)"
          
        # format loop 5
        - name: "Phân tích TXT"
          format: "TXT"
          link: "/parser/net/extract-table/txt/"
          description: "(Tập tin văn bản)"
          
        # format loop 6
        - name: "Phân tích RTF"
          format: "RTF"
          link: "/parser/net/extract-table/rtf/"
          description: "(Định dạng văn bản phong phú)"
          
        # format loop 7
        - name: "Phân tích XML"
          format: "XML"
          link: "/parser/net/extract-table/xml/"
          description: "(Ngôn ngữ đánh dấu mở rộng)"
          
        # format loop 8
        - name: "Phân tích EPUB"
          format: "EPUB"
          link: "/parser/net/extract-table/epub/"
          description: "(Tập tin eBook mở)"
         
          

---