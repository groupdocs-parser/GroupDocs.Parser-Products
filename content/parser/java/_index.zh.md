---
############################# Static ############################
layout: "landing"
date: 2025-12-09T14:10:41
draft: false

lang: zh
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

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
head_title: "GroupDocs.Parser for Java 文档解析 SDK for Java"
head_description: "针对 Java 的高性能文档解析 SDK。可从 PDF、Word、Excel、电子邮件以及 50 多种文档格式中提取文本、图像、元数据、条形码、表格等数据。"

############################# Header ############################
title: "适用于 Java 的文档解析 SDK"
description: "为您的 Java 应用添加快速、精确的文档解析功能，提取文档和图像中的文本、图像、元数据以及结构化数据。"
words:
  for: "用于"

actions:
  main: "Maven 下载"
  main_link: "https://releases.groupdocs.com/java/repo/com/groupdocs/groupdocs-parser/"
  alt: "授权"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/java/"
  title: "准备开始了吗？"
  description: "免费试用 GroupDocs.Parser 功能或申请许可证"

release:
  title: "版本 {0} 已发布"
  notes: "查看新增功能"
  downloads: "下载"

code:
  title: "使用 SDK 快速解析文档内容"
  more: "更多示例"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java/"
  install: |
    <dependency>
      <groupId>com.groupdocs</groupId>
      <artifactId>groupdocs-parser</artifactId>
      <version>{0}</version>
    </dependency>
  content: |
    ```java {style=abap}  
    // 将源文件传递给 Parser 实例
    try (Parser parser = new Parser("source.pdf"))
    {
        // 将文档文本传递给 TextReader
        try (TextReader reader = parser.getText())
        {
            // 处理文档文本
            System.out.println(reader == null 
                ? "" 
                : reader.readToEnd());
        }
    }
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser 一览"
  description: "用于在 Java 应用中执行高精度文档解析的 Document Parser SDK"
  features:
    # feature loop
    - title: "从文档中提取数据"
      content: "GroupDocs.Parser for Java API 使您能够从包括 Office 文档、电子邮件、附件和归档在内的广泛文件格式中检索文本、元数据和图像。此强大工具帮助您高效访问和处理这些文件中包含的有价值信息，可用于数据分析、搜索引擎索引或内容管理系统等多种应用。"

    # feature loop
    - title: "解析文档"
      content: "从 PDF 表单中提取超链接、表格、二维码、条形码和数据等各种元素。此外，还可使用自定义模板解析文档中的任何所需信息。"

    # feature loop
    - title: "自定义结果"
      content: "Java API 允许您以原始、结构化、HTML 或 Markdown 等多种格式检索数据。此外，API 还提供搜索功能，可在文档文本中定位特定单词或短语。"

############################# Platforms ############################
platforms:
  enable: true
  title: "平台独立性"
  description: "GroupDocs.Parser for Java 支持以下操作系统、框架和软件包管理器"
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
    - title: "Eclipse"
      image: "eclipse"
    # platform loop
    - title: "IntelliJ"
      image: "intellij"
    # platform loop
    - title: "Windows"
      image: "windows"
    # platform loop
    - title: "Linux"
      image: "linux"
    # platform loop
    - title: "Maven"
      image: "maven"

############################# File formats ############################
formats:
  enable: true
  title: "支持的文件格式"
  description: |
    GroupDocs.Parser for Java 支持以下 [文件格式](https://docs.groupdocs.com/parser/java/supported-document-formats/)的操作。
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
        ### 图像及其他格式
        * **可移植:** PDF 
        * **图像:** JPG, BMP, PNG, TIFF, GIF
        * **其他办公格式:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### 其他格式
        * **Web:** HTML, MHTML 
        * **归档文件:** ZIP, TAR, 7Z 
        * **电子书:** CHM, EPUB, FB2, MOBI 
        
        

############################# Features ############################
features:
  enable: true
  title: "GroupDocs.Parser for Java 功能"
  description: "使用我们的 Java Document Parser SDK，快速且准确地从 PDF、Office 文档、图像及其他格式中提取数据。"

  items:
    # feature loop
    - icon: "text"
      title: "提取文本"
      content: "从各种文件格式（如 Office 文档、PDF 文件和图像）中提取文本信息，便于阅读和分析。"

    # feature loop
    - icon: "image"
      title: "提取图像"
      content: "从 Office 文档、PDF 文件等多种来源检索视觉内容，以便轻松访问和使用。"

    # feature loop
    - icon: "qr"
      title: "扫描二维码"
      content: "检测并解码 Office 文档、PDF 文件或视觉内容中存在的二维码，实现高效的信息检索。"

    # feature loop
    - icon: "email"
      title: "从电子邮件附件和归档文件中提取数据"
      content: "从电子邮件、文件附件和压缩数据源中收集有价值的信息，以便进行有效的分析和利用。"

    # feature loop
    - icon: "table"
      title: "提取表格"
      content: "识别并提取 PDF 文档中的表格数据，以便进行有条理的分析和使用。"

    # feature loop
    - icon: "hyperlink"
      title: "提取超链接"
      content: "在 Office 文档或 PDF 文件中定位并提取超链接和电子邮件地址，以实现高效访问。"

    # feature loop
    - icon: "pdf"
      title: "解析 PDF 表单"
      content: "PDF 表单是具有可填写字段的数字文档，供用户交互并电子方式输入信息。.NET API 可用于从这些表单中提取数据，以实现高效处理。"

    # feature loop
    - icon: "template"
      title: "通过模板解析数据"
      content: "创建自定义模板并使用 .NET API 对 PDF 文件中的特定信息进行解析，从而简化数据提取过程。"

    # feature loop
    - icon: "search"
      title: "在文档中搜索文本"
      content: "快速定位文档中的特定词语或模式。"


############################# Code samples ############################
code_samples:
  enable: true
  title: "代码示例"
  description: "常见 GroupDocs.Parser for Java 操作的使用案例"
  items:
    # code sample loop
    - title: "从 PDF 文档中提取图像"
      content: |
        GroupDocs.Parser for Java 让 Java 开发者轻松从[文档](https://docs.groupdocs.com/parser/java/extract-images-from-documents/)中提取图像：
        {{< landing/code title="在 Java 中从 PDF 文档提取图像">}}
        ```java {style=abap}
        // 创建 Parser 类的实例
        try (Parser parser = new Parser("source.pdf"))
        {
            // 提取图像
            Iterable<PageImageArea> images = parser.getImages();

            // 检查是否成功提取
            if (images == null) {
                return;
            }

            // 遍历图像
            for (PageImageArea image : images) {
                // 打印页面索引、矩形区域和图像类型
                System.out.println(String.format("Page: %d, R: %s, Type: %s", 
                    image.getPage().getIndex(), image.getRectangle(), image.getFileType()));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "从图像中提取条形码"
      content: |
        使用我们的 Java API 从图像中提取 [条形码](https://docs.groupdocs.com/parser/java/extract-barcodes-from-document/)：
        {{< landing/code title="在 Java 中从图像提取条形码">}}
        ```java {style=abap}   
        // 将源图像加载到 Parser
        try (Parser parser = new Parser("source.jpg")){

            // 检查文件是否支持条形码提取
            if (!parser.getFeatures().isBarcodes()) {

                // 从文件中提取条形码
                Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();

                // 遍历条形码
                for (PageBarcodeArea barcode : barcodes) {
                    // 打印页面索引
                    System.out.println("Page: " + barcode.getPage().getIndex());
                    // 打印条形码值
                    System.out.println("Value: " + barcode.getValue());
                }
            }
        }
        ```
        {{< /landing/code >}}

---
