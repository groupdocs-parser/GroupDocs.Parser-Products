---
############################# Static ############################
layout: "auto-gen-gist"
draft: false
path: "zh/parser/net/extract/barcode//xlt/"
otherformats: DOC DOT DOCX DOCM DOTX DOTM TXT ODT OTT RTF PDF XHTML MHTML MD XML EPUB FB2 CHM XLS XLSX XLSM XLSB XLTX XLTM ODS CSV OTS XLA XLAM PPT PPTX  PPS POT PPSX PPTM POTX PPSM ODP OTP PST OST EML EMLX MSG ONE 

############################# Head ############################
head_title: ".NET API 从 PDF、DOCX、PPTX、XLSX、EPUB 等中提取条形码 "
head_description: "GroupDocs.Parser .NET API 允许软件开发人员从 .NET 应用程序中的 PDF、DOC、DOCX、PPT、PPTX、EML、MSG、XLS、XLSX、CSV、ODT、RTF 和 EPUB 文档中提取条形码。"

############################# Header ############################
title: "通过 C#.NET API 从 Excel、Word、PDF 和 PowerPoint 文档中提取条形码"
description: "GroupDocs.Parser .NET API 允许程序员从 PDF、DOC、DOCX、PPT、PPTX、EML、MSG、XLS、XLSX、CSV、ODT、RTF 和 EPUB 文档或页面 aea 中提取条形码。"

######################### Download Button #######################
button:
    enable: true

############################# About ############################
about:
    enable: true
    title: "如何通过 .NET API 从 Excel、Word、PDF 和其他文档中提取条形码？"
    content: |
       条形码是数字和字符的机器可读表示，在世界范围内广泛用于许多情况，例如产品扫描和识别、汽车零件跟踪、库存管理等。 GroupDocs.Parser for .NET 是一个功能强大的 API，可帮助开发人员开发用于从不同类型的受支持文档格式（例如 PDF、电子邮件、电子书、Microsoft Office 格式）中提取文本、图像和条形码的解决方案：Word（DOC、DOCX )、PowerPoint（PPT、PPTX）、Excel（XLS、XLSX）、电子邮件（EML、MSG）格式等等。 该 API 支持多种高级文档解析功能，例如按关键字搜索文本、准确提取文本、HTML 或 Markdown 格式的文本提取、带坐标的文本区域提取、提取元数据或条形码等。  

############################# content ############################
steps:
    enable: true
    block:
    - title_left: "如何通过 C# .NET 从 XLT 文档中提取条形码 "
      content_left: |
       GroupDocs.Parser .NET API 帮助软件开发人员轻松地从 XLT 文档中提取条形码。 以下 C# .NET 代码示例演示了如何从 XLT 文档中提取条形码。

      title_right: "从文档中提取条码"
      content_right: |
        * 创建 [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser)的实例
        * 检查是否支持条码提取
        * 调用 [getBarcodes](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/getBarcodes) 方法从整个文档中提取所有条形码。
        * 遍历文档中的条码
        * 打印页面索引和条码值

      gisthash: "f9329c432da312e75f5f1c3702c02c52"
      gistfile: "barcode_extraction_form_documents.cs"

    - title_left: "通过 .NET 从 XLT 文档页面提取条形码"
      content_left: |
       GroupDocs.Parser .NET 使软件程序员能够从 XLT 文档的页面中提取条形码。 下面的 C# .NET 代码显示了如何在 XLT 文档中实现条码提取。 

      title_right: "通过 C# .NET 提取条形码"
      content_right: |
        * 创建 [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser) 的实例
        * 检查文档以获取条码提取支持
        * 调用 [getBarcodes](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/getBarcodes) 方法从整个文档中提取所有条形码。
        * 遍历页面并打印页码
        * 打印页面索引和条码值
     
      gisthash: "80779aaa36b7d11b69c29296cfa73bd1"
      gistfile: "barcodes_extraction_form_documents_page.cs"
      
    - title_left: "通过 .NET 从 XLT 文档的页面区域获取条形码"
      content_left: |
       GroupDocs.Parser .NET 是一个强大的 API，它为使用几行 .NET 代码从 XLT 文档中提取条形码提供了完整的支持。 以下 .NET 代码示例显示了如何从 XLT 文档页面区域执行条形码提取。

      title_right: "从 XLT 页面区域提取条形码"
      content_right: |
        * 创建 [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser) 的实例
        * 检查文档以获取条码提取支持
        * 创建可用于条码提取的自定义选项
        * 通过使用自定义选项调用 [getBarcodes](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/getBarcodes) 方法从页面的右上角提取条形码。
        * 打印页面索引和条码值
     
      gisthash: "932e868be1c52982f8c2ced2fc4c0640"
      gistfile: "barcodes_extraction_from_documents_page_area.cs"

    - title_left: "系统要求"
      content_left: |
        所有主要平台和操作系统都支持 GroupDocs.Parser for .NET。 如需完整的系统要求指南，请访问 [系统要求](hhttps://docs.groupdocs.com/parser/net/system-requirements/) 在执行以下代码之前，请确保您已安装以下先决条件 系统：
         * 操作系统：Microsoft Windows、Linux、MacOS
         * 开发环境：Visual Studio、Xamarin、MonoDevelop 等
         * 框架：.NET Framework、.NET Standard、.NET Core、Mono
         * 从 [NuGet](https://www.nuget.org/packages/GroupDocs.parser/) 获取最新版本的 GroupDocs.Parser .NET API
        
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