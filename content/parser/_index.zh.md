---
############################# Static ############################
layout: "family"
date:  2025-12-09T14:52:35
draft: false

product: "Parser"
product_tag: "parser"

lang: zh

############################# Head ############################
head_title: "适用于 PDF、Word 和 Excel 的文档解析 SDK | GroupDocs"
head_description: "文档解析 SDK，用于从 PDF、Word、Excel、电子邮件以及 50 多种其他文档格式中提取文本、图像、元数据、条形码和表格，适用于 .NET、Java 和 Python 应用程序。"

############################# Header ############################
title: "文档解析 SDK"
description:  |
  面向开发者的文档解析 SDK，可从 50 多种文档和图像格式中提取文本、图像、条形码、元数据和表格。

  在 .NET、Java 和 Python 应用程序中集成高性能文档解析，代码编写工作量最小化。

  使用灵活的模板和高级 API 定制解析规则，并提供干净、结构化的数据输出。

############################# Supported Platforms ###############################
supported_platforms:
  enable: true
  head_title: "选择你的平台"
  title: "平台独立性"
  description: "GroupDocs.Parser 库支持以下操作系统和框架："
  details_link_title: "了解更多"

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
  title: "GroupDocs.Parser 一览"
  description: "强大的文档解析 SDK，可从 PDF、Office 文档、图像、电子邮件和归档文件中提取结构化和非结构化数据。"

  items:
    # items loop
    - icon: "text"
      title: "提取文本"
      content: "从各种文件格式中提取文本信息"

    # items loop
    - icon: "image"
      title: "提取图像"
      content: "从多种来源获取视觉内容"

    # items loop
    - icon: "template"
      title: "通过模板解析数据"
      content: "创建自定义模板并利用其解析特定信息"

    # items loop
    - icon: "pdf"
      title: "解析 PDF 表单"
      content: "PDF 表单是带有可填写字段的数字文档，用于用户交互"

############################# Code Samples ###############################
code_samples:
  enable: true
  title: "GroupDocs.Parser 代码示例"
  description: "在 C#, Java 和 Python 中的典型 GroupDocs.Parser 操作用例"

  items:
    # items loop
    - title: "如何从 PDF 文档中提取文本"
      content: "GroupDocs.Parser API 通过几个步骤即可轻松从文档中提取文本。"
      samples:
          # samples loop
          - language: "C#"
            color: "blue"
            content: |
              ```csharp {style=abap}  
                // 创建 Parser 类的实例并传入所需文件
                using (var parser = new Parser("source.pdf"))
                {
                    // 提取文本
                    using (var textReader = parser.GetText())
                    {
                        // 处理提取的文本
                        Console.WriteLine(textReader?.ReadToEnd());
                    }
                }     
              ```
          # samples loop
          - language: "Java"
            color: "red"
            content: |
              ```java {style=abap}
                // 创建 Parser 类的实例并传入所需文件
                try (Parser parser = new Parser("source.pdf"))
                {
                    // 提取文本
                    try (TextReader reader = parser.getText())
                    {
                        // 处理提取的文本
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

                # 创建 Parser 类的实例并传入所需文件
                with Parser("source.pdf") as parser:
                    # 提取文本
                    text = parser.get_text()

                    # 处理提取的文本
                    print(text)
              ```
############################# Supported Formats ###############################
formats:
  enable: true
  title: "支持 50 多种文档和图像格式"
  description: "GroupDocs.Parser 文档解析 SDK 可在 Office 文档、PDF、图像、电子邮件、归档文件等多种类型上执行解析操作。"

############################# Metrics ###############################
metrics:
  enable: true
  title: "GroupDocs.Parser 成就"
  description: "了解我们库的关键指标和成就"

  items:
    # items loop
    - number: "50+"
      title: "支持的格式"
      content: "GroupDocs.Parser 支持超过 50 种主流文件格式的操作。"

    # items loop
    - number: "1600k"
      title: "NuGet 下载量"
      content: "GroupDocs.Parser 的 .NET NuGet 包已下载超过 1,600,000 次。"

    # items loop
    - number: "18k"
      title: "Maven 下载量"
      content: "GroupDocs.Parser 在 Maven 上已下载 18,000 次，具备强大的 Java 解析功能。"

    # items loop
    - number: "140+"
      title: "满意的客户"
      content: "知名企业和独立开发者都倾向于使用 GroupDocs 产品构建创新解决方案。"


############################# Customers ###############################
customers:
  enable: true
  title: "我们的满意客户"
  description: "GroupDocs 库被全球知名且卓越的品牌所采用。"

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
  title: "准备开始了吗？"
  description: "在您的平台上免费试用 GroupDocs.Parser 功能"

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
  title: "常见问题"
  description: "对最常见问题的回答。"

  items:
    # items loop
    - question: "GroupDocs.Parser 库是否需要其他第三方软件来处理文档？"
      answer: "GroupDocs.Parser 不需要安装任何外部软件，例如 Adobe Acrobat、Microsoft Office 或其他软件。"

    # items loop
    - question: "我可以在购买前试用 GroupDocs.Parser 库吗？"
      answer: "是的，您可以在不购买许可证的情况下试用 GroupDocs.Parser。未授权安装后，库将以试用模式运行。在此模式下，生成的文档会添加试用徽章，并截取前 3 页。如果您希望在不受试用版限制的情况下测试 GroupDocs.Parser，还可以申请 30 天的临时许可证。更多详情，请[查看](https://purchase.groupdocs.com/temporary-license/)。"

    # items loop
    - question: "您提供哪些许可证？"
      answer: "我们提供多种许可证类型，以满足特定开发者或公司的需求。许可证类型取决于开发者人数、开发者站点位置数量，以及是否需要向最终客户交付我们的 SDK/API。您也可以根据产品的月度使用量选择计量许可证。了解更多信息，请[点击此处](https://purchase.groupdocs.com/pricing/parser/net/)。"

############################# Cloud Links ###############################
cloud_links:
  enable: true
  title: "GroupDocs.Parser 低代码文档解析 API"
  description: "使用我们的基于云的 REST API 和 SDK，将文档解析功能集成到任何应用程序中。"
  
  items:
    # items loop
    - title: "GroupDocs.Parser Cloud for cURL"
      content: "cURL 命令用于 RESTful 文档解析云 API，可解析跨多种受支持的流行文件格式的文档。"
      icon: "groupdocs_parser-for-curl"
      link: "https://products.groupdocs.cloud/parser/curl"

    # items loop
    - title: "GroupDocs.Parser Cloud for .NET"
      content: "在您的 Microsoft .NET 应用程序中，提取图像、文本、文档信息，甚至通过用户自定义模板解析任何文档。"
      icon: "groupdocs_parser-for-net"
      link: "https://products.groupdocs.cloud/parser/net"

    # items loop
    - title: "GroupDocs.Parser Cloud for Java"
      content: "面向 Java 开发者的云 SDK，用于在基于 Java 的应用程序中解析文档、提取文档信息和数据。"
      icon: "groupdocs_parser-for-java"
      link: "https://products.groupdocs.cloud/parser/java"

############################# App links ###############################
app_links:
  enable: true
  title: "GroupDocs.Parser 文档解析无代码应用"
  description: "基于网页的文档解析应用，让您直接在浏览器中从超过 50 种流行文件格式提取数据。"

  items:
    # items loop
    - title: "GroupDocs.Parser Total"
      content: "免费在线应用，可解析 Word、Excel、PowerPoint、PDF 等 50 多种文档类型。"
      icon: "groupdocs_parser-app"
      link: "https://products.groupdocs.app/parser/total"

    # items loop
    - title: "GroupDocs.Parser DOCX"
      content: "直接在网页浏览器中解析 Word 文档，提取图像、文本或元数据。"
      icon: "groupdocs_words-app"
      link: "https://products.groupdocs.app/parser/docx"

    # items loop
    - title: "GroupDocs.Parser PDF"
      content: "免费 PDF 解析应用，可在任何平台或设备上使用，且没有任何限制。"
      icon: "groupdocs_pdf-app"
      link: "https://products.groupdocs.app/parser/pdf"


      


---