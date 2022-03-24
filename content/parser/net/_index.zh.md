---
############################# Static ############################
layout: "product"
date: 2021-04-27T09:31:06+03:00
draft: false

product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: ".NET 解析 API 从 PDF Word Excel 中提取文本图像元数据"
head_description: "C# .NET 文档解析 API，用于从数据库、PDF、Word、Excel、演示文稿、Web、电子邮件、EPUB 和 zip 文件格式中提取文本、图像、元数据和编码."

############################# Header ############################
title: ".NET API 来提取文档数据"
description: "从 .NET 应用程序中的文档、电子表格、演示文稿、电子邮件和档案中提取图像、原始或格式化文本和元数据。"
button:
    enable: true

############################# SubMenu ############################
submenu:
    enable: true
    
    left:
        img_alt: "GroupDocs.Parser for .NET"
        image: "/border/groupdocs-parser-net.svg"
        product: "GroupDocs.Parser"
        platform: ".NET"

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
            - link: "https://purchase.groupdocs.com/pricing/parser/net"
              text: "价钱"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/net/"
        link_buy: "https://purchase.groupdocs.com"

############################# 概述 ############################
overview:
    enable: true
    content: |
      GroupDocs.Parser for .NET 是一个文本、元数据和图像提取器 API，用于使用 C#、ASP.NET 和其他 .NET 技术开发的业务应用程序。它支持从支持格式的文件中提取原始、格式化和结构化文本以及元数据。通过 GroupDocs.Parser for .NET，您的应用程序还可以对流行格式的受密码保护的文档进行解析，例如文字处理文档、Excel 电子表格、PowerPoint 演示文稿、OneNote、PDF 文件和 ZIP 档案。
    tabs:
      enable: true
      
      ## TAB ONE ##
      tab_one:
        description: |
          以下是 .NET 的 GroupDocs.Parser 的概述：
      
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
          GroupDocs.Parser for .NET 支持以下 [文档文件格式](https://docs.groupdocs.com/parser/net/supported-document-formats/)：

        left:
          enable: true
          table:
            # table loop
            - title: "文本提取"
              content: |
                * **文本**：DOC、DOCX、DOT、DOTM、DOTX、DOCM、RTF、ODT、OTT、TXT、MD、WordprocessingML (XML)
                * **电子表格**：XLS、XLSX、CSV、XLSM、XLSB、ODS、SpreadsheetML (XML)、XLT、XLTX、XLTM、OTS、XLA、XLAM、TSV
                * **演示文稿**：PPT、PPTX、PPTM、PPS、PPSX、PPSM、POT、POTX、POTM、ODP、OTP
                * **OneNote**：一个
                * **电子邮件**：MSG、EML、EMLX、PST、OST、MS EXCHANGE SERVER、POP、IMAP
                * **电子出版**：EPUB、FB2
                * **便携式文档**：PDF、PDF 包、加密 PDF
                * **基于DOM的**：XML、HTML、XHTML、MHTML
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
          GroupDocs.Parser for .NET 支持以下操作系统、框架和包管理器:
        
        left:
          enable: true
          table:
            # table loop
            - icon: "fab fa-windows"
              title: "操作系统"
              content: |
                * Windows Desktop
                * Windows Server
                * Windows Azure
                * Linux

            # table loop
            - icon: "fas fa-code"
              title: "支持的框架"
              content: |
                * .NET Framework 2.0 或更高版本
                * Mono 框架 1.2 或更高版本
                * .NET 标准 2.0
                * .NET Core 2.0

        right:
          enable: true
          table:
            # table loop
            - icon: "fas fa-box"
              title: "包管理器"
              content: |
                * NuGet

            # table loop
            - icon: "fas fa-tools"
              title: "开发环境"
              content: |
                * Microsoft Visual Studio
                * Xamarin.Android
                * Xamarin.IOS
                * Xamarin.Mac
                * MonoDevelop

############################# 特征 ############################
features:
    enable: true
    title: "GroupDocs.Parser for .NET 特征"

    feature:
      # feature loop
      - icon: "fas fa-copy"
        content: "统计单个或多个文件中的单词出现次数"

      # feature loop
      - icon: "fas fa-eye"
        content: "从 Excel 工作表和演示模板中提取文本和元数据"

      # feature loop
      - icon: "fas fa-bolt"
        content: "在不安装文档阅读器的情况下从文件或流中提取文本内容"
      
      # feature loop
      - icon: "fas fa-file-powerpoint"
        content: "使用快速或标准文本提取模式从文档中获取格式化文本"

      # feature loop
      - icon: "fas fa-code"
        content: "检测受密码保护的 XML 文档的媒体类型并从中提取文本"

      # feature loop
      - icon: "fas fa-cloud"
        content: "以编程方式从电子邮件和附件中获取格式化文本"

      # feature loop
      - icon: "fas fa-remove-format"
        content: "从 OneNote 文档的单页或多页中提取文本"

      # feature loop
      - icon: "fas fa-comment-slash"
        content: "从 PDF、MS Word、Excel 和演示文档中提取数据"

      # feature loop
      - icon: "fas fa-location-arrow"
        content: "从 PDF 表单中提取数据并从简单的 PDF 文件或 PDF 组合文档中提取文本"

      # feature loop
      - icon: "fas fa-border-all"
        content: "从 PowerPoint 演示文稿中获取格式化文本或从特定幻灯片中删除文本"

      # feature loop
      - icon: "fas fa-wrench"
        content: "从 Excel 电子表格的单元格、行和列中收集原始或格式化文本"

      # feature loop
      - icon: "fas fa-columns"
        content: "从 Word 文档中提取原始或 HTML 格式的文本"

      # feature loop
      - icon: "fas fa-file-word"
        content: "HTML Formatter 支持段落、超链接、字体、标题、列表和表格的格式化"

      # feature loop
      - icon: "fas fa-envelope"
        content: "从 EPUB、CHM、Markdown 和 FB2 文件中提取单个句子或整个文本"

      # feature loop
      - icon: "fas fa-print"
        content: "摘自数据库、PDF、EPUB、CHM 和文字处理文档的目录"

      # feature loop
      - icon: "fas fa-file-archive"
        content: "提取具有完整内容结构的文本并从文档中摘录突出显示的文本"

      # feature loop
      - icon: "fas fa-lock"
        content: "从文档中获取文本区域进行分析并从支持的文档格式中提取元数据"

      # feature loop
      - icon: "fas fa-file-code"
        content: "从支持的格式中获取所有或选定的图像并旋转提取的图像"
      
      # feature loop
      - icon: "fas fa-fill-drip"
        content: "从 Zip 档案和 OST 容器中的文件中取出文本并检测 ZIP 容器项目的文件类型"

      # feature loop
      - icon: "fas fa-file-excel"
        content: "从电子邮件容器（Exchange Web 服务器、POP3、IMAP）获取数据"

      # feature loop
      - icon: "fas fa-heading"
        content: "在文档中搜索简单文本、整个单词和正则表达式"

      # feature loop
      - icon: "fas fa-project-diagram"
        content: "准备文档模板，从文档中提取数据并分析数据字段和表格"

      # feature loop
      - icon: "fas fa-cube"
        content: "在文档中搜索和提取突出显示的表达式"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "使用纯文本格式化程序（简单和 ASCII）或 Markdown 格式化程序获取文本"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Markdown Formatter 支持字体、超链接、标题、列表和表格的格式化"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "使用边缘、角度和交叉点执行自定义格式以格式化纯文本"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "通过列分隔符移动表格布局和检测矩形区域中的表格"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "从 Microsoft Office 文件格式中的形状、艺术字对象和文本框中提取文本"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "将图像提取到文件 - 保存为 JPG、PNG、GIF、BMP、PNG 或 WEBP 格式"

    more_feature:
      # more_feature_loop
      - title: "从文档中提取文本"
        content: |
          使用 GroupDocs.Parser for .NET API 从文档中提取文本很简单，只需几行代码即可实现：

          ```cs
          // 创建 Parser 类的实例
          using(Parser parser = new Parser("sample.docx"))
          {
            // 将文本提取到阅读器中
            using(TextReader reader = parser.GetText())
            {
              // 打印文档中的文本
              // 如果不支持文本提取，则 reader 为 null
              Console.WriteLine(reader == null ? "Text extraction isn't supported." : reader.ReadToEnd());
            }
          }
          ```

############################# Support ############################
support:
    enable: true

############################# Solutions ############################
solutions:
    enable: true
    title: "GroupDocs.Parser 为其他流行的开发环境提供文档查看 API"

    solution:
        # solution loop
        - img_alt: "GroupDocs.Parser for Java"
          image: "/border/groupdocs-parser-java.svg"
          product: "GroupDocs.Parser"
          platform: "Java"
          link: "/parser/java/"

############################# Back to top ###############################
back_to_top:
  enable: true
---