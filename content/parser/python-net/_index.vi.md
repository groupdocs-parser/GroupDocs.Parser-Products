---
############################# Static ############################
layout: "landing"
date: 2025-12-09T21:34:38
draft: false

lang: vi
product: "Parser"
product_tag: "parser"
platform: "Python"
platform_tag: "python-net"

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
head_title: "GroupDocs.Parser for Python via .NET Document Parser SDK cho Python"
head_description: "Document Parser SDK hiệu năng cao cho Python. Trích xuất văn bản, hình ảnh, siêu dữ liệu, mã vạch, bảng và các dữ liệu khác từ PDF, Word, Excel, email và hơn 50 định dạng tài liệu."

############################# Header ############################
title: "Document Parser SDK cho Python"
description: "Thêm khả năng phân tích tài liệu nhanh chóng, chính xác vào các ứng dụng Python của bạn và trích xuất văn bản, hình ảnh, siêu dữ liệu và dữ liệu có cấu trúc từ tài liệu và hình ảnh."
words:
  for: "cho"

actions:
  hidden: true # Hide version 0 is released
  main: "PyPI Tải xuống"
  main_link: "https://pypi.org/project/groupdocs-parser-net/"
  alt: "Cấp phép"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/python-net/"
  title: "Sẵn sàng bắt đầu?"
  description: "Dùng thử các tính năng của GroupDocs.Parser miễn phí hoặc yêu cầu giấy phép"

release:
  enable: false
  title: "Phiên bản {0} đã phát hành"
  notes: "Xem những gì mới"
  downloads: "Tải xuống"

code:
  title: "Trích xuất văn bản bằng Python"
  more: "Thêm ví dụ"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Python-via-.NET/"
  install: "pip install groupdocs-parser-net"
  content: |
    ```python {style=abap}  
    from groupdocs.parser import Parser

    # Tải tài liệu
    with Parser("sample.pdf") as parser:
        # Trích xuất văn bản từ tài liệu
        text = parser.GetText()

        # In toàn bộ văn bản đã trích xuất
        print(text)
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser trong một cái nhìn tổng quan"
  description: "Document Parser SDK để thực hiện việc phân tích tài liệu độ chính xác cao trong các ứng dụng Python"
  features:
    # feature loop
    - title: "Trích xuất dữ liệu từ tài liệu"
      content: "GroupDocs.Parser for Python via .NET API cho phép bạn truy xuất văn bản, siêu dữ liệu và hình ảnh từ nhiều định dạng tệp khác nhau như tài liệu Office, email, tệp đính kèm và lưu trữ. Công cụ mạnh mẽ này giúp bạn tiếp cận và xử lý thông tin quan trọng có trong các tệp này một cách hiệu quả cho các ứng dụng như phân tích dữ liệu, lập chỉ mục công cụ tìm kiếm hoặc hệ thống quản lý nội dung."

    # feature loop
    - title: "Phân tích tài liệu"
      content: "Trích xuất các yếu tố khác nhau như liên kết siêu văn bản, bảng, mã QR, mã vạch và dữ liệu từ biểu mẫu PDF. Ngoài ra, phân tích bất kỳ thông tin mong muốn nào từ tài liệu bằng các mẫu tùy chỉnh."

    # feature loop
    - title: "Tùy chỉnh kết quả"
      content: "Python API cho phép bạn truy xuất dữ liệu ở nhiều định dạng như thô, có cấu trúc, HTML hoặc Markdown. Ngoài ra, API còn cung cấp chức năng tìm kiếm để xác định các từ hoặc cụm từ cụ thể trong văn bản của tài liệu."

############################# Platforms ############################
platforms:
  enable: true
  title: "Độc lập nền tảng"
  description: "GroupDocs.Parser for Python via .NET hỗ trợ các hệ điều hành, khung công tác và trình quản lý gói sau đây"
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
    - title: "VS Code"
      image: "vs_code"
    # platform loop
    - title: "ReSharper"
      image: "resharper"
    # platform loop
    - title: "macOS"
      image: "finder"
    # platform loop
    - title: "Linux"
      image: "linux"
    # platform loop
    - title: "NuGet"
      image: "nuget"

############################# File formats ############################
formats:
  enable: true
  title: "Các định dạng tệp được hỗ trợ"
  description: |
    GroupDocs.Parser for Python via .NET hỗ trợ các thao tác với [định dạng tệp](https://docs.groupdocs.com/parser/python-net/supported-document-formats/) sau đây.
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
  title: "Tính năng của GroupDocs.Parser for Python via .NET"
  description: "Trích xuất dữ liệu từ PDF, tài liệu Office, hình ảnh và các định dạng khác một cách nhanh chóng và chính xác với Document Parser SDK Python của chúng tôi"

  items:
    # feature loop
    - icon: "text"
      title: "Trích xuất văn bản"
      content: "Trích xuất thông tin văn bản từ nhiều định dạng tệp như tài liệu Office, tệp PDF và hình ảnh để dễ đọc và phân tích."

    # feature loop
    - icon: "image"
      title: "Trích xuất hình ảnh"
      content: "Lấy nội dung hình ảnh từ các nguồn đa dạng như tài liệu Office, tệp PDF để truy cập và sử dụng thuận tiện."

    # feature loop
    - icon: "qr"
      title: "Quét mã QR"
      content: "Phát hiện và giải mã các mã QR có trong tài liệu Office, tệp PDF hoặc nội dung hình ảnh để truy xuất thông tin một cách hiệu quả."

    # feature loop
    - icon: "email"
      title: "Trích xuất dữ liệu từ tệp đính kèm email và lưu trữ"
      content: "Thu thập thông tin giá trị từ tin email, tệp đính kèm và nguồn dữ liệu nén để phân tích và sử dụng hiệu quả."

    # feature loop
    - icon: "table"
      title: "Trích xuất bảng"
      content: "Xác định và trích xuất dữ liệu bảng từ tài liệu PDF để phân tích và sử dụng có tổ chức."

    # feature loop
    - icon: "hyperlink"
      title: "Trích xuất liên kết siêu văn bản"
      content: "Xác định và trích xuất siêu liên kết và địa chỉ email trong tài liệu Office hoặc tệp PDF để truy cập hiệu quả."

    # feature loop
    - icon: "pdf"
      title: "Phân tích biểu mẫu PDF"
      content: "Biểu mẫu PDF là các tài liệu kỹ thuật số có các trường có thể điền để người dùng tương tác, cho phép họ nhập thông tin điện tử. API Python có thể được sử dụng để trích xuất dữ liệu từ các biểu mẫu này nhằm xử lý hiệu quả."

    # feature loop
    - icon: "template"
      title: "Phân tích dữ liệu bằng mẫu"
      content: "Tạo các mẫu tùy chỉnh và sử dụng chúng với API Python để phân tích thông tin cụ thể từ các tệp PDF, đơn giản hóa quy trình trích xuất dữ liệu."

    # feature loop
    - icon: "search"
      title: "Tìm kiếm văn bản trong tài liệu"
      content: "Nhanh chóng xác định các từ hoặc mẫu cụ thể trong tài liệu."


############################# Code samples ############################
code_samples:
  enable: true
  title: "Mẫu code"
  description: "Ngoài việc trích xuất văn bản cơ bản, dưới đây là các trường hợp sử dụng phổ biến nhất cho việc trích xuất nhanh văn bản, hình ảnh và siêu dữ liệu."
  items:
    # code sample loop
    - title: "Tìm kiếm văn bản trong tài liệu"
      content: |
        Ví dụ này cho thấy cách tìm kiếm một cụm từ cụ thể trong tài liệu PDF và in ra vị trí nó được tìm thấy.
        {{< landing/code title="Tìm kiếm văn bản trong tài liệu bằng Python">}}
        ```python {style=abap}
        from groupdocs.parser import Parser

        # Tải tài liệu
        with Parser("sample.pdf") as parser:
            # In chỉ mục trang và hình chữ nhật nơi cụm từ được tìm thấy
            for area in parser.Search("Total Amount"):
                # In chỉ mục trang và hình chữ nhật nơi cụm từ được tìm thấy
                print(f"Page {area.PageIndex}, Rectangle: {area.Rectangle}")
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Trích xuất hình ảnh từ tài liệu"
      content: |
        Ví dụ này cho thấy cách trích xuất hình ảnh từ tài liệu PDF và lưu chúng vào tệp.
        {{< landing/code title="Trích xuất hình ảnh từ tài liệu bằng Python">}}
        ```python {style=abap}    
        from groupdocs.parser import Parser

        # Tải tài liệu
        with Parser("sample.docx") as parser:
            # Trích xuất hình ảnh từ tài liệu
            images = parser.GetImages()

            # Lưu hình ảnh vào tệp
            index = 1
            for image in images:
                image.Save(f"image_{index}.png")
                index += 1
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Trích xuất siêu dữ liệu từ tài liệu"
      content: |
        Ví dụ này cho thấy cách trích xuất siêu dữ liệu từ tài liệu PDF và in ra.
        {{< landing/code title="Trích xuất siêu dữ liệu từ tài liệu bằng Python">}}
        ```python {style=abap}    
        from groupdocs.parser import Parser

        # Tải tài liệu
        with Parser("sample.pdf") as parser:
            # Trích xuất siêu dữ liệu từ tài liệu
            metadata = parser.GetMetadata()

            # In siêu dữ liệu
            for item in metadata:
                print(f"{item.Name}: {item.Value}")
        ```
        {{< /landing/code >}}
---
