---
############################# Static ############################
layout: "family"
date:  2025-12-09T14:52:35
draft: false

product: "Parser"
product_tag: "parser"

lang: vi

############################# Head ############################
head_title: "SDK Trình Phân Tích Tài Liệu cho PDF, Word & Excel | GroupDocs"
head_description: "SDK Trình Phân Tích Tài Liệu để trích xuất văn bản, hình ảnh, metadata, mã vạch và bảng từ PDF, Word, Excel, email và hơn 50 định dạng tài liệu khác cho các ứng dụng .NET, Java và Python."

############################# Header ############################
title: "SDK Trình Phân Tích Tài Liệu"
description:  |
  SDK Trình Phân Tích Tài Liệu thân thiện với nhà phát triển, cho phép trích xuất văn bản, hình ảnh, mã vạch, metadata và bảng từ hơn 50 định dạng tài liệu và hình ảnh.

  Tích hợp việc phân tích tài liệu hiệu năng cao vào các ứng dụng .NET, Java và Python của bạn với nỗ lực mã hóa tối thiểu.

  Sử dụng các mẫu linh hoạt và API nâng cao để tùy chỉnh quy tắc phân tích và cung cấp đầu ra dữ liệu sạch, có cấu trúc.

############################# Supported Platforms ###############################
supported_platforms:
  enable: true
  head_title: "Chọn nền tảng của bạn"
  title: "Độc lập nền tảng"
  description: "Thư viện GroupDocs.Parser hỗ trợ các hệ điều hành và framework sau:"
  details_link_title: "Tìm hiểu thêm"

  items:
    # items loop
    - title: ".NET"
      description: GroupDocs.Parser for .NET 
      color: "blue"
      tag: "net"
      link: "/parser/net/"
      features_link: "https://docs.groupdocs.com/parser/net/system-requirements/"
      features:
          # features loop
          - rows: "3"
            content: |
                    .NET Framework 4.6.2 or higher <br> .NET Core 2.0 or higher <br> .NET 6.0 or higher
      
          # features loop
          - rows: "1"
            content: |
                    Windows <br> Linux <br> Mac OS
      
          # features loop
          - rows: "4"
            content: |
                    Microsoft Visual Studio <br> JetBrains Rider <br> Microsoft Visual Code
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats
      

    # items loop
    - title: "Java"
      description: GroupDocs.Parser for Java
      color: "red"
      tag: "java"
      link: "/parser/java/"
      features_link: "https://docs.groupdocs.com/parser/java/system-requirements/"
      features:
          # features loop
          - rows: "3"
            content: |
                    Java 8 or higher <br> Kotlin
      
          # features loop
          - rows: "1"
            content: |
                    Windows <br> Linux <br> Mac OS
      
          # features loop
          - rows: "4"
            content: |
                    IntelliJ IDEA <br> Eclipse <br> NetBeans
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats


    # items loop
    - title: "Python"
      description: GroupDocs.Parser for Python
      color: "yellow"
      tag: "python-net"
      link: "/parser/python-net/"
      features_link: "https://docs.groupdocs.com/parser/python-net/system-requirements/"
      features:
          # features loop
          - rows: "3"
            content: |
                    Python 3.5+
      
          # features loop
          - rows: "1"
            content: |
                    Windows <br> Linux <br> macOS
      
          # features loop
          - rows: "4"
            content: |
                    PyCharm, VS Code, Jupyter Notebook
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats                    

############################# Features ###############################
features:
  enable: true
  title: "GroupDocs.Parser trong một cái nhìn tổng quan"
  description: "SDK Trình Phân Tích Tài Liệu mạnh mẽ để trích xuất dữ liệu có cấu trúc và không có cấu trúc từ PDF, tài liệu Office, hình ảnh, email và lưu trữ."

  items:
    # items loop
    - icon: "text"
      title: "Trích xuất văn bản"
      content: "Trích xuất thông tin văn bản từ nhiều định dạng tệp"

    # items loop
    - icon: "image"
      title: "Trích xuất hình ảnh"
      content: "Lấy nội dung hình ảnh từ các nguồn đa dạng"

    # items loop
    - icon: "template"
      title: "Phân tích dữ liệu bằng mẫu"
      content: "Tạo mẫu tùy chỉnh và sử dụng chúng để phân tích thông tin cụ thể"

    # items loop
    - icon: "pdf"
      title: "Phân tích biểu mẫu PDF"
      content: "Biểu mẫu PDF là tài liệu kỹ thuật số có các trường có thể điền để người dùng tương tác"

############################# Code Samples ###############################
code_samples:
  enable: true
  title: "GroupDocs.Parser mẫu code"
  description: "Một số trường hợp sử dụng điển hình của các thao tác GroupDocs.Parser trong C#, Java và Python"

  items:
    # items loop
    - title: "Cách trích xuất văn bản từ tài liệu PDF"
      content: "API GroupDocs.Parser giúp bạn dễ dàng trích xuất văn bản từ tài liệu bằng một vài bước."
      samples:
          # samples loop
          - language: "C#"
            color: "blue"
            content: |
              ```csharp {style=abap}  
                // Tạo một thể hiện của lớp Parser và truyền tệp mong muốn
                using (var parser = new Parser("source.pdf"))
                {
                    // Trích xuất văn bản
                    using (var textReader = parser.GetText())
                    {
                        // Xử lý văn bản đã trích xuất
                        Console.WriteLine(textReader?.ReadToEnd());
                    }
                }     
              ```
          # samples loop
          - language: "Java"
            color: "red"
            content: |
              ```java {style=abap}
                // Tạo một thể hiện của lớp Parser và truyền tệp mong muốn
                try (Parser parser = new Parser("source.pdf"))
                {
                    // Trích xuất văn bản
                    try (TextReader reader = parser.getText())
                    {
                        // Xử lý văn bản đã trích xuất
                        System.out.println(reader == null 
                                ? "" 
                                : reader.readToEnd());
                    }
                }  
              ```
          # samples loop
          - language: "Python"
            color: "green"
            content: |
              ```python {style=abap}
                from groupdocs.parser import Parser

                # Tạo một thể hiện của lớp Parser và truyền tệp mong muốn
                with Parser("source.pdf") as parser:
                    # Trích xuất văn bản
                    text = parser.get_text()

                    # Xử lý văn bản đã trích xuất
                    print(text)
              ```
############################# Supported Formats ###############################
formats:
  enable: true
  title: "Hơn 50 định dạng tài liệu và hình ảnh được hỗ trợ"
  description: "SDK Trình Phân Tích Tài Liệu GroupDocs.Parser cho phép thực hiện các thao tác phân tích trên tài liệu Office, PDF, hình ảnh, email, lưu trữ và hơn thế nữa."

############################# Metrics ###############################
metrics:
  enable: true
  title: "GroupDocs.Parser thành tựu"
  description: "Khám phá các chỉ số chính về thành tựu của thư viện của chúng tôi"

  items:
    # items loop
    - number: "50+"
      title: "Định dạng được hỗ trợ"
      content: "GroupDocs.Parser hỗ trợ các thao tác với hơn 50 định dạng tệp phổ biến."

    # items loop
    - number: "1600k"
      title: "Lượt tải xuống NuGet"
      content: "Gói NuGet GroupDocs.Parser cho .NET đã được tải xuống hơn 1.600.000 lần."

    # items loop
    - number: "18k"
      title: "Lượt tải xuống Maven"
      content: "GroupDocs.Parser đã có 18.000 lượt tải xuống trên Maven. Tính năng phân tích Java mạnh mẽ."

    # items loop
    - number: "140+"
      title: "Khách hàng hài lòng"
      content: "Các công ty nổi tiếng cũng như các nhà phát triển cá nhân đều ưu tiên các sản phẩm của GroupDocs để xây dựng các giải pháp sáng tạo."


############################# Customers ###############################
customers:
  enable: true
  title: "Khách hàng hài lòng của chúng tôi"
  description: "GroupDocs được các thương hiệu danh tiếng và nổi tiếng trên toàn cầu sử dụng."

  items:
    # items loop
    - title: "BenQ Corporation"
      logo: "benq"
      
    # items loop
    - title: "Nasdaq Stock Market"
      logo: "nasdaq"
      
    # items loop
    - title: "AT&T Inc."
      logo: "att"
      
    # items loop
    - title: "Customer logo AstraZeneca"
      logo: "astrazeneca"
      
    # items loop
    - title: "Central Bank of Argentina"
      logo: "argentinacentralbank"
      
    # items loop
    - title: "Roche Holding AG"
      logo: "roche"
      
    # items loop
    - title: "Capita"
      logo: "capita"
      
    # items loop
    - title: "Axa S.A."
      logo: "axa"
      
    # items loop
    - title: "Instructure Inc."
      logo: "instructure"
      
    # items loop
    - title: "Wipro"
      logo: "wipro"


############################# Actions ###############################
actions:
  enable: true
  title: "Sẵn sàng bắt đầu?"
  description: "Dùng thử các tính năng của GroupDocs.Parser miễn phí trên nền tảng của bạn"

  items:
    # items loop
    - title: ".NET"
      color: "blue"
      link: "/parser/net/"

    # items loop
    - title: "Java"
      color: "red"
      link: "/parser/java/"

############################# FAQ ###############################
faq:
  enable: true
  title: "Câu hỏi thường gặp"
  description: "Câu trả lời cho các câu hỏi thường gặp nhất."

  items:
    # items loop
    - question: "Thư viện GroupDocs.Parser có cần bất kỳ phần mềm bên thứ ba nào khác để xử lý tài liệu không?"
      answer: "GroupDocs.Parser không yêu cầu cài đặt bất kỳ phần mềm bên ngoài nào như Adobe Acrobat, Microsoft Office hoặc bất kỳ phần mềm nào khác."

    # items loop
    - question: "Tôi có thể dùng thử thư viện GroupDocs.Parser trước khi mua không?"
      answer: "Có, bạn có thể dùng thử GroupDocs.Parser mà không cần mua giấy phép. Khi được cài đặt không có giấy phép, thư viện sẽ hoạt động ở chế độ dùng thử. Trong chế độ này, các nhãn dán dùng thử được thêm vào tài liệu kết quả và tài liệu sẽ được cắt giảm chỉ còn 3 trang đầu. Nếu bạn muốn kiểm tra GroupDocs.Parser mà không bị giới hạn của phiên bản dùng thử, bạn cũng có thể yêu cầu giấy phép tạm thời 30 ngày. Để biết thêm chi tiết, [xem](https://purchase.groupdocs.com/temporary-license/)."

    # items loop
    - question: "Bạn có những loại giấy phép nào?"
      answer: "Chúng tôi cung cấp một số loại giấy phép để đáp ứng nhu cầu của các nhà phát triển hoặc công ty cụ thể. Các loại giấy phép phụ thuộc vào số lượng nhà phát triển, số địa điểm nơi các nhà phát triển làm việc và việc bạn có cần cung cấp SDK/API của chúng tôi cho khách hàng cuối hay không. Ngoài ra, bạn có thể chọn giấy phép theo mức sử dụng hàng tháng (Metered) dựa trên lượng sử dụng sản phẩm. Tìm hiểu thêm [tại đây](https://purchase.groupdocs.com/pricing/parser/net/)."

############################# Cloud Links ###############################
cloud_links:
  enable: true
  title: "GroupDocs.Parser API Phân tích Tài liệu low‑code"
  description: "Tích hợp khả năng phân tích tài liệu vào bất kỳ ứng dụng nào bằng cách sử dụng REST API và SDK dựa trên đám mây của chúng tôi."
  
  items:
    # items loop
    - title: "GroupDocs.Parser Cloud for cURL"
      content: "Các lệnh cURL cho API Đám mây phân tích tài liệu RESTful để phân tích tài liệu trên nhiều định dạng tệp phổ biến được hỗ trợ."
      icon: "groupdocs_parser-for-curl"
      link: "https://products.groupdocs.cloud/parser/curl"

    # items loop
    - title: "GroupDocs.Parser Cloud for .NET"
      content: "Trích xuất hình ảnh, văn bản, thông tin tài liệu hoặc thậm chí phân tích bất kỳ tài liệu nào bằng mẫu do người dùng định nghĩa trong các ứng dụng Microsoft .NET của bạn."
      icon: "groupdocs_parser-for-net"
      link: "https://products.groupdocs.cloud/parser/net"

    # items loop
    - title: "GroupDocs.Parser Cloud for Java"
      content: "SDK đám mây cho các nhà phát triển Java để phân tích tài liệu, trích xuất thông tin và dữ liệu tài liệu trong các ứng dụng dựa trên Java."
      icon: "groupdocs_parser-for-java"
      link: "https://products.groupdocs.cloud/parser/java"

############################# App links ###############################
app_links:
  enable: true
  title: "GroupDocs.Parser Ứng dụng Phân tích Tài liệu Không cần mã"
  description: "Các ứng dụng phân tích tài liệu dựa trên web cho phép bạn trích xuất dữ liệu từ hơn 50 định dạng tệp phổ biến trực tiếp trong trình duyệt."

  items:
    # items loop
    - title: "GroupDocs.Parser Total"
      content: "Ứng dụng trực tuyến miễn phí để phân tích Word, Excel, PowerPoint, PDF và hơn 50 loại tài liệu khác."
      icon: "groupdocs_parser-app"
      link: "https://products.groupdocs.app/parser/total"

    # items loop
    - title: "GroupDocs.Parser DOCX"
      content: "Phân tích tài liệu Word trực tiếp từ trình duyệt web của bạn để trích xuất hình ảnh, văn bản hoặc siêu dữ liệu."
      icon: "groupdocs_words-app"
      link: "https://products.groupdocs.app/parser/docx"

    # items loop
    - title: "GroupDocs.Parser PDF"
      content: "Ứng dụng phân tích PDF miễn phí hoạt động trên bất kỳ nền tảng hoặc thiết bị nào mà không có bất kỳ giới hạn nào."
      icon: "groupdocs_pdf-app"
      link: "https://products.groupdocs.app/parser/pdf"


      


---