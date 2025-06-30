


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:53
draft: false
lang: zh
format: Docx
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "在C#应用中解析DOCX文件中的数据"
head_description: "使用GroupDocs.Parser从C#文件中提取文本、图像、表格和其他数据，无需依赖第三方工具。"

############################# Header ############################
title: "使用C#解析DOCX文档" 
description: "在您的.NET项目中，使用GroupDocs.Parser高效提取PDF、Word、Excel和图像文件中的文本、元数据、表格和图像。"
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
    title: "GroupDocs.Parser for .NET API简介"
    link: "/parser/net/"
    link_title: "了解更多"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/) 是一款功能丰富的文档解析API，专为.NET开发人员设计。它支持从常见格式如PDF、DOCX、XLSX、PPTX等中提取纯文本和结构化文本、元数据、图像、表格和条形码，均无需额外的软件依赖。

############################# Steps ############################
steps:
    enable: true
    title: "在C#中从Docx提取数据的步骤"
    content: |
      按照以下步骤使用[GroupDocs.Parser](/parser/net/)在您的.NET应用中解析DOCX文档的内容：
      
      1. 使用Parser实例加载DOCX文档。
      2. 提取所需的内容，例如文本、表格或元数据。
      3. 验证提取的数据是否有效。
      4. 在您的下游处理、自动化或业务系统中使用解析的输出。
   
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
        // 将文档加载到Parser中
        using (Parser parser = new Parser("input.docx")) {

            // 从文件中提取所有文本内容
            using (TextReader reader = parser.GetText()) 
            {
                // 如果文本不可用，结果将为null
                // 在您的应用中使用提取的文本
                Console.WriteLine(reader == null ? 
                    "此格式不支持文本提取" : reader.ReadToEnd());
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "全面的文档解析能力"
  description: "GroupDocs.Parser不仅支持文本读取，还支持条形码提取、图像解析、元数据访问和结构化数据处理，以进行高级自动化和数据分析。"
  image: "/img/parser/features_parse.webp" # 500x500 px
  image_description: "文档内容提取和解析能力"
  features:
    # feature loop
    - title: "支持多种文件内容类型"
      content: "从PDF、Word、Excel、HTML等文档格式中提取文本、图像、表格和字段等数据。"

    # feature loop
    - title: "处理扫描和数字文件"
      content: "支持从扫描文档和数字文件中解析数据，同时支持OCR和布局感知提取。"

    # feature loop
    - title: "可配置的提取参数"
      content: "通过灵活的选项调整解析逻辑，如页面范围选择、区域定位和字段检测模板。"
      
  code_samples:
    # code sample loop
    - title: "如何使用模板解析PDF"
      content: |
        此示例展示了如何使用GroupDocs.Parser通过预定义的解析模板提取PDF中的结构化数据。
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  使用Parser类加载PDF文件
        using (Parser parser = new Parser("input.pdf"))
        {
            // 根据模板解析文档
            DocumentData data = parser.ParseByTemplate(GetTemplate());

            // 检查是否支持表单提取
            if (data == null)
            {
                return;
            }

            // 处理获得的字段
            for (int i = 0; i < data.Count; i++)
            {
                Console.Write(data[i].Name + ": ");
                PageTextArea area = data[i].PageArea as PageTextArea;
                Console.WriteLine(area == null ? "Not a template field" : area.Text);
            }
        }

        private static Template GetTemplate()
        {
            // 为'详情'表创建检测器参数
            TemplateTableParameters detailsTableParameters = 
                new TemplateTableParameters(new Rectangle(new Point(35, 320), new Size(530, 55)), null);

            TemplateItem[] templateItems = new TemplateItem[]
            {
                new TemplateTable(detailsTableParameters, "details", null)
            };

            Template template = new Template(templateItems);
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
    title: "支持的数据提取格式"
    exclude: "DOCX"
    description: "GroupDocs.Parser能够解析广泛的文档和图像格式。了解在数据提取工作流程中常用的支持文件类型。"
    items: 
        # format loop 1
        - name: "解析 PDF"
          format: "PDF"
          link: "/parser/net/parse/pdf/"
          description: "(可移植文档格式)"
          
        # format loop 2
        - name: "解析 DOCX"
          format: "DOCX"
          link: "/parser/net/parse/docx/"
          description: "(Office 2007+ Word 文档)"
          
        # format loop 3
        - name: "解析 PPTX"
          format: "PPTX"
          link: "/parser/net/parse/pptx/"
          description: "(Open XML 演示格式)"
          
        # format loop 4
        - name: "解析 XLSX"
          format: "XLSX"
          link: "/parser/net/parse/xlsx/"
          description: "(Open XML 工作簿)"
          
        # format loop 5
        - name: "解析 TXT"
          format: "TXT"
          link: "/parser/net/parse/txt/"
          description: "(文本文件)"
          
        # format loop 6
        - name: "解析 RTF"
          format: "RTF"
          link: "/parser/net/parse/rtf/"
          description: "(富文本格式)"
          
        # format loop 7
        - name: "解析 XML"
          format: "XML"
          link: "/parser/net/parse/xml/"
          description: "(可扩展标记语言)"
          
        # format loop 8
        - name: "解析 EPUB"
          format: "EPUB"
          link: "/parser/net/parse/epub/"
          description: "(开放电子书文件)"
         
          

---