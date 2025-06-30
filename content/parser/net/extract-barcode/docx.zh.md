


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:20
draft: false
lang: zh
format: Docx
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "在 C# 应用中从 DOCX 文件提取条形码"
head_description: "使用 GroupDocs.Parser 检测并提取 C# 中 DOCX 文件的条形码数据，无需额外的软件。"

############################# Header ############################
title: "使用 C# 从 DOCX 提取条形码" 
description: "在您的 .NET 应用中，利用 GroupDocs.Parser 检测并提取 PDF、Word、Excel 和图像文件中的条形码信息。"
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "下载免费试用"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "关于 GroupDocs.Parser for .NET API"
    link: "/parser/net/"
    link_title: "了解更多"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/) 是一个强大的文档解析 API，专为 .NET 开发者设计。它能够从多种文件格式中提取文本、图像、结构化内容和条形码，包括 PDF、Word、Excel、PowerPoint 等，全部操作无需依赖外部工具。

############################# Steps ############################
steps:
    enable: true
    title: "在 C# 中从 Docx 提取条形码的步骤"
    content: |
      [GroupDocs.Parser](/parser/net/) 使您能够通过以下简单步骤在 .NET 应用中提取 DOCX 文件的条形码数据：
      
      1. 使用 Parser 实例加载 DOCX 文件。
      2. 验证文档是否支持条形码提取。
      3. 从文档中检索条形码列表。
      4. 遍历结果并使用提取的条形码值。
   
    code:
      platform: "net"
      copy_title: "复制"
      install:
        command: |
        command: "dotnet add package GroupDocs.Parser"
        copy_tip: "点击以复制"
        copy_done: "已复制"
      links:
        #  loop
        - title: "更多示例"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
        #  loop
        - title: "文档"
          link: "https://docs.groupdocs.com/parser/net/"
          
      content: |
        ```csharp {style=abap}
        // 使用 Parser 类加载包含条形码的文档
        using (Parser parser = new Parser("input.docx")) {

            // 验证文件是否支持条形码提取
            if (!parser.Features.Barcodes) {
                Console.WriteLine("不支持条形码提取");
                return;
            }

            // 获取并处理提取的条形码
            IEnumerable<PageBarcodeArea> barcodes = parser.GetBarcodes();

            foreach (PageBarcodeArea barcode in barcodes) {
                Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                Console.WriteLine("Value: " + barcode.Value);
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "高级文档解析功能"
  description: "除了条形码提取，GroupDocs.Parser 还允许您提取纯文本、图像和结构化数据，以支持高级自动化和数据处理工作流程。"
  image: "/img/parser/features_extract-barcode.webp" # 500x500 px
  image_description: "条形码识别和文档解析"
  features:
    # feature loop
    - title: "支持多种条形码格式"
      content: "识别常见的条形码类型，包括 QR 码、Code 128、Data Matrix、EAN、Aztec 等。"

    # feature loop
    - title: "从文档和图像中提取条形码"
      content: "从 PDF、Word、Excel 文档，及 JPEG、PNG、BMP 等图像格式中读取条形码。"

    # feature loop
    - title: "可定制的提取设置"
      content: "配置检测选项，例如扫描区域和处理多页文档。"
      
  code_samples:
    # code sample loop
    - title: "如何使用条形码选项从 PDF 中提取条形码"
      content: |
        本示例演示如何使用特定的条形码提取选项从 PDF 文件中提取条形码。
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  使用 Parser 类加载 PDF 文件
        using (Parser parser = new Parser("input.pdf"))
        {
            // 确认支持条形码提取
            if (!parser.Features.Barcodes)
            {
                return;
            }

            // 使用条形码选项过滤结果
            BarcodeOptions options = new BarcodeOptions(QualityMode.Low, QualityMode.Low, "QR");

            // 从文档中检索条形码数据
            IEnumerable<PageBarcodeArea> barcodes = parser.GetBarcodes(options);

            // 处理提取的条形码列表
            foreach (PageBarcodeArea barcode in barcodes)
            {
                Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                Console.WriteLine("Value: " + barcode.Value);
            }
        }
        ```
        {{< /landing/code >}}


############################# Actions ############################

actions:
  enable: true
  title: "准备好开始了吗？"
  description: "免费试用 GroupDocs.Parser 功能或请求许可证"
  items:
    #  loop
    - title: "Nuget 下载"
      link: "https://releases.groupdocs.com/parser/net/"
      color: "red"
        #  loop
    - title: "许可信息"
      link: "https://purchase.groupdocs.com/pricing/parser/net/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "条形码提取支持的格式"
    exclude: "DOCX"
    description: "GroupDocs.Parser 支持多种文档和图像格式中的条形码检测。请查看下面常用的文件类型。"
    items: 
        # format loop 1
        - name: "解析 PDF"
          format: "PDF"
          link: "/parser/net/extract-barcode/pdf/"
          description: "(可移植文档格式)"
          
        # format loop 2
        - name: "解析 DOCX"
          format: "DOCX"
          link: "/parser/net/extract-barcode/docx/"
          description: "(Office 2007+ Word 文档)"
          
        # format loop 3
        - name: "解析 PPTX"
          format: "PPTX"
          link: "/parser/net/extract-barcode/pptx/"
          description: "(Open XML 演示格式)"
          
        # format loop 4
        - name: "解析 XLSX"
          format: "XLSX"
          link: "/parser/net/extract-barcode/xlsx/"
          description: "(Open XML 工作簿)"
          
        # format loop 5
        - name: "解析 ODT"
          format: "ODT"
          link: "/parser/net/extract-barcode/odt/"
          description: "(OpenDocument 文本文档)"
          
        # format loop 6
        - name: "解析 ODS"
          format: "ODS"
          link: "/parser/net/extract-barcode/ods/"
          description: "(OpenDocument 电子表格)"
          
        # format loop 7
        - name: "解析 ODP"
          format: "ODP"
          link: "/parser/net/extract-barcode/odp/"
          description: "(OpenDocument 演示文稿)"
          
        # format loop 8
        - name: "解析 EPUB"
          format: "EPUB"
          link: "/parser/net/extract-barcode/epub/"
          description: "(开放电子书文件)"
          
        # format loop 9
        - name: "解析 FB2"
          format: "FB2"
          link: "/parser/net/extract-barcode/fb2/"
          description: "(FictionBook 电子书)"
         
          

---