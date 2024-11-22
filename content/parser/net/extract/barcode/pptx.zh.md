---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:05
draft: false
otherformats: vdx vsdm vsdx vssm vssx vstm vstx vsx vtx xlam xls xlsb xlsm xlsx xlt xltm

############################# Head ############################
head_title: ".NET 用于从 PDF、DOCX、PPTX、XLSX、EPUB 等提取条形码的 API"
head_description: "GroupDocs.Parser .NET API 允许软件开发者从 PDF、DOC、DOCX、PPT、PPTX、EML、MSG、XLS、XLSX、 .NET 个应用内的 CSV、ODT、RTF 和 EPUB 文档。"

############################# Header ############################
title: "通过 C#.NET API 从 Excel、Word、PDF 和 PowerPoint 文档中提取条形码"
description: "GroupDocs.Parser .NET API 允许程序员从 PDF、DOC、DOCX、PPT、PPTX、EML、MSG、XLS、XLSX、CSV 中提取条形码、ODT、RTF 和 EPUB 文档或页面区域。"
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
    title: "如何从PPTX文件.NET API中提取条形码？"
    content: |
        条形码是数字和字符的机器可读表示形式，在世界各地的许多环境中普遍使用，例如产品扫描和识别、汽车零部件跟踪、库存管理等。 GroupDocs.Parser for .NET 是一个功能强大的 API，可帮助开发者开发从不同类型的受支持文档格式（例如 PDF、电子邮件、电子书、Microsoft Office 格式）中提取文本、图像和条形码的解决方案：Word ({ 377}、DOCX)、PowerPoint (PPT、PPTX)、Excel (XLS、XLSX)、电子邮件 (EML、MSG) 格式等等。 .NET API 支持多种高级文档解析功能，例如按关键字搜索文本、准确的文本提取、HTML 或 Markdown 格式的文本提取、带坐标的文本区域提取、提取元数据或条形码等。
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: "从.NET中的PPTX中提取条形码"
    content_left: |
        [GroupDocs.Parser for .NET](/zh/parser/net/) 让 C# 开发者只需执行几个简单的步骤即可轻松从 PPTX 文件中提取条形码。
        
        * 实例化初始文档的 [Parser](https://reference.groupdocs.com/net/parser/groupdocs.parser/parser) 对象；
        * 检查文件是否支持条码提取；
        * 调用 [GetBarcodes](https://reference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/getbarcodes) 方法并获取  的集合 [PageBarcodeArea](https://reference.groupdocs.com/parser/net/groupdocs.parser.data/pagebarcodearea) 对象；
        * 迭代集合并获取条形码值。

    title_right: "了解有关条形码提取的更多信息"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/net/extract-barcodes-from-document/">如何从文档中提取条形码</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-barcodes-from-document-page/">如何从文档页面中提取条形码</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-barcodes-from-document-page-area/">如何从文档页面区域提取条形码</a>
    
    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="如何使用 C# 示例代码从 PPTX 文件中提取条形码">}}

        ```csharp    
        // 使用 GroupDocs.Parser API 从 PPTX 文件中提取条形码
        // 创建 Parser 类的实例
        using (Parser parser = new Parser(Constants.SamplePdfWithBarcodes)) {
            // 检查文件是否支持条形码提取
            if (!parser.Features.Barcodes) {
                Console.WriteLine("该文件不支持条形码提取。");
                return;
            }

            // {steps.code.scan}
            IEnumerable<PageBarcodeArea> barcodes = parser.GetBarcodes();

            // 迭代条形码
            foreach (PageBarcodeArea barcode in barcodes) {
                // 打印页面索引
                Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                // 打印条形码值
                Console.WriteLine("Value: " + barcode.Value);
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

############################# Demos ############################
demos:
    enable: true
    title: "现场演示 - 在线从文档中提取条形码"
    content: |
       立即访问 [GroupDocs.Parser 现场演示](https://products.groupdocs.app/parser/barcodes/) 网站，从文档中提取条形码。
       现场演示有以下好处。
        
############################# About Formats ############################
about_formats:
    enable: true

############################# More Formats ############################
more_formats:
    enable: true
    title: "从其他文档格式中提取条形码"
    content: |
        .NET 针对文件格式和图像的文档解析和条形码提取 API。提取一些流行文件格式的数据，如下所述。

############################# Back to top ###############################
back_to_top:
    enable: true
---