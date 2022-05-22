---
############################# Static ############################
layout: "auto-gen-gist"
draft: false
path: "parser/net/extract/one"
otherformats: DOC DOT DOCX DOCM DOTX DOTM TXT ODT OTT RTF PDF XHTML MHTML MD XML EPUB FB2 CHM XLS XLT XLSX XLSM XLSB XLTX XLTM ODS CSV OTS XLA XLAM PPT PPTX  PPS POT PPSX PPTM POTX PPSM ODP OTP PST OST EML EMLX MSG 

############################# Head ############################
head_title: ".NET API to Parse & Extract Hyperlinks from Documents, Pages or Page Area"
head_description: "GroupDocs.Parser .NET API enables software programmers to extract hyperlinks from documents, pages or page Area of PDF, DOCX, XLSX, CSV, PPTX, EML, MSG, EPUB & many more."

############################# Header ############################
title: "Extract Hyperlinks from Documents, Pages or Specific page Area via C#/VB.NET API"
description: "GroupDocs.Parser .NET API allows software developers to  parse & extract hyperlinks from documents, pages or page Area of PDF, DOC, DOCX, PPT, PPTX, EML, MSG, XLS, XLSX, CSV, ODT, RTF, EPUB and many other documents."

######################### Download Button #######################
button:
    enable: true

############################# About ############################
about:
    enable: true
    title: "How to Parse & Extract Hyperlinks from Documents or Pages  via .NET?"
    content: |
       A hyperlink is a piece of text or an image or icon that points to an entire document or to a particular part within a document.  The use of hyperlinks allows users to navigate to a web page or document. It is often required to extract hyperlinks from a document and use it to access external document or webpage.  GroupDocs.Parser .NET API is a fascinating document text extraction API that provides complete functionality for implementing text and metadata extraction solutions. It supports text & hyperlinks extraction from PDF, Emails, Ebooks, Microsoft Office formats: Word (DOC, DOCX), PowerPoint (PPT, PPTX), Excel (XLS, XLSX), LibreOffice formats and many more.  It supports several advanced features for documents parsing, extracting plain and structured text, text searching by  keywords, extract metadata or images, containers as well as attachments and many more. 

############################# content ############################
steps:
    enable: true
    block:
    - title_left: "Extract Hyperlinks from ONE Documents via .NET"
      content_left: |
       GroupDocs.Parser .NET provides complete support for extracting Hyperlinks from ONE documents. The following C# .NET code example demonstrates how to extract hyperlinks inside a ONE document. 

      title_right: "How to Extract Hyperlinks"
      content_right: |
        * Create an instance of [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser) 
        * Check document for hyperlink extraction support
        * Extract hyperlinks from the document
        * Call [GetHyperlinks](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/gethyperlinks) method extract all hyperlinks from the whole document.
        * Iterate over hyperlinks and Print the hyperlink URL

      gisthash: "35be3a09e0135c65be790c42c5c86d37"
      gistfile: "Extract_hyperlinks_form_documents.cs"

    - title_left: "Extract Hyperlinks from ONE Documents Page"
      content_left: |
       GroupDocs.Parser .NET allows software developers to extract hyperlinks from ONE documents with a couple of lines of code. The below C# .NET code shows hyperlinks extraction inside a ONE document. 

      title_right: "Extract Hyperlinks via .NET"
      content_right: |
        * Create an instance of [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser) 
        * Check document for hyperlink extraction support
        * Get document info by calling [GetDocumentInfo](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/getdocumentinfo) 
        * Iterate over pages and Print a page number
        * Extract hyperlinks from the document
        * Call [GetHyperlinks](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/gethyperlinks) method extract all hyperlinks from the whole document.
        * Iterate over hyperlinks and Print the hyperlink URL
     
      gisthash: "e71f8e39ba36ebf97034dfbf6fceeec1"
      gistfile: "hyperlinks_extraction_form_documents_page.cs"
      
    - title_left: "Extract Hyperlinks from ONE Documents Page Area"
      content_left: |
       GroupDocs.Parser .NET API fully supports extraction of hyperlinks from ONE documents with ease. The following .NET code example demonstrates how to extract hyperlinks from a ONE document page area.

      title_right: "How to Extract Hyperlinks using .NET"
      content_right: |
        * Create an instance of [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser) 
        * Check document for hyperlink extraction support
        * Create the options which are used for hyperlink extraction
        * Call [GetHyperlinks](https://apireference.groupdocs.com/parser/net/groupdocs.parser.parser/gethyperlinks/methods/1) method to extract hyperlinks from a document page are.
        * Iterate over hyperlinks and Print the hyperlink URL
     
      gisthash: "eefbede6f391ea44ddb6901edb353950"
      gistfile: "hyperlinks_extraction_from__documents_page_area.cs"

    - title_left: "System Requirements"
      content_left: |
        GroupDocs.Assembly .NET APIs are supported on all major platforms and operating systems. For complete system requirements guide, please visit [system requirements](hhttps://docs.groupdocs.com/parser/net/system-requirements/) Before executing the code below, please make sure that you have the following prerequisites installled on your system:
        * Operating Systems: Microsoft Windows, Linux, MacOS
        * Development Environment:  Visual Studio, Xamarin, MonoDevelop etc
        * Frameworks: .NET Framework, .NET Standard, .NET Core, Mono
        * Get the latest version of GroupDocs.Assembly .NET APIs from [NuGet](https://www.nuget.org/packages/GroupDocs.parser/)
        
      title_right: "Why Use GroupDocs.Assembly"
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