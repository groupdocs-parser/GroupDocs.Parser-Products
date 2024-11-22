---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:10
draft: false
otherformats: doc docm docx dot dotm dotx epub html mht mhtml odp ods odt one otp ott pdf

############################# Head ############################
head_title: "如何通过Java从Excel、Word、PDF和其他文档中提取图像？"
head_description: "GroupDocs.Parser for Java API 允许软件开发者从 Java 应用内的 PDF、DOC、DOCX、PPT、PPTX、XLS、XLSX 文档和电子邮件中解析和提取图像。"

############################# Header ############################
title: "Java 用于从 Excel、Word、PowerPoint、PDF 和其他文档页面解析和提取图像的 API"
description: "GroupDocs.Parser for Java API 允许程序员从 PDF、DOC、DOCX、PPT、PPTX、EML、MSG、XLS、XLSX、CSV、{358 }、RTF 和 EPUB 文档或 Java 应用程序内的文档页面。"
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
    title: "了解如何通过 Java API 从 {{EXT}} 文档或特定页面提取图像"
    content: |
        一张图片胜过一千个文字，在当今的视觉世界中，在创建引人入胜的内容时，不容忽视。图像可以成为信息交流的重要来源，也可以吸引用户的注意力。通常需要从文档、期刊或演示文稿中获取图像并在其他地方使用它们。 GroupDocs.Parser for Java 是一个功能强大的 API，可帮助软件开发人员和程序员构建从多种文档类型中解析和提取图像或其他信息的解决方案。它还支持将图片保存为PNG、JPEG、WebP、GIF、BMP等格式。该 API 支持一些流行的文档格式，例如 PDF、Microsoft Office 格式：Word (DOC、DOCX)、PowerPoint (PPT、PPTX)、{282 }（XLS、XLSX）、LibreOffice 格式、电子邮件、电子书等等。它还支持一些与文档解析、提取纯文本和结构化文本、按关键字进行文本搜索、提取元数据或图像、容器以及附件等相关的高级功能。
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: "从 Java 中的文档中提取图像"
    content_left: |
        [GroupDocs.Parser for Java](/zh/parser/java/) 让 Java 开发者只需执行几个简单的步骤即可轻松从文档中提取图像。
        
        * 实例化初始文档的 [Parser](https://reference.groupdocs.com/java/parser/com.groupdocs.parser/Parser) 对象；
        * 调用 [getImages](https://reference.groupdocs.com/parser/java/com.groupdocs.parser/parser/#getImages--) 方法并获取图像对象集合；
        * 检查 reader 是否不为*null*（文档支持图像提取）；
        * 迭代集合并获取尺寸、图像类型和图像内容。

    title_right: "了解有关图像提取的更多信息"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/java/extract-images-from-document/">如何从文档中提取图像</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-images-from-document-page/">如何从文档页面中提取图像</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-images-from-document-page-area/">如何从文档页面区域提取图像</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-images-to-files/">如何将图像提取到文件</a>

    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="如何使用 Java 示例代码从文档中提取图像">}}

        ```java    
        // 使用 GroupDocs.Parser API 从文档中提取图像
        // 创建 Parser 类的实例
        try (Parser parser = new Parser(Constants.SampleImagesPdf)) {
            // 提取图像
            Iterable<PageImageArea> images = parser.getImages();
            // 检查是否支持图像提取
            if (images == null) {
                System.out.println("不支持图像提取");
                return;
            }
            // 迭代图像
            for (PageImageArea image : images) {
                // 打印页面索引、矩形和图像类型：
                System.out.println(String.format("Page: %d, R: %s, Type: %s", image.getPage().getIndex(), image.getRectangle(), image.getFileType()));
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
        Java 用于文件格式和图像的文档解析和图像提取 API。提取一些流行文件格式的数据，如下所述。

############################# Back to top ###############################
back_to_top:
    enable: true
---