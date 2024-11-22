---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:10
draft: false
otherformats: doc docm docx dot dotm dotx epub html mht mhtml odp ods odt one otp ott pdf

############################# Head ############################
head_title: "通过 .NET 从 Excel、Word、PDF 和其他文档或页面中提取图像"
head_description: "GroupDocs.Parser .NET API 使软件程序员能够从其 .NET 应用内的不同文档（例如 MS Excel、Word、PowerPoint、PDF 等）中提取图像。"

############################# Header ############################
title: "通过 C#.NET API 从 PDF、DOCX、PPTX、MSG、XLSX 文档和页面中提取图像"
description: "GroupDocs.Parser .NET API 允许程序员从 PDF、DOC、DOCX、PPT、PPTX、EML、MSG、XLS、XLSX、CSV 中提取图像、ODT、RTF 和 EPUB 文档或文档页面。"
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
    title: "如何通过.NET从文档中提取图像？"
    content: |
        图像可以用来以文字无法表达的方式传递信息。图像帮助我们吸引用户的注意力并轻松解释困难的概念。有时，在阅读文档、期刊或从演示文稿中受益时，我们经常会发现一些引人入胜的图像并想要下载它。 GroupDocs.Parser for .NET 是一个功能强大的 API，可帮助用户开发有用的应用程序，用于从不同类型的文档中提取图像并将其保存为 PNG、JPEG、WebP、GIF、BMP 和其他格式。该 API 支持从一些最常用的文件格式中提取文本和图像，例如 PDF、电子邮件、电子书、Microsoft Office 格式：Word (DOC、DOCX)、{ 284} (PPT、PPTX)、Excel (XLS、XLSX)、LibreOffice 格式等等。该 API 还完全支持文档解析、提取纯文本和结构化文本、按关键字进行文本搜索、提取元数据或图像、容器以及附件等等。
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: "从 .NET 中的文档中提取图像"
    content_left: |
        [GroupDocs.Parser for .NET](/zh/parser/net/) 让 C# 开发者只需执行几个简单的步骤即可轻松从文档中提取图像。
        
        * 实例化初始文档的 [Parser](https://reference.groupdocs.com/net/parser/groupdocs.parser/parser) 对象；
        * 调用[GetImages](https://reference.groupdocs.com/net/parser/groupdocs.parser/parser/methods/getimages)方法并获取图像对象集合；
        * 检查 reader 是否不为*null*（文档支持图像提取）；
        * 迭代集合并获取尺寸、图像类型和图像内容。

    title_right: "了解有关图像提取的更多信息"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/net/extract-images-from-document/">如何从文档中提取图像</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-images-from-document-page/">如何从文档页面中提取图像</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-images-from-document-page-area/">如何从文档页面区域提取图像</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-images-to-files/">如何将图像提取到文件</a>

    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="如何使用 C# 示例代码从文档中提取图像">}}

        ```csharp    
        // 使用 GroupDocs.Parser API 从文档中提取图像
        // 创建 Parser 类的实例
        using (Parser parser = new Parser(filePath)) {
            // 提取图像
            IEnumerable<PageImageArea> images = parser.GetImages();
            // 检查是否支持图像提取
            if (images == null) {
                Console.WriteLine("不支持图像提取");
                return;
            }
            // 迭代图像
            foreach (PageImageArea image in images) {
                // 打印页面索引、矩形和图像类型：
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Type: {2}", image.Page.Index, image.Rectangle, image.FileType));
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
    title: "现场演示 - 在线从文档中提取图像"
    content: |
       立即访问 [GroupDocs.Parser 现场演示](https://products.groupdocs.app/parser/images/) 网站，从文档中提取图像。
       现场演示有以下好处。
        
############################# About Formats ############################
about_formats:
    enable: true

############################# More Formats ############################
more_formats:
    enable: true
    title: "从其他文档格式中提取图像"
    content: |
        .NET 用于文件格式和图像的文档解析和图像提取 API。提取一些流行文件格式的数据，如下所述。

############################# Back to top ###############################
back_to_top:
    enable: true
---