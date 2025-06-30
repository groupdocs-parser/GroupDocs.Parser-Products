


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:30
draft: false
lang: zh
format: Odt
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "在Java应用程序中从ODT文件提取图像"
head_description: "使用GroupDocs.Parser，您可以在Java中轻松地从ODT文件中提取图像，无需第三方工具。"

############################# Header ############################
title: "使用Java从ODT提取图像" 
description: "使用GroupDocs.Parser在您的Java开发环境中从PDF、Word、Excel等文件中检索嵌入的图像。"
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "下载免费试用"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "GroupDocs.Parser for Java是什么？"
    link: "/parser/java/"
    link_title: "了解更多"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) 是一个功能丰富的解析API，专为Java开发者量身定制。它能够从各种文件格式中提取图像、文本、链接和结构化元素，包括DOCX、XLSX、PDF、PNG、JPG等，无需依赖外部库或应用程序。

############################# Steps ############################
steps:
    enable: true
    title: "如何在Java中从Odt提取图像"
    content: |
      按照以下步骤使用[GroupDocs.Parser](/parser/java/)在您的Java应用程序中提取ODT文档的图像：
      
      1. 创建一个Parser实例并加载ODT文件。
      2. 从加载的文档中提取图像数据。
      3. 根据需要使用或导出提取的图像。
   
    code:
      platform: "net"
      copy_title: "复制"
      install:
        command: |
          <dependencies>
            <dependency>
              <groupId>com.groupdocs</groupId>
              <artifactId>groupdocs-parser</artifactId>
              <version>{0}</version>
            </dependency>
          </dependencies>

          <repositories>
            <repository>
              <id>repository.groupdocs.com</id>
              <name>GroupDocs Repository</name>
              <url>https://repository.groupdocs.com/repo/</url>
            </repository>
          </repositories>
        copy_tip: "点击以复制"
        copy_done: "已复制"
      links:
        #  loop
        - title: "更多示例"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java/"
        #  loop
        - title: "文档"
          link: "https://docs.groupdocs.com/parser/java/"
          
      content: |
        ```java {style=abap}
        // 初始化解析器并使用Parser加载包含图像的文档
        try (Parser parser = new Parser("input.odt"))
        {
            // 收集文档中嵌入的所有图像元素
            Iterable<PageImageArea> images = parser.getImages();

            // 如果文档没有图像，则跳过处理
            if (images == null) {
                return;
            }

            // 根据需要处理每一张图像
            for (PageImageArea image : images) {
                System.out.println(String.format("Page: %d, R: %s, Type: %s", image.getPage().getIndex(), 
                    image.getRectangle(), image.getFileType()));
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "更多文档解析功能"
  description: "除了图像提取外，GroupDocs.Parser还允许您提取原始内容，如文本、链接、元数据和结构化数据，以便进行处理和分析。"
  image: "/img/parser/features_extract-image.webp" # 500x500 px
  image_description: "从文档中提取图像和内容"
  features:
    # feature loop
    - title: "支持多种格式"
      content: "从不同类型的文档中提取图像，包括PDF、DOCX、PPTX、XLSX，以及PNG、JPEG和GIF等图像格式。"

    # feature loop
    - title: "保持图像清晰度和分辨率"
      content: "所有提取的图像均保留其原始分辨率和文件类型，以确保一致的质量和可用性。"

    # feature loop
    - title: "灵活的配置选项"
      content: "通过按类型、大小、页面索引或文件格式过滤图像，自定义图像提取过程。"
      
  code_samples:
    # code sample loop
    - title: "从PDF文件中提取并保存图像"
      content: |
        本示例演示如何从PDF文档中提取图像，并单独将其保存在您的设备上。
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  使用Parser打开PDF文件
        try (Parser parser = new Parser("input.pdf"))
        {
            // 从文档内容中获取图像
            Iterable<PageImageArea> images = parser.getImages();

            // 设置输出参数，例如格式（如JPEG或PNG）
            ImageOptions options = new ImageOptions(ImageFormat.Png);

            // 将提取的图像保存到本地目录
            int imageNumber = 0;
            for (PageImageArea image : images)
            {
                image.save(Constants.getOutputFilePath(String.format("%d.png", imageNumber)), options);
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
    - title: "Maven 下载"
      link: "https://releases.groupdocs.com/parser/java/"
      color: "red"
        #  loop
    - title: "许可信息"
      link: "https://purchase.groupdocs.com/pricing/parser/java/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "支持图像提取的文件类型"
    exclude: "ODT"
    description: "GroupDocs.Parser支持在广泛的文档和图像之间进行图像提取。探索下面常见的支持格式。"
    items: 
        # format loop 1
        - name: "解析 PDF"
          format: "PDF"
          link: "/parser/java/extract-image/pdf/"
          description: "(可移植文档格式)"
          
        # format loop 2
        - name: "解析 DOCX"
          format: "DOCX"
          link: "/parser/java/extract-image/docx/"
          description: "(Office 2007+ Word 文档)"
          
        # format loop 3
        - name: "解析 PPTX"
          format: "PPTX"
          link: "/parser/java/extract-image/pptx/"
          description: "(Open XML 演示格式)"
          
        # format loop 4
        - name: "解析 XLSX"
          format: "XLSX"
          link: "/parser/java/extract-image/xlsx/"
          description: "(Open XML 工作簿)"
          
        # format loop 5
        - name: "解析 ODT"
          format: "ODT"
          link: "/parser/java/extract-image/odt/"
          description: "(OpenDocument 文本文档)"
          
        # format loop 6
        - name: "解析 ODS"
          format: "ODS"
          link: "/parser/java/extract-image/ods/"
          description: "(OpenDocument 电子表格)"
          
        # format loop 7
        - name: "解析 ODP"
          format: "ODP"
          link: "/parser/java/extract-image/odp/"
          description: "(OpenDocument 演示文稿)"
          
        # format loop 8
        - name: "解析 EPUB"
          format: "EPUB"
          link: "/parser/java/extract-image/epub/"
          description: "(开放电子书文件)"
          
        # format loop 9
        - name: "解析 FB2"
          format: "FB2"
          link: "/parser/java/extract-image/fb2/"
          description: "(FictionBook 电子书)"
         
          

---