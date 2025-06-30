


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:20
draft: false
lang: vi
format: Xlsx
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "Trích xuất mã vạch từ tệp XLSX trong ứng dụng C#"
head_description: "Sử dụng GroupDocs.Parser để phát hiện và trích xuất dữ liệu mã vạch từ tệp XLSX trong C# mà không cần phần mềm bổ sung."

############################# Header ############################
title: "Trích xuất mã vạch từ XLSX bằng C#" 
description: "Phát hiện và trích xuất thông tin mã vạch từ các tệp PDF, Word, Excel và hình ảnh bằng GroupDocs.Parser trong các ứng dụng .NET của bạn."
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Tải Xuống Bản Dùng Thử Miễn Phí"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "Giới thiệu về API GroupDocs.Parser for .NET"
    link: "/parser/net/"
    link_title: "Tìm hiểu thêm"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/) là một API phân tích tài liệu mạnh mẽ cho các nhà phát triển .NET. Nó cho phép trích xuất văn bản, hình ảnh, nội dung có cấu trúc và mã vạch từ nhiều định dạng tệp khác nhau bao gồm PDF, Word, Excel, PowerPoint và hơn thế nữa — tất cả đều không phụ thuộc vào công cụ bên ngoài.

############################# Steps ############################
steps:
    enable: true
    title: "Các bước để trích xuất mã vạch từ Xlsx trong C#"
    content: |
      [GroupDocs.Parser](/parser/net/) cho phép bạn trích xuất dữ liệu mã vạch từ các tệp XLSX trong ứng dụng .NET bằng cách làm theo các bước đơn giản sau:
      
      1. Tải tệp XLSX bằng cách sử dụng một phiên bản Parser.
      2. Xác nhận rằng tài liệu hỗ trợ trích xuất mã vạch.
      3. Lấy danh sách mã vạch từ tài liệu.
      4. Lặp qua các kết quả và sử dụng các giá trị mã vạch đã trích xuất.
   
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
        // Tải tài liệu chứa mã vạch bằng lớp Parser
        using (Parser parser = new Parser("input.xlsx")) {

            // Xác nhận rằng tệp hỗ trợ trích xuất mã vạch
            if (!parser.Features.Barcodes) {
                Console.WriteLine("Trích xuất mã vạch không được hỗ trợ");
                return;
            }

            // Lấy và xử lý các mã vạch đã trích xuất
            IEnumerable<PageBarcodeArea> barcodes = parser.GetBarcodes();

            foreach (PageBarcodeArea barcode in barcodes) {
                Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                Console.WriteLine("Value: " + barcode.Value);
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "Các tính năng phân tích tài liệu nâng cao"
  description: "Ngoài việc trích xuất mã vạch, GroupDocs.Parser cho phép bạn trích xuất văn bản thuần, hình ảnh và dữ liệu có cấu trúc để hỗ trợ tự động hóa nâng cao và quy trình xử lý dữ liệu."
  image: "/img/parser/features_extract-barcode.webp" # 500x500 px
  image_description: "Nhận diện mã vạch và phân tích tài liệu"
  features:
    # feature loop
    - title: "Hỗ trợ nhiều định dạng mã vạch"
      content: "Nhận diện các loại mã vạch phổ biến bao gồm QR Code, Code 128, Data Matrix, EAN, Aztec và nhiều hơn nữa."

    # feature loop
    - title: "Trích xuất mã vạch từ tài liệu và hình ảnh"
      content: "Đọc mã vạch từ tài liệu PDF, Word, Excel và các định dạng hình ảnh như JPEG, PNG và BMP."

    # feature loop
    - title: "Cài đặt trích xuất có thể tùy chỉnh"
      content: "Cấu hình các tùy chọn phát hiện như vùng quét và xử lý tài liệu nhiều trang."
      
  code_samples:
    # code sample loop
    - title: "Cách trích xuất mã vạch từ một tệp PDF bằng các tùy chọn mã vạch"
      content: |
        Ví dụ này minh họa cách trích xuất mã vạch từ tệp PDF bằng các tùy chọn trích xuất mã vạch cụ thể.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Tải tệp PDF bằng lớp Parser
        using (Parser parser = new Parser("input.pdf"))
        {
            // Xác nhận hỗ trợ trích xuất mã vạch
            if (!parser.Features.Barcodes)
            {
                return;
            }

            // Sử dụng các tùy chọn mã vạch để lọc kết quả
            BarcodeOptions options = new BarcodeOptions(QualityMode.Low, QualityMode.Low, "QR");

            // Lấy dữ liệu mã vạch từ tài liệu
            IEnumerable<PageBarcodeArea> barcodes = parser.GetBarcodes(options);

            // Xử lý danh sách mã vạch đã trích xuất
            foreach (PageBarcodeArea barcode in barcodes)
            {
                Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                Console.WriteLine("Value: " + barcode.Value);
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
    title: "Các định dạng được hỗ trợ cho việc trích xuất mã vạch"
    exclude: "XLSX"
    description: "GroupDocs.Parser hỗ trợ phát hiện mã vạch trong nhiều định dạng tài liệu và hình ảnh khác nhau. Xem bên dưới để biết các loại tệp thường được hỗ trợ."
    items: 
        # format loop 1
        - name: "Phân tích PDF"
          format: "PDF"
          link: "/parser/net/extract-barcode/pdf/"
          description: "(Định dạng tài liệu di động)"
          
        # format loop 2
        - name: "Phân tích DOCX"
          format: "DOCX"
          link: "/parser/net/extract-barcode/docx/"
          description: "(Tài liệu Microsoft Word 2007+)"
          
        # format loop 3
        - name: "Phân tích PPTX"
          format: "PPTX"
          link: "/parser/net/extract-barcode/pptx/"
          description: "(Định dạng trình bày Open XML)"
          
        # format loop 4
        - name: "Phân tích XLSX"
          format: "XLSX"
          link: "/parser/net/extract-barcode/xlsx/"
          description: "(Sổ làm việc Open XML)"
          
        # format loop 5
        - name: "Phân tích ODT"
          format: "ODT"
          link: "/parser/net/extract-barcode/odt/"
          description: "(Tài liệu văn bản OpenDocument)"
          
        # format loop 6
        - name: "Phân tích ODS"
          format: "ODS"
          link: "/parser/net/extract-barcode/ods/"
          description: "(Bảng tính OpenDocument)"
          
        # format loop 7
        - name: "Phân tích ODP"
          format: "ODP"
          link: "/parser/net/extract-barcode/odp/"
          description: "(Trình bày OpenDocument)"
          
        # format loop 8
        - name: "Phân tích EPUB"
          format: "EPUB"
          link: "/parser/net/extract-barcode/epub/"
          description: "(Tập tin eBook mở)"
          
        # format loop 9
        - name: "Phân tích FB2"
          format: "FB2"
          link: "/parser/net/extract-barcode/fb2/"
          description: "(eBook FictionBook)"
         
          

---