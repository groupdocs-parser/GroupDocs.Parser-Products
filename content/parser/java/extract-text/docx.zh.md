


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:45
draft: false
lang: zh
format: Docx
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "从DOCX文件中获取文本信息，适用于Java应用程序"
head_description: "利用GroupDocs.Parser从Java中的DOCX文档中提取非结构化或结构化文本内容，无需任何外部依赖。"

############################# Header ############################
title: "使用Java从DOCX中提取文本" 
description: "在您的Java开发项目中，使用GroupDocs.Parser无缝提取PDF、Word、Excel等文件中的可读或结构化文本。"
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "免费下载试用版"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "介绍GroupDocs.Parser for Java API"
    link: "/parser/java/"
    link_title: "了解更多"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/)是为Java开发者设计的强大且可扩展的文档解析器。它能够准确从包括PDF、DOCX、XLSX、PPTX等多种格式中提取文本、表格、图像和结构化组件，而无需依赖外部工具。

############################# Steps ############################
steps:
    enable: true
    title: "如何使用Java从Docx中提取文本"
    content: |
      按照以下步骤使用[GroupDocs.Parser](/parser/java/)在您的Java项目中从DOCX文件中提取文本：
      
      1. 使用Parser类加载DOCX文档。
      2. 从文件内容中执行文本提取。
      3. 检查文本是否成功检索。
      4. 在搜索、分析或自动化系统中使用文本数据。
   
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
        // 使用您的文档初始化Parser
        try (Parser parser = new Parser("input.docx"))
        {
            // 读取并提取所有文本数据
            try (TextReader reader = parser.getText())
            {
                // 如文本内容缺失，则返回null
                // 将提取的文本集成到您的工作流中
                System.out.println(reader == null ? 
                    "跳过不支持的文本提取格式" : reader.readToEnd());
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "丰富的文本提取功能"
  description: "GroupDocs.Parser不仅支持简单的文本提取，还能检索图像、元数据和结构化数据，以增强内容处理任务。"
  image: "/img/parser/features_extract-text.webp" # 500x500 px
  image_description: "从文档中提取和结构化文本内容"
  features:
    # feature loop
    - title: "支持多种文档格式"
      content: "从DOCX、XLSX、PPTX、PDF、HTML等多种格式中捕获原始和结构化文本。"

    # feature loop
    - title: "从视觉和文本内容中提取文本"
      content: "从扫描文档、幻灯片、电子表格和其他文件类型中解析文本，同时保留逻辑结构。"

    # feature loop
    - title: "对提取过程进行详细控制"
      content: "配置页面范围、布局区域和精度参数，以实现精确的文本解析。"
      
  code_samples:
    # code sample loop
    - title: "示例：从PPTX文档中提取文本区域"
      content: |
        该示例演示如何使用GroupDocs.Parser从PowerPoint演示文稿中提取文本块及其空间坐标。
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  使用Parser API加载您的PPTX文件
        try (Parser parser = new Parser("input.pptx"))
        {
            // 获取所有矩形文本区域
            IEnumerable<PageTextArea> areas = parser.GetTextAreas();

            // 如果不支持此功能则退出
            if (areas == null)
            {
                return;
            }

            // 按照页面循环遍历文本区域
            for (PageTextArea a : areas)
            {
                // 处理每个文本块及其页码和边界矩形
                System.out.println(String.format("Page: %d, R: %s, Text: %s", a.getPage().getIndex(), a.getRectangle(), a.getText()));
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
    title: "支持文本提取的文件类型"
    exclude: "DOCX"
    description: "GroupDocs.Parser能够从众多文件和图像格式中提取文本内容。以下是其支持的最常用类型。"
    items: 
        # format loop 1
        - name: "解析 PDF"
          format: "PDF"
          link: "/parser/java/extract-text/pdf/"
          description: "(可移植文档格式)"
          
        # format loop 2
        - name: "解析 DOCX"
          format: "DOCX"
          link: "/parser/java/extract-text/docx/"
          description: "(Office 2007+ Word 文档)"
          
        # format loop 3
        - name: "解析 PPTX"
          format: "PPTX"
          link: "/parser/java/extract-text/pptx/"
          description: "(Open XML 演示格式)"
          
        # format loop 4
        - name: "解析 XLSX"
          format: "XLSX"
          link: "/parser/java/extract-text/xlsx/"
          description: "(Open XML 工作簿)"
          
        # format loop 5
        - name: "解析 TXT"
          format: "TXT"
          link: "/parser/java/extract-text/txt/"
          description: "(文本文件)"
          
        # format loop 6
        - name: "解析 RTF"
          format: "RTF"
          link: "/parser/java/extract-text/rtf/"
          description: "(富文本格式)"
          
        # format loop 7
        - name: "解析 XML"
          format: "XML"
          link: "/parser/java/extract-text/xml/"
          description: "(可扩展标记语言)"
          
        # format loop 8
        - name: "解析 EPUB"
          format: "EPUB"
          link: "/parser/java/extract-text/epub/"
          description: "(开放电子书文件)"
         
          

---