---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:09
draft: false
otherformats: doc docm docx dot dotm dotx epub html mht mhtml odp ods odt one otp ott pdf

############################# Head ############################
head_title: "Extract Images from Excel, Word, PDF & Other Document or Page via .NET "
head_description: "GroupDocs.Parser .NET API enables software programmers to extract images from different documents such as MS  Excel, Word, PowerPoint, PDF & more inside their .NET Apps."

############################# Header ############################
title: "Extract Images from PDF, DOCX, PPTX, MSG, XLSX Documents & Pages via C#.NET API"
description: "GroupDocs.Parser .NET API allows programmers to extract images from PDF, DOC, DOCX, PPT, PPTX, EML, MSG, XLS, XLSX, CSV, ODT, RTF & EPUB documents or document's Pages."
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
    title: "How to Extract Images from documents via .NET?"
    content: |
        Images can be used to deliver information in such a way that may not be expressible by words. Images help us in grabbing user’s attention and explain tough concepts with ease. Sometimes while reading documents, journals or benefiting from presentations we often found some fascinating images and wanted to download it. GroupDocs.Parser for .NET is a powerful API that help users to develop useful applications for extracting images from different types of documents and save them in PNG, JPEG, WebP, GIF, BMP and other formats. The API has included supports for text as well images extraction from some of the most commonly used file formats, such as PDF, Emails, Ebooks, Microsoft Office formats: Word (DOC, DOCX), PowerPoint (PPT, PPTX), Excel (XLS, XLSX), LibreOffice formats and many more. The API also fully supports documents parsing, extracting plain and structured text, text searching by keywords, extract metadata or images, containers as well as attachments and many more.
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: "Extract images from documents in .NET"
    content_left: |
        [GroupDocs.Parser for .NET](/parser/net/) makes it easy for C# developers to extract images from a documents by implementing a few easy steps.
        
        * Instantiate [Parser](https://reference.groupdocs.com/net/parser/groupdocs.parser/parser) object for the initial document;
        * Call [GetImages](https://reference.groupdocs.com/net/parser/groupdocs.parser/parser/methods/getimages) method and obtain collection of image objects;
        * Check if reader isn’t *null* (images extraction is supported for the document);
        * Iterate through the collection and get sizes, image types and image contents.

    title_right: "Learn more about the images extraction"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/net/extract-images-from-document/">How to extract images from document</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-images-from-document-page/">How to extract images from document page</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-images-from-document-page-area/">How to extract images from document page area</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-images-to-files/">How to extract images to files</a>

    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="How to extract images from documents using C# example code">}}

        ```csharp    
        // Extract images from documents using GroupDocs.Parser API
        // Create an instance of Parser class
        using (Parser parser = new Parser(filePath)) {
            // Extract images
            IEnumerable<PageImageArea> images = parser.GetImages();
            // Check if images extraction is supported
            if (images == null) {
                Console.WriteLine("Images extraction isn't supported");
                return;
            }
            // Iterate over images
            foreach (PageImageArea image in images) {
                // Print a page index, rectangle and image type:
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Type: {2}", image.Page.Index, image.Rectangle, image.FileType));
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
    title: "Live Demos - Extract images from documents Online"
    content: |
       Extract images from documents right now by visiting [GroupDocs.Parser Live Demos](https://products.groupdocs.app/parser/images/) website.
       The live demo has the following benefits.
        
############################# About Formats ############################
about_formats:
    enable: true

############################# More Formats ############################
more_formats:
    enable: true
    title: "Extract Images From Other Document Formats"
    content: |
        .NET documents parse & images extraction API for file formats and images. Extract data for some of the popular file formats as stated below.

############################# Back to top ###############################
back_to_top:
    enable: true
---