---
############################# Static ############################
layout: "auto-gen-gist"
draft: false
path: "zh/parser/net/extract/image/one/"
otherformats: DOC DOT DOCX DOCM DOTX DOTM TXT ODT OTT RTF PDF XHTML MHTML MD XML EPUB FB2 CHM XLS XLT XLSX XLSM XLSB XLTX XLTM ODS CSV OTS XLA XLAM PPT PPTX  PPS POT PPSX PPTM POTX PPSM ODP OTP PST OST EML EMLX MSG 

############################# Head ############################
head_title: "通过 .NET 从 Excel、Word、PDF 和其他文档或页面中提取图像"
head_description: "GroupDocs.Parser .NET API 使软件程序员能够从他们的 .NET 应用程序中的不同文档（例如 MS Excel、Word、PowerPoint、PDF 等）中提取图像。"

############################# Header ############################
title: "通过 C#.NET API 从 PDF、DOCX、PPTX、MSG、XLSX 文档和页面中提取图像"
description: "GroupDocs.Parser .NET API 允许程序员从 PDF、DOC、DOCX、PPT、PPTX、EML、MSG、XLS、XLSX、CSV、ODT、RTF 和 EPUB 文档或文档页面中提取图像。"

######################### Download Button #######################
button:
    enable: true

############################# About ############################
about:
    enable: true
    title: "如何通过 .NET 从文档或页面区域中提取图像？"
    content: |
       图像可用于以无法用文字表达的方式传递信息。 图像帮助我们抓住用户的注意力并轻松解释棘手的概念。 有时在阅读文档、期刊或从演示文稿中受益时，我们经常会发现一些迷人的图像并想下载它。 GroupDocs.Parser for .NET 是一个功能强大的 API，可帮助用户开发有用的应用程序，用于从不同类型的文档中提取图像并将其保存为 PNG、JPEG、WebP、GIF、BMP 和其他格式。 API 支持从一些最常用的文件格式中提取文本和图像，例如 PDF、电子邮件、电子书、Microsoft Office 格式：Word（DOC、DOCX）、PowerPoint（PPT、PPTX）、Excel（XLS） , XLSX), LibreOffice 格式等等。 该 API 还完全支持文档解析、提取纯文本和结构化文本、按关键字搜索文本、提取元数据或图像、容器以及附件等等。

############################# content ############################
steps:
    enable: true
    block:
    - title_left: "通过 C# 从 ONE 文档中提取图像"
      content_left: |
       GroupDocs.Parser .NET API 使软件开发人员能够从 ONE 文档中提取图像。 以下 C# .NET 代码示例演示了如何在 ONE 文档中提取图像。 

      title_right: "如何通过 .NET 提取图像"
      content_right: |
        * 创建 [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser) 的实例
        * 检查是否支持图像提取 
        * 遍历文档中的图像
        * 调用 [getImages](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/getimages) 方法从整个文档中提取所有图像。
        * 打印所有图像

      gisthash: "6bc9e8fea228c9e1b99425b338bb0f00"
      gistfile: "images_extraction_form_documents.cs"

    - title_left: "通过 C# 从 ONE 文档页面中提取图像"
      content_left: |
       GroupDocs.Parser .NET 允许软件开发人员从 ONE 文档的页面中提取图像。 下面的 C# .NET 代码显示了如何在 ONE 文档中实现图像提取。 

      title_right: "通过 .NET 提取文件图像"
      content_right: |
        * 创建 [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser) 的实例
        * 检查是否支持图像提取
        * 通过调用[GetDocumentInfo](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/getdocumentinfo) 获取文档信息
        * 检查文档是否存在页面
        * 遍历文档中的图像
        * 调用 [getImages(Int32)](https://apireference.groupdocs.com/parser/net/groupdocs.parser.parser/getimages/methods/2) 方法从整个文档中提取所有图像。
        * 迭代图像并打印图像
     
      gisthash: "2000d476c202a688677f57a2fbd7ceab"
      gistfile: "images_extraction_form_documents_page.cs"
      
    - title_left: "如何从 ONE 文档页面区域提取图像"
      content_left: |
       GroupDocs.Parser .NET API 完全支持使用几行 .NET 代码从 ONE 文档中提取图像。 以下 .NET 代码示例展示了如何从 ONE 文档页面区域执行图像提取。

      title_right: "通过 .NET 从文件页面区域中提取图像"
      content_right: |
        * 创建 [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser) 的实例  
        * 自定义可用于图像提取的选项创建
        * 检查是否支持图像提取
        * 通过使用自定义选项调用 [getImages(options)](https://apireference.groupdocs.com/parser/net/groupdocs.parser.parser/getimages/methods/3) 方法从页面的左上角提取图像 .
        * 迭代图像并打印图像
     
      gisthash: "ea6c6b8fa613384f1e7f637dabcb7bca"
      gistfile: "extract_images_form_documents_page_area.cs"

    - title_left: "如何通过 C# .NET 提取图像并将其保存到文件"
      content_left: |
       GroupDocs.Parser .NET API 允许软件开发人员从文档中提取图像并将其保存到一个文件中，只需几行 .NET 代码。 以下示例演示如何从 ONE 文档中提取图像并将图像内容保存到文件中。 

      title_right: "通过 .NET 将图像保存到文件"
      content_right: |
        * 创建 [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser) 的实例
        * 从文档中提取图像
        * 检查是否支持图像提取
        * 通过使用自定义选项调用 [getImages(options)](https://apireference.groupdocs.com/parser/net/groupdocs.parser.parser/getimages/methods/3) 方法从页面的左上角提取图像 .
        * 用于以 PNG 格式保存图像的选项创建
        * 迭代图像并将图像保存到PNG文件
     
      gisthash: "bc242d5ff4050564fa275858ffa7d34f"
      gistfile: "images_saving_to_files.cs"

    - title_left: "系统要求"
      content_left: |
        所有主要平台和操作系统都支持 GroupDocs.Parser for .NET。 如需完整的系统要求指南，请访问 [系统要求](hhttps://docs.groupdocs.com/parser/net/system-requirements/) 在执行以下代码之前，请确保您已安装以下先决条件 系统：
         * 操作系统：Microsoft Windows、Linux、MacOS
         * 开发环境：Visual Studio、Xamarin、MonoDevelop 等
         * 框架：.NET Framework、.NET Standard、.NET Core、Mono
         * 从 [NuGet](https://www.nuget.org/packages/GroupDocs.parser/) 获取最新版本的 GroupDocs.Assembly .NET API
        
      title_right: "为什么使用 GroupDocs.Parser"
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