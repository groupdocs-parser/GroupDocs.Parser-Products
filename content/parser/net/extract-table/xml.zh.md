


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:41
draft: false
lang: zh
format: Xml
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "在 C# 应用程序中从 XML 文件提取表格"
head_description: "使用 GroupDocs.Parser 在 C# 应用程序中定位并提取来自 XML 文件的结构化表格数据，无需额外依赖。"

############################# Header ############################
title: "使用 C# 从 XML 提取表格" 
description: "使用 GroupDocs.Parser 快速识别并提取来自 PDF、Word、Excel 和其他文件格式的表格结构，适用于您的 .NET 项目。"
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
       [GroupDocs.Parser](/parser/net/) 是一款专为 .NET 开发人员构建的全面文档解析 API。它能够从 PDF、DOCX、XLSX、PPTX 等格式中精确提取文本、表格、图像、超链接和其他结构化元素，无需第三方软件。

############################# Steps ############################
steps:
    enable: true
    title: "在 C# 中从 Xml 提取表格的步骤"
    content: |
      请按照以下说明使用 [GroupDocs.Parser](/parser/net/) 在您的 .NET 环境中提取 XML 文件中的表格：
      
      1. 初始化一个 Parser 实例并加载您的 XML 文档。
      2. 检查输入格式是否支持表格提取。
      3. 从文件中提取表格内容。
      4. 利用结构化表格数据进行报告、自动化或分析。
   
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
        // 使用 Parser 打开包含表格数据的文档
        using (Parser parser = new Parser("input.xml")) {

            // 检查格式是否支持表格识别
            if (!parser.Features.Tables) {
                Console.WriteLine("处理不支持表格解析的文档");
                return;
            }

            // 定义如何识别表格结构
            TemplateTableLayout layout = new TemplateTableLayout(
                new double[] { 50, 95, 275, 415, 485, 545 },
                new double[] { 325, 340, 365, 395 });

            // 指定表格数据的提取参数
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            //  从文件内容中提取表格
            IEnumerable<PageTableArea> tables = parser.GetTables(options);

            //  遍历每个检测到的表格
            foreach (PageTableArea t in tables)
            {
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "强大的数据提取能力"
  description: "除了表格解析，GroupDocs.Parser 还能够提取丰富的内容，如文本块、图像、元数据及其他结构化数据，以促进文档自动化。"
  image: "/img/parser/features_extract-table.webp" # 500x500 px
  image_description: "表格识别和内容提取"
  features:
    # feature loop
    - title: "准确的多格式表格检测"
      content: "高精度地从 DOCX、XLSX、PDF、HTML 和类似格式中提取表格数据。"

    # feature loop
    - title: "从文件中解析表格结构"
      content: "高效地从文档和电子表格中检索表格数据，无需格式损失。"

    # feature loop
    - title: "灵活的表格提取配置"
      content: "调整布局检测、列对齐和页眉/页脚选项，以精确控制输出。"
      
  code_samples:
    # code sample loop
    - title: "如何从 Excel 电子表格提取表格"
      content: |
        这个代码示例展示了如何使用 GroupDocs.Parser 读取和遍历 XLSX 文件中的表格数据。
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  使用 Parser API 打开 Excel 文件
        using (Parser parser = new Parser("input.xlsx"))
        {
            // 如果无法从文件中提取表格，则退出
            if (!parser.Features.Tables)
            {
                return;
            }

            // 使用布局规则定位表格内容
            TemplateTableLayout layout = new TemplateTableLayout(
                    new double[] { 50, 95, 275, 415, 485, 545 },
                    new double[] { 325, 340, 365, 395 });

            // 设置表格的提取参数
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            // 执行表格提取操作
            IEnumerable<PageTableArea> tables = parser.GetTables(options);

            // 遍历每个检测到的表格结构
            foreach (PageTableArea t in tables)
            {
                // 遍历表格中的每一行
                for (int row = 0; row < t.RowCount; row++)
                {
                    // 循环遍历每行中的单元格
                    for (int column = 0; column < t.ColumnCount; column++)
                    {
                        // 访问当前表格单元格
                        PageTableAreaCell cell = t[row, column];
                        if (cell != null)
                        {
                            // 显示每个单元格的文本内容
                            Console.Write(cell.Text);
                            Console.Write(" | ");
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
    title: "支持的表格提取格式"
    exclude: "XML"
    description: "GroupDocs.Parser 能够从多种文档类型中提取表格数据。以下是进行结构化表格解析时最常用的格式。"
    items: 
        # format loop 1
        - name: "解析 PDF"
          format: "PDF"
          link: "/parser/net/extract-table/pdf/"
          description: "(可移植文档格式)"
          
        # format loop 2
        - name: "解析 DOCX"
          format: "DOCX"
          link: "/parser/net/extract-table/docx/"
          description: "(Office 2007+ Word 文档)"
          
        # format loop 3
        - name: "解析 PPTX"
          format: "PPTX"
          link: "/parser/net/extract-table/pptx/"
          description: "(Open XML 演示格式)"
          
        # format loop 4
        - name: "解析 XLSX"
          format: "XLSX"
          link: "/parser/net/extract-table/xlsx/"
          description: "(Open XML 工作簿)"
          
        # format loop 5
        - name: "解析 TXT"
          format: "TXT"
          link: "/parser/net/extract-table/txt/"
          description: "(文本文件)"
          
        # format loop 6
        - name: "解析 RTF"
          format: "RTF"
          link: "/parser/net/extract-table/rtf/"
          description: "(富文本格式)"
          
        # format loop 7
        - name: "解析 XML"
          format: "XML"
          link: "/parser/net/extract-table/xml/"
          description: "(可扩展标记语言)"
          
        # format loop 8
        - name: "解析 EPUB"
          format: "EPUB"
          link: "/parser/net/extract-table/epub/"
          description: "(开放电子书文件)"
         
          

---