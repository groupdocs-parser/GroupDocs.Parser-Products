---
############################# Static ############################
layout: "family"
date:  2025-06-30T10:26:00
draft: false

product: "Parser"
product_tag: "parser"

lang: vi

############################# Head ############################
head_title: "Những ứng dụng phân tích tài liệu "
head_description: "Giải pháp phân tích tài liệu toàn diện cho các ứng dụng .NET, Java. Trích xuất dữ liệu từ các định dạng tài liệu trực tuyến bằng tính năng kéo và thả đơn giản."

############################# Header ############################
title: "Giải pháp phân tích tài liệu"
description:  |
  API mạnh mẽ để trích xuất dữ liệu từ các định dạng tệp khác nhau.

  Phân tích tài liệu với nỗ lực lập trình tối thiểu.

  Tùy chỉnh kết quả phân tích.

############################# Supported Platforms ###############################
supported_platforms:
  enable: true
  head_title: "Chọn nền tảng của bạn"
  title: "Tính độc lập của nền tảng"
  description: "Thư viện GroupDocs.Parser hỗ trợ các hệ điều hành và khung làm việc sau:"
  details_link_title: "Tìm hiểu thêm"

  items:
    # items loop
    - title: ".NET"
      description: GroupDocs.Parser .NET 
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
      description: GroupDocs.Parser Java
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

############################# Features ###############################
features:
  enable: true
  title: "GroupDocs.Parser tổng quan"
  description: "API để phân tích dữ liệu qua PDF, Word, Excel và nhiều hơn nữa"

  items:
    # items loop
    - icon: "text"
      title: "Trích xuất văn bản"
      content: "Trích xuất thông tin văn bản từ các định dạng tệp khác nhau"

    # items loop
    - icon: "image"
      title: "Trích xuất hình ảnh"
      content: "Lấy nội dung hình ảnh từ các nguồn đa dạng"

    # items loop
    - icon: "template"
      title: "Phân tích dữ liệu theo mẫu"
      content: "Tạo các mẫu tùy chỉnh và sử dụng chúng để phân tích thông tin cụ thể"

    # items loop
    - icon: "pdf"
      title: "Phân tích biểu mẫu PDF"
      content: "Biểu mẫu PDF là tài liệu số có các trường có thể điền để tương tác của người dùng"

############################# Code Samples ###############################
code_samples:
  enable: true
  title: "Ví dụ mã GroupDocs.Parser"
  description: "Một số trường hợp sử dụng các thao tác điển hình của GroupDocs.Parser trong C# và Java"

  items:
    # items loop
    - title: "Cách trích xuất văn bản từ tài liệu PDF"
      content: "API GroupDocs.Parser giúp trích xuất văn bản từ tài liệu bằng cách thực hiện một vài bước."
      samples:
          # samples loop
          - language: "C#"
            color: "blue"
            content: |
                    <code class="language-csharp" data-lang="csharp">

                        // Tạo một đối tượng của lớp Parser với tệp mong muốn
                        using (var parser = new Parser("source.pdf"))
                        {
                            // Trích xuất văn bản
                            using (var textReader = parser.GetText())
                            {
                                // Xử lý văn bản đã trích xuất
                                Console.WriteLine(textReader?.ReadToEnd());
                            }
                        }     
                        
                    </code>

          # samples loop
          - language: "Java"
            color: "red"
            content: |
                    <code class="language-java" data-lang="java">

                        // Tạo một đối tượng của lớp Parser với tệp mong muốn
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

                    </code>


############################# Supported Formats ###############################
formats:
  enable: true
  title: "Hơn 50 định dạng tệp được hỗ trợ"
  description: "GroupDocs.Parser cho phép thực hiện các thao tác phân tích trong nhiều gia đình định dạng khác nhau"

############################# Metrics ###############################
metrics:
  enable: true
  title: "GroupDocs.Parser thành tựu"
  description: "Khám phá các chỉ số chính của những thành tựu thư viện của chúng tôi"

  items:
    # items loop
    - number: "50+"
      title: "Các định dạng được hỗ trợ"
      content: "GroupDocs.Parser hỗ trợ các thao tác với hơn 50 định dạng tệp phổ biến."

    # items loop
    - number: "1600k"
      title: "Tải xuống NuGet"
      content: "Gói NuGet GroupDocs.Parser cho .NET đã được tải xuống hơn 1.600.000 lần."

    # items loop
    - number: "18k"
      title: "Tải xuống Maven"
      content: "GroupDocs.Parser có 18.000 lượt tải xuống trên Maven. Các tính năng phân tích Java mạnh mẽ."

    # items loop
    - number: "140+"
      title: "Khách hàng hài lòng"
      content: "Các công ty nổi tiếng cũng như các nhà phát triển cá nhân chọn sản phẩm của GroupDocs để xây dựng các giải pháp sáng tạo."


############################# Customers ###############################
customers:
  enable: true
  title: "Khách hàng hài lòng của chúng tôi"
  description: "Các thư viện của GroupDocs được sử dụng bởi các thương hiệu nổi tiếng và uy tín trên toàn cầu."

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
  description: "Thử các tính năng của GroupDocs.Parser miễn phí trên nền tảng của bạn"

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
  description: "Các câu trả lời cho những câu hỏi thường gặp nhất."

  items:
    # items loop
    - question: "Thư viện GroupDocs.Parser có cần bất kỳ phần mềm bên thứ ba nào khác để thao tác tài liệu không?"
      answer: "GroupDocs.Parser không yêu cầu cài đặt bất kỳ phần mềm bên ngoài nào như Adobe Acrobat, Microsoft Office, hay bất kỳ phần mềm nào khác."

    # items loop
    - question: "Tôi có thể thử thư viện GroupDocs.Parser trước khi mua không?"
      answer: "Có, bạn có thể thử GroupDocs.Parser mà không cần mua giấy phép. Khi được cài đặt mà không có giấy phép, thư viện hoạt động ở chế độ thử nghiệm. Trong chế độ này, có các huy hiệu thử nghiệm được thêm vào tài liệu kết quả, và nó bị cắt lại để chỉ 3 trang đầu tiên. Nếu bạn muốn thử GroupDocs.Parser mà không bị hạn chế của phiên bản thử nghiệm, bạn cũng có thể yêu cầu giấy phép tạm thời 30 ngày. Để biết thêm chi tiết, [xem](https://purchase.groupdocs.com/temporary-license/)"

    # items loop
    - question: "Các loại giấy phép bạn có là gì?"
      answer: "Chúng tôi cung cấp nhiều loại giấy phép khác nhau để phù hợp với nhu cầu của các nhà phát triển hoặc công ty cụ thể. Các loại giấy phép phụ thuộc vào số lượng nhà phát triển, số lượng địa điểm của nhà phát triển, và liệu bạn có cần giao SDK/API của chúng tôi cho khách hàng của bạn hay không. Ngoài ra, bạn có thể chọn giấy phép theo mức sử dụng hàng tháng của sản phẩm. Tìm hiểu thêm [tại đây](https://purchase.groupdocs.com/pricing/parser/net/)"

############################# Cloud Links ###############################
cloud_links:
  enable: true
  title: "API mã thấp của GroupDocs.Parser"
  description: "Kết hợp khả năng phân tích tài liệu vào bất kỳ ứng dụng nào bằng cách sử dụng REST API trên đám mây của chúng tôi."
  
  items:
    # items loop
    - title: "GroupDocs.Parser Cloud for cURL"
      content: "Lệnh cURL cho Cloud API phân tích tài liệu RESTful để phân tích các tài liệu qua nhiều định dạng tệp phổ biến được hỗ trợ."
      icon: "groupdocs_parser-for-curl"
      link: "https://products.groupdocs.cloud/parser/curl"

    # items loop
    - title: "GroupDocs.Parser Cloud for .NET"
      content: "Trích xuất hình ảnh, văn bản, thông tin tài liệu hoặc thậm chí phân tích bất kỳ tài liệu nào theo mẫu do người dùng định nghĩa trong các ứng dụng Microsoft .NET của bạn."
      icon: "groupdocs_parser-for-net"
      link: "https://products.groupdocs.cloud/parser/net"

    # items loop
    - title: "GroupDocs.Parser Cloud for Java"
      content: "SDK đám mây cho các nhà phát triển Java để phân tích các tài liệu, trích xuất thông tin tài liệu và dữ liệu trong các ứng dụng dựa trên Java."
      icon: "groupdocs_parser-for-java"
      link: "https://products.groupdocs.cloud/parser/java"

############################# App links ###############################
app_links:
  enable: true
  title: "GroupDocs.Parser Ứng dụng không mã"
  description: "Ứng dụng web cho phép bạn thực hiện phân tích qua hơn 50 định dạng tài liệu phổ biến trực tiếp trong trình duyệt của bạn."

  items:
    # items loop
    - title: "GroupDocs.Parser Total"
      content: "Ứng dụng trực tuyến miễn phí để phân tích Word, Excel, PowerPoint, PDF & hơn 50 loại tài liệu khác."
      icon: "groupdocs_parser-app"
      link: "https://products.groupdocs.app/parser/total"

    # items loop
    - title: "GroupDocs.Parser DOCX"
      content: "Phân tích tài liệu Word trực tiếp từ trình duyệt của bạn để trích xuất hình ảnh, văn bản hoặc siêu dữ liệu."
      icon: "groupdocs_words-app"
      link: "https://products.groupdocs.app/parser/docx"

    # items loop
    - title: "GroupDocs.Parser PDF"
      content: "Ứng dụng phân tích PDF miễn phí hoạt động trên bất kỳ nền tảng hoặc thiết bị nào mà không có giới hạn."
      icon: "groupdocs_pdf-app"
      link: "https://products.groupdocs.app/parser/pdf"


      


---