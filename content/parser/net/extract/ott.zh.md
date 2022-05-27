---
############################# Static ############################
layout: "auto-gen-gist"
draft: false
path: "zh/parser/net/extract/ott/"
otherformats: DOC DOT DOCX DOCM DOTX DOTM TXT ODT OTT  PDF XHTML MHTML MD XML EPUB FB2 CHM XLS XLT XLSX XLSM XLSB XLTX XLTM ODS CSV OTS XLA XLAM PPT PPTX  PPS POT PPSX PPTM POTX PPSM ODP OTP PST OST EML EMLX MSG ONE 

############################# Head ############################
head_title: ".NET API 从文档、页面或页面区域解析和提取超链接"
head_description: "GroupDocs.Parser .NET API 使软件程序员能够从 PDF、DOCX、XLSX、CSV、PPTX、EML、MSG、EPUB 等的文档、页面或页面区域中提取超链接。"

############################# Header ############################
title: "通过 C#/VB.NET API 从文档、页面或特定页面区域中提取超链接"
description: "GroupDocs.Parser .NET API 允许软件开发人员从 PDF、DOC、DOCX、PPT、PPTX、EML、MSG、XLS、XLSX、CSV、ODT、RTF、EPUB 等的文档、页面或页面区域解析和提取超链接 文件。"

######################### Download Button #######################
button:
    enable: true

############################# About ############################
about:
    enable: true
    title: "如何通过 .NET 从文档或页面中解析和提取超链接？"
    content: |
       超链接是指向整个文档或文档中特定部分的一段文本或图像或图标。 超链接的使用允许用户导航到网页或文档。 通常需要从文档中提取超链接并使用它来访问外部文档或网页。 GroupDocs.Parser .NET API 是一个引人入胜的文档文本提取 API，它为实现文本和元数据提取解决方案提供了完整的功能。 它支持从 PDF、电子邮件、电子书、Microsoft Office 格式中提取文本和超链接：Word（DOC、DOCX）、PowerPoint（PPT、PPTX）、Excel（XLS、XLSX）、LibreOffice 格式等等。 它支持文档解析、提取纯文本和结构化文本、按关键字搜索文本、提取元数据或图像、容器以及附件等多种高级功能。
############################# content ############################
steps:
    enable: true
    block:
    - title_left: "通过 .NET 从 OTT 文档中提取超链接"
      content_left: |
       GroupDocs.Parser .NET 完全支持从 OTT 文档中提取超链接。 以下 C# .NET 代码示例演示了如何在 OTT 文档中提取超链接。

      title_right: "如何提取超链接"
      content_right: |
        * 创建 [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser) 的实例
        * 检查文档以获取超链接提取支持
        * 从文档中提取超链接
        * 调用 [GetHyperlinks](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/gehyperlinks) 方法从整个文档中提取所有超链接。
        * 遍历超链接并打印超链接 URL

      gisthash: "35be3a09e0135c65be790c42c5c86d37"
      gistfile: "Extract_hyperlinks_form_documents.cs"

    - title_left: "从 OTT 文档页面中提取超链接"
      content_left: |
       GroupDocs.Parser .NET 允许软件开发人员使用几行代码从 OTT 文档中提取超链接。 下面的 C# .NET 代码显示了 OTT 文档中的超链接提取。

      title_right: "通过 .NET 提取超链接"
      content_right: |
        * 创建 [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser) 的实例 
        * 检查文档以获取超链接提取支持
        * 通过调用[GetDocumentInfo](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/getdocumentinfo) 获取文档信息
        * 遍历页面并打印页码
        * 从文档中提取超链接
        * 调用 [GetHyperlinks](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/gehyperlinks) 方法从整个文档中提取所有超链接。
        * 遍历超链接并打印超链接 URL
     
      gisthash: "e71f8e39ba36ebf97034dfbf6fceeec1"
      gistfile: "hyperlinks_extraction_form_documents_page.cs"
      
    - title_left: "从 OTT 文档页面区域提取超链接"
      content_left: |
       GroupDocs.Parser .NET API 完全支持从 OTT 文档中轻松提取超链接。 以下 .NET 代码示例演示了如何从 OTT 文档页面区域中提取超链接。

      title_right: "如何使用 .NET 提取超链接"
      content_right: |
        * 创建 [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser) 的实例 
        * 检查文档以获取超链接提取支持
        * 创建用于超链接提取的选项
        * 调用 [GetHyperlinks](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/gehyperlinks) 方法从整个文档中提取所有超链接。
        * 遍历超链接并打印超链接 URL
     
      gisthash: "eefbede6f391ea44ddb6901edb353950"
      gistfile: "hyperlinks_extraction_from__documents_page_area.cs"

    - title_left: "系统要求"
      content_left: |
        所有主要平台和操作系统都支持 GroupDocs.Assembly .NET API。 如需完整的系统要求指南，请访问 [系统要求](hhttps://docs.groupdocs.com/parser/net/system-requirements/) 在执行以下代码之前，请确保您已安装以下先决条件 系统：
         * 操作系统：Microsoft Windows、Linux、MacOS
         * 开发环境：Visual Studio、Xamarin、MonoDevelop 等
         * 框架：.NET Framework、.NET Standard、.NET Core、Mono
         * 从 [NuGet](https://www.nuget.org/packages/GroupDocs.parser/) 获取最新版本的 GroupDocs.Assembly .NET API
        
      title_right: "为什么使用 GroupDocs.Assembly"
      content_right: |
        * 从任何受支持的文档中提取纯文本支持
        * 通过用户定义的模板解析文档。
        * 完全支持结构化文本提取
        * 通过关键字和正则表达式进行文本搜索
        * 提取格式化文本、元数据、图像、容器和附件。
        * 提取一些支持的文档格式的目录。
        * 从 PDF 文档中解析表单数据。
        * 从文档中提取超链接

demos:
    enable: true


more_formats:
    enable: true


back_to_top:
    enable: true
---