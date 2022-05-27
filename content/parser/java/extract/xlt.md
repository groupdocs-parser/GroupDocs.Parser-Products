---
############################# Static ############################
layout: "auto-gen-gist"
draft: false
path: "parser/java/extract/xlt"
otherformats: DOC DOT DOCX DOCM DOTX DOTM TXT ODT OTT RTF PDF XHTML MHTML MD XML EPUB FB2 CHM XLS XLSX XLSM XLSB XLTX XLTM ODS CSV OTS XLA XLAM PPT PPTX  PPS POT PPSX PPTM POTX PPSM ODP OTP PST OST EML EMLX MSG ONE 

############################# Head ############################
head_title: "Hyperlinks Extraction from Documents, Pages or Page Area via Java API"
head_description: "GroupDocs.Parser Java API allows developers to extract hyperlinks from documents, doc’s page or specific page area of Excel, PowerPoint, PDF, Outlook & more."

############################# Header ############################
title: "Java API to Extract Hyperlinks from Documents, Pages or Particular page Area "
description: "GroupDocs.Parser Java API makes developers job easy by allowing them to extract hyperlinks from documents, document’s page or specific page Area of  PDF, DOCX, PPTX, EML, MSG, XLS, XLSX, CSV, RTF, EPUB and many more."

######################### Download Button #######################
button:
    enable: true

############################# About ############################
about:
    enable: true
    title: "How to Perform Hyperlinks Extraction from Various Documents via Java?"
    content: |
       This web page explains how to parse and extract hyperlinks from different types of document, document’s page or a particular area of a page using just a couple of lines of Java code.  Hyperlink can be very useful to navigate between pages or Web sites and can points to an entire document or to a particular part within a document, graphics, sounds, e-mail addresses and more.   GroupDocs.Parser for Java is a very powerful API that allows software developers to parse documents and extract text as well as metadata from various popular documents inside their own Java applications. It has included several advanced features for extracting text & hyperlinks from  various documents types such as PDF, Emails, Ebooks, Microsoft Office formats: Word (DOC, DOCX), PowerPoint (PPT, PPTX), Excel (XLS, XLSX), LibreOffice formats and many more.

############################# content ############################
steps:
    enable: true
    block:
    - title_left: "How to Extract Hyperlinks from XLT Documents"
      content_left: |
       GroupDocs.Parser Java has included functionality for extracting Hyperlinks from XLT documents. The following Java code example shows how hyperlinks can be extracted from XLT document. 

      title_right: "Extract Hyperlinks via Java"
      content_right: |
        * Create an instance of [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser) 
        * Check if the document supports hyperlink extraction
        * Extract hyperlinks from the document
        * Call [GetHyperlinks](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getHyperlinks()) method extract all hyperlinks from the whole document.
        * Iterate over hyperlinks and Print the hyperlink URL

      gisthash: "036de701f5f17a02dd2353ee547afd5b"
      gistfile: "extract_hyperlinks_form_documents.java"

    - title_left: "How to Extract Hyperlinks from XLT Documents Page"
      content_left: |
       GroupDocs.Parser .NET allows software developers to extract hyperlinks from XLT documents with a couple of lines of code. The below C# .NET code shows hyperlinks extraction inside a XLT document. 

      title_right: "Extract Hyperlinks via Java"
      content_right: |
        * Create an instance of [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser) 
        * Check if the document supports hyperlink extraction
        * Get document info by calling [getDocumentInfo](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getDocumentInfo()) method.
        * Iterate over pages and Print a page number
        * Extract hyperlinks from the document
        * Call [GetHyperlinks](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getHyperlinks()) method extract all hyperlinks from the whole document.
        * Iterate over hyperlinks and Print the hyperlink URL
     
      gisthash: "bcca6319f2287edb7295443c1def46ee"
      gistfile: "extract_hyperlinks_form_documents_page.java"
      
    - title_left: "Extract Hyperlinks from XLT Documents Page Area"
      content_left: |
       GroupDocs.Parser Java API has provided complete support to extract hyperlinks from XLT document's page ease. The following Java code shows how programmers can extract hyperlinks from a XLT document page area inside their own Java applications.

      title_right: "How to Extract Hyperlinks using Java?"
      content_right: |
        * Create an instance of [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser) 
        * Check document for hyperlink extraction support
        * Create the options which are used for hyperlink extraction
        * Call [GetHyperlinks](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getHyperlinks()) method extract all hyperlinks from the whole document.
        * Iterate over hyperlinks and Print the hyperlink URL
     
      gisthash: "4aefff1fcc6733c0fc12b736d7e36711"
      gistfile: "hyperlinks_extraction_from_document_page_area.java"

    - title_left: "System Requirements"
      content_left: |
        GroupDocs.Parser for Java is supported on all major platforms and operating systems. It can generate documents in Microsoft Word, Excel, PowerPoint, Outlook, OpenOffice & 50+ other formats. For complete system requirements guide, please visit system requirements before executing the code below, please make sure that you have the following prerequisites installed on your system:
        * Operating Systems: Microsoft Windows, Linux, MacOS
        * Java Versions Support: J2SE 7.0 (1.7), J2SE 8.0 (1.8) or above
        * Get the latest version of GroupDocs.Assembly Java APIs from GroupDocs [Repository](https://repository.groupdocs.com/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs-parser)
        
      title_right: "Why Use GroupDocs.Assembly"
      content_right: |
        * Extract a plain text from any of the supported documents.
        * Table of contents extraction support
        * Extract formatted text, metadata, images, containers, and attachments.
        * Documents parsing via user-defined templates.
        * Search Text using keyword or regular expression. 
        * Structured text extraction support
        * Extract table of contents for some supported document formats.
        * Parse form data from PDF documents.

demos:
    enable: true
        

about_formats:
    enable: true


more_formats:
    enable: true


back_to_top:
    enable: true
---