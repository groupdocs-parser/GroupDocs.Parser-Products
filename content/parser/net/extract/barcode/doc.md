---
############################# Static ############################
layout: "auto-gen-gist"
draft: false
path: "parser/net/extract/barcode/doc/"
otherformats: DOT DOCX DOCM DOTX DOTM TXT ODT OTT RTF PDF XHTML MHTML MD XML EPUB FB2 CHM XLS XLT XLSX XLSM XLSB XLTX XLTM ODS CSV OTS XLA XLAM PPT PPTX  PPS POT PPSX PPTM POTX PPSM ODP OTP PST OST EML EMLX MSG ONE 

############################# Head ############################
head_title: ".NET API to Extract Barcodes from PDF, DOCX, PPTX, XLSX, EPUB & More "
head_description: "GroupDocs.Parser .NET API allow software developers to extract barcodes from PDF, DOC, DOCX, PPT, PPTX, EML, MSG, XLS, XLSX, CSV, ODT, RTF & EPUB documents inside .NET Apps."

############################# Header ############################
title: "Extract Barcodes from Excel, Word, PDF & PowerPoint Documents via C#.NET API"
description: "GroupDocs.Parser .NET API allows programmers to extract barcodes from PDF, DOC, DOCX, PPT, PPTX, EML, MSG, XLS, XLSX, CSV, ODT, RTF & EPUB documents or page aea."

######################### Download Button #######################
button:
    enable: true

############################# About ############################
about:
    enable: true
    title: "How to Extract Barcodes from Excel, Word, PDF & Other Documents via .NET API?"
    content: |
       Barcodes are machine-readable representation of numerals and characters that are commonly used across the World in many contexts, such as product scanning and identification, automobile parts tracking, inventory management and so on.  GroupDocs.Parser for .NET is a powerful API that help developers to develop solution for extracting text, images and barcodes from different types of supported documents formats, such as such as PDF, Emails, Ebooks, Microsoft Office formats: Word (DOC, DOCX), PowerPoint (PPT, PPTX), Excel (XLS, XLSX), Emails (EML, MSG)  formats and many more. The API has included support for several advanced documents parsing features such as searching text by keywords, accurate text extraction, HTML or Markdown formatted text extraction, text areas extraction with coordinates, extract metadata or barcodes and so on.  

############################# content ############################
steps:
    enable: true
    block:
    - title_left: "How to Extract Barcodes from DOC Documents via C# .NET "
      content_left: |
       GroupDocs.Parser .NET API helps software developers to extract Barcodes from DOC documents with ease. The following C# .NET code example demonstrates how to extract barcodes from a DOC document. 

      title_right: "Barcodes Extraction from Documents"
      content_right: |
        * Create an instance of [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser) 
        * check if barcodes extraction is supported 
        * Call [getBarcodes](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/getBarcodes) method to extract all barcodes from the whole document.
        * Iterate over barcodes in the document
        * Print page index and barcode value

      gisthash: "f9329c432da312e75f5f1c3702c02c52"
      gistfile: "barcode_extraction_form_documents.cs"

    - title_left: "Barcodes Extraction from DOC Document's Page via .NET"
      content_left: |
       GroupDocs.Parser .NET enables software programmers to extract barcodes from DOC documents's page. The below C# .NET code shows how barcodes extraction can be achived  inside a DOC document. 

      title_right: "Extract Barcodes via C# .NET"
      content_right: |
        * Create an instance of [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser)  
        * Check document for barcodes extraction support
        * Call [getBarcodes](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/getBarcodes) method to extract all barcodes from the whole document.
        * Iterate over pages and Print a page number
        * Print page index and barcode value
     
      gisthash: "80779aaa36b7d11b69c29296cfa73bd1"
      gistfile: "barcodes_extraction_form_documents_page.cs"
      
    - title_left: "Get Barcodes from DOC Document's Page Area via .NET"
      content_left: |
       GroupDocs.Parser .NET is a powerful  API that provides complete support for barcodes extraction from DOC documents using a couple of lines of .NET code. The following .NET code example shows how to perform barcodes extraction from a DOC document page area.

      title_right: "Extract Barcodes from DOC Page Area "
      content_right: |
        * Create an instance of [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser)   
        * Check document for barcodes extraction support
        * create a customize Options that can be used for barcodes extraction
        * Extract barcodes from the upper-right corner of a page by calling [getBarcodes](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/getBarcodes) method using customize Options.
        * Print page index and barcode value
     
      gisthash: "932e868be1c52982f8c2ced2fc4c0640"
      gistfile: "barcodes_extraction_from_documents_page_area.cs"

    - title_left: "System Requirements"
      content_left: |
        GroupDocs.Parser for .NET is fully supported on all major platforms and operating systems. For complete system requirements guide, please visit [system requirements](hhttps://docs.groupdocs.com/parser/net/system-requirements/) Before executing the code below, please make sure that you have the following prerequisites installled on your system:
        * Operating Systems: Microsoft Windows, Linux, MacOS
        * Development Environment:  Visual Studio, Xamarin, MonoDevelop etc
        * Frameworks: .NET Framework, .NET Standard, .NET Core, Mono
        * Get the latest version of GroupDocs.Parser .NET APIs from [NuGet](https://www.nuget.org/packages/GroupDocs.parser/)
        
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