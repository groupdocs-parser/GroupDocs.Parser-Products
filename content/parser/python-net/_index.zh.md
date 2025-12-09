---
############################# Static ############################
layout: "landing"
date: 2025-12-09T21:34:38
draft: false

lang: zh
product: "Parser"
product_tag: "parser"
platform: "Python"
platform_tag: "python-net"

############################# Drop-down ############################
supported_platforms:
  items:
    # supported_platforms loop
    - title: ".NET"
      tag: "net"
    # supported_platforms loop
    - title: "Java"
      tag: "java"
    # supported_platforms loop
    - title: "Python"
      tag: "python-net"

############################# Head ############################
head_title: "GroupDocs.Parser for Python via .NET 文档解析 SDK（适用于 Python）"
head_description: "高性能的 Python 文档解析 SDK。可从 PDF、Word、Excel、电子邮件以及 50 多种文档格式中提取文本、图像、元数据、条形码、表格和其他数据。"

############################# Header ############################
title: "适用于 Python 的文档解析 SDK"
description: "将快速、准确的文档解析添加到您的 Python 应用程序中，并从文档和图像中提取文本、图像、元数据和结构化数据。"
words:
  for: "用于"

actions:
  hidden: true # Hide version 0 is released
  main: "PyPI 下载"
  main_link: "https://pypi.org/project/groupdocs-parser-net/"
  alt: "授权"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/python-net/"
  title: "准备开始了吗？"
  description: "免费试用 GroupDocs.Parser 功能或申请许可证"

release:
  enable: false
  title: "版本 {0} 已发布"
  notes: "查看新增功能"
  downloads: "下载"

code:
  title: "使用 Python 提取文本"
  more: "更多示例"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Python-via-.NET/"
  install: "pip install groupdocs-parser-net"
  content: |
    ```python {style=abap}  
    from groupdocs.parser import Parser

    # 加载文档
    with Parser("sample.pdf") as parser:
        # 从文档中提取文本
        text = parser.GetText()

        # 打印所有提取的文本
        print(text)
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser 一览"
  description: "用于在 Python 应用程序中执行高精度文档解析的 Document Parser SDK"
  features:
    # feature loop
    - title: "从文档中提取数据"
      content: "GroupDocs.Parser for Python via .NET API 使您能够从各种文件格式（如 Office 文档、电子邮件、附件和压缩包）检索文本、元数据和图像。此强大工具帮助您高效访问和处理这些文件中包含的有价值信息，可用于数据分析、搜索引擎索引或内容管理系统等各种应用。"

    # feature loop
    - title: "解析文档"
      content: "从 PDF 表单中提取超链接、表格、二维码、条形码和数据等各种元素。还可使用自定义模板解析文档中的任意所需信息。"

    # feature loop
    - title: "自定义结果"
      content: "Python API 使您能够以原始、结构化、HTML 或 Markdown 等多种格式检索数据。此外，API 还提供搜索功能，可在文档文本中定位特定单词或短语。"

############################# Platforms ############################
platforms:
  enable: true
  title: "平台独立性"
  description: "GroupDocs.Parser for Python via .NET 支持以下操作系统、框架和包管理器"
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
    - title: "VS Code"
      image: "vs_code"
    # platform loop
    - title: "ReSharper"
      image: "resharper"
    # platform loop
    - title: "macOS"
      image: "finder"
    # platform loop
    - title: "Linux"
      image: "linux"
    # platform loop
    - title: "NuGet"
      image: "nuget"

############################# File formats ############################
formats:
  enable: true
  title: "支持的文件格式"
  description: |
    GroupDocs.Parser for Python via .NET 支持以下 [文件格式](https://docs.groupdocs.com/parser/python-net/supported-document-formats/)。
  groups:
    # group loop
    - color: "green"
      content: |
        ### Microsoft Office 格式
        * **Word:** DOCX, DOC, DOCM, DOT, DOTX, DOTM, RTF
        * **Excel:** XLSX, XLS, XLSM, XLSB, XLTM, XLT, XLTM, XLTX, XLAM, SXC, SpreadsheetML
        * **PowerPoint:** PPT, PPTX, PPS, PPSX, PPSM, POT, POTM, POTX, PPTM
    # group loop
    - color: "blue"
      content: |
        ### 图像及其他格式
        * **可移植:** PDF 
        * **图像:** JPG, BMP, PNG, TIFF, GIF
        * **其他办公格式:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### 其他格式
        * **Web:** HTML, MHTML 
        * **归档文件:** ZIP, TAR, 7Z 
        * **电子书:** CHM, EPUB, FB2, MOBI 

############################# Features ############################
features:
  enable: true
  title: "GroupDocs.Parser for Python via .NET 功能"
  description: "使用我们的 Python Document Parser SDK，迅速且准确地从 PDF、Office 文档、图像及其他格式中提取数据"

  items:
    # feature loop
    - icon: "text"
      title: "提取文本"
      content: "从各种文件格式（如 Office 文档、PDF 文件和图像）中提取文本信息，便于阅读和分析。"

    # feature loop
    - icon: "image"
      title: "提取图像"
      content: "从 Office 文档、PDF 文件等各种来源检索可视内容，方便访问和使用。"

    # feature loop
    - icon: "qr"
      title: "扫描二维码"
      content: "检测并解码 Office 文档、PDF 文件或视觉内容中的二维码，实现高效信息检索。"

    # feature loop
    - icon: "email"
      title: "从电子邮件附件和压缩包中提取数据"
      content: "从电子邮件、文件附件和压缩数据源中收集有价值的信息，以便进行有效的分析和利用。"

    # feature loop
    - icon: "table"
      title: "提取表格"
      content: "识别并提取 PDF 文档中的表格数据，以便进行有序的分析和使用。"

    # feature loop
    - icon: "hyperlink"
      title: "提取超链接"
      content: "在 Office 文档或 PDF 文件中定位并提取超链接和电子邮件地址，以实现高效访问。"

    # feature loop
    - icon: "pdf"
      title: "解析 PDF 表单"
      content: "PDF 表单是具有可填写字段的数字文档，供用户交互，可电子方式输入信息。Python API 可用于从这些表单中提取数据，以实现高效处理。"

    # feature loop
    - icon: "template"
      title: "使用模板解析数据"
      content: "创建自定义模板并使用 Python API 对其进行调用，以解析 PDF 文件中的特定信息，简化数据提取流程。"

    # feature loop
    - icon: "search"
      title: "在文档中搜索文本"
      content: "快速定位文档中的特定单词或模式。"


############################# Code samples ############################
code_samples:
  enable: true
  title: "代码示例"
  description: "除基本文本提取外，这里列出最常见的快速文本、图像和元数据提取用例。"
  items:
    # code sample loop
    - title: "在文档中搜索文本"
      content: |
        此示例演示如何在 PDF 文档中搜索特定短语并打印其出现位置。
        {{< landing/code title="使用 Python 在文档中搜索文本">}}
        ```python {style=abap}
        from groupdocs.parser import Parser

        # 加载文档
        with Parser("sample.pdf") as parser:
            # 打印短语所在的页面索引和矩形区域
            for area in parser.Search("Total Amount"):
                # 打印短语所在的页面索引和矩形区域
                print(f"Page {area.PageIndex}, Rectangle: {area.Rectangle}")
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "从文档中提取图像"
      content: |
        此示例演示如何从 PDF 文档中提取图像并将其保存到文件。
        {{< landing/code title="使用 Python 从文档中提取图像">}}
        ```python {style=abap}    
        from groupdocs.parser import Parser

        # 加载文档
        with Parser("sample.docx") as parser:
            # 从文档中提取图像
            images = parser.GetImages()

            # 将图像保存到文件
            index = 1
            for image in images:
                image.Save(f"image_{index}.png")
                index += 1
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "从文档中提取元数据"
      content: |
        此示例演示如何从 PDF 文档中提取元数据并打印。
        {{< landing/code title="使用 Python 从文档中提取元数据">}}
        ```python {style=abap}    
        from groupdocs.parser import Parser

        # 加载文档
        with Parser("sample.pdf") as parser:
            # 从文档中提取元数据
            metadata = parser.GetMetadata()

            # 打印元数据
            for item in metadata:
                print(f"{item.Name}: {item.Value}")
        ```
        {{< /landing/code >}}
---
