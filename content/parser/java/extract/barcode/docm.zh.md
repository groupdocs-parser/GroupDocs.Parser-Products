---
############################# Static ############################
layout: "auto-gen-gist"
draft: false
path: "zh/parser/java/extract/barcode/docm/"
otherformats: DOC DOT DOCX DOTX DOTM TXT ODT OTT RTF PDF XHTML MHTML MD XML EPUB FB2 CHM XLS XLT XLSX XLSM XLSB XLTX XLTM ODS CSV OTS XLA XLAM PPT PPTX  PPS POT PPSX PPTM POTX PPSM ODP OTP PST OST EML EMLX MSG ONE 

############################# Head ############################
head_title: "通过 Java API 从 Excel、Word、PDF 和其他文档中提取条形码"
head_description: "GroupDocs.Parser Java API 使软件开发人员能够从 Java 应用程序中的 PDF、MS Excel、Word、PowerPoint、Outlook、OneNote 和更多文档中提取条形码。"

############################# Header ############################
title: "如何通过 Java API 从 PDF、DOCX、PPTX、EML、MSG、XLSX 和 EPUB 中提取条形码"
description: "GroupDocs.Parser Java API 使软件开发人员能够从 PDF、Word（DOC、DOCX）、Excel（XLS、XLSX）、PowerPoint（PPT、PPTX）、Outlook（EML、MSG）和许多其他文档页面区域中提取条形码。"

######################### Download Button #######################
button:
    enable: true

############################# About ############################
about:
    enable: true
    title: "了解如何通过 Java 从 Excel、Word、PDF 和其他文档中提取条形码？"
    content: |
      条形码图像由一系列平行的黑线和不同宽度的空白空间组成，可用于将信息编码为视觉图案。 它于 1970 年代推出，现在已成为商业企业的通用部分。 GroupDocs.Parser for Java 是一个强大的 API，允许软件程序员构建应用程序来解析不同类型的文档并从中提取文本、图像和条形码。 它支持一些最常见的文档类型，例如 PDF、电子邮件、电子书、Microsoft Office 格式：Word（DOC、DOCX）、PowerPoint（PPT、PPTX）、Excel（XLS、XLSX）、电子邮件（EML、MSG） ) 格式等等。 Java API 包含对与文档解析和数据提取相关的几个重要功能的支持，例如纯文本提取、结构化文本提取、提取 markdown 格式文本、从特定页面或页面区域提取文本、从文档中提取条形码、提取元数据或 图像等等。

############################# content ############################
steps:
    enable: true
    block:
    - title_left: "如何通过 Java 从 DOCM 文档中提取条形码"
      content_left: |
       GroupDocs.Parser Java API 使程序员能够轻松地从 DOCM 文档中提取条形码。 以下 Java 代码示例演示了如何以最少的工作量和成本提取 DOCM 文档中的条形码图像。 

      title_right: "通过 Java 从文档中提取条形码"
      content_right: |
        * 创建 [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser) 的实例
        * 检查是否支持条码提取
        * 调用 [GetBarcodes](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getBarcodes()) 方法从整个文档中提取所有条形码。
        * 遍历文档中的条码
        * 打印所有条码及其价值

      gisthash: "bb2393a5db93e1795d41d908ad23e158"
      gistfile: "barcode_extraction_form_documents.java"

    - title_left: "通过 Java 从 DOCM 文档页面获取条形码"
      content_left: |
       GroupDocs.Parser Java 使软件开发人员能够轻松地从 DOCM 文档的页面解析和获取条形码。 以下 Java 代码显示了如何从 DOCM 文档中的特定文档页面中提取条形码。 

      title_right: "如何从文件页面获取条形码"
      content_right: |
        * 创建 [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser) 的实例
        * 检查文档以获取条码提取支持
        * 调用 [GetBarcodes](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getBarcodes(int)) 方法从文档第 2 页提取所条码。
        * 遍历页面的条形码
        * 打印页码和条码值
     
      gisthash: "ff09980eef6df60d5a3272b91b5607cf"
      gistfile: "barcodes_extraction_form_documents_page.java"
      
    - title_left: "如何从 DOCM 文档页面区域提取条形码"
      content_left: |
       GroupDocs.Parser Java API 完全支持轻松地从 DOCM 文档中提取条形码。 以下 Java 代码示例显示如何从 DOCM 文档页面区域执行条形码提取。

      title_right: "通过 Java 从文件页面区域中提取条形码"
      content_right: |
        * 创建 [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser) 的实例
        *自定义可用于条码提取的选项创建
        * 检查文档以获取条码提取支持
        * 调用 [GetBarcodes](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getBarcodes(int)) 方法从文档第 2 页提取所有条码。
        * 遍历文档中的条码
        * 打印页码和条码值
     
      gisthash: "1737589e775a06a6300245cea525dac0"
      gistfile: "barcodes_extraction_from_documents_page_area.java"

    - title_left: "系统要求"
      content_left: |
        所有主要平台和操作系统都支持 Java 的 GroupDocs.Parser。 它可以生成 Microsoft Word、Excel、PowerPoint、Outlook、OpenOffice 和 50 多种其他格式的文档。 有关完整的系统要求指南，请在执行以下代码之前访问系统要求，请确保您的系统上安装了以下先决条件：
        * 操作系统：Microsoft Windows、Linux、MacOS
        * Java 版本支持：J2SE 7.0 (1.7)、J2SE 8.0 (1.8) 或以上
        * 从 GroupDocs [Repository](https://repository.groupdocs.com/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs-parser) 获取最新版本的 GroupDocs.Parser Java API
        
      title_right: "为什么使用 GroupDocs.Parser"
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