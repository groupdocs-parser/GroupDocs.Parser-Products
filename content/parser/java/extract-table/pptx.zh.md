


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:38
draft: false
lang: zh
format: Pptx
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "使用 Java 应用从 PPTX 文档中提取表格"
head_description: "使用 GroupDocs.Parser 从 Java 应用程序中提取 PPTX 文件的结构化表格数据——无需外部工具。"

############################# Header ############################
title: "使用 Java 从 PPTX 提取表格数据" 
description: "在您的 Java 工作流中，使用 GroupDocs.Parser 无缝检测和提取 PDF、DOCX 和 XLSX 等格式的表格。"
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "下载免费试用版"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "GroupDocs.Parser for Java API 介绍"
    link: "/parser/java/"
    link_title: "了解更多"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) 是一个功能丰富的内容提取 API，适用于 Java 平台。它允许开发人员准确解析 PDF、Word 文档、Excel 表格、PowerPoint 演示文稿等中的表格、文本、图形、链接和结构化数据——不需要第三方插件。

############################# Steps ############################
steps:
    enable: true
    title: "如何在 Java 中从 Pptx 获取表格"
    content: |
      要使用 [GroupDocs.Parser](/parser/java/) 从 PPTX 文档中解析表格，请按照以下步骤在您的 Java 环境中操作：
      
      1. 创建一个 Parser 实例并加载目标 PPTX 文件。
      2. 验证该文件是否支持结构化表格提取。
      3. 使用 API 从文档中检索表格元素。
      4. 在分析、报告或自动化系统中使用提取的数据。
   
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
        // 加载包含表格元素的输入文档
        try (Parser parser = new Parser("input.pptx"))
        {
            // 验证文档类型是否允许表格识别
            if (!parser.getFeatures().isTables()) {
                System.out.println("为不支持表格的文件添加逻辑");
                return;
            }

            // 定义解释表格结构的规则
            TemplateTableLayout layout = new TemplateTableLayout(
                    java.util.Arrays.asList(new Double[]{50.0, 95.0, 275.0, 415.0, 485.0, 545.0}),
                    java.util.Arrays.asList(new Double[]{325.0, 340.0, 365.0, 395.0}));

            // 设置提取表格的参数
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            //  在加载的文档上运行表格提取
            Iterable<PageTableArea> tables = parser.getTables(options);

            //  处理提取结果中的每个表格
            for (PageTableArea t : tables) 
            {
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "高级内容提取工具"
  description: "除了读取表格，GroupDocs.Parser 还支持捕获纯文本、视觉元素、嵌入的元数据和结构化对象，以增强文档处理任务。"
  image: "/img/parser/features_extract-table.webp" # 500x500 px
  image_description: "提取结构化内容和表格数据"
  features:
    # feature loop
    - title: "跨格式精准解析表格"
      content: "支持从 PDF、Word、Excel 和 HTML 等标准文档类型中高精度提取表格。"

    # feature loop
    - title: "从多种来源读取表格结构"
      content: "在保留结构和对齐的前提下，从电子表格、文档和报告中提取表格数据。"

    # feature loop
    - title: "可自定义的表格提取设置"
      content: "控制布局检测，管理页眉和页脚，并通过灵活的配置选项细化提取。"
      
  code_samples:
    # code sample loop
    - title: "示例：从 Excel 文档中提取表格"
      content: |
        此示例显示如何使用 GroupDocs.Parser 提取 Excel（XLSX）文件中的表格内容并进行循环。
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  使用 Excel 文件初始化 Parser
        try (Parser parser = new Parser("input.pdf"))
        {
            // 如果此文档不支持表格提取，则退出
            if (!parser.getFeatures().isTables())
            {
                return;
            }

            // 应用规则以定位表格布局
            TemplateTableLayout layout = new TemplateTableLayout(
                    java.util.Arrays.asList(new Double[]{50.0, 95.0, 275.0, 415.0, 485.0, 545.0}),
                    java.util.Arrays.asList(new Double[]{325.0, 340.0, 365.0, 395.0}));

            // 配置表格提取的设置
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            // 调用提取过程
            Iterable<PageTableArea> tables = parser.getTables(options);

            // 循环遍历所有解析的表格结构
            for (PageTableArea t : tables)
            {
                // 迭代表格中的每一行
                for (int row = 0; row < t.getRowCount(); row++)
                {
                    // 处理当前行中的每个单元格
                    for (int column = 0; column < t.getColumnCount(); column++) 
                    {
                        // 访问并读取当前单元格的内容
                        PageTableAreaCell cell = t.getCell(row, column);
                        if (cell != null)
                        {
                            // 输出每个表格单元格的文本值
                            System.out.print(cell.getText());
                            System.out.print(" | ");
                        }
                    }
                }
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
    title: "支持提取表格的文档类型"
    exclude: "PPTX"
    description: "GroupDocs.Parser 提供多个文件类型的可靠表格检测。以下是支持提取表格的最常见文档格式列表。"
    items: 
        # format loop 1
        - name: "解析 PDF"
          format: "PDF"
          link: "/parser/java/extract-table/pdf/"
          description: "(可移植文档格式)"
          
        # format loop 2
        - name: "解析 DOCX"
          format: "DOCX"
          link: "/parser/java/extract-table/docx/"
          description: "(Office 2007+ Word 文档)"
          
        # format loop 3
        - name: "解析 PPTX"
          format: "PPTX"
          link: "/parser/java/extract-table/pptx/"
          description: "(Open XML 演示格式)"
          
        # format loop 4
        - name: "解析 XLSX"
          format: "XLSX"
          link: "/parser/java/extract-table/xlsx/"
          description: "(Open XML 工作簿)"
          
        # format loop 5
        - name: "解析 TXT"
          format: "TXT"
          link: "/parser/java/extract-table/txt/"
          description: "(文本文件)"
          
        # format loop 6
        - name: "解析 RTF"
          format: "RTF"
          link: "/parser/java/extract-table/rtf/"
          description: "(富文本格式)"
          
        # format loop 7
        - name: "解析 XML"
          format: "XML"
          link: "/parser/java/extract-table/xml/"
          description: "(可扩展标记语言)"
          
        # format loop 8
        - name: "解析 EPUB"
          format: "EPUB"
          link: "/parser/java/extract-table/epub/"
          description: "(开放电子书文件)"
         
          

---