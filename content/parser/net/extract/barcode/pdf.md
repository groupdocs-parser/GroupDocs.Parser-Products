---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:03
draft: false
otherformats: ppsx ppt pptx rtf tex vdx vsdm vsdx vssm vssx vstm vstx vsx vtx xlam xls

############################# Head ############################
head_title: ".NET API to Extract Barcodes from PDF, DOCX, PPTX, XLSX, EPUB & More"
head_description: "GroupDocs.Parser .NET API allow software developers to extract barcodes from PDF, DOC, DOCX, PPT, PPTX, EML, MSG, XLS, XLSX, CSV, ODT, RTF & EPUB documents inside .NET Apps."

############################# Header ############################
title: "Extract Barcodes from Excel, Word, PDF & PowerPoint Documents via C#.NET API"
description: "GroupDocs.Parser .NET API allows programmers to extract barcodes from PDF, DOC, DOCX, PPT, PPTX, EML, MSG, XLS, XLSX, CSV, ODT, RTF & EPUB documents or page area."
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
    title: "How to Extract Barcodes from PDF files .NET API?"
    content: |
        Barcodes are machine-readable representation of numerals and characters that are commonly used across the World in many contexts, such as product scanning and identification, automobile parts tracking, inventory management and so on. GroupDocs.Parser for .NET is a powerful API that help developers to develop solution for extracting text, images and barcodes from different types of supported documents formats, such as such as PDF, Emails, Ebooks, Microsoft Office formats: Word (DOC, DOCX), PowerPoint (PPT, PPTX), Excel (XLS, XLSX), Emails (EML, MSG) formats and many more. The .NET API has included support for several advanced documents parsing features such as searching text by keywords, accurate text extraction, HTML or Markdown formatted text extraction, text areas extraction with coordinates, extract metadata or barcodes and so on.
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: "Extract barcodes from PDF in .NET"
    content_left: |
        [GroupDocs.Parser for .NET](/parser/net/) makes it easy for C# developers to extract barcodes from a PDF file by implementing a few easy steps.
        
        * Instantiate [Parser](https://reference.groupdocs.com/net/parser/groupdocs.parser/parser) object for the initial document;
        * Check if the file supports barcode extracting;
        * Call [GetBarcodes](https://reference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/getbarcodes) method and obtain collection of [PageBarcodeArea](https://reference.groupdocs.com/parser/net/groupdocs.parser.data/pagebarcodearea) objects;
        * Iterate through the collection and get a barcode value.

    title_right: "Learn more about the barcode extraction"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/net/extract-barcodes-from-document/">How to extract barcodes from document</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-barcodes-from-document-page/">How to extract barcodes from document page</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-barcodes-from-document-page-area/">How to extract barcodes from document page area</a>
    
    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="How to extract barcodes from PDF file using C# example code">}}

        ```csharp    
        // Extract barcodes from PDF file using GroupDocs.Parser API
        // Create an instance of Parser class
        using (Parser parser = new Parser(Constants.SamplePdfWithBarcodes)) {
            // Check if the file supports barcode extracting
            if (!parser.Features.Barcodes) {
                Console.WriteLine("The file doesn't support barcode extracting.");
                return;
            }

            // {steps.code.scan}
            IEnumerable<PageBarcodeArea> barcodes = parser.GetBarcodes();

            // Iterate over barcodes
            foreach (PageBarcodeArea barcode in barcodes) {
                // Print the page index
                Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                // Print the barcode value
                Console.WriteLine("Value: " + barcode.Value);
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

############################# Demos ############################
demos:
    enable: true
    title: "Live Demos - Extract barcodes from documents Online"
    content: |
       Extract barcodes from documents right now by visiting [GroupDocs.Parser Live Demos](https://products.groupdocs.app/parser/barcodes/) website.
       The live demo has the following benefits.
        
############################# About Formats ############################
about_formats:
    enable: true

############################# More Formats ############################
more_formats:
    enable: true
    title: "Extract Barcodes From Other Document Formats"
    content: |
        .NET documents parse & barcode extracting API for file formats and images. Extract data for some of the popular file formats as stated below.

############################# Back to top ###############################
back_to_top:
    enable: true
---