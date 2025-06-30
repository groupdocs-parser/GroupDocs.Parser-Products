


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:50
draft: false
lang: zh
format: Xlsx
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "在Java应用程序中从XLSX文件中提取内容"
head_description: "利用GroupDocs.Parser解析并检索Java中XLSX文件的结构化数据、文本、表格和图像，而无需外部工具。"

############################# Header ############################
title: "在Java中提取XLSX文档的数据" 
description: "通过在Java应用程序中使用GroupDocs.Parser，无缝提取PDF、Word、Excel及基于图像的文档中的结构化内容，例如文本、元数据、表格和图形。"
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
       [GroupDocs.Parser](/parser/java/)是一个强大的API，面向Java开发者，提供先进的文档解析功能。它允许您从PDF、DOCX、XLSX、PPTX等多种格式中提取和处理文本数据、图像、表格、结构化字段和条形码，且无需安装额外的库。

############################# Steps ############################
steps:
    enable: true
    title: "如何使用Java从Xlsx提取数据"
    content: |
      要在您的Java项目中使用[GroupDocs.Parser](/parser/java/)从XLSX文档中提取有用信息，请遵循以下步骤：
      
      1. 使用Parser对象打开XLSX文件。
      2. 使用解析器检索所需的数据（文本、表格、元数据等）。
      3. 确保输出正确且完整。
      4. 将解析的内容集成到您的数据流、业务流程或应用程序中。
   
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
        // 使用输入文档初始化Parser
        try (Parser parser = new Parser("input.xlsx"))
        {
            // 从文档中检索所有可用的文本内容
            try (TextReader reader = parser.getText())
            {
                // 如果未找到文本，返回值将为null
                // 将提取的内容整合到您的解决方案中
                System.out.println(reader == null ? 
                    "此格式可能不支持文本提取" : reader.readToEnd());
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "多功能文档解析功能"
  description: "GroupDocs.Parser不仅支持文本提取——它支持对条形码、元数据、图像、表格和其他数据的全面解析，以推动智能自动化和数据驱动的应用程序。"
  image: "/img/parser/features_parse.webp" # 500x500 px
  image_description: "文档数据解析和提取的视觉概述"
  features:
    # feature loop
    - title: "从多种文件格式提取"
      content: "从PDF、Word、Excel、PowerPoint、HTML等广泛使用的文件类型中访问文本、表格和媒体等数据。"

    # feature loop
    - title: "解析数字和扫描来源的内容"
      content: "处理来自原生数字文件和扫描图像的内容，在必要时使用OCR来解释嵌入文本。"

    # feature loop
    - title: "灵活的配置选项"
      content: "通过页面选择、布局区域和自定义字段模板的设置，量身定制您的解析以满足特定的提取需求。"
      
  code_samples:
    # code sample loop
    - title: "使用数据提取模板解析PDF"
      content: |
        该示例展示了如何通过GroupDocs.Parser使用自定义模板从PDF中提取结构化字段。
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  使用Parser类打开PDF
        try (Parser parser = new Parser("input.pdf"))
        {
            // 应用解析模板以提取定义的数据
            DocumentData data = parser.parseByTemplate(GetTemplate());

            // 检查模板基础的提取是否可用
            if (data == null) {
                return;
            }

            // 处理提取的数据字段
            for (int i = 0; i < data.getCount(); i++) {
                System.out.print(data.get(i).getName() + ": ");
                PageTextArea area = data.get(i).getPageArea() instanceof PageTextArea
                        ? (PageTextArea) data.get(i).getPageArea() : null;
                System.out.println(area == null ? "Not a template field" : area.getText());
            }
        }

        private static Template GetTemplate()
        {
            // 定义提取“详情”部分的检测器设置
            TemplateTableParameters detailsTableParameters = 
                new TemplateTableParameters(new Rectangle(new Point(35, 320), new Size(530, 55)), null);

            TemplateItem[] templateItems = new TemplateItem[]
            {
                new TemplateTable(detailsTableParameters, "details", null)
            };

            Template template = new Template(java.util.Arrays.asList(templateItems));
            return template;
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
    title: "支持内容提取的文件类型"
    exclude: "XLSX"
    description: "GroupDocs.Parser与广泛的文档和图像文件类型兼容，使得在解析和数据自动化场景中从常用格式提取信息变得简单。"
    items: 
        # format loop 1
        - name: "解析 PDF"
          format: "PDF"
          link: "/parser/java/parse/pdf/"
          description: "(可移植文档格式)"
          
        # format loop 2
        - name: "解析 DOCX"
          format: "DOCX"
          link: "/parser/java/parse/docx/"
          description: "(Office 2007+ Word 文档)"
          
        # format loop 3
        - name: "解析 PPTX"
          format: "PPTX"
          link: "/parser/java/parse/pptx/"
          description: "(Open XML 演示格式)"
          
        # format loop 4
        - name: "解析 XLSX"
          format: "XLSX"
          link: "/parser/java/parse/xlsx/"
          description: "(Open XML 工作簿)"
          
        # format loop 5
        - name: "解析 TXT"
          format: "TXT"
          link: "/parser/java/parse/txt/"
          description: "(文本文件)"
          
        # format loop 6
        - name: "解析 RTF"
          format: "RTF"
          link: "/parser/java/parse/rtf/"
          description: "(富文本格式)"
          
        # format loop 7
        - name: "解析 XML"
          format: "XML"
          link: "/parser/java/parse/xml/"
          description: "(可扩展标记语言)"
          
        # format loop 8
        - name: "解析 EPUB"
          format: "EPUB"
          link: "/parser/java/parse/epub/"
          description: "(开放电子书文件)"
         
          

---