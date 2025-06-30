---
############################# Static ############################
layout: "landing"
date: 2025-06-30T10:26:00
draft: false

lang: zh
product: "Parser"
product_tag: "parser"
platform: "Net"
platform_tag: "net"

############################# Drop-down ############################
supported_platforms:
  items:
    # supported_platforms loop
    - title: ".NET"
      tag: "net"
    # supported_platforms loop
    - title: "Java"
      tag: "java"

############################# Head ############################
head_title: "GroupDocs.Parser for .NET 文档解析应用程序"
head_description: "为 .NET 应用程序提供一体化文档解析解决方案。使用简单的拖放功能在线提取文档格式中的数据"

############################# Header ############################
title: "通过 .NET API 解析文档"
description: "使用我们的灵活 API 和基于应用的解决方案，从任何平台的文档和图像中提取数据。"
words:
  for: "用于"

actions:
  main: "Nuget 下载"
  main_link: "https://www.nuget.org/packages/GroupDocs.Parser"
  alt: "许可"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/net/"
  title: "准备开始吗？"
  description: "免费试用 GroupDocs.Parser 功能或申请许可证"

release:
  title: "版本 {0} 已发布"
  notes: "查看新功能"
  downloads: "下载"

code:
  title: "快速解析文档内容"
  more: "更多示例"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
  install: "dotnet add package GroupDocs.Parser"
  content: |
    ```csharp {style=abap}   
    // 将源文件传递给 Parser 实例
    using (var parser = new Parser("source.pdf"))
    {
        // 将文档文本传递给 TextReader
        using (var textReader = parser.GetText())
        {
            // 处理文档文本
            Console.WriteLine(textReader?.ReadToEnd());
        }
    }  
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser 一览"
  description: "在 .NET 应用程序中执行文档解析的 API"
  features:
    # feature loop
    - title: "从文档中提取数据"
      content: "GroupDocs.Parser for .NET API 使您能够从各种文件格式（如办公文档、电子邮件、附件和档案）中检索文本、元数据和图像。这个强大的工具可以帮助您高效访问和处理这些文件中包含的有价值的信息，适用于数据分析、搜索引擎索引或内容管理系统等多种应用。"

    # feature loop
    - title: "解析文档"
      content: "提取超链接、表格、二维码、条形码和 PDF 表单中的数据等各种元素。还可以使用自定义模板解析文档中的任何所需信息。"

    # feature loop
    - title: "自定义结果"
      content: ".NET API 可以让您以原始、结构化、HTML 或 Markdown 等多种格式检索数据。此外，API 提供搜索功能，以便在文档的文本中查找特定单词或短语。"

############################# Platforms ############################
platforms:
  enable: true
  title: "平台独立性"
  description: "GroupDocs.Parser for .NET 支持以下操作系统、框架和包管理器"
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
  title: "支持的文件格式"
  description: |
    GroupDocs.Parser for .NET 支持与以下 [文件格式](https://docs.groupdocs.com/parser/net/supported-document-formats/) 的操作。
  groups:
    # group loop
    - color: "green"
      content: |
        ### Microsoft Office 格式
        * **Word:** DOCX, DOC, DOCM, DOT, DOTX, DOTM, RTF
        * **Excel:** XLSX, XLS, XLSM, XLSB, XLTM, XLT, XLTM, XLTX, XLAM, SXC, SpreadsheetML
        * **PowerPoint:** PPT, PPTX, PPS, PPSX, PPSM, POT, POTM, POTX, PPTM
    # group loop
    - color: "blue"
      content: |
        ### 图像与其他格式
        * **可移植:** PDF 
        * **图像:** JPG, BMP, PNG, TIFF, GIF
        * **其他办公格式:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### 其他格式
        * **网络:** HTML, MHTML 
        * **档案:** ZIP, TAR, 7Z 
        * **电子书:** CHM, EPUB, FB2, MOBI 
        
        

############################# Features ############################
features:
  enable: true
  title: "GroupDocs.Parser for .NET 功能"
  description: "快速准确地从 PDF、办公文档和图像中提取数据"

  items:
    # feature loop
    - icon: "text"
      title: "提取文本"
      content: "从各种文件格式（如办公文档、PDF 文件和图像）中提取文本信息，以便进行阅读和分析。"

    # feature loop
    - icon: "image"
      title: "提取图像"
      content: "从办公文档、PDF 文件等不同来源检索视觉内容，以便于访问和使用。"

    # feature loop
    - icon: "qr"
      title: "扫描二维码"
      content: "检测并解码存在于办公文档、PDF 文件或视觉内容中的二维码，以便高效地获取信息。"

    # feature loop
    - icon: "email"
      title: "从电子邮件附件和档案中提取数据"
      content: "从电子邮件消息、文件附件和压缩数据源中收集有价值的信息，以便高效分析和利用。"

    # feature loop
    - icon: "table"
      title: "提取表格"
      content: "从 PDF 文档中识别并提取表格数据，以便进行有组织的分析和使用。"

    # feature loop
    - icon: "hyperlink"
      title: "提取超链接"
      content: "在办公文档或 PDF 文件中查找并提取超链接和电子邮件地址，以便高效访问。"

    # feature loop
    - icon: "pdf"
      title: "解析 PDF 表单"
      content: "PDF 表单是数字文档，具有可供用户交互填写的字段，允许他们以电子方式输入信息。可以利用 .NET API 提取这些表单中的数据，以便高效处理。"

    # feature loop
    - icon: "template"
      title: "按模板解析数据"
      content: "创建自定义模板，并结合 .NET API 使用，以从 PDF 文件中解析特定信息，从而简化数据提取流程。"

    # feature loop
    - icon: "search"
      title: "在文档中搜索文本"
      content: "快速定位文档中的特定单词或模式。"


############################# Code samples ############################
code_samples:
  enable: true
  title: "代码示例"
  description: "一些典型 GroupDocs.Parser for .NET 操作的用例"
  items:
    # code sample loop
    - title: "从 PDF 文档中提取图像"
      content: |
        GroupDocs.Parser for .NET 简化了 C# 开发人员从 [文档](https://docs.groupdocs.com/parser/net/extract-images-from-documents/) 中提取图像的过程：
        {{< landing/code title="在 C# 中从 PDF 文档中提取图像">}}
        ```csharp {style=abap}
        // 创建一个 Parser 类的实例
        using (var parser = new Parser("source.pptx"))
        {
            // 提取图像
            var images = parser.GetImages();

            // 检查是否有图像被提取
            if (images == null)
            {
                return;
            }
            // 遍历图像
            foreach (PageImageArea image in images)
            {
                // 打印页面索引、矩形和图像类型
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Type: {2}", 
                    image.Page.Index, image.Rectangle, image.FileType));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "从图像中提取条形码"
      content: |
        使用我们的 .NET API 从图像中提取 [条形码](https://docs.groupdocs.com/parser/net/extract-barcodes-from-document/)：
        {{< landing/code title="在 C# 中从图像中提取条形码">}}
        ```csharp {style=abap}   
        // 将源图像加载到 Parser
        using (var parser = new Parser("source.jpg"))
        {
            // 检查文件是否支持条形码提取
            if (parser.Features.Barcodes)
            {
                // 从文件中提取条形码
                var barcodes = parser.GetBarcodes();

                // 遍历条形码
                foreach (var barcode in barcodes)
                {
                    // 打印页面索引
                    Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                    // 打印条形码值
                    Console.WriteLine("Value: " + barcode.Value);
                }
            }
        }
        ```
        {{< /landing/code >}}

---
