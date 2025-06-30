---
############################# Static ############################
layout: "family"
date:  2025-06-30T10:26:00
draft: false

product: "Parser"
product_tag: "parser"

lang: zh

############################# Head ############################
head_title: ".NET、Java、云 API 和在线文档解析器应用程序"
head_description: "为 .NET、Java 和基于云的应用程序提供一体化文档解析解决方案。使用简单的拖放功能从文档格式中提取数据"

############################# Header ############################
title: "文档解析解决方案"
description:  |
  用于从各种文件格式中提取数据的强大 API。

  以最小的编码工作量解析文档。

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
  title: "GroupDocs.Parser 一览"
  description: "跨 PDF、Word、Excel 等进行数据解析的 API"

  items:
    # items loop
    - icon: "text"
      title: "提取文本"
      content: "从各种文件格式中提取文本信息"

    # items loop
    - icon: "image"
      title: "提取图像"
      content: "从不同来源检索视觉内容"

    # items loop
    - icon: "template"
      title: "按模板解析数据"
      content: "创建自定义模板并利用它们解析特定信息"

    # items loop
    - icon: "pdf"
      title: "解析 PDF 表单"
      content: "PDF 表单是带有可供用户交互填写的字段的数字文档"

############################# Code Samples ###############################
code_samples:
  enable: true
  title: "GroupDocs.Parser 代码示例"
  description: "一些典型 GroupDocs.Parser 操作的用例，使用 C# 和 Java"

  items:
    # items loop
    - title: "如何从 PDF 文档中提取文本"
      content: "GroupDocs.Parser API 通过实现几个步骤使提取文本变得简单。"
      samples:
          # samples loop
          - language: "C#"
            color: "blue"
            content: |
                    <code class="language-csharp" data-lang="csharp">

                        // 创建一个 Parser 类的实例并传入所需的文件
                        using (var parser = new Parser("source.pdf"))
                        {
                            // 提取文本
                            using (var textReader = parser.GetText())
                            {
                                // 处理提取的文本
                                Console.WriteLine(textReader?.ReadToEnd());
                            }
                        }     
                        
                    </code>

          # samples loop
          - language: "Java"
            color: "red"
            content: |
                    <code class="language-java" data-lang="java">

                        // 创建一个 Parser 类的实例并传入所需的文件
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

                    </code>


############################# Supported Formats ###############################
formats:
  enable: true
  title: "支持 50 种以上文件格式"
  description: "GroupDocs.Parser 可在各种格式族中进行解析操作"

############################# Metrics ###############################
metrics:
  enable: true
  title: "GroupDocs.Parser 成就"
  description: "发现我们的库成功的关键指标"

  items:
    # items loop
    - number: "50+"
      title: "支持的格式"
      content: "GroupDocs.Parser 支持操作超过 50 种流行的文件格式。"

    # items loop
    - number: "1600k"
      title: "NuGet 下载量"
      content: "GroupDocs.Parser 的 .NET NuGet 包下载次数超过 1,600,000 次。"

    # items loop
    - number: "18k"
      title: "Maven 下载量"
      content: "GroupDocs.Parser 在 Maven 上有 18,000 次下载。强大的 Java 解析功能。"

    # items loop
    - number: "140+"
      title: "满意的客户"
      content: "许多知名公司和独立开发者都选择 GroupDocs 产品来构建创新的解决方案。"


############################# Customers ###############################
customers:
  enable: true
  title: "我们的满意客户"
  description: "GroupDocs 库被全球众多知名品牌广泛使用。"

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
  title: "准备开始吗？"
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
  description: "对常见问题的回答。"

  items:
    # items loop
    - question: "GroupDocs.Parser 库需要其他第三方软件来处理文档吗？"
      answer: "GroupDocs.Parser 无需安装任何外部软件，例如 Adobe Acrobat、Microsoft Office 或其他。"

    # items loop
    - question: "我可以在购买之前尝试 GroupDocs.Parser 库吗？"
      answer: "是的，您可以在未购买许可证的情况下尝试 GroupDocs.Parser。在未授权的情况下安装时，该库将以试用模式工作。在此模式下，试用徽章会添加到生成的文档中，并且文档被截断为前 3 页。如果您希望在没有试用版限制的情况下测试 GroupDocs.Parser，您还可以申请 30 天的临时许可证。有关更多详情，[请看](https://purchase.groupdocs.com/temporary-license/)"

    # items loop
    - question: "你们有什么许可证？"
      answer: "我们提供几种许可证类型，以满足特定开发者或公司的需求。许可证类型取决于开发者人数、开发者网站地点数量，以及是否需要将我们的 SDK/API 交付给最终客户。或者，您可以选择基于产品每月使用量的计量许可证。了解更多[在这里](https://purchase.groupdocs.com/pricing/parser/net/)"

############################# Cloud Links ###############################
cloud_links:
  enable: true
  title: "GroupDocs.Parser 低代码 API"
  description: "利用我们的基于云的 REST API 将文档解析能力集成到任何应用程序中"
  
  items:
    # items loop
    - title: "GroupDocs.Parser Cloud for cURL"
      content: "用于 RESTful 文档解析器云 API 的 cURL 命令，可跨多种流行文件格式解析文档。"
      icon: "groupdocs_parser-for-curl"
      link: "https://products.groupdocs.cloud/parser/curl"

    # items loop
    - title: "GroupDocs.Parser Cloud for .NET"
      content: "在您的 Microsoft .NET 应用程序中提取图像、文本、文档信息，或者通过用户定义的模板解析任何文档。"
      icon: "groupdocs_parser-for-net"
      link: "https://products.groupdocs.cloud/parser/net"

    # items loop
    - title: "GroupDocs.Parser Cloud for Java"
      content: "为 Java 开发人员提供的云 SDK，用于解析文档、提取文档信息和数据。"
      icon: "groupdocs_parser-for-java"
      link: "https://products.groupdocs.cloud/parser/java"

############################# App links ###############################
app_links:
  enable: true
  title: "GroupDocs.Parser 无代码应用程序"
  description: "网页应用程序，使您能够直接在浏览器中解析超过 50 种流行文件格式。"

  items:
    # items loop
    - title: "GroupDocs.Parser Total"
      content: "免费的在线应用程序，用于解析 Word、Excel、PowerPoint、PDF 和 50 多种文档类型。"
      icon: "groupdocs_parser-app"
      link: "https://products.groupdocs.app/parser/total"

    # items loop
    - title: "GroupDocs.Parser DOCX"
      content: "直接从您的网页浏览器解析 Word 文档，以提取图像、文本或元数据。"
      icon: "groupdocs_words-app"
      link: "https://products.groupdocs.app/parser/docx"

    # items loop
    - title: "GroupDocs.Parser PDF"
      content: "适用于任何平台或设备的免费 PDF 解析应用程序，没有任何限制。"
      icon: "groupdocs_pdf-app"
      link: "https://products.groupdocs.app/parser/pdf"


      


---