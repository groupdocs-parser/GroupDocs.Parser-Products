---
############################# Static ############################
layout: "auto-gen-gist"
draft: false
path: "zh/parser/java/extract/table/eml/"
otherformats: DOC DOT DOCX DOCM DOTX DOTM TXT ODT OTT RTF PDF XHTML MHTML MD XML EPUB FB2 CHM XLS XLT XLSX XLSM XLSB XLTX XLTM ODS CSV OTS XLA XLAM PPT PPTX  PPS POT PPSX PPTM POTX PPSM ODP OTP PST OST EMLX MSG ONE 

############################# Head ############################
head_title: "从各种文档（Excel、Word、PDF）中提取表格的 Java API"
head_description: "GroupDocs.Parser Java API 提供了从 PDF、DOCX、PPTX、EML、MSG、XLSX、CSV、ODT、RTF 和 EPUB 文档和页面中提取表格的完整功能。"

############################# Header ############################
title: "用于从 PDF、Excel、Word、电子邮件等文档中提取表格的 Java API"
description: "GroupDocs.Parser Java API 使软件程序员能够从 PDF、DOCX、PPTX、EML、MSG、XLSX、CSV、ODT、RTF、EPUB 等文档中提取表格。"

######################### Download Button #######################
button:
    enable: true

############################# About ############################
about:
    enable: true
    title: "如何通过 Java API 从流行文档文件格式中提取表格？"
    content: |
     表格是组织成行和列的单元格网格，可用于以视觉上吸引人的方式有效地向读者展示数据或信息。表格在组织文档中的数据方面起着非常重要的作用，并具有许多有用的好处，例如信息分组、按行或列排列数据、制作列表、组织整个句子的布局、在文档中定位图像、突出数据中的趋势或模式以及很快。 GroupDocs.Parser for Java API 使软件工程师和开发人员能够创建强大的 Java 应用程序来处理各种文档类型。它可用于从一些流行的文档格式中提取表格、文本和图像，例如 PDF、电子邮件、电子书、Word（DOC、DOCX）、PowerPoint（PPT、PPTX）、Excel（XLS、XLSX）、电子邮件（ EML、MSG）格式等等。 Java API 提供了对文档中与表格管理相关的几个重要功能的支持，例如从文档中提取所有表格或特定表格，从特定文档页面获取表格，表格单元格数据提取，获取表格行总数和列，获取行高，打印表格数据等。 

############################# content ############################
steps:
    enable: true
    block:
    - title_left: "使用 Java 代码从 EML 文档中提取表 "
      content_left: |
       GroupDocs.Parser Java API 包含对处理各种文档类型和从中提取数据的完整支持。 下面的 Java 代码示例展示了软件程序员如何通过几行代码从 EML 文档中提取表格。 

      title_right: "从 EML 文档中提取表格"
      content_right: |
        * 创建 [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser) 的实例
        * 检查是否支持表格提取
        * 创建表格布局
        * 创建表格提取的选项
        * 调用 [getTables(options)](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getTables(com.groupdocs.parser.options.PageTableAreaOptions)) 方法提取表格 整个文档。
        * 遍历行和列
        * 提取和打印表格单元格文本

      gisthash: "dda6d3d4866e63ae1614d86dd847fecd"
      gistfile: "tables_extraction_form_documents.cs"

    - title_left: "如何从 EML 文档的页面中提取表格"
      content_left: |
       GroupDocs.Parser Java API 允许计算机程序员用几行 Java 代码从 EML 文档的页面中提取表格。 它将检查文档是否存在表格，然后从特定文档页面中提取表格。 以下示例演示了 Java 开发人员如何轻松地在 EML 文档中执行表提取。  

      title_right: "Extract Document's Tables via Java"
      content_right: |
        * 创建 [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser) 的实例
        * 检查是否支持表格提取
        * 创建表格布局
        * 创建从文档页面提取表格的选项
        * 通过 [getDocumentInfo)](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getDocumentInfo()) 获取文档信息
        * 检查文档是否存在页面
        * 从文档页面中提取表格
        * 调用 [getTables(options)](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getTables(com.groupdocs.parser.options.PageTableAreaOptions)) 方法提取表格 整个文档。
        * 遍历表、行和列
        * 提取和打印表格单元格文本
     
      gisthash: "2dc42054bba3abdc297c63f4534281d8"
      gistfile: "tables_extraction_form_documents_page.cs"
      
    - title_left: "系统要求"
      content_left: |
       所有主要平台和操作系统都支持 Java 的 GroupDocs.Parser。 它可以生成 Microsoft Word、Excel、PowerPoint、Outlook、OpenOffice 和 50 多种其他格式的文档。 有关完整的系统要求指南，请在执行以下代码之前访问系统要求，请确保您的系统上安装了以下先决条件：
        * 操作系统：Microsoft Windows、Linux、MacOS
        * Java 版本支持：J2SE 7.0 (1.7)、J2SE 8.0 (1.8) 或以上
        * 从 GroupDocs [Repository](https://repository.groupdocs.com/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs-parser) 获取最新版本的 GroupDocs.Parser Java API
        
      title_right: "为什么使用 GroupDocs.Parser"
      content_right: |
        * 从任何受支持的文档中提取纯文本。
        * 目录提取支持
        * 提取格式化文本、元数据、图像、容器和附件。
        * 通过用户定义的模板解析文档。
        * 使用关键字或正则表达式搜索文本。
        * 结构化文本提取支持
        * 提取一些支持的文档格式的目录。
        * 从 PDF 文档中解析表单数据。

demos:
    enable: true
        

more_formats:
    enable: true


back_to_top:
    enable: true
---