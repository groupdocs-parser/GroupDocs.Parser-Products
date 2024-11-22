---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:07
draft: false
otherformats: odp ods odt one otp ott pdf pps ppsx ppt pptx rtf tex vdx vsdm vsdx
ext: xlam

############################# Head ############################
head_title: ".NET 用于从文档、页面或页面区域解析和提取超链接的 API"
head_description: "GroupDocs.Parser .NET API 使软件程序员能够从 PDF、DOCX、XLSX、CSV、PPTX、EML、MSG、EPUB 的文档、页面或页面区域中提取超链接＆ 还有很多。"

############################# Header ############################
title: "通过 C#/VB.NET API 从文档、页面或特定页面区域提取超链接"
description: "GroupDocs.Parser .NET API 允许软件开发者从 PDF、DOC、DOCX、PPT、PPTX、EML、MSG 的文档、页面或页面区域中解析和提取超链接、XLS、XLSX、CSV、ODT、RTF、EPUB 和许多其他文档。"
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
    title: "如何通过 .NET API 解析和提取 XLAM 文档中的超链接？"
    content: |
        超链接是指向整个文档或文档中特定部分的一段文本、图像或图标。使用超链接允许用户导航到网页或文档。通常需要从文档中提取超链接并使用它来访问外部文档或网页。 GroupDocs.Parser for .NET 是一个令人着迷的文档文本提取 API，它提供了用于实施文本和元数据提取解决方案的完整功能。它支持从 PDF、电子邮件、电子书、Microsoft Office 格式中提取文本和超链接：Word (DOC、DOCX)、PowerPoint (PPT、PPTX)、Excel ( XLS、XLSX）、LibreOffice 格式等等。它支持多种高级功能，用于文档解析、提取纯文本和结构化文本、按关键字搜索文本、提取元数据或图像、容器以及附件等等。
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: "从 .NET 中的 XLAM 中提取超链接"
    content_left: |
        [GroupDocs.Parser for .NET](/zh/parser/net/) 让 C# 开发者只需执行几个简单的步骤即可轻松从 XLAM 文件中提取超链接。
        
        * 实例化初始文档的 [Parser](https://reference.groupdocs.com/net/parser/groupdocs.parser/parser) 对象；
        * 检查文档是否支持超链接提取；
        * 调用 [GetHyperlinks](https://reference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/gethyperlinks) 方法并获取 [PageHyperlinkArea](https://reference.groupdocs.com/parser/net/groupdocs.parser.data/pagehyperlinkarea) 对象；
        * 遍历集合并获取超链接文本和 URL。

    title_right: "了解有关超链接提取的更多信息"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/net/extract-hyperlinks-from-document/">如何从文档中提取超链接</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-hyperlinks-from-document-page/">如何从文档页面中提取超链接</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-hyperlinks-from-document-page-area/">如何从文档页面区域中提取超链接</a>
    
    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="如何使用 C# 示例代码从 XLAM 文件中提取超链接">}}

        ```csharp    
        // 使用 GroupDocs.Parser API 从 XLAM 文件中提取超链接
        // 创建 Parser 类的实例
        using (Parser parser = new Parser(filePath)) {
            // 检查文档是否支持超链接提取
            if (!parser.Features.Hyperlinks) {
                Console.WriteLine("文档不支持超链接提取。");
                return;
            }
            // 从文档中提取超链接
            IEnumerable<PageHyperlinkArea> hyperlinks = parser.GetHyperlinks();
            // 迭代超链接
            foreach (PageHyperlinkArea h in hyperlinks) {
                // 打印超链接文本
                Console.WriteLine(h.Text);
                // 打印超链接 URL
                Console.WriteLine(h.Url);
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
    title: "从其他文档格式中提取超链接"
    content: |
        .NET 针对文件格式和图像的文档解析和超链接提取 API。提取一些流行文件格式的数据，如下所述。

############################# Back to top ###############################
back_to_top:
    enable: true
---