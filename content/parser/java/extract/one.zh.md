---
############################# Static ############################
layout: "auto-gen-gist"
draft: false
path: "zh/parser/java/extract/one/"
otherformats: DOC DOT DOCX DOCM DOTX DOTM TXT ODT OTT RTF PDF XHTML MHTML MD XML EPUB FB2 CHM XLS XLT XLSX XLSM XLSB XLTX XLTM ODS CSV OTS XLA XLAM PPT PPTX  PPS POT PPSX PPTM POTX PPSM ODP OTP PST OST EML EMLX MSG 

############################# Head ############################
head_title: "通过 Java API 从文档、页面或页面区域中提取超链接"
head_description: "GroupDocs.Parser Java API 允许开发人员从文档、文档页面或 Excel、PowerPoint、PDF、Outlook 等的特定页面区域中提取超链接。"

############################# Header ############################
title: "Java API 从文档、页面或特定页面区域中提取超链接 "
description: "GroupDocs.Parser Java API 允许开发人员从文档、文档页面或 PDF、DOCX、PPTX、EML、MSG、XLS、XLSX、CSV、RTF、EPUB 等的特定页面区域中提取超链接，从而使他们的工作变得轻松。"

######################### Download Button #######################
button:
    enable: true

############################# About ############################
about:
    enable: true
    title: "如何通过 Java 从各种文档中提取超链接？"
    content: |
       该网页解释了如何仅使用几行 Java 代码从不同类型的文档、文档页面或页面的特定区域解析和提取超链接。 超链接对于在页面或网站之间导航非常有用，可以指向整个文档或文档中的特定部分、图形、声音、电子邮件地址等。 GroupDocs.Parser for Java 是一个非常强大的 API，它允许软件开发人员解析文档并从他们自己的 Java 应用程序中的各种流行文档中提取文本和元数据。 它包含几个高级功能，用于从 PDF、电子邮件、电子书、Microsoft Office 格式等各种文档类型中提取文本和超链接：Word（DOC、DOCX）、PowerPoint（PPT、PPTX）、Excel（XLS、XLSX）、LibreOffice 格式 还有很多。

############################# content ############################
steps:
    enable: true
    block:
    - title_left: "如何从 ONE 文档中提取超链接"
      content_left: |
       GroupDocs.Parser Java 包含从 ONE 文档中提取超链接的功能。 以下 Java 代码示例显示了如何从 ONE 文档中提取超链接。 

      title_right: "通过 Java 提取超链接"
      content_right: |
        * 创建 [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser) 的实例
        * 检查文档是否支持超链接提取
        * 从文档中提取超链接
        * 调用 [GetHyperlinks](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getHyperlinks()) 方法从整个文档中提取所有超链接。
        * 遍历超链接并打印超链接 URL

      gisthash: "036de701f5f17a02dd2353ee547afd5b"
      gistfile: "extract_hyperlinks_form_documents.java"

    - title_left: "如何从 ONE 文档页面中提取超链接"
      content_left: |
       GroupDocs.Parser .NET 允许软件开发人员使用几行代码从 ONE 文档中提取超链接。 下面的 C# .NET 代码显示了 ONE 文档中的超链接提取。 

      title_right: "通过 Java 提取超链接"
      content_right: |
        * 创建 [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser) 的实例
        * 检查文档是否支持超链接提取
        * 通过调用 [getDocumentInfo][https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getDocumentInfo()) 方法获取文档信息。
        * 遍历页面并打印页码
        * 从文档中提取超链接
        * 调用 [GetHyperlinks](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getHyperlinks()) 方法从整个文档中提取所有超链接。
        * 遍历超链接并打印超链接 URL
     
      gisthash: "bcca6319f2287edb7295443c1def46ee"
      gistfile: "extract_hyperlinks_form_documents_page.java"
      
    - title_left: "从 ONE 文档页面区域提取超链接"
      content_left: |
       GroupDocs.Parser Java API 提供了从 ONE 文档的页面轻松提取超链接的完整支持。 下面的 Java 代码展示了程序员如何从他们自己的 Java 应用程序中的 ONE 文档页面区域中提取超链接。

      title_right: "如何使用 Java 提取超链接？"
      content_right: |
        *创建 [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser)  的实例
        * 检查文档是否支持超链接提取
        * 创建用于超链接提取的选项
        * 调用 [GetHyperlinks](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getHyperlinks()) 方法从整个文档中提取所有超链接。
        * 遍历超链接并打印超链接 URL
     
      gisthash: "4aefff1fcc6733c0fc12b736d7e36711"
      gistfile: "hyperlinks_extraction_from_document_page_area.java"

    - title_left: "系统要求"
      content_left: |
        所有主要平台和操作系统都支持 Java 的 GroupDocs.Parser。 它可以生成 Microsoft Word、Excel、PowerPoint、Outlook、OpenOffice 和 50 多种其他格式的文档。 有关完整的系统要求指南，请在执行以下代码之前访问系统要求，请确保您的系统上安装了以下先决条件：
        * 操作系统：Microsoft Windows、Linux、MacOS
        * Java 版本支持：J2SE 7.0 (1.7)、J2SE 8.0 (1.8) 或以上
        * 从 GroupDocs [Repository](https://repository.groupdocs.com/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs-parser) 获取最新版本的 GroupDocs.Assembly Java API
        
      title_right: "为什么使用 GroupDocs.Assembly"
      content_right: |
        * 从任何支持的文档中提取纯文本。
        * 目录提取支持
        * 提取格式化文本、元数据、图像、容器和附件。
        * 通过用户定义的模板解析文档。
        *使用关键字或正则表达式搜索文本。
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