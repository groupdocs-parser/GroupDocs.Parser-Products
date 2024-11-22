---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:14
draft: false
otherformats: 

############################# Head ############################
head_title: "从 C# 中的 FB2 中提取文本"
head_description: "从 C# 中的文档文件中快速提取文本。"

############################# Header ############################
title: "从 C# 中的 FB2 中提取文本"
description: "使用几行 .NET 代码从 FB2 中提取文本。"
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
    title: "如何从 FB2 文件 .NET API 中提取文本？"
    content: |
        [GroupDocs.Parser for .NET](/zh/parser/net/) 是一个文本、元数据和图像提取器 API，适用于使用 C#、ASP.NET 和其他 .NET 技术开发的业务应用程序。它支持从支持格式的文件中提取原始、格式化和结构化文本以及元数据。通过 GroupDocs.Parser for .NET，您的应用程序还可以解析流行格式的受密码保护的文档，例如 Word 处理文档、Excel 电子表格、PowerPoint 演示文稿、OneNote、PDF 文件和 ZIP 存档。
        
        GroupDocs.Parser API 是需要文件文本提取功能的企业解决方案的正确选择。这些 API 在所有主要操作系统和平台（包括 Frameworks: .NET Framework, .NET Standard, .NET Core, Mono）上均得到良好支持。

############################# Steps ############################
steps:
    enable: true
    title_left: "从 .NET 中的 FB2 中提取文本"
    content_left: |
        [GroupDocs.Parser for .NET](/zh/parser/net/) 让 C# 开发者只需执行几个简单的步骤即可轻松从 FB2 文件中提取文本。
        
        * 实例化初始文档的 [Parser](https://reference.groupdocs.com/net/parser/groupdocs.parser/parser) 对象；
        * 调用 [GetText](https://reference.groupdocs.com/net/parser/groupdocs.parser/parser/methods/gettext) 方法并获取 [TextReader](https://docs.microsoft.com/en-us/dotnet/api/system.io.textreader?view=netframework-2.0) 对象；
        * 检查 reader 是否不为*null*（文档支持文本提取）；
        * 阅读读者的文字。

    title_right: "了解有关文本提取的更多信息"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/net/extract-text-in-accurate-mode/">如何在精确模式下提取文本</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-text-in-raw-mode/">如何在原始模式下提取文本</a>
 
    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="如何使用 C# 示例代码从 FB2 文件中提取文本">}}

        ```csharp    
        // 使用 GroupDocs.Parser API 从 FB2 文件中提取文本
        // 创建 Parser 类的实例
        using (Parser parser = new Parser(filePath)) {
            // 将文本提取到阅读器中
            using (TextReader reader = parser.GetText()) {
                // 打印文档中的文本
                // 如果不支持文本提取，则 reader 为空
                Console.WriteLine(reader == null ? "不支持文本提取" : reader.ReadToEnd());
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
    title: "现场演示 - 从 FB2 在线提取文本"
    content: |
       立即访问 [GroupDocs.Parser 现场演示](https://products.groupdocs.app/parser/text/fb2) 网站，从 FB2 文件中提取文本。
       现场演示有以下好处。
        
############################# About Formats ############################
about_formats:
    enable: true

############################# More Formats ############################
more_formats:
    enable: true
    title: "从其他文档格式中提取文本"
    content: |
        .NET 用于文件格式和图像的文档解析和文本提取 API。提取一些流行文件格式的数据，如下所述。

############################# Back to top ###############################
back_to_top:
    enable: true
---