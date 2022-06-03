---
############################# Static ############################
layout: "auto-gen-gist"
draft: false
path: "ru/parser/java/extract/image/emlx/"
otherformats: DOC DOT DOCX DOCM DOTX DOTM TXT ODT OTT RTF PDF XHTML MHTML MD XML EPUB FB2 CHM XLS XLT XLSX XLSM XLSB XLTX XLTM ODS CSV OTS XLA XLAM PPT PPTX  PPS POT PPSX PPTM POTX PPSM ODP OTP PST OST EML MSG ONE 

############################# Head ############################
head_title: "如何通过 Java 从 Excel、Word、PDF 和其他文档中提取图像？"
head_description: "GroupDocs.Parser Java API 允许软件开发人员从 Java 应用程序内的 PDF、DOC、DOCX、PPT、PPTX、XLS、XLSX 文档、页面区域和电子邮件中解析和提取图像。"

############################# Header ############################
title: "用于从 Excel、Word、PowerPoint、PDF 和其他文档页面解析和提取图像的 Java API"
description: "GroupDocs.Parser Java API 允许程序员从 PDF、DOC、DOCX、PPT、PPTX、EML、MSG、XLS、XLSX、CSV、ODT、RTF 和 EPUB 文档或 Java 应用程序中的文档页面中提取图像。"

######################### Download Button #######################
button:
    enable: true

############################# About ############################
about:
    enable: true
    title: "了解如何通过 Java API 从文档或特定页面中提取图像？"
    content: |
       在创建引人入胜的内容时，图像值一千字，在当今的视觉世界中不容忽视。图像可以成为信息交流的重要来源，也可以吸引用户的注意力。通常需要从文档、期刊或演示文稿中获取图像并在其他地方使用它们。 GroupDocs.Parser for Java 是一个功能强大的 API，可帮助软件开发人员和程序员构建解决方案，以从众多文档类型中解析和提取图像或其他信息。它还支持以PNG、JPEG、WebP、GIF、BMP等格式保存图像。 API 支持一些流行的文档格式，例如 PDF、Microsoft Office 格式：Word（DOC、DOCX）、PowerPoint（PPT、PPTX）、Excel（XLS、XLSX）、LibreOffice 格式、电子邮件、电子书等等.它还支持一些与文档解析、提取纯文本和结构化文本、按关键字搜索文本、提取元数据或图像、容器以及附件等相关的高级功能。

############################# content ############################
steps:
    enable: true
    block:
    - title_left: "如何从 EMLX 文档中提取图像"
      content_left: |
       GroupDocs.Parser Java 包含从 EMLX 文档中提取图像的功能。 以下 Java 代码示例展示了如何轻松地从 EMLX 文档中提取图像。 

      title_right: "通过 Java 从文档中获取图像"
      content_right: |
        * 创建 [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser) 的实例
        * 检查文档是否支持图像提取
        * 调用 [getImages()](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getImages()) 方法从整个文档中提取所有图像。
        * 从文档中提取所有图像
        * 遍历图像并打印图像类型

      gisthash: "b13e690d2593f92081abd99948363e06"
      gistfile: "extract_images_form_documents.java"

    - title_left: "从 EMLX 文档页面提取图像"
      content_left: |
       GroupDocs.Parser Java API 允许软件开发人员使用几行代码从 EMLX 文档中提取图像。 下面的 Java 代码显示了从 EMLX 文档中提取的图像。 

      title_right: "如何通过 Java 提取文件图像"
      content_right: |
        * 创建 [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser) 的实例 
        * 检查文档是否支持图像提取
        * 通过调用 [getDocumentInfo](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getDocumentInfo()) 方法获取文档信息。
        * 检查文档是否存在页面
        * 遍历页面并打印页码
        * 调用 [getImages()](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getImages()) 方法从整个文档中提取所有图像。
        * 迭代图像和打印图像类型
     
      gisthash: "68450336a57c5d8df06b4ef1ea69b29f"
      gistfile: "extract_images_form_documents_page.java"
      
    - title_left: "如何从 EMLX 文档页面区域提取图像"
      content_left: |
       GroupDocs.Parser Java API 为从 EMLX 文档的页面轻松提取提供了完整的支持。 以下 Java 代码演示了程序员如何从他们自己的 Java 应用程序内的 EMLX 文档页面区域提取图像。

      title_right: "使用Java提取图像？"
      content_right: |
        * 创建 [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser) 的实例  
        * 创建用于图像提取的选项
        * 检查文档以获取图像提取支持
        * 调用[getImages()](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getImages())方法从页面左上角提取图片。
        * 遍历图像并打印图像 URL
     
      gisthash: "40143a56569ae88e7e7c972ccca041b5"
      gistfile: "extract_images_form_documents_page_area.java"

    - title_left: "如何通过 Java API 将图像提取到文件"
      content_left: |
       GroupDocs.Parser Java API 允许从 EMLX 文档中提取图像并将图像内容保存到文件中。 以下 Java 代码演示了程序员如何在自己的 Java 应用程序中将图像提取到他们选择的文件中。

      title_right: "将文档中的图像提取到文件中"
      content_right: |
        * 创建 [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser) 的实例 
        * 检查文档以获取图像提取支持
        * 调用[getImages()](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getImages())方法从页面左上角提取图片。
        * 创建选项以支持的文件格式保存图像
        * 遍历图像并打印图像 URL
     
      gisthash: "6faeafc93e4412265b7439209828950b"
      gistfile: "images_saving_to_files.java"

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