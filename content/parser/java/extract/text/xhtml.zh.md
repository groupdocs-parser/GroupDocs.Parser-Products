---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:14
draft: false
otherformats: 

############################# Head ############################
head_title: "从 Java 中的 XHTML 中提取文本"
head_description: "从 Java 中的文档文件中快速提取文本。"

############################# Header ############################
title: "从 Java 中的 XHTML 中提取文本"
description: "使用几行 Java 代码从 XHTML 中提取文本。"
bg_image: "https://cms.admin.containerize.com/templates/aspose/App_Themes/V3/images/bg/header1.png"
bg_overlay: false
button:
    enable: true
    icon: "fas fa-arrow-down"
    label: "下载免费试用版"
    link: "https://downloads.groupdocs.com/parser/java"

############################# SubMenu ############################
submenu:
    enable: true

    left:
        img_alt: "GroupDocs.Parser for Java"
        image: "https://cms.admin.containerize.com/templates/groupdocs/images/product-logos/90x90-noborder/groupdocs-parser-java.png"
        product: "GroupDocs.Parser"
        platform: "Java"

    middle:
        button:

            # button loop
            - link: "https://apireference.groupdocs.com/parser/java"
              text: "API参考"

            # button loop
            - link: "https://github.com/groupdocs-parser"
              text: "代码示例"

            # button loop
            - link: "https://products.groupdocs.app/parser/family"
              text: "现场演示"

            # button loop
            - link: "https://purchase.groupdocs.com/pricing/parser/java"
              text: "价钱"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/java"
        link_buy: "https://purchase.groupdocs.com"

############################# About ############################
about:
    enable: true
    title: "如何从 XHTML 文件 Java API 中提取文本？"
    content: |
        [GroupDocs.Parser for Java](/zh/parser/java/) 是一个文本、图像和元数据提取器 API，支持 50 多种流行的文档类型，有助于构建具有解析原始、结构化和格式化文本功能的业务应用程序。它还支持使用预定义模板解析文档，并允许快速、准确地从发票和其他典型文档中提取复杂数据。 GroupDocs.Parser for Java 使您能够从所有流行格式的受密码保护的文件中提取文本和元数据，包括Word 处理文档、Excel 电子表格、PowerPoint 演示文稿、OneNote、PDF 文件和 ZIP 存档。
        
        GroupDocs.Parser API 是需要文件文本提取功能的企业解决方案的正确选择。这些 API 在所有主要操作系统和平台（包括 Java runtime: J2SE 6.0 and above）上均得到良好支持。

############################# Steps ############################
steps:
    enable: true
    title_left: "从 Java 中的 XHTML 中提取文本"
    content_left: |
        [GroupDocs.Parser for Java](/zh/parser/java/) 让 Java 开发者只需执行几个简单的步骤即可轻松从 XHTML 文件中提取文本。
        
        * 实例化初始文档的 [Parser](https://reference.groupdocs.com/java/parser/com.groupdocs.parser/Parser) 对象；
        * 调用 [getText](https://reference.groupdocs.com/parser/java/com.groupdocs.parser/parser/#getText--) 方法并获取 [TextReader](https://reference.groupdocs.com/java/parser/com.groupdocs.parser.data/TextReader) 对象；
        * 检查 reader 是否不为*null*（文档支持文本提取）；
        * 阅读读者的文字。

    title_right: "了解有关文本提取的更多信息"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/java/extract-text-in-accurate-mode/">如何在精确模式下提取文本</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-text-in-raw-mode/">如何在原始模式下提取文本</a>
 
    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="如何使用 Java 示例代码从 XHTML 文件中提取文本">}}

        ```java    
        // 使用 GroupDocs.Parser API 从 XHTML 文件中提取文本
        // 创建 Parser 类的实例
        try (Parser parser = new Parser(filePath)) {
            // 将文本提取到阅读器中
            try (TextReader reader = parser.getText()) {
                // 打印文档中的文本
                // 如果不支持文本提取，则 reader 为空
                System.out.println(reader == null ? "不支持文本提取" : reader.readToEnd());
            }
        }
        ```
     {{< /parser/code-parser >}}

############################# More ############################
more:
    enable: true
    title_left: "系统要求"
    content_left: |
        GroupDocs.Parser for Java 所有主要平台和操作系统均支持 API。在执行下面的代码之前，请确保您的系统上安装了以下先决条件。
        
        * 操作系统：Microsoft Windows、Linux、MacOS
        * 开发环境：NetBeans, Intellij IDEA, Eclipse, etc.
        * 构架
        * 从 [Maven](https://repository.groupdocs.com/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs-parser) 下载最新版本的 GroupDocs.Parser for Java

    title_right: "为什么使用GroupDocs.Parser for Java"
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
    title: "现场演示 - 从 XHTML 在线提取文本"
    content: |
       立即访问 [GroupDocs.Parser 现场演示](https://products.groupdocs.app/parser/text/xhtml) 网站，从 XHTML 文件中提取文本。
       现场演示有以下好处。
        
############################# About Formats ############################
about_formats:
    enable: true

############################# More Formats ############################
more_formats:
    enable: true
    title: "从其他文档格式中提取文本"
    content: |
        Java 用于文件格式和图像的文档解析和文本提取 API。提取一些流行文件格式的数据，如下所述。

############################# Back to top ###############################
back_to_top:
    enable: true
---