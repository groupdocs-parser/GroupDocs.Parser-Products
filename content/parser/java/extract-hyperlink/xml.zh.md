


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:24
draft: false
lang: zh
format: Xml
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "从 XML 文件中提取超链接，适用于 Java 应用程序"
head_description: "使用 GroupDocs.Parser 在 Java 项目中查找并提取 XML 文档中的网址链接，无需额外软件。"

############################# Header ############################
title: "使用 Java 从 XML 中提取超链接" 
description: "在您的 Java 环境中，使用 GroupDocs.Parser 从 PDF、Word 文件、Excel 表及其他文档中提取网站链接和超链接。"
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
    title: "GroupDocs.Parser for Java API 介绍"
    link: "/parser/java/"
    link_title: "了解更多"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) 是一款强大的内容提取 API，旨在为 Java 开发者提供服务。它提供了从 DOCX、XLSX、PDF、HTML 等流行格式中提取超链接、结构化数据、图像和文本的工具，所有操作无需任何外部插件。

############################# Steps ############################
steps:
    enable: true
    title: "如何在 Java 中从 Xml 提取超链接"
    content: |
      [GroupDocs.Parser](/parser/java/) 通过以下基本步骤简化在 Java 应用程序中从 XML 文件中提取超链接的过程：
      
      1. 使用 Parser 的实例打开 XML 文件。
      2. 确保该文件格式支持超链接提取。
      3. 使用相应的方法提取所有超链接。
      4. 遍历结果并根据需要处理每个链接。
   
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
        // 使用 Parser 加载可能包含超链接的文件
        try (Parser parser = new Parser("input.xml")) {

            // 检查文档格式是否支持超链接解析
            if (!parser.getFeatures().isHyperlinks()) {
                System.out.println("该文件不支持超链接提取");
                return;
            }

            // 从文档中提取并使用超链接数据
            Iterable<PageHyperlinkArea> hyperlinks = parser.getHyperlinks();

            for (PageHyperlinkArea h : hyperlinks) {
                System.out.println(h.getText());
                System.out.println(h.getUrl());
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "全面的文档解析工具"
  description: "除了提取超链接，GroupDocs.Parser 允许您收集其他有用的内容，例如纯文本、嵌入式媒体和结构化数据，以便在自动化工作流程中使用。"
  image: "/img/parser/features_extract-hyperlink.webp" # 500x500 px
  image_description: "超链接提取和文档分析"
  features:
    # feature loop
    - title: "准确的链接检测"
      content: "从不同文档布局中捕捉所有类型的超链接，包括可点击的文本和隐藏的 URL。"

    # feature loop
    - title: "适用于文档和网页内容"
      content: "从包含嵌入超链接的 PDF、DOCX、XLSX、HTML 和图像文件中提取链接。"

    # feature loop
    - title: "自定义提取行为"
      content: "使用页面范围、链接类型或内容过滤器等选项精炼超链接的提取方式。"
      
  code_samples:
    # code sample loop
    - title: "示例：使用自定义选项从 PDF 中提取超链接"
      content: |
        此示例演示如何使用链接提取设置从 PDF 文件中提取所有链接。
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  使用 Parser 类打开 PDF
        try (Parser parser = new Parser("input.docx"))
        {
            // 验证此文档是否启用了超链接支持
            if (!parser.getFeatures().isHyperlinks()) {
                return;
            }

            // 应用选项以过滤链接
            PageAreaOptions options = new PageAreaOptions(new Rectangle(new Point(380, 90), new Size(150, 50)));

            // 使用解析器获取超链接数据
            Iterable<PageHyperlinkArea> hyperlinks = parser.getHyperlinks(options);

            // 遍历链接并相应处理
            for (PageHyperlinkArea h : hyperlinks) {
                System.out.println(h.getText());
                System.out.println(h.getUrl());
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
    title: "支持超链接提取的文档格式"
    exclude: "XML"
    description: "通过 GroupDocs.Parser，您可以从许多常用的文件格式中提取超链接。以下是通常支持的格式列表。"
    items: 
        # format loop 1
        - name: "解析 PDF"
          format: "PDF"
          link: "/parser/java/extract-hyperlink/pdf/"
          description: "(可移植文档格式)"
          
        # format loop 2
        - name: "解析 DOCX"
          format: "DOCX"
          link: "/parser/java/extract-hyperlink/docx/"
          description: "(Office 2007+ Word 文档)"
          
        # format loop 3
        - name: "解析 PPTX"
          format: "PPTX"
          link: "/parser/java/extract-hyperlink/pptx/"
          description: "(Open XML 演示格式)"
          
        # format loop 4
        - name: "解析 XLSX"
          format: "XLSX"
          link: "/parser/java/extract-hyperlink/xlsx/"
          description: "(Open XML 工作簿)"
          
        # format loop 5
        - name: "解析 TXT"
          format: "TXT"
          link: "/parser/java/extract-hyperlink/txt/"
          description: "(文本文件)"
          
        # format loop 6
        - name: "解析 RTF"
          format: "RTF"
          link: "/parser/java/extract-hyperlink/rtf/"
          description: "(富文本格式)"
          
        # format loop 7
        - name: "解析 XML"
          format: "XML"
          link: "/parser/java/extract-hyperlink/xml/"
          description: "(可扩展标记语言)"
          
        # format loop 8
        - name: "解析 EPUB"
          format: "EPUB"
          link: "/parser/java/extract-hyperlink/epub/"
          description: "(开放电子书文件)"
         
          

---