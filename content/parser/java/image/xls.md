---
############################# Static ############################
layout: "auto-gen-gist"
draft: false
path: "parser/net/extract/image"
otherformats: DOC DOT DOCX DOCM DOTX DOTM TXT ODT OTT RTF PDF XHTML MHTML MD XML EPUB FB2 CHM XLT XLSX XLSM XLSB XLTX XLTM ODS CSV OTS XLA XLAM PPT PPTX  PPS POT PPSX PPTM POTX PPSM ODP OTP PST OST EML EMLX MSG ONE 

############################# Head ############################
head_title: "Extract Images from Excel, Word, PDF & Other Document or Page via .NET "
head_description: "GroupDocs.Parser .NET API enables software programmers to extract images from different documents such as MS  Excel, Word, PowerPoint, PDF & more inside their .NET Apps."

############################# Header ############################
title: "Extract Images from PDF, DOCX, PPTX, MSG, XLSX Documents & Pages via C#.NET API"
description: "GroupDocs.Parser .NET API allows programmers to extract images from PDF, DOC, DOCX, PPT, PPTX, EML, MSG, XLS, XLSX, CSV, ODT, RTF & EPUB documents or document's Pages."

######################### Download Button #######################
button:
    enable: true

############################# About ############################
about:
    enable: true
    title: "How to Extract Images from Documents or Page Area  via .NET?"
    content: |
       Images can be used to deliver information in such a way that may not be expressible by words. Images help us in grabbing user’s attention and explain tough concepts with ease. Sometimes while reading documents, journals or benefiting from presentations we often found some fascinating images and wanted to download it.  GroupDocs.Parser  for .NET is a powerful API that help users to develop useful applications for extracting images from different types of documents and save them in PNG, JPEG, WebP, GIF, BMP and other formats. The API has included supports for text as well images extraction from some of the most commonly used file formats, such as PDF, Emails, Ebooks, Microsoft Office formats: Word (DOC, DOCX), PowerPoint (PPT, PPTX), Excel (XLS, XLSX), LibreOffice formats and many more.  The API also fully supports documents parsing, extracting plain and structured text, text searching by  keywords, extract metadata or images, containers as well as attachments and many more. 

############################# content ############################
steps:
    enable: true
    block:
    - title_left: "Extract Images from XLS Documents via C# "
      content_left: |
       GroupDocs.Parser .NET API enables software developers to extract images from XLS documents. The following C# .NET code example demonstrates how to extract images inside a XLS document. 

      title_right: "How to Extract Images via .NET"
      content_right: |
        * Create an instance of [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser) 
        * check if images extraction is supported 
        * Iterate over images in the document
        * Call [getImages](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/getimages) method extract all images from the whole document.
        * Print all images

      gisthash: "6bc9e8fea228c9e1b99425b338bb0f00"
      gistfile: "images_extraction_form_documents.cs"

    - title_left: "Images Extraction from XLS Document's Page via C#"
      content_left: |
       GroupDocs.Parser .NET allows software developers to extract images from XLS documents's page. The below C# .NET code shows how images extraction can be achived  inside a XLS document. 

      title_right: "Extract File Image via .NET"
      content_right: |
        * Create an instance of [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser)  
        * Check document for images extraction support
        * Get document info by calling [GetDocumentInfo](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/getdocumentinfo) 
        * Check document for pages existing
        * Iterate over pages and Print a page number
        * Call [getImages(Int32)](https://apireference.groupdocs.com/parser/net/groupdocs.parser.parser/getimages/methods/2) method extract all images from the whole document.
        * Iterate over images and Print the images
     
      gisthash: "2000d476c202a688677f57a2fbd7ceab"
      gistfile: "images_extraction_form_documents_page.cs"
      
    - title_left: "How to Extract Image from XLS Documents Page Area"
      content_left: |
       GroupDocs.Parser .NET API fully supports extraction of images from XLS documents using a couple of lines of .NET code. The following .NET code example shows how to perform images extraction from a XLS document page area.

      title_right: "Extract Images from a File Page Area via .NET"
      content_right: |
        * Create an instance of [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser)   
        * customize Options creation that can be used for images extraction
        * Check document for images extraction support
        * Extract images from the upper-left corner of a page by calling [getImages(options)](https://apireference.groupdocs.com/parser/net/groupdocs.parser.parser/getimages/methods/3) method using customize Options.
        * Iterate over images and Print the images
     
      gisthash: "ea6c6b8fa613384f1e7f637dabcb7bca"
      gistfile: "extract_images_form_documents_page_area.cs"

    - title_left: "How to Extract & Save Image to a File via C# .NET"
      content_left: |
       GroupDocs.Parser .NET API allows software developers to extract images from a document and save it into a file with a just couple of lines of .NET code. The following example demonstrates  how to perform images extraction from a XLS document and save the image contents to the file. 

      title_right: "Save Images to a File via .NET"
      content_right: |
        * Create an instance of [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser) class
        * Extract images from document
        * Call [getImages](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/getimages) method extract all images from the whole document.
        * Check document for images extraction support
        * Extract images from the upper-left corner of a page by calling [getImages(options)](https://apireference.groupdocs.com/parser/net/groupdocs.parser.parser/getimages/methods/3) method using customize Options.
        * option Creation for saving  images in PNG format
        * Iterate over images and Save the image to the PNG file
     
      gisthash: "bc242d5ff4050564fa275858ffa7d34f"
      gistfile: "images_saving_to_files.cs"

    - title_left: "System Requirements"
      content_left: |
        GroupDocs.Parser for .NET is fully supported on all major platforms and operating systems. For complete system requirements guide, please visit [system requirements](hhttps://docs.groupdocs.com/parser/net/system-requirements/) Before executing the code below, please make sure that you have the following prerequisites installled on your system:
        * Operating Systems: Microsoft Windows, Linux, MacOS
        * Development Environment:  Visual Studio, Xamarin, MonoDevelop etc
        * Frameworks: .NET Framework, .NET Standard, .NET Core, Mono
        * Get the latest version of GroupDocs.Assembly .NET APIs from [NuGet](https://www.nuget.org/packages/GroupDocs.parser/)
        
      title_right: "Why Use GroupDocs.Parser"
      content_right: |
        * Plain text extraction support  from any supported documents
        * Documents parsing via user-defined templates.
        * Fully support structured text extraction
        * Text searching via keyword as well as regular expression
        * Extract formatted text, metadata, images, containers, and attachments.
        * Extract table of contents for some supported document formats.
        * Parse form data from PDF documents.
        * Extract hyperlinks from the document

demos:
    enable: true
        

about_formats:
    enable: true


more_formats:
    enable: true


back_to_top:
    enable: true
---