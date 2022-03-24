---
############################# Static ############################
layout: "product"
date: 2021-04-27T09:31:06+03:00
draft: false

product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Java API 从 PDF Word Excel HTML 中解析文本、图像和元数据"
head_description: "Java 文档解析器 API，用于从数据库、Word、Excel、演示文稿、PDF、电子邮件、EPUB 和 ZIP 文件中提取文本、图像、元数据和编码."

############################# Header ############################
title: "用于提取数据的 Java Parser API"
description: "Java API，用于从文档、演示文稿、档案和电子邮件中解析和提取带有元数据的图像和文本。"
button:
    enable: true

############################# SubMenu ############################
submenu:
    enable: true
    
    left:
        img_alt: "GroupDocs.Parser for Java"
        image: "/border/groupdocs-parser-java.svg"
        product: "GroupDocs.Parser"
        platform: "Java"

    middle:
        button:
            # button loop
            - link: "#overview"
              text: "概述"

            # button loop
            - link: "#features"
              text: "特征"

            # button loop
            - link: "#support"
              text: "Support"

            # button loop
            - link: "https://products.groupdocs.app/parser"
              text: "Live Demo"

            # button loop
            - link: "https://purchase.groupdocs.com/pricing/parser/java"
              text: "价钱"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/java/"
        link_buy: "https://purchase.groupdocs.com"

############################# 概述 ############################
overview:
    enable: true
    content: |
      GroupDocs.Parser for Java 是一个文本、图像和元数据提取器 API，支持 50 多种流行的文档类型，以帮助构建具有解析原始、结构化和格式化文本功能的业务应用程序。它还支持使用预定义模板解析文档，并允许从发票和其他典型文档中快速准确地提取复杂数据。 GroupDocs.Parser for Java 使您能够从所有流行格式的受密码保护的文件中提取文本和元数据，包括文字处理文档、Excel 电子表格、PowerPoint 演示文稿、OneNote、PDF 文件和 ZIP 档案。
    tabs:
      enable: true     
      
      ## TAB ONE ##
      tab_one:
        description: |
          以下是 Java 的 GroupDocs.Parser 的概述：

        left:
          enable: true
          icon: "fas fa-tools"
          title: "特征"
          content: |
            * 提取图像
            * 提取原始文本
            * 提取格式化文本
            * 提取结构化文本
            * 提取元数据
            * 从 ZIP 文件中的文件中提取
            * 搜索提取
            * 使用文本格式化程序提取
            * 检测编码标准
            * 检测媒体类型
        
        right:
          enable: true
          icon: "fab fa-html5"
          title: "API"
          content: |
            * 获取输入文件
            * 获取原始或格式化文本
            * 获取元数据
      
      ## TAB TWO ##
      tab_two:
        description: |
          GroupDocs.Parser for Java 支持以下 [文档文件格式](https://docs.groupdocs.com/parser/java/supported-document-formats/)：

        left:
          enable: true
          table:
            # table loop
            - title: "文本提取"
              content: |
                * **文本**：DOC、DOCX、DOT、DOTM、DOTX、DOCM、RTF、ODT、OTT、TXT、MD、WordprocessingML (XML)
                * **电子表格**：XLS、XLSX、CSV、XLSM、XLSB、ODS、SpreadsheetML (XML)、XLT、XLTX、XLTM、OTS、XLA、、XLAM、TSV
                * **演示文稿**：PPT、PPTX、PPTM、PPS、PPSX、PPSM、POT、POTX、POTM、ODP、OTP
                * **OneNote**：一个
                * **电子邮件**：MSG、EML、EMLX、PST、OST、MS EXCHANGE SERVER、POP、IMAP
                * **电子出版**：EPUB、FB2
                * **便携式文档**：PDF、PDF 包、加密 PDF
                * **基于 DOM 的**：XML、HTML、XHTML、MHTML
                * **压缩和包装**：ZIP、CHM
                * **数据库**：ADO.NET

            # table loop
            - title: "编码检测"
              content: |
                * **BOM**：UTF32 LE、UTF32 BE、UTF16 LE、UTF16 BE、UTF8 和 UTF7
                * **内容**：UTF32 LE、UTF32 BE、UTF16 LE、UTF16 BE、UTF8 和 ANSI

        right:
          enable: true
          table:
            # table loop
            - title: "元数据提取"
              content: |
                * **文本**：DOC、DOCX、DOT、DOTX、DOTM、OTT、ODT
                * **电子表格**：XLS、XLSX、XLT、XLTX、XLTM、XLA、XLAM、OTS、ODS
                * **演示文稿**：PPT、PPTX、POT、POTX、POTM、PPSM、PPTM、OTP、ODP
                * **电子邮件**：味精、EML、EMLX
                * **电子出版**：EPUB、FB2
                * **其他**：PDF

            # table loop
            - title: "Text & 元数据提取"
              content: |
                * **模板**：DOTX、POTX
                * **启用宏的模板**：DOTM、POTM、PPSM、PPTM
                * **OpenDocument 模板**：OTT

            # table loop
            - title: "图像提取"
              content: |
                * **文本**：DOC、DOCX、DOCM、RTF、DOT、DOTM、DOTX、ODT
                * **电子表格**：XLS、XLSX、XLSM、XLSB、ODS、XLT、XLTM、XLTX
                * **演示文稿**：PPT、PPTX、PPTM、ODP、POT、POTM、POTX、PPS、PPSX、PPSM
                * **便携式文档**：PDF、POT、POTM、POTX
                * **电子书**：CHM、EPUB、FB2
                * **标记**：HTML

      ## TAB THREE ##
      tab_three:
        description: |
          GroupDocs.Parser for Java 支持以下操作系统、框架和包管理器:
        
        left:
          enable: true
          table:
            # table loop
            - icon: "fab fa-windows"
              title: "操作系统"
              content: |
                * Microsoft Windows Desktop
                * Microsoft Windows Server
                * Linux
                * MacOS

            # table loop
            - icon: "fas fa-code"
              title: "支持的框架"
              content: |
                * Java 7 (1.7) 及更高版本

        right:
          enable: true
          table:
            # table loop
            - icon: "fas fa-cogs"
              title: "开发环境"
              content: |
                * NetBeans
                * IntelliJ IDEA
                * Eclipse
            # table loop
            - icon: "fas fa-tools"
              title: "构建自动化工具"
              content: |
                * Maven

############################# 特征 ############################
features:
    enable: true
    title: "GroupDocs.Parser for Java 特征"

    feature:
      # feature loop
      - icon: "fas fa-copy"
        content: "统计单个或多个文档的单词出现次数"

      # feature loop
      - icon: "fas fa-eye"
        content: "从 Excel 电子表格和 PowerPoint 演示模板中提取文本和元数据"

      # feature loop
      - icon: "fas fa-bolt"
        content: "从文件或流中获取文本，无需安装文档阅读器"
      
      # feature loop
      - icon: "fas fa-file-powerpoint"
        content: "使用快速或标准文本提取模式从文档中提取格式化文本"

      # feature loop
      - icon: "fas fa-code"
        content: "检测受密码保护的 XML 文档的媒体类型并从中提取文本"

      # feature loop
      - icon: "fas fa-cloud"
        content: "以编程方式从 PowerPoint 演示文稿、电子邮件和附件中获取格式化文本"

      # feature loop
      - icon: "fas fa-remove-format"
        content: "从 OneNote 文档的单页或多页中删除文本"

      # feature loop
      - icon: "fas fa-comment-slash"
        content: "从简单的 PDF 文件或 PDF 组合文档中提取原始文本"

      # feature loop
      - icon: "fas fa-location-arrow"
        content: "从 PDF、MS Word、Excel 和演示文档中提取数据"

      # feature loop
      - icon: "fas fa-border-all"
        content: "从 Excel 电子表格的单元格、行和列中提取原始或格式化文本"

      # feature loop
      - icon: "fas fa-wrench"
        content: "从 Word 文档中收集原始或 HTML 格式的文本并从文档中摘录突出显示的文本"

      # feature loop
      - icon: "fas fa-columns"
        content: "从 PDF 表单中获取数据并从 PDF 或 Word 文档中获取格式化表格"

      # feature loop
      - icon: "fas fa-file-word"
        content: "从 EPUB、CHM、Markdown 和 FB2 文件中提取单个句子或整个文本"

      # feature loop
      - icon: "fas fa-envelope"
        content: "摘自数据库、PDF、EPUB、CHM 和文字处理文档的目录"

      # feature loop
      - icon: "fas fa-print"
        content: "从文档中检索文本区域以进行分析并提取内容结构完整的文本"

      # feature loop
      - icon: "fas fa-file-archive"
        content: "从支持的文档格式中获取元数据"

      # feature loop
      - icon: "fas fa-lock"
        content: "从支持的格式中提取所有或选定的图像并旋转提取的图像"

      # feature loop
      - icon: "fas fa-file-code"
        content: "从 Zip 档案和 OST 容器中的文件中提取文本 – Zip 容器项目的检测媒体类型"
      
      # feature loop
      - icon: "fas fa-fill-drip"
        content: "从电子邮件容器中获取数据（Exchange Web 服务器、POP3、IMAP）"

      # feature loop
      - icon: "fas fa-file-excel"
        content: "快速、可靠、高效地从数据库容器中提取文本"

      # feature loop
      - icon: "fas fa-heading"
        content: "在文档中查找简单文本、整个单词和正则表达式"

      # feature loop
      - icon: "fas fa-project-diagram"
        content: "准备文档模板，从文档中提取数据并分析数据字段和表格"

      # feature loop
      - icon: "fas fa-cube"
        content: "在文档中搜索和提取突出显示的表达式"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "使用纯文本格式化程序（简单和 ASCII）或使用边缘、角度和交叉点的自定义格式提取文本"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "使用 Markdown Formatter 获取和格式化文本（字体、超链接、标题、列表和表格）"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "使用 HTML 格式化程序获取文本并将格式化程序应用于段落、超链接、字体、标题、列表和表格"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "通过列分隔符移动表格布局和检测矩形区域中的表格"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "从微软办公软件文件格式中的形状、艺术字对象和文本框中提取文本"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "提取图像到文件 - 保存为 JPG、PNG、GIF、BMP、PNG 或 WEBP 格式"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "通过 JDBC 从电子邮件服务器和数据库中提取文本"

    more_feature:
      # more_feature_loop
      - title: "使用纯文本或 HTML 格式化程序获取文本"
        content: |
          使用 GroupDocs.Parser for Java，您可以将各种格式化程序应用于文本和 HTML。您可以使用纯文本格式化程序为简单和 ASCII 提取文本。您还可以使用 HTML Formatter 获取文本并将格式应用于段落、超链接、字体、标题、列表和表格。

############################# Support ############################
support:
    enable: true

############################# Solutions ############################
solutions:
    enable: true
    title: "GroupDocs.Parser 为其他流行的开发环境提供文档查看 API"

    solution:
        # solution loop
        - img_alt: "GroupDocs.Parser for .NET"
          image: "/border/groupdocs-parser-net.svg"
          product: "GroupDocs.Parser"
          platform: ".NET"
          link: "/parser/net/"

############################# Back to top ###############################
back_to_top:
  enable: true
---