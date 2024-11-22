---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:05
draft: false
otherformats: vdx vsdm vsdx vssm vssx vstm vstx vsx vtx xlam xls xlsb xlsm xlsx xlt xltm
ext: pptx

############################# Head ############################
head_title: ".NET API to Parse & Extract Hyperlinks from Documents, Pages or Page Area"
head_description: "GroupDocs.Parser .NET API enables software programmers to extract hyperlinks from documents, pages or page Area of PDF, DOCX, XLSX, CSV, PPTX, EML, MSG, EPUB & many more."

############################# Header ############################
title: "Extract Hyperlinks from Documents, Pages or Specific page Area via C#/VB.NET API"
description: "GroupDocs.Parser .NET API allows software developers to  parse & extract hyperlinks from documents, pages or page Area of PDF, DOC, DOCX, PPT, PPTX, EML, MSG, XLS, XLSX, CSV, ODT, RTF, EPUB and many other documents."
bg_image: "https://cms.admin.containerize.com/templates/aspose/App_Themes/V3/images/bg/header1.png"
bg_overlay: false
button:
    enable: true
    icon: "fas fa-arrow-down"
    label: "Download Free Trial"
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
              text: "API Reference"

            # button loop
            - link: "https://github.com/groupdocs-parser"
              text: "Code Examples"

            # button loop
            - link: "https://products.groupdocs.app/parser/family"
              text: "Live Demos"

            # button loop
            - link: "https://purchase.groupdocs.com/pricing/parser/net"
              text: "Pricing"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/net"
        link_buy: "https://purchase.groupdocs.com"

############################# About ############################
about:
    enable: true
    title: "How to Parse & Extract Hyperlinks from PPTX documents via .NET API?"
    content: |
        A hyperlink is a piece of text or an image or icon that points to an entire document or to a particular part within a document. The use of hyperlinks allows users to navigate to a web page or document. It is often required to extract hyperlinks from a document and use it to access external document or webpage. GroupDocs.Parser for .NET is a fascinating document text extraction API that provides complete functionality for implementing text and metadata extraction solutions. It supports text & hyperlinks extraction from PDF, Emails, Ebooks, Microsoft Office formats: Word (DOC, DOCX), PowerPoint (PPT, PPTX), Excel (XLS, XLSX), LibreOffice formats and many more. It supports several advanced features for documents parsing, extracting plain and structured text, text searching by keywords, extract metadata or images, containers as well as attachments and many more.
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: "Extract hyperlinks from PPTX in .NET"
    content_left: |
        [GroupDocs.Parser for .NET](/parser/net/) makes it easy for C# developers to extract hyperlinks from a PPTX file by implementing a few easy steps.
        
        * Instantiate [Parser](https://reference.groupdocs.com/net/parser/groupdocs.parser/parser) object for the initial document;
        * Check if the document supports hyperlink extraction;
        * Call [GetHyperlinks](https://reference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/gethyperlinks) method and obtain collection of [PageHyperlinkArea](https://reference.groupdocs.com/parser/net/groupdocs.parser.data/pagehyperlinkarea) objects;
        * Iterate through the collection and get a hyperlink text and URL.

    title_right: "Learn more about the hyperlinks extraction"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/net/extract-hyperlinks-from-document/">How to extract hyperlinks from document</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-hyperlinks-from-document-page/">How to extract hyperlinks from document page</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-hyperlinks-from-document-page-area/">How to extract hyperlinks from document page area</a>
    
    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="How to extract hyperlinks from PPTX file using C# example code">}}

        ```csharp    
        // Extract hyperlinks from PPTX file using GroupDocs.Parser API
        // Create an instance of Parser class
        using (Parser parser = new Parser(filePath)) {
            // Check if the document supports hyperlink extraction
            if (!parser.Features.Hyperlinks) {
                Console.WriteLine("Document isn't supports hyperlink extraction.");
                return;
            }
            // Extract hyperlinks from the document
            IEnumerable<PageHyperlinkArea> hyperlinks = parser.GetHyperlinks();
            // Iterate over hyperlinks
            foreach (PageHyperlinkArea h in hyperlinks) {
                // Print the hyperlink text
                Console.WriteLine(h.Text);
                // Print the hyperlink URL
                Console.WriteLine(h.Url);
                Console.WriteLine();
            }
        }
        ```
     {{< /parser/code-parser >}}

############################# More ############################
more:
    enable: true
    title_left: "System Requirements"
    content_left: |
        GroupDocs.Parser for .NET APIs are supported on all major platforms and operating systems. Before executing the code below, please make sure that you have the following prerequisites installed on your system.
        
        * Operating Systems: Microsoft Windows, Linux, MacOS
        * Development Environments: Microsoft Visual Studio, Xamarin, MonoDevelop
        * Frameworks
        * Download the latest version of GroupDocs.Parser for .NET from [Nuget](https://www.nuget.org/packages/groupdocs.parser)

    title_right: "Why Use GroupDocs.Parser for .NET"
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
        .NET documents parse & hyperlinks extraction API for file formats and images. Extract data for some of the popular file formats as stated below.

############################# Back to top ###############################
back_to_top:
    enable: true
---