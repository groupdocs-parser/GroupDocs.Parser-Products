---
############################# Static ############################
layout: "auto-gen-gist"
draft: false
path: "parser/java/extract/image/pot"
otherformats: DOC DOT DOCX DOCM DOTX DOTM TXT ODT OTT RTF PDF XHTML MHTML MD XML EPUB FB2 CHM XLS XLT XLSX XLSM XLSB XLTX XLTM ODS CSV OTS XLA XLAM PPT PPTX  PPS PPSX PPTM POTX PPSM ODP OTP PST OST EML EMLX MSG ONE 

############################# Head ############################
head_title: "How to Extract Images from Excel, Word, PDF & Other Documents via Java?"
head_description: "GroupDocs.Parser Java API allows software developers to parse & extract images from PDF, DOC, DOCX, PPT, PPTX, XLS, XLSX documents & Emails inside Java Apps."

############################# Header ############################
title: "Java API to Parse & Extract Images from Excel, Word, PowerPoint, PDF & Other Document's Pages"
description: "GroupDocs.Parser Java API allows programmers to extract images from PDF, DOC, DOCX, PPT, PPTX, EML, MSG, XLS, XLSX, CSV, ODT, RTF & EPUB documents or document’s Pages inside Java applications."

######################### Download Button #######################
button:
    enable: true

############################# About ############################
about:
    enable: true
    title: "Learn How to Extract Images from Documents or a Specific Page via Java API?"
    content: |
       An Image is worth a thousand words and cannot be ignored in today’s visual world while creating engaging content.  Images can be a great source of information communication as well as grabbing user’s attention. It is often needed to get images from documents, journals or presentations and use them somewhere else. GroupDocs.Parser  for Java is a powerful API that helps software developers and programmers to build solution for parsing and extracting images  or other information from numerous  documents types.  It also support saving images in PNG, JPEG, WebP, GIF, BMP and other formats. The API has included support for some popular documents formats, such as PDF, Microsoft Office formats: Word (DOC, DOCX), PowerPoint (PPT, PPTX), Excel (XLS, XLSX), LibreOffice formats, Emails, Ebooks, and many more.  It has also included support for some advanced features related to documents parsing, extracting plain and structured text, text searching by keywords, extract metadata or images, containers as well as attachments and many more.

############################# content ############################
steps:
    enable: true
    block:
    - title_left: "How to Extract images from POT Documents"
      content_left: |
       GroupDocs.Parser Java has included functionality for extracting images from POT documents. The following Java code example shows how images can be extracted from POT document with ease. 

      title_right: "Get Images from Documents via Java"
      content_right: |
        * Create an instance of [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser) 
        * Check if the document supports images extraction
        * Call [getImages()](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getImages()) method extract all images from the whole document.
        * Extract all images from the document
        * Iterate over images and Print the image type

      gisthash: "b13e690d2593f92081abd99948363e06"
      gistfile: "extract_images_form_documents.java"

    - title_left: "Images Extraction from POT Documents Page"
      content_left: |
       GroupDocs.Parser Java API allows software developers to extract images from POT documents with a couple of lines of code. The below Java code shows images extraction from a POT document. 

      title_right: "How to Extract File Images via Java"
      content_right: |
        * Create an instance of [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser) 
        * Check if the document supports images extraction
        * Get document info by calling [getDocumentInfo](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getDocumentInfo()) method.
        * Check document for pages existance
        * Iterate over pages and Print a page number
        * Call [getImages()](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getImages()) method extract all images from the whole document.
        * Iterate over images and Print image type
     
      gisthash: "68450336a57c5d8df06b4ef1ea69b29f"
      gistfile: "extract_images_form_documents_page.java"
      
    - title_left: "How to Extract Images from POT Documents Page Area"
      content_left: |
       GroupDocs.Parser Java API has provided complete support for extracting from POT document's page ease. The following Java code demonstrates how programmers can extract images from a POT document page area inside their own Java apps.

      title_right: "Extract Images using Java?"
      content_right: |
        * Create an instance of [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser) 
        * Create the options which are used for images extraction
        * Check document for images extraction support
        * Call [getImages()](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getImages()) method to extract images from the upper-left corner of a page.
        * Iterate over images and Print the images URL
     
      gisthash: "40143a56569ae88e7e7c972ccca041b5"
      gistfile: "extract_images_form_documents_page_area.java"

    - title_left: "How to Extract Images to a File via Java API"
      content_left: |
       GroupDocs.Parser Java API allows extracting images from POT document's and save  image contents to a file. The following Java code demonstrates how programmers can extract images from to file of their choice inside their own Java apps.

      title_right: "Extract Images form a Document to a File"
      content_right: |
        * Create an instance of [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser) 
        * Check document for images extraction support
        * Call [getImages()](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getImages()) method to extract images from the upper-left corner of a page.
        * Create the options to save image in the supported file format 
        * Iterate over images and Print the images URL
     
      gisthash: "6faeafc93e4412265b7439209828950b"
      gistfile: "images_saving_to_files.java"

    - title_left: "System Requirements"
      content_left: |
        GroupDocs.Parser for Java is supported on all major platforms and operating systems. It can generate documents in Microsoft Word, Excel, PowerPoint, Outlook, OpenOffice & 50+ other formats. For complete system requirements guide, please visit system requirements before executing the code below, please make sure that you have the following prerequisites installed on your system:
        * Operating Systems: Microsoft Windows, Linux, MacOS
        * Java Versions Support: J2SE 7.0 (1.7), J2SE 8.0 (1.8) or above
        * Get the latest version of GroupDocs.Assembly Java APIs from GroupDocs [Repository](https://repository.groupdocs.com/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs-parser)
        
      title_right: "Why Use GroupDocs.Parser"
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