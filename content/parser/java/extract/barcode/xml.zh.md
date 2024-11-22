---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:05
draft: false
otherformats: 

############################# Head ############################
head_title: "通过 Java API 从 Excel、Word、PDF 和其他文档中提取条形码"
head_description: "GroupDocs.Parser for Java 使软件开发人员能够从 Java 应用内的 PDF、MS Excel、Word、PowerPoint、Outlook、OneNote 及更多文档中提取条形码。"

############################# Header ############################
title: "如何通过 {ProductName}} API 从 PDF、DOCX、PPTX、EML、MSG、XLSX 和 EPUB 中提取条形码"
description: "GroupDocs.Parser for Java API 使软件开发者能够从 PDF、Word (DOC、DOCX)、Excel (XLS、XLSX)、PowerPoint( PPT、{ 330})、Outlook (EML、MSG) 和许多其他文档页面区域。"
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
    title: "如何从XML文件Java API中提取条形码？"
    content: |
        条形码图像由一系列平行的黑线和不同宽度的空白组成，可用于将信息编码为视觉图案。它于 20 世纪 70 年代引入，现已成为商业企业的普遍组成部分。 GroupDocs.Parser for Java 是一个功能强大的 API，允许软件程序员构建用于解析不同类型文档并从中提取文本、图像和条形码的应用程序。它支持一些最常见的文档类型，例如 PDF、电子邮件、电子书、Microsoft Office 格式：Word (DOC、DOCX)、PowerPoint (PPT、{330 })、Excel (XLS、XLSX)、电子邮件 (EML、MSG) 格式等等。 Java API 支持与文档解析和数据提取相关的多项重要功能，例如纯文本提取、结构化文本提取、提取 Markdown 格式文本、从特定页面或页面区域提取文本、从文档中提取条形码、提取元数据或图像等等。
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: "从Java中的XML中提取条形码"
    content_left: |
        [GroupDocs.Parser for Java](/zh/parser/java/) 让 Java 开发者只需执行几个简单的步骤即可轻松从 XML 文件中提取条形码。
        
        * 实例化初始文档的 [Parser](https://reference.groupdocs.com/net/parser/groupdocs.parser/parser) 对象；
        * 检查文件是否支持条码提取；
        * 调用 [getBarcodes](https://reference.groupdocs.com/parser/java/com.groupdocs.parser/parser/#getBarcodes--) 方法并获取  的集合 [PageBarcodeArea](https://reference.groupdocs.com/parser/java/com.groupdocs.parser.data/pagebarcodearea/) 对象；
        * 迭代集合并获取条形码值。

    title_right: "了解有关条形码提取的更多信息"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/java/extract-barcodes-from-document/">如何从文档中提取条形码</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-barcodes-from-document-page/">如何从文档页面中提取条形码</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-barcodes-from-document-page-area/">如何从文档页面区域提取条形码</a>
    
    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="如何使用 Java 示例代码从 XML 文件中提取条形码">}}

        ```java    
        // 使用 GroupDocs.Parser API 从 XML 文件中提取条形码
        // 创建 Parser 类的实例
        try (Parser parser = new Parser(Constants.SamplePdfWithBarcodes)) {
            // // 检查文件是否支持条形码提取
            if (!parser.getFeatures().isBarcodes()) {
                System.out.println("该文件不支持条形码提取。");
                return;
            }

            // {steps.code.scan}
            Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();

            // 迭代条形码
            for (PageBarcodeArea barcode : barcodes) {
                // 打印页面索引
                System.out.println("Page: " + barcode.getPage().getIndex());
                // 打印条形码值
                System.out.println("Value: " + barcode.getValue());
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
    title: "现场演示 - 从 XML 在线提取条形码"
    content: |
       立即访问 [GroupDocs.Parser 现场演示](https://products.groupdocs.app/parser/barcodes/xml) 网站，从 XML 文件中提取条形码。
       现场演示有以下好处。
        
############################# About Formats ############################
about_formats:
    enable: true

############################# More Formats ############################
more_formats:
    enable: true
    title: "从其他文档格式中提取条形码"
    content: |
        Java 针对文件格式和图像的文档解析和条形码提取 API。提取一些流行文件格式的数据，如下所述。

############################# Back to top ###############################
back_to_top:
    enable: true
---