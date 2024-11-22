---
############################# Static ############################
layout: "landing"
date: 2024-02-13T17:01:03
draft: false
#operation: 
#parsertype: 
#fileformat: 
#productName: Java
lang: "zh"
#productCode: java
#otherformats: 
#breadcrumb: Put  parser on  for Java
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: ".NET、Java、云 API 和在线文档解析器应用"
head_description: "获取适用于 .NET、Java 和基于云的应用程序的一体化文档解析解决方案。使用简单的拖放功能在线从文档格式中提取数据"

############################# Header ############################
title: "解析文档<br>通过 Java API"
description: "使用我们为程序员和最终用户提供的灵活 API 和基于应用程序的解决方案，从任何平台上的文档和图像中提取数据。"
words:
  for: "为了"

actions:
  main: "免费 Maven 下载"
  main_link: "https://releases.groupdocs.com/java/repo/com/groupdocs/groupdocs-parser/"
  alt: "许可"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/java"
  title: "准备好开始了吗？"
  description: "免费试用 GroupDocs.Parser 功能或申请许可"

release:
  title: "版本 {0} 已发布"
  notes: "看看有什么新鲜事"
  downloads: "下载"

code:
  title: "从 Java 中的 PDF 文件中提取文本"
  more: "更多示例"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java"
  install: |
    <dependency>
      <groupId>com.groupdocs</groupId>
      <artifactId>groupdocs-parser</artifactId>
      <version>{0}</version>
    </dependency>
  content: |
    ```java {style=abap}  
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
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser 概述"
  description: "用于在 Java 应用程序中执行文档解析的 API"
  features:
    # feature loop
    - title: "从文档中提取数据"
      content: "Java API 使您能够从各种文件格式（例如 Office 文档、电子邮件、附件和存档）中检索文本、元数据和图像。这个强大的工具可帮助您有效地访问和处理这些文件中包含的有价值的信息，以用于各种应用程序，例如数据分析、搜索引擎索引或内容管理系统。"

    # feature loop
    - title: "解析文档"
      content: "从PDF表单中提取各种元素，例如超链接、表格、二维码、条形码和数据。还可以使用自定义模板从文档中解析任何所需的信息。"

    # feature loop
    - title: "定制结果"
      content: "Java API 可让您检索各种格式的数据，例如原始格式、结构化格式、HTML 或 Markdown 格式。此外，API 还提供搜索功能，用于在文档文本中查找特定单词或短语。"

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
    GroupDocs.Parser for Java 支持以下[文件格式](https://docs.groupdocs.com/parser/java/supported-document-formats/) 的操作。
  groups:
    # group loop
    - color: "green"
      content: |
        ### Microsoft Office 格式
        * **Word:**  DOCX, DOC, DOCM, DOT, DOTX, DOTM, RTF
        * **Excel:** XLSX, XLS, XLSM, XLSB, XLTM, XLT, XLTM, XLTX, XLAM, SXC, SpreadsheetML
        * **PowerPoint:** PPT, PPTX, PPS, PPSX, PPSM, POT, POTM, POTX, PPTM
    # group loop
    - color: "blue"
      content: |
        ### 图像和其他格式
        * **Portable:** PDF
        * **图片:** JPG, BMP, PNG, TIFF, GIF, DICOM, WEBP
        * **其他办公形式:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
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
  title: "GroupDocs.Parser 功能"
  description: "快速准确地从 PDF、Office 文档和图像中提取数据。"

  items:
    # feature loop
    - icon: "text"
      title: "提取文本"
      content: "从各种文件格式（例如 Office 文档、PDF 文件和图像）中提取文本信息，以便于阅读和分析。"

    # feature loop
    - icon: "image"
      title: "提取图像"
      content: "从办公文档、PDF 文件等不同来源检索视觉内容，以便于访问和使用。"

    # feature loop
    - icon: "qr"
      title: "扫描二维码"
      content: "检测和解码办公文档、PDF 文件或视觉内容中存在的 QR 码，以实现高效的信息检索。"

    # feature loop
    - icon: "email"
      title: "从电子邮件附件和档案中提取数据"
      content: "从电子邮件、文件附件和压缩数据源中收集有价值的信息，以便进行有效分析和利用。"

    # feature loop
    - icon: "table"
      title: "提取表格"
      content: "从 PDF 文档中识别并提取表格数据，以便进行有组织的分析和使用。"

    # feature loop
    - icon: "hyperlink"
      title: "提取超链接"
      content: "找到并提取 Office 文档或 PDF 文件中的超链接和电子邮件地址，以便高效访问。"

    # feature loop
    - icon: "pdf"
      title: "解析 PDF 表单"
      content: "PDF 表单是数字文档，具有用于用户交互的可填写字段，允许用户以电子方式输入信息。 Java API 可用于从这些表单中提取数据，以便进行高效处理。"

    # feature loop
    - icon: "template"
      title: "通过模板解析数据"
      content: "创建自定义模板并通过 Java API 使用它们来解析 PDF 文件中的特定信息，从而简化数据提取过程。"

    # feature loop
    - icon: "search"
      title: "在文档中搜索文本"
      content: "快速定位文档中的特定单词或模式。"

############################# Code samples ############################
code_samples:
  enable: true
  title: "代码示例"
  description: "典型 GroupDocs.Parser for Java 操作的一些用例"
  items:
    # code sample loop
    - title: "从 PDF 文档中提取图像"
      content: |
        Java API 使 Java 开发者只需执行几个简单的步骤即可轻松从文档中提取图像。
        {{< landing/code title="从 Java 中的 PDF 个文档中提取图像">}}
        ```java {style=abap}
        // Create an instance of Parser class
        try (Parser parser = new Parser(fileName)) {
            // Extract images
            Iterable<PageImageArea> images = parser.getImages();
            // Check if images extraction is supported
            if (images != null) {
                int imageIndex = 0;
                // Iterate over images
                for (PageImageArea image : images) {
                    // Save the image to the file
                    image.save(String.format("%s%s", imageIndex, image.getFileType().getExtension()));
                }
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "从图像中提取条形码"
      content: |
        Java API 使 Java 开发者只需执行几个简单的步骤即可轻松从文档中提取条形码。
        {{< landing/code title="从图像中提取条形码">}}
        ```java {style=abap}   
        // Create an instance of Parser class
        try (Parser parser = new Parser(fileName)) {
            // // Check if the file supports barcode extracting
            if (!parser.getFeatures().isBarcodes()) {
                // Extract barcodes from the file.
                Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();
                // Iterate over barcodes
                for (PageBarcodeArea barcode : barcodes) {
                    // Print the page index
                    System.out.println("Page: " + barcode.getPage().getIndex());
                    // Print the barcode value
                    System.out.println("Value: " + barcode.getValue());
                }
            }
        }
        ```
        {{< /landing/code >}}

---
