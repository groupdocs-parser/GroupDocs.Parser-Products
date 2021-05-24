---
############################# Static ############################
layout: "product"
date: 2021-04-27T09:31:06+03:00
draft: false

product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: ".NET Parsing API, extract Text Images Metadata from PDF Word Excel"
head_description: "C# .NET document parsing API to extract text, images, metadata & encoding from databases, PDF, Word, Excel, presentations, web, email, EPUB & zip file formats."

############################# Header ############################
title: ".NET API to Extract Document Data"
description: "‎Extract images, raw or formatted text and metadata from documents, spreadsheets, presentations, emails & archives from within .NET apps.‎"
button:
    enable: true

############################# SubMenu ############################
submenu:
    enable: true
    
    left:
        img_alt: "GroupDocs.Parser for .NET"
        image: "https://www.groupdocs.cloud/templates/groupdocs/images/product-logos/groupdocs-parser-net.png"
        product: "GroupDocs.Parser"
        platform: ".NET"

    middle:
        button:
            # button loop
            - link: "#overview"
              text: "Overview"

            # button loop
            - link: "#features"
              text: "Features"

            # button loop
            - link: "#support"
              text: "Support"

            # button loop
            - link: "https://products.groupdocs.app/parser"
              text: "Live Demo"

            # button loop
            - link: "https://purchase.groupdocs.com/pricing/parser/net"
              text: "Pricing"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/net/"
        link_buy: "https://purchase.groupdocs.com"

############################# Overview ############################
overview:
    enable: true
    content: |
      GroupDocs.Parser for .NET is a text, metadata and image extractor API for business applications developed using C#, ASP.NET, and other .NET technologies. It supports extraction of raw, formatted & structured text as well as metadata from the files of supported formats. Through GroupDocs.Parser for .NET, your applications can also perform parsing of password protected documents for popular formats, such as Word processing documents, Excel spreadsheets, PowerPoint presentations, OneNote, PDF files and ZIP archives.
    tabs:
      enable: true
      
      ## TAB ONE ##
      tab_one:
        description: |
          Following is an overview of GroupDocs.Parser for .NET:
      
        left:
          enable: true
          icon: "fas fa-tools"
          title: "Features"
          content: |
            * Extract Images
            * Extract Raw Text
            * Extract Formatted Text
            * Extract Structured Text
            * Extract Metadata
            * Extract from Files within ZIP file
            * Extract by Searching
            * Extract with Text Formatters
            * Detect Encoding Standard
            * Detect Media Type
        
        right:
          enable: true
          icon: "fab fa-html5"
          title: "The API"
          content: |
            * Gets Input File
            * Fetches Raw or Formatted Text
            * Fetches Metadata
      
      ## TAB TWO ##
      tab_two:
        description: |
          GroupDocs.Parser for .NET supports following [document file formats](https://docs.groupdocs.com/parser/net/supported-document-formats/):

        left:
          enable: true
          table:
            # table loop
            - title: "Text Extraction"
              content: |
                * **Text**: DOC, DOCX, DOT, DOTM, DOTX, DOCM, RTF, ODT, OTT, TXT, MD, WordprocessingML (XML)
                * **Spreadsheets**: XLS, XLSX, CSV, XLSM, XLSB, ODS, SpreadsheetML (XML), XLT, XLTX, XLTM, OTS, XLA,, XLAM, TSV
                * **Presentations**: PPT, PPTX, PPTM, PPS, PPSX, PPSM, POT, POTX, POTM, ODP, OTP
                * **OneNote**: ONE
                * **Email**: MSG, EML, EMLX, PST, OST, MS EXCHANGE SERVER, POP, IMAP
                * **Electronic Publishing**: EPUB, FB2
                * **Portable Document**: PDF, PDF Portfolio, Encrypted PDF
                * **DOM-Based**: XML, HTML, XHTML, MHTML
                * **Compression & Packaging**: ZIP, CHM
                * **Database**: ADO.NET

            # table loop
            - title: "Encoding Detection"
              content: |
                * **BOM**: UTF32 LE, UTF32 BE, UTF16 LE, UTF16 BE, UTF8, and UTF7
                * **Content**: UTF32 LE, UTF32 BE, UTF16 LE, UTF16 BE, UTF8, and ANSI

        right:
          enable: true
          table:
            # table loop
            - title: "Metadata Extraction"
              content: |
                * **Text**: DOC, DOCX, DOT, DOTX, DOTM, OTT, ODT
                * **Spreadsheets**: XLS, XLSX, XLT, XLTX, XLTM, XLA, XLAM, OTS, ODS
                * **Presentations**: PPT, PPTX, POT, POTX, POTM, PPSM, PPTM, OTP, ODP
                * **Email**: MSG, EML, EMLX
                * **Electronic Publishing**: EPUB, FB2
                * **Other**: PDF

            # table loop
            - title: "Text & Metadata Extraction"
              content: |
                * **Template**: DOTX, POTX
                * **Macro-Enabled Template**: DOTM, POTM, PPSM, PPTM
                * **OpenDocument Template**: OTT

            # table loop
            - title: "Image Extraction"
              content: |
                * **Text**: DOC, DOCX, DOCM, RTF, DOT, DOTM, DOTX, ODT
                * **Spreadsheets**: XLS, XLSX, XLSM, XLSB, ODS, XLT, XLTM, XLTX
                * **Presentations**: PPT, PPTX, PPTM, ODP, POT, POTM, POTX, PPS, PPSX, PPSM
                * **Portable Document**: PDF, POT, POTM, POTX
                * **Ebook**: CHM, EPUB, FB2
                * **Markup**: HTML

      ## TAB THREE ##
      tab_three:
        description: |
          GroupDocs.Parser for .NET supports following Operating Systems, Frameworks & Package Managers:‎
        
        left:
          enable: true
          table:
            # table loop
            - icon: "fab fa-windows"
              title: "Operating Systems"
              content: |
                * Windows Desktop
                * Windows Server
                * Windows Azure
                * Linux

            # table loop
            - icon: "fas fa-code"
              title: "Supported Frameworks"
              content: |
                * .NET Framework 2.0 or higher
                * Mono Framework 1.2 or higher
                * .NET Standard 2.0
                * .NET Core 2.0

        right:
          enable: true
          table:
            # table loop
            - icon: "fas fa-box"
              title: "Package Manager"
              content: |
                * NuGet

            # table loop
            - icon: "fas fa-tools"
              title: "Development Environments"
              content: |
                * Microsoft Visual Studio
                * Xamarin.Android
                * Xamarin.IOS
                * Xamarin.Mac
                * MonoDevelop

############################# Features ############################
features:
    enable: true
    title: "GroupDocs.Parser for .NET Features"

    feature:
      # feature loop
      - icon: "fas fa-copy"
        content: "Statistically Count Word Occurrence in Single or Multiple Files"

      # feature loop
      - icon: "fas fa-eye"
        content: "Extract Text and Metadata from Excel Worksheets and Presentation Templates"

      # feature loop
      - icon: "fas fa-bolt"
        content: "Extract Text Content from a File or Stream without Installing Document Reader"
      
      # feature loop
      - icon: "fas fa-file-powerpoint"
        content: "Get Formatted Text from a Document using Fast or Standard Text Extraction Mode"

      # feature loop
      - icon: "fas fa-code"
        content: "Detect the Media Type of Password Protected XML Documents & Pull Text from them"

      # feature loop
      - icon: "fas fa-cloud"
        content: "Programmatically Get Formatted Text from Within Emails & Attachments"

      # feature loop
      - icon: "fas fa-remove-format"
        content: "Draw Out Text from Single or Multiple Pages of OneNote Document"

      # feature loop
      - icon: "fas fa-comment-slash"
        content: "Extract Data from PDF, MS Word, Excel and Presentation Documents‎"

      # feature loop
      - icon: "fas fa-location-arrow"
        content: "Extract Data from the PDF Forms & Take Out Text from Simple PDF File or a PDF Portfolio Document"

      # feature loop
      - icon: "fas fa-border-all"
        content: "Get Formatted Text from PowerPoint Presentation or Drive out Text from Specific Slide"

      # feature loop
      - icon: "fas fa-wrench"
        content: "Gather Raw or Formatted Text from Cells, Rows, and Columns from Excel Spreadsheet"

      # feature loop
      - icon: "fas fa-columns"
        content: "Extract Raw or HTML Formatted Text from Word Document"

      # feature loop
      - icon: "fas fa-file-word"
        content: "HTML Formatter Supports Formatting of Paragraph, Hyperlink, Font, Headings, Lists & Tables"

      # feature loop
      - icon: "fas fa-envelope"
        content: "Pull Out Single Sentence or Whole Text from EPUB, CHM, Markdown & FB2 Files"

      # feature loop
      - icon: "fas fa-print"
        content: "Excerpt Table of Contents from Databases, PDF, EPUB, CHM & Word Processing Documents"

      # feature loop
      - icon: "fas fa-file-archive"
        content: "Pull Out Text with its Content Structure Intact & Excerpt Highlighted Text from Documents"

      # feature loop
      - icon: "fas fa-lock"
        content: "Obtain Text Area from Documents for Analysis & Draw out Metadata from Supported Document Formats"

      # feature loop
      - icon: "fas fa-file-code"
        content: "Obtain All or Selected Images from Supported Formats & Rotate Extracted Image(s)"
      
      # feature loop
      - icon: "fas fa-fill-drip"
        content: "Take Out Text from Files within Zip Archives & OST Containers & Detect file types of ZIP Container Items"

      # feature loop
      - icon: "fas fa-file-excel"
        content: "Get Data from Email Container (Exchange Web Server, POP3, IMAP)"

      # feature loop
      - icon: "fas fa-heading"
        content: "Search Simple Text, Whole Word & Regular Expression within Documents"

      # feature loop
      - icon: "fas fa-project-diagram"
        content: "Prepare Document Template, Extract Data from Document and Analyze Data Fields & Tables"

      # feature loop
      - icon: "fas fa-cube"
        content: "Search and Extract Highlighted Expressions in Documents"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Get Text with Plain Text Formatter (Simple & ASCII) or with Markdown Formatter"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Markdown Formatter Supports Formatting of Font, Hyperlinks, Headings, Lists & Tables"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Perform Custom Formatting with Edges, Angles, and Intersections to Format Plain Text"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Move Table Layout & Detect Tables in a Rectangular Area by Column Separators"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Extract Text from Shapes, WordArt Objects & Text Boxes within Microsoft Office File Formats"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Extract Images to Files – Save to JPG, PNG, GIF, BMP, PNG or WEBP Formats"

    more_feature:
      # more_feature_loop
      - title: "Extracting Text from a Document"
        content: |
          Using GroupDocs.Parser for .NET API to extract text from a document is simple and achieved with just a few lines of code:

          ```cs
          // Create an instance of Parser class
          using(Parser parser = new Parser("sample.docx"))
          {
            // Extract text into the reader
            using(TextReader reader = parser.GetText())
            {
              // Print text from the document
              // If text extraction isn't supported, reader is null
              Console.WriteLine(reader == null ? "Text extraction isn't supported." : reader.ReadToEnd());
            }
          }
          ```

############################# Support ############################
support:
    enable: true

############################# Solutions ############################
solutions:
    enable: true
    title: "GroupDocs.Parser offers document viewing APIs for other popular development environments"

    solution:
        # solution loop
        - img_alt: "GroupDocs.Parser for Java"
          image: "https://www.groupdocs.cloud/templates/groupdocs/images/product-logos/groupdocs-parser-java.png"
          product: "GroupDocs.Parser"
          platform: "Java"
          link: "/parser/java"

############################# Back to top ###############################
back_to_top:
  enable: true
---