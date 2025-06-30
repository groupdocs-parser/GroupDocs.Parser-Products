


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:34
draft: false
lang: zh
format: Xlsx
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "在C#应用程序中从XLSX文件提取图像"
head_description: "使用GroupDocs.Parser在C#中检测并提取XLSX文件中的图像，无需额外工具。"

############################# Header ############################
title: "使用C#从XLSX提取图像" 
description: "使用GroupDocs.Parser，能够方便地定位并提取PDF、Word文档、Excel表格及其他文件类型中的嵌入图像，适用于您的.NET应用程序。"
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "免费下载试用"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "关于GroupDocs.Parser for .NET API"
    link: "/parser/net/"
    link_title: "了解更多"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/)是一个强大的文档解析库，专为.NET开发者设计。它允许从流行文件格式（如PDF、DOCX、XLSX、PPTX等）中提取图像、文本、超链接和结构化数据，无需任何第三方应用程序。

############################# Steps ############################
steps:
    enable: true
    title: "在C#中从Xlsx提取图像的步骤"
    content: |
      借助[GroupDocs.Parser](/parser/net/)，您可以在数个步骤中从XLSX文档中提取图像：
      
      1. 用XLSX文件初始化Parser。
      2. 从文档中获取图像元素。
      3. 按需在您的工作流程中使用提取的图像。
   
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
        // 使用Parser打开包含图像的文档
        using (Parser parser = new Parser("input.xlsx")) {

            // 从文件中提取所有嵌入的图像
            IEnumerable<PageImageArea> images = parser.GetImages();

            // 处理未找到图像的情况
            if (images == null)
            {
                return;
            }

            // 处理或保存检索到的图像
            foreach (PageImageArea image in images)
            {
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Type: {2}", 
                    image.Page.Index, image.Rectangle, image.FileType));
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "全面的文档内容提取"
  description: "GroupDocs.Parser不仅提供图像提取功能，还支持提取原始文本、超链接、元数据和结构化内容，满足高级自动化场景的需求。"
  image: "/img/parser/features_extract-image.webp" # 500x500 px
  image_description: "图像提取和文档解析工作流"
  features:
    # feature loop
    - title: "从多种格式中提取图像"
      content: "从多种文件格式（包括DOCX、PDF、PPTX、XLSX以及图像文件如PNG、JPG和TIFF）中提取嵌入图像。"

    # feature loop
    - title: "保持原始图像质量"
      content: "图像以高保真度提取，保持原始分辨率、格式和色彩配置文件。"

    # feature loop
    - title: "高级提取选项"
      content: "通过按页、格式或分辨率筛选定制图像提取，并支持多页文档。"
      
  code_samples:
    # code sample loop
    - title: "如何从PDF文档中提取和保存图像"
      content: |
        本示例演示如何从PDF文件中提取所有图像资源并保存到本地文件系统。
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  使用Parser类加载PDF
        using (Parser parser = new Parser("input.pdf"))
        {
            // 从文件中提取嵌入图像
            IEnumerable<PageImageArea> images = parser.GetImages();

            // 设置输出格式和图像选项（例如，PNG）
            ImageOptions options = new ImageOptions(ImageFormat.Png);

            // 将提取的图像写入磁盘
            int imageNumber = 0;
            foreach (PageImageArea image in images)
            {
                image.Save(imageNumber.ToString() + ".png", options);
                imageNumber++;
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
    title: "支持的图像提取格式"
    exclude: "XLSX"
    description: "GroupDocs.Parser能够准确地从多种文档和图像格式中提取图像。请查看下面的常见支持类型列表。"
    items: 
        # format loop 1
        - name: "解析 PDF"
          format: "PDF"
          link: "/parser/net/extract-image/pdf/"
          description: "(可移植文档格式)"
          
        # format loop 2
        - name: "解析 DOCX"
          format: "DOCX"
          link: "/parser/net/extract-image/docx/"
          description: "(Office 2007+ Word 文档)"
          
        # format loop 3
        - name: "解析 PPTX"
          format: "PPTX"
          link: "/parser/net/extract-image/pptx/"
          description: "(Open XML 演示格式)"
          
        # format loop 4
        - name: "解析 XLSX"
          format: "XLSX"
          link: "/parser/net/extract-image/xlsx/"
          description: "(Open XML 工作簿)"
          
        # format loop 5
        - name: "解析 ODT"
          format: "ODT"
          link: "/parser/net/extract-image/odt/"
          description: "(OpenDocument 文本文档)"
          
        # format loop 6
        - name: "解析 ODS"
          format: "ODS"
          link: "/parser/net/extract-image/ods/"
          description: "(OpenDocument 电子表格)"
          
        # format loop 7
        - name: "解析 ODP"
          format: "ODP"
          link: "/parser/net/extract-image/odp/"
          description: "(OpenDocument 演示文稿)"
          
        # format loop 8
        - name: "解析 EPUB"
          format: "EPUB"
          link: "/parser/net/extract-image/epub/"
          description: "(开放电子书文件)"
          
        # format loop 9
        - name: "解析 FB2"
          format: "FB2"
          link: "/parser/net/extract-image/fb2/"
          description: "(FictionBook 电子书)"
         
          

---