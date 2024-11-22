---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:07
draft: false
otherformats: pdf pps ppsx ppt pptx rtf tex vdx vsdm vsdx vssm vssx vstm vstx vsx vtx
ext: otp

############################# Head ############################
head_title: "从 Java 中的文档中提取超链接"
head_description: "GroupDocs.Parser for Java API 允许开发者从文档、文档页面或 Excel、PowerPoint、PDF、Outlook 等特定页面区域中提取超链接。"

############################# Header ############################
title: "Java 用于从文档、页面或特定页面区域提取超链接的 API"
description: "GroupDocs.Parser for Java API 允许开发者从文档、文档页面或 PDF、DOCX、PPTX、EML、MSG、XLS、{322 的特定页面区域中提取超链接，从而简化开发人员的工作}、CSV、RTF、EPUB 等等。"
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
    title: "如何通过 Java API 解析和提取 OTP 文档中的超链接？"
    content: |
        超链接是指向整个文档或文档中特定部分的一段文本、图像或图标。使用超链接允许用户导航到网页或文档。通常需要从文档中提取超链接并使用它来访问外部文档或网页。 GroupDocs.Parser for Java 是一个令人着迷的文档文本提取 API，它提供了用于实施文本和元数据提取解决方案的完整功能。它支持从 PDF、电子邮件、电子书、Microsoft Office 格式中提取文本和超链接：Word (DOC、DOCX)、PowerPoint (PPT、PPTX)、Excel ( XLS、XLSX）、LibreOffice 格式等等。它支持多种高级功能，用于文档解析、提取纯文本和结构化文本、按关键字搜索文本、提取元数据或图像、容器以及附件等等。
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: "从 Java 中的 OTP 中提取超链接"
    content_left: |
        [GroupDocs.Parser for Java](/zh/parser/java/) 让 Java 开发者只需执行几个简单的步骤即可轻松从 OTP 文件中提取超链接。
        
        * 实例化初始文档的 [Parser](https://reference.groupdocs.com/java/parser/com.groupdocs.parser/Parser) 对象；
        * 检查文档是否支持超链接提取；
        * 调用 [getHyperlinks](https://reference.groupdocs.com/parser/java/com.groupdocs.parser/parser/#getHyperlinks--) 方法并获取 [PageHyperlinkArea](https://reference.groupdocs.com/parser/java/com.groupdocs.parser.data/PageHyperlinkArea) 对象；
        * 遍历集合并获取超链接文本和 URL。

    title_right: "了解有关超链接提取的更多信息"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/java/extract-hyperlinks-from-document/">如何从文档中提取超链接</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-hyperlinks-from-document-page/">如何从文档页面中提取超链接</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-hyperlinks-from-document-page-area/">如何从文档页面区域中提取超链接</a>
    
    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="如何使用 Java 示例代码从 OTP 文件中提取超链接">}}

        ```java    
        // 使用 GroupDocs.Parser API 从 OTP 文件中提取超链接
        // 创建 Parser 类的实例
        try (Parser parser = new Parser(Constants.HyperlinksPdf)) {
            // 检查文档是否支持超链接提取
            if (!parser.getFeatures().isHyperlinks()) {
                System.out.println("文档不支持超链接提取。");
                return;
            }
            // 从文档中提取超链接
            Iterable<PageHyperlinkArea> hyperlinks = parser.getHyperlinks();
            // 迭代超链接
            for (PageHyperlinkArea h : hyperlinks) {
                // 打印超链接文本
                System.out.println(h.getText());
                // 打印超链接 URL
                System.out.println(h.getUrl());
                System.out.println();
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
        
############################# About Formats ############################
about_formats:
    enable: true

############################# More Formats ############################
more_formats:
    enable: true
    title: "从其他文档格式中提取超链接"
    content: |
        Java 针对文件格式和图像的文档解析和超链接提取 API。提取一些流行文件格式的数据，如下所述。

############################# Back to top ###############################
back_to_top:
    enable: true
---