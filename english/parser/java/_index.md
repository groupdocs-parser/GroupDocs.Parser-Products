---
############################# Static ############################
layout: "product"
date: 2021-04-27T09:31:06+03:00
draft: false

product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Java API to Parse Text, Images & Metadata from PDF Word Excel HTML"
head_description: "Java document parser API to extract text, images, metadata & encoding from databases, Word, Excel, presentations, PDF, email, EPUB and ZIP files."

############################# Header ############################
title: "Java Parser API to Extract Data"
description: "‎Java API to parse & extract images and text with metadata from documents, presentations, archives & emails.‎"
button:
    enable: true

############################# SubMenu ############################
submenu:
    enable: true
    
    left:
        img_alt: "GroupDocs.Parser for Java"
        image: "https://www.groupdocs.cloud/templates/groupdocs/images/product-logos/groupdocs-parser-java.png"
        product: "GroupDocs.Parser"
        platform: "Java"

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
            - link: "https://purchase.groupdocs.com/pricing/parser/java"
              text: "Pricing"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/java/"
        link_buy: "https://purchase.groupdocs.com"

############################# Overview ############################
overview:
    enable: true
    content: |
      GroupDocs.Parser for Java is a text, image and metadata extractor API, supporting more than 50 popular document types to help building business applications with features of parsing raw, structured & formatted text. It also supports parsing documents using predefined templates and allows extracting complex data from invoices and other typical documents with speed and accuracy. GroupDocs.Parser for Java enables you to extract text and metadata from password protected files of all popular formats including Word processing documents, Excel spreadsheets, PowerPoint presentations, OneNote, PDF files and ZIP archives.
    tabs:
      enable: true     
      
      ## TAB ONE ##
      tab_one:
        description: |
          Following is an overview of GroupDocs.Parser for Java:

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
          GroupDocs.Parser for Java supports following [document file formats](https://docs.groupdocs.com/parser/java/supported-document-formats/):

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
          GroupDocs.Parser for Java supports following Operating Systems, Frameworks & Package ‎Managers:‎
        
        left:
          enable: true
          table:
            # table loop
            - icon: "fab fa-windows"
              title: "Operating Systems"
              content: |
                * Microsoft Windows Desktop
                * Microsoft Windows Server
                * Linux
                * MacOS

            # table loop
            - icon: "fas fa-code"
              title: "Supported Frameworks"
              content: |
                * Java 7 (1.7) and above

        right:
          enable: true
          table:
            # table loop
            - icon: "fas fa-cogs"
              title: "Development Environments"
              content: |
                * NetBeans
                * IntelliJ IDEA
                * Eclipse
            # table loop
            - icon: "fas fa-tools"
              title: "Build Automation Tool"
              content: |
                * Maven

############################# Features ############################
features:
    enable: true
    title: "GroupDocs.Parser for Java Features"

    feature:
      # feature loop
      - icon: "fas fa-copy"
        content: "Count Word Occurrence for Single or Multiple Documents Statistically"

      # feature loop
      - icon: "fas fa-eye"
        content: "Extract Text and Metadata from Excel Spreadsheets and PowerPoint Presentation Templates"

      # feature loop
      - icon: "fas fa-bolt"
        content: "Fetch Text from a File or Stream, Without Installing Document Reader"
      
      # feature loop
      - icon: "fas fa-file-powerpoint"
        content: "Pull Out Formatted Text from a Document Using Fast or Standard Text Extraction Mode"

      # feature loop
      - icon: "fas fa-code"
        content: "Detect the Media Type of Password Protected XML Documents & Extract Text from Them"

      # feature loop
      - icon: "fas fa-cloud"
        content: "Fetch Formatted Text from PowerPoint Presentation, Emails & Attachments Programmatically"

      # feature loop
      - icon: "fas fa-remove-format"
        content: "Drive out Text from Single or Multiple Pages of OneNote Document"

      # feature loop
      - icon: "fas fa-comment-slash"
        content: "Pull out Raw Text from Simple PDF File or a PDF Portfolio Document‎"

      # feature loop
      - icon: "fas fa-location-arrow"
        content: "Extract Data from PDF, MS Word, Excel and Presentation Documents"

      # feature loop
      - icon: "fas fa-border-all"
        content: "Extract Raw or Formatted Text from Cells, Rows And Columns from Excel Spreadsheet"

      # feature loop
      - icon: "fas fa-wrench"
        content: "Gather Raw or HTML Formatted Text from Word Document & Excerpt Highlighted Text from Documents"

      # feature loop
      - icon: "fas fa-columns"
        content: "Get Data from the PDF Forms & Obtain Formatted Table From a PDF or Word Document"

      # feature loop
      - icon: "fas fa-file-word"
        content: "Pull Out Single Sentence or Whole Text from EPUB, CHM, Markdown & FB2 Files"

      # feature loop
      - icon: "fas fa-envelope"
        content: "Excerpt Table of Contents from Databases, PDF, EPUB, CHM & Word Processing Documents"

      # feature loop
      - icon: "fas fa-print"
        content: "Retrieve Text Area from Documents for Analysis & Pull Out text with its Content Structure Intact"

      # feature loop
      - icon: "fas fa-file-archive"
        content: "Obtain Metadata from Supported Document Formats"

      # feature loop
      - icon: "fas fa-lock"
        content: "Draw Out All or Selected Images from Supported Formats & Rotate Extracted Image(s)‎"

      # feature loop
      - icon: "fas fa-file-code"
        content: "Extract Text from Files within Zip Archives & OST Containers – Detect Media Types for Zip Container Items"
      
      # feature loop
      - icon: "fas fa-fill-drip"
        content: "Fetch Data from Email Container (Exchange Web Server, POP3, IMAP)‎"

      # feature loop
      - icon: "fas fa-file-excel"
        content: "Take Out Text from Database Containers in Fast, Reliable and Efficient Manner"

      # feature loop
      - icon: "fas fa-heading"
        content: "Find Simple Text, Whole Word & Regular Expression within Documents"

      # feature loop
      - icon: "fas fa-project-diagram"
        content: "Prepare Document Template, Extract Data from Document and Analyze Data Fields & Tables"

      # feature loop
      - icon: "fas fa-cube"
        content: "Search & Extract Highlighted Expressions in Documents"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Pull out Text with Plain Text Formatter (Simple & ASCII) or Custom Formatting with Edges, Angles, & Intersections"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Fetch & Format Text (Font, Hyperlinks, Headings, Lists & Tables) with Markdown Formatter"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Get Text with HTML Formatter & Apply Formatter to Paragraph, Hyperlink, Font, Headings, Lists & Tables"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Move Table Layout & Detect Tables in a Rectangular Area by Column Separators"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Extract Text from Shapes, WordArt Objects & Text Boxes within Microsoft Office File Formats"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Extract Images to Files – Save to JPG, PNG, GIF, BMP, PNG or WEBP Formats"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Extract Text from Email Servers and Databases via JDBC"

    more_feature:
      # more_feature_loop
      - title: "Get Text with Plain Text or HTML Formatters"
        content: |
          With GroupDocs.Parser for Java, you can apply various formatters to the Text and HTML. You can pull text with Plain Text Formatter for both Simple and ASCII. You can also get Text with HTML Formatter and apply formatting to paragraph, hyperlink, font, headings, lists and tables.‎

############################# Support ############################
support:
    enable: true

############################# Solutions ############################
solutions:
    enable: true
    title: "GroupDocs.Parser offers document viewing APIs for other popular development environments"

    solution:
        # solution loop
        - img_alt: "GroupDocs.Parser for .NET"
          image: "https://www.groupdocs.cloud/templates/groupdocs/images/product-logos/groupdocs-parser-net.png"
          product: "GroupDocs.Parser"
          platform: ".NET"
          link: "/parser/net"

############################# Back to top ###############################
back_to_top:
  enable: true
---