


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:47
draft: false
lang: zh
format: Xml
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "在 C# 应用中从 XML 文件提取文本"
head_description: "使用 GroupDocs.Parser 在 C# 应用程序中提取 XML 文件的纯文本或结构化文本，无需外部工具。"

############################# Header ############################
title: "使用 C# 从 XML 提取文本" 
description: "使用 GroupDocs.Parser 快速提取 PDF、Word、Excel 及其他文件类型中的可读和结构化文本，适用于您的 .NET 解决方案。"
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "下载免费试用版"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "GroupDocs.Parser for .NET API 介绍"
    link: "/parser/net/"
    link_title: "了解更多"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/) 是为 .NET 开发者提供的高性能文档解析 API。它简化了从 PDF、DOCX、XLSX、PPTX 等多种文件格式中提取文本、图像、表格和结构化内容的过程，无需依赖第三方库。

############################# Steps ############################
steps:
    enable: true
    title: "在 C# 中从 Xml 提取文本的步骤"
    content: |
      通过遵循以下步骤，您可以使用 [GroupDocs.Parser](/parser/net/) 从 XML 文档中提取清晰的结构化文本：
      
      1. 使用 Parser 实例打开 XML 文档。
      2. 从文件内容中提取文本。
      3. 检查结果以确认文本提取成功。
      4. 将提取的文本应用于业务逻辑、索引或数据管道。
   
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
        // 将文档加载到 Parser 中
        using (Parser parser = new Parser("input.xml")) {

            // 从文件中提取所有文本内容
            using (TextReader reader = parser.GetText()) 
            {
                // 如果文本不可用，结果将为 null
                // 在您的应用中使用提取的文本
                Console.WriteLine(reader == null ? 
                    "此格式不支持文本提取" : reader.ReadToEnd());
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "全面的内容提取功能"
  description: "除了纯文本，GroupDocs.Parser 还可以提取图像、结构化元素和元数据，以支持内容分析、转换和自动化。"
  image: "/img/parser/features_extract-text.webp" # 500x500 px
  image_description: "文本识别和结构化文档解析"
  features:
    # feature loop
    - title: "跨多种文件类型提取文本"
      content: "从 PDF、DOCX、XLSX、PPTX、HTML 及其他格式中获取纯文本或结构化文本。"

    # feature loop
    - title: "处理文档和视觉文本"
      content: "从扫描的图像、演示文稿、电子表格和数字文档中提取文本，同时保留结构。"

    # feature loop
    - title: "高级文本提取配置"
      content: "自定义文本检测方式——定义页面范围、布局区域，并调整输出以实现最大准确性。"
      
  code_samples:
    # code sample loop
    - title: "如何从 PPTX 文件提取文本区域"
      content: |
        此代码示例展示了如何使用 GroupDocs.Parser 从 PowerPoint 文件中检索文本内容及区域坐标。
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  使用 Parser 加载 PowerPoint 演示文稿
        using (Parser parser = new Parser("input.pptx"))
        {
            // 从文档中提取所有文本区域矩形
            IEnumerable<PageTextArea> areas = parser.GetTextAreas();

            // 如果文本区域提取不可用则退出
            if (areas == null)
            {
                return;
            }

            // 遍历每个页面的文本区域
            foreach (PageTextArea a in areas)
            {
                // 访问页面索引、区域矩形和文本值
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Text: {2}", a.Page.Index, a.Rectangle, a.Text));
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
    title: "支持的文本提取格式"
    exclude: "XML"
    description: "GroupDocs.Parser 支持从多种文档和图像类型中提取文本。查看下面列出的常见支持格式。"
    items: 
        # format loop 1
        - name: "解析 PDF"
          format: "PDF"
          link: "/parser/net/extract-text/pdf/"
          description: "(可移植文档格式)"
          
        # format loop 2
        - name: "解析 DOCX"
          format: "DOCX"
          link: "/parser/net/extract-text/docx/"
          description: "(Office 2007+ Word 文档)"
          
        # format loop 3
        - name: "解析 PPTX"
          format: "PPTX"
          link: "/parser/net/extract-text/pptx/"
          description: "(Open XML 演示格式)"
          
        # format loop 4
        - name: "解析 XLSX"
          format: "XLSX"
          link: "/parser/net/extract-text/xlsx/"
          description: "(Open XML 工作簿)"
          
        # format loop 5
        - name: "解析 TXT"
          format: "TXT"
          link: "/parser/net/extract-text/txt/"
          description: "(文本文件)"
          
        # format loop 6
        - name: "解析 RTF"
          format: "RTF"
          link: "/parser/net/extract-text/rtf/"
          description: "(富文本格式)"
          
        # format loop 7
        - name: "解析 XML"
          format: "XML"
          link: "/parser/net/extract-text/xml/"
          description: "(可扩展标记语言)"
          
        # format loop 8
        - name: "解析 EPUB"
          format: "EPUB"
          link: "/parser/net/extract-text/epub/"
          description: "(开放电子书文件)"
         
          

---