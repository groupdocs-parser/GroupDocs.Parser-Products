---
############################# Static ############################
layout: "family"
date:  2024-02-13T17:01:03
draft: false

product: "Parser"
product_tag: "parser"

lang: zh

############################# Head ############################
head_title: ".NET、Java、云 API 和在线文档解析器应用"
head_description: "获取适用于 .NET、Java 和基于云的应用程序的一体化文档解析解决方案。使用简单的拖放功能在线从文档格式中提取数据"

############################# Header ############################
title: "文档解析解决方案"
description: |
  用于从各种文件格式中提取数据的强大 API。

  以最少的编码工作来解析文档。

  自定义解析结果。

############################# Supported Platforms ###############################
supported_platforms:
  enable: true
  head_title: "选择您的平台"
  title: "平台独立性"
  description: "GroupDocs.Parser 库支持以下操作系统和框架："
  details_link_title: "了解更多"

  items:
    # items loop
    - title: ".NET"
      description: GroupDocs.Parser 为了 .NET 
      color: "blue"
      tag: "net"
      link: "/parser/net/"
      features_link: "https://docs.groupdocs.com/parser/net/system-requirements/"
      features:
          # features loop
          - rows: "4"
            content: |
                    .NET Framework 4.6.2 or higher
                    .NET Core 2.0 or higher
                    .NET 6.0 or higher
      
          # features loop
          - rows: "1"
            content: |
                    Windows, Linux, Mac OS
      
          # features loop
          - rows: "3"
            content: |
                    Microsoft Visual Studio
                    JetBrains Rider
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats
      

    # items loop
    - title: "Java"
      description: GroupDocs.Parser 为了 Java
      color: "red"
      tag: "java"
      link: "/parser/java/"
      features_link: "https://docs.groupdocs.com/parser/java/system-requirements/"
      features:
          # features loop
          - rows: "4"
            content: |
                    Java 8 or higher
                    Kotlin
      
          # features loop
          - rows: "1"
            content: |
                    Windows, Linux, Mac OS
      
          # features loop
          - rows: "3"
            content: |
                    IntelliJ IDEA
                    Eclipse
                    NetBeans
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats

############################# Features ###############################
features:
  enable: true
  title: "GroupDocs.Parser 一目了然"
  description: "用于跨 PDF、Word、Excel 等进行数据解析的 API。"

  items:
    # items loop
    - icon: "text"
      title: "提取文本"
      content: "从各种文件格式中提取文本信息。"

    # items loop
    - icon: "image"
      title: "提取图像"
      content: "从不同来源检索视觉内容。"

    # items loop
    - icon: "template"
      title: "通过模板解析数据"
      content: "创建自定义模板并利用它们来解析特定信息。"

    # items loop
    - icon: "pdf"
      title: "解析 PDF 表单"
      content: "PDF 表单是数字文档，具有用于用户交互的可填写字段。"

############################# Code Samples ###############################
code_samples:
  enable: true
  title: "GroupDocs.Parser 代码示例"
  description: "C# 和 Java 中典型 GroupDocs.Parser 操作的一些用例。"

  items:
    # items loop
    - title: "如何从 PDF 文档中提取文本"
      content: "GroupDocs.Parser API 使 C# 开发者只需执行几个简单的步骤即可轻松从文档中提取文本。"
      samples:
          # samples loop
          - language: "C#"
            color: "blue"
            content: |
              <pre>
              // Create an instance of Parser class
              using (var parser = new Parser(fileName))
              {
                  // Extract a text into the reader
                  using (var textReader = parser.GetText())
                  {
                      // Print a text from the document
                      Console.WriteLine(textReader?.ReadToEnd());
                  }
              }
              </pre>
          # samples loop
          - language: "Java"
            color: "red"
            content: |
              <pre>
              // Create an instance of Parser class
              try (Parser parser = new Parser(fileName)) {
                  // Extract a text into the reader
                  try (TextReader reader = parser.getText()) {
                      // Print a text from the document
                      System.out.println(reader == null 
                              ? "" 
                              : reader.readToEnd());
                  }
              }
              <pre>

############################# Supported Formats ###############################
formats:
  enable: true
  title: "支持 50 多种文件格式"
  description: "GroupDocs.Parser 支持各种格式系列中的解析器操作。"

############################# Metrics ###############################
metrics:
  enable: false
  title: "详细的指标和统计见解"
  description: "探索对我们关键人物的彻底分析，提供有关我们的成就、影响力和扩张的全面指标和统计见解。"

  items:
    # items loop
    - number: "50+"
      title: "支持的格式"
      content: "该 API 可容纳 50 多种最广泛使用的文件和文档格式。"

    # items loop
    - number: "700k"
      title: "NuGet下载"
      content: "GroupDocs.Parser for .NET 通过 NuGet 软件包管理器获得了超过 80 万次下载。"

    # items loop
    - number: "15k"
      title: "Maven 下载"
      content: "GroupDocs.Parser for Java 已从我们的 Maven 存储库累积超过 15000 次下载。"


############################# Customers ###############################
customers:
  enable: true
  title: "我们满意的客户"
  description: "GroupDocs 图书馆被世界各地的全球知名和杰出品牌所采用。"

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
  title: "准备好开始了吗？"
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
  title: "经常问的问题"
  description: "最常见问题的解答。"

  items:
    # items loop
    - question: "GroupDocs.Parser 库是否需要任何其他第三方软件来操作文档？"
      answer: "GroupDocs.Parser 不需要安装任何外部软件，例如 Adob​​e Acrobat、Microsoft Office 或任何其他软件。"

    # items loop
    - question: "我可以在购买之前试用 GroupDocs.Parser 库吗？"
      answer: "是的，您可以尝试 GroupDocs.Parser，而无需购买许可证。一旦在没有许可证的情况下安装，该库就会以试用模式运行。在此模式下，试用徽章将添加到生成的文档中，并被修剪到前 3 页。如果您希望不受试用版限制地测试 GroupDocs.Parser，您还可以请求 30 天的临时许可证。有关更多详细信息，请参阅 [purchase.groupdocs.com/temporary-license/](https://purchase.groupdocs.com/temporary-license/)"

    # items loop
    - question: "您拥有什么许可证？"
      answer: "我们提供多种许可证类型来满足特定开发商或公司的需求。许可证类型取决于开发人员的数量、开发人员站点位置的数量以及您是否需要向最终客户提供我们的 SDK/API。或者，您可以根据产品的每月使用情况选择计量许可证。了解更多信息，请访问 [purchase.groupdocs.com/policies/](https://purchase.groupdocs.com/policies/)"

############################# Cloud Links ###############################
cloud_links:
  enable: true
  title: "GroupDocs.Parser 低代码 API"
  description: "使用我们基于云的 REST API 将文档解析器功能合并到任何应用程序中。"
  
  items:
    # items loop
    - title: "GroupDocs.Parser Cloud for cURL"
      content: "cURL 命令用于REST完整的文档解析器 Cloud API，可解析各种受支持的流行文件格式的文档。"
      icon: "groupdocs_parser-for-curl"
      link: "https://products.groupdocs.cloud/parser/curl"

    # items loop
    - title: "GroupDocs.Parser Cloud for .NET"
      content: "在 Microsoft .NET 应用程序中提取图像、文本、文档信息，甚至通过用户定义的模板解析任何文档。"
      icon: "groupdocs_parser-for-net"
      link: "https://products.groupdocs.cloud/parser/net"

    # items loop
    - title: "GroupDocs.Parser Cloud for Java"
      content: "Cloud SDK 供 Java 开发者在基于 Java 的应用程序中解析文档、提取文档信息和数据。"
      icon: "groupdocs_parser-for-java"
      link: "https://products.groupdocs.cloud/parser/java"

############################# App links ###############################
app_links:
  enable: true
  title: "GroupDocs.Parser NoCode 应用"
  description: "基于 Web 的应用程序，使您能够直接在浏览器中对 50 多种流行的文件格式进行解析。"

  items:
    # items loop
    - title: "GroupDocs.Parser Total"
      content: "免费在线应用程序可解析 Word、Excel、PowerPoint、PDF 及 30 多种文档类型。"
      icon: "groupdocs_parser-app"
      link: "https://products.groupdocs.app/parser/total"

    # items loop
    - title: "GroupDocs.Parser DOCX"
      content: "直接从网络浏览器解析 Word 文档以提取图像、文本或元数据。"
      icon: "groupdocs_words-app"
      link: "https://products.groupdocs.app/parser/docx"

    # items loop
    - title: "GroupDocs.Parser PDF"
      content: "免费的 PDF 解析应用程序，可在任何平台或设备上运行，没有任何限制。"
      icon: "groupdocs_pdf-app"
      link: "https://products.groupdocs.app/parser/pdf"     


---