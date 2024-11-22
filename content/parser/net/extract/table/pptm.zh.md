---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:12
draft: false
otherformats: 

############################# Head ############################
head_title: "通过 C#.NET API 从 PDF、DOCX、PPTX、XLSX、EPUB 等中提取表"
head_description: "GroupDocs.Parser .NET API 使程序员能够从 PDF、DOC、DOCX、PPT、PPTX、EML、MSG、XLS、XLSX、CSV 中提取表格、ODT、RTF 以及 .NET 应用内的许多其他文档类型。"

############################# Header ############################
title: "通过 C#.NET API 从 Excel、Word、PDF 和 PowerPoint 文档中提取表格"
description: "GroupDocs.Parser .NET API 允许程序员从 PDF、DOC、DOCX、PPT、PPTX、EML、MSG、XLS、XLSX、CSV 中提取表、ODT、RTF 和 EPUB 文档或页面。"
bg_image: "https://cms.admin.containerize.com/templates/aspose/App_Themes/V3/images/bg/header1.png"
bg_overlay: false
button:
    enable: true
    icon: "fas fa-arrow-down"
    label: "下载免费试用版"
    link: "https://downloads.groupdocs.com/parser/net"

############################# SubMenu ############################
submenu:
    enable: true

    left:
        img_alt: "GroupDocs.Parser for .NET"
        image: "https://cms.admin.containerize.com/templates/groupdocs/images/product-logos/90x90-noborder/groupdocs-parser-net.png"
        product: "GroupDocs.Parser"
        platform: ".NET"

    middle:
        button:

            # button loop
            - link: "https://apireference.groupdocs.com/parser/net"
              text: "API参考"

            # button loop
            - link: "https://github.com/groupdocs-parser"
              text: "代码示例"

            # button loop
            - link: "https://products.groupdocs.app/parser/family"
              text: "现场演示"

            # button loop
            - link: "https://purchase.groupdocs.com/pricing/parser/net"
              text: "价钱"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/net"
        link_buy: "https://purchase.groupdocs.com"

############################# About ############################
about:
    enable: true
    title: "如何通过 .NET API 从 PPTM 文件中提取表？"
    content: |
        表是按行和列排列的单元格的集合。表格在存储和组织详细或复杂的数据方面发挥着非常重要的作用，使用户可以轻松阅读和查看数据。表格的使用方式有多种，例如制作列表、比较信息、对齐数据、对信息进行分组、突出显示数据中的趋势或模式等等。 GroupDocs.Parser for .NET 是一个实用的 API，允许软件程序员开发从各种受支持的文档格式中提取表格、文本和图像的解决方案，例如 PDF、电子邮件、电子书、Word (DOC、{ 318})、PowerPoint (PPT、PPTX)、Excel (XLS、XLSX)、电子邮件 (EML、MSG) 格式等等。 .NET API 包含一些用于处理表格的重要功能，例如从文档中提取所有表格、从特定页面提取表格、获取表格单元格数据、获取表格行数和列数、获取行高、打印表格的数据以及更多。
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: "从 .NET 中的 PPTM 中提取表"
    content_left: |
        [GroupDocs.Parser for .NET](/zh/parser/net/) 让 C# 开发者只需执行几个简单的步骤即可轻松从 PPTM 文件中提取表。
        
        * 实例化初始文档的 [Parser](https://reference.groupdocs.com/net/parser/groupdocs.parser/parser) 对象；
        * 检查文档是否支持表格提取；
        * 实例化 [PageTableAreaOptions](https://reference.groupdocs.com/parser/net/groupdocs.parser.options/pagetableareaoptions/) 和 [TemplateTableLayout](https://reference.groupdocs.com/parser/net/groupdocs.parser .templates/templatetablelayout/) 类来设置表格的布局
        * 调用 [GetTables](https://reference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/gettables) 方法并获取 [PageTableArea](https://reference.groupdocs.com/parser/net/groupdocs.parser.data/pagetablearea) 对象；

    title_right: "了解有关表提取的更多信息"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/net/extract-tables-from-document/">如何从文档中提取表格</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-tables-from-document-page/">如何从文档页面中提取表格</a>
 
    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="如何使用 C# 示例代码从 PPTM 文件中提取表">}}

        ```csharp    
        // 使用 GroupDocs.Parser API 从 PPTM 文件中提取表
        // 创建 Parser 类的实例
        using (Parser parser = new Parser(filePath)) {
            // 检查文档是否支持表格提取
            if (!parser.Features.Tables) {
                Console.WriteLine("文档不支持表格提取。");
                return;
            }
            // 创建表格布局
            TemplateTableLayout layout = new TemplateTableLayout(
                new double[] { 50, 95, 275, 415, 485, 545 },
                new double[] { 325, 340, 365, 395 });
            // 创建表提取选项
            PageTableAreaOptions options = new PageTableAreaOptions(layout);
            // 从文档中提取表格。
            IEnumerable<PageTableArea> tables = parser.GetTables(options);
            // 迭代表
            foreach (PageTableArea t in tables) {
                // 迭代行
                for (int row = 0; row < t.RowCount; row++) {
                    // 迭代列
                    for (int column = 0; column < t.ColumnCount; column++) {
                        // 获取表格单元格
                        PageTableAreaCell cell = t[row, column];
                        if (cell != null) {
                            // 打印表格单元格文本
                            Console.Write(cell.Text);
                            Console.Write(" | ");
                        }
                    }
                    Console.WriteLine();
                }
                Console.WriteLine();
            }
        }
        ```
     {{< /parser/code-parser >}}

############################# More ############################
more:
    enable: true
    title_left: "系统要求"
    content_left: |
        GroupDocs.Parser for .NET 所有主要平台和操作系统均支持 API。在执行下面的代码之前，请确保您的系统上安装了以下先决条件。
        
        * 操作系统：Microsoft Windows、Linux、MacOS
        * 开发环境：Microsoft Visual Studio, Xamarin, MonoDevelop
        * 构架
        * 从 [Nuget](https://www.nuget.org/packages/groupdocs.parser) 下载最新版本的 GroupDocs.Parser for .NET

    title_right: "为什么使用GroupDocs.Parser for .NET"
    content_right: |
        * 支持从任何支持的文档中提取纯文本    
        * 通过用户定义的模板解析文档    
        * 全面支持结构化文本提取    
        * 通过关键字和正则表达式进行文本搜索    
        * 提取格式化文本、元数据、图像、容器和附件    
        * 提取某些支持的文档格式的目录    
        * 从 PDF 文档解析表单数据    
        * 从文档中提取超链接   

############################# About Formats ############################
about_formats:
    enable: true

############################# More Formats ############################
more_formats:
    enable: true
    title: "从其他文档格式中提取表格"
    content: |
        .NET 针对文件格式和图像的文档解析和表扫描 API。提取一些流行文件格式的数据，如下所述。

############################# Back to top ###############################
back_to_top:
    enable: true
---