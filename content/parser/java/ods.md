---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:05
draft: false
otherformats: odt one otp ott pdf pps ppsx ppt pptx rtf tex vdx vsdm vsdx vssm vssx
ext: ods

############################# Head ############################
head_title: "Extract Hyperlinks from documents in Java"
head_description: "GroupDocs.Parser for Java API allows developers to extract hyperlinks from documents, doc’s page or specific page area of Excel, PowerPoint, PDF, Outlook & more."

############################# Header ############################
title: "Java API to Extract Hyperlinks from Documents, Pages or Particular page Area"
description: "GroupDocs.Parser for Java API makes developers job easy by allowing them to extract hyperlinks from documents, document’s page or specific page Area of  PDF, DOCX, PPTX, EML, MSG, XLS, XLSX, CSV, RTF, EPUB and many more."
bg_image: "https://cms.admin.containerize.com/templates/aspose/App_Themes/V3/images/bg/header1.png"
bg_overlay: false
button:
    enable: true
    icon: "fas fa-arrow-down"
    label: "Download Free Trial"
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
              text: "API Reference"

            # button loop
            - link: "https://github.com/groupdocs-parser"
              text: "Code Examples"

            # button loop
            - link: "https://products.groupdocs.app/parser/family"
              text: "Live Demos"

            # button loop
            - link: "https://purchase.groupdocs.com/pricing/parser/java"
              text: "Pricing"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/java"
        link_buy: "https://purchase.groupdocs.com"

############################# About ############################
about:
    enable: true
    title: "How to Parse & Extract Hyperlinks from ODS documents via Java API?"
    content: |
        A hyperlink is a piece of text or an image or icon that points to an entire document or to a particular part within a document. The use of hyperlinks allows users to navigate to a web page or document. It is often required to extract hyperlinks from a document and use it to access external document or webpage. GroupDocs.Parser for Java is a fascinating document text extraction API that provides complete functionality for implementing text and metadata extraction solutions. It supports text & hyperlinks extraction from PDF, Emails, Ebooks, Microsoft Office formats: Word (DOC, DOCX), PowerPoint (PPT, PPTX), Excel (XLS, XLSX), LibreOffice formats and many more. It supports several advanced features for documents parsing, extracting plain and structured text, text searching by keywords, extract metadata or images, containers as well as attachments and many more.
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: "Extract hyperlinks from ODS in Java"
    content_left: |
        [GroupDocs.Parser for Java](/parser/java/) makes it easy for Java developers to extract hyperlinks from a ODS file by implementing a few easy steps.
        
        * Instantiate [Parser](https://reference.groupdocs.com/java/parser/com.groupdocs.parser/Parser) object for the initial document;
        * Check if the document supports hyperlink extraction;
        * Call [getHyperlinks](https://reference.groupdocs.com/parser/java/com.groupdocs.parser/parser/#getHyperlinks--) method and obtain collection of [PageHyperlinkArea](https://reference.groupdocs.com/parser/java/com.groupdocs.parser.data/PageHyperlinkArea) objects;
        * Iterate through the collection and get a hyperlink text and URL.

    title_right: "Learn more about the hyperlinks extraction"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/java/extract-hyperlinks-from-document/">How to extract hyperlinks from document</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-hyperlinks-from-document-page/">How to extract hyperlinks from document page</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-hyperlinks-from-document-page-area/">How to extract hyperlinks from document page area</a>
    
    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="How to extract hyperlinks from ODS file using Java example code">}}

        ```java    
        // Extract hyperlinks from ODS file using GroupDocs.Parser API
        // Create an instance of Parser class
        try (Parser parser = new Parser(Constants.HyperlinksPdf)) {
            // Check if the document supports hyperlink extraction
            if (!parser.getFeatures().isHyperlinks()) {
                System.out.println("Document isn't supports hyperlink extraction.");
                return;
            }
            // Extract hyperlinks from the document
            Iterable<PageHyperlinkArea> hyperlinks = parser.getHyperlinks();
            // Iterate over hyperlinks
            for (PageHyperlinkArea h : hyperlinks) {
                // Print the hyperlink text
                System.out.println(h.getText());
                // Print the hyperlink URL
                System.out.println(h.getUrl());
                System.out.println();
            }
        }
        ```
     {{< /parser/code-parser >}}

############################# More ############################
more:
    enable: true
    title_left: "System Requirements"
    content_left: |
        GroupDocs.Parser for Java APIs are supported on all major platforms and operating systems. Before executing the code below, please make sure that you have the following prerequisites installed on your system.
        
        * Operating Systems: Microsoft Windows, Linux, MacOS
        * Development Environments: NetBeans, Intellij IDEA, Eclipse, etc.
        * Frameworks
        * Download the latest version of GroupDocs.Parser for Java from [Maven](https://repository.groupdocs.com/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs-parser)

    title_right: "Why Use GroupDocs.Parser for Java"
    content_right: |
        * Plain text extraction support from any supported documents    
        * Documents parsing via user-defined templates    
        * Fully support structured text extraction    
        * Text searching via keyword as well as regular expression    
        * Extract formatted text, metadata, images, containers, and attachments    
        * Extract table of contents for some supported document formats    
        * Parse form data from PDF documents    
        * Extract hyperlinks from the document   
        
############################# About Formats ############################
about_formats:
    enable: true

############################# More Formats ############################
more_formats:
    enable: true
    title: "Extract Hyperlinks From Other Document Formats"
    content: |
        Java documents parse & hyperlinks extraction API for file formats and images. Extract data for some of the popular file formats as stated below.

############################# Back to top ###############################
back_to_top:
    enable: true
---