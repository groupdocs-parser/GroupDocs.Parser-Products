---
############################# Static ############################
layout: "landing"
date: 2025-06-30T10:26:00
draft: false

lang: en
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Drop-down ############################
supported_platforms:
  items:
    # supported_platforms loop
    - title: ".NET"
      tag: "net"
    # supported_platforms loop
    - title: "Java"
      tag: "java"

############################# Head ############################
head_title: "GroupDocs.Parser for Java Document Parsing Apps"
head_description: "Get all-in-one document parsing solution for Java applications. Extract data from document formats online using simple drag and drop feature"

############################# Header ############################
title: "Parse documents via Java API"
description: "Extract data from documents and images on any platform using our flexible APIs and app based solutions for programmers and end-users."
words:
  for: "for"

actions:
  main: "Maven Download"
  main_link: "https://releases.groupdocs.com/java/repo/com/groupdocs/groupdocs-parser/"
  alt: "Licensing"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/java/"
  title: "Ready to get started?"
  description: "Try GroupDocs.Parser features for free or request a license"

release:
  title: "Version {0} released"
  notes: "See what’s new"
  downloads: "Downloads"

code:
  title: "Quickly Get Document Content"
  more: "More examples"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java/"
  install: |
    <dependency>
      <groupId>com.groupdocs</groupId>
      <artifactId>groupdocs-parser</artifactId>
      <version>{0}</version>
    </dependency>
  content: |
    ```java {style=abap}  
    // Pass source file to Parser instance
    try (Parser parser = new Parser("source.pdf"))
    {
        // Pass document text to TextReader
        try (TextReader reader = parser.getText())
        {
            // Process document text
            System.out.println(reader == null 
                ? "" 
                : reader.readToEnd());
        }
    }
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser at a glance"
  description: "API for performing document parsing in Java applications"
  features:
    # feature loop
    - title: "Extract data from documents"
      content: "GroupDocs.Parser for Java API enables you to retrieve text, metadata, and images from a wide range of file formats such as Office documents, emails, attachments, and archives. This powerful tool helps you efficiently access and process valuable information contained within these files for various applications like data analysis, search engine indexing, or content management systems."

    # feature loop
    - title: "Parse documents"
      content: "Extract various elements such as hyperlinks, tables, QR codes, barcodes and data from PDF forms. Also parse any desired information from documents using custom templates."

    # feature loop
    - title: "Customizing results"
      content: "Java API enables you to retrieve data in various formats such as raw, structured, HTML, or Markdown. Additionally, API offers a search functionality for locating specific words or phrases within the text of documents."

############################# Platforms ############################
platforms:
  enable: true
  title: "Platform Independence"
  description: "GroupDocs.Parser for Java supports the following operating systems, frameworks and package managers"
  items:
    # platform loop
    - title: "Amazon"
      image: "amazon"
    # platform loop
    - title: "Docker"
      image: "docker"
    # platform loop
    - title: "Azure"
      image: "azure"
    # platform loop
    - title: "Eclipse"
      image: "eclipse"
    # platform loop
    - title: "IntelliJ"
      image: "intellij"
    # platform loop
    - title: "Windows"
      image: "windows"
    # platform loop
    - title: "Linux"
      image: "linux"
    # platform loop
    - title: "Maven"
      image: "maven"

############################# File formats ############################
formats:
  enable: true
  title: "Supported file formats"
  description: |
    GroupDocs.Parser for Java supports operations with the following [file formats](https://docs.groupdocs.com/parser/java/supported-document-formats/).
  groups:
    # group loop
    - color: "green"
      content: |
        ### Microsoft Office formats
        * **Word:** DOCX, DOC, DOCM, DOT, DOTX, DOTM, RTF
        * **Excel:** XLSX, XLS, XLSM, XLSB, XLTM, XLT, XLTM, XLTX, XLAM, SXC, SpreadsheetML
        * **PowerPoint:** PPT, PPTX, PPS, PPSX, PPSM, POT, POTM, POTX, PPTM
    # group loop
    - color: "blue"
      content: |
        ### Images & Other Formats
        * **Portable:** PDF 
        * **Images:** JPG, BMP, PNG, TIFF, GIF
        * **Other office formats:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### Other formats
        * **Web:** HTML, MHTML 
        * **Archives:** ZIP, TAR, 7Z 
        * **e-Books:** CHM, EPUB, FB2, MOBI 
        
        

############################# Features ############################
features:
  enable: true
  title: "GroupDocs.Parser for Java features"
  description: "Extract data from PDFs, Office Documents, and Images swiftly and accurately"

  items:
    # feature loop
    - icon: "text"
      title: "Extract text"
      content: "Extract textual information from various file formats such as office documents, PDF files and images for easy readability and analysis."

    # feature loop
    - icon: "image"
      title: "Extract images"
      content: "Retrieve visual content from diverse sources like office documents, PDF files for convenient access and use."

    # feature loop
    - icon: "qr"
      title: "Scan QR Codes"
      content: "Detect and decode QR codes present within office documents, PDF files, or visual content for efficient information retrieval."

    # feature loop
    - icon: "email"
      title: "Extract data from email attachments and archives"
      content: "Gather valuable information from email messages, file attachments, and compressed data sources for effective analysis and utilization."

    # feature loop
    - icon: "table"
      title: "Extract tables"
      content: "Identify and extract tabular data from PDF documents for organized analysis and use."

    # feature loop
    - icon: "hyperlink"
      title: "Extract hyperlinks"
      content: "Locate and extract hyperlinks and email addresses within office documents or PDF files for efficient access ."

    # feature loop
    - icon: "pdf"
      title: "Parse PDF Forms"
      content: "PDF Forms are digital documents featuring fillable fields for user interaction, allowing them to input information electronically. .NET API can be utilized to extract data from these forms for efficient processing."

    # feature loop
    - icon: "template"
      title: "Parse data by templates"
      content: "Create custom templates and utilize them with .NET API to parse specific information from PDF files, simplifying data extraction processes."

    # feature loop
    - icon: "search"
      title: "Search a text in documents"
      content: "Quickly locate specific words or patterns within documents."


############################# Code samples ############################
code_samples:
  enable: true
  title: "Code samples"
  description: "Some use cases of typical GroupDocs.Parser for Java operations"
  items:
    # code sample loop
    - title: "Extract images from PDF documents"
      content: |
        GroupDocs.Parser for Java makes it easy for Java developers to extract images from [documents](https://docs.groupdocs.com/parser/java/extract-images-from-documents/):
        {{< landing/code title="Extract images from PDF documents in Java">}}
        ```java {style=abap}
        // Create an instance of Parser class
        try (Parser parser = new Parser("source.pdf"))
        {
            // Extract images
            Iterable<PageImageArea> images = parser.getImages();

            // Check if something is extracted
            if (images == null) {
                return;
            }

            // Iterate over images
            for (PageImageArea image : images) {
                // Print a page index, rectangle and image type
                System.out.println(String.format("Page: %d, R: %s, Type: %s", 
                    image.getPage().getIndex(), image.getRectangle(), image.getFileType()));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Extract barcodes from images"
      content: |
        Use our Java API to extract [barcodes](https://docs.groupdocs.com/parser/java/extract-barcodes-from-document/) from images:
        {{< landing/code title="Extract barcodes from images in Java">}}
        ```java {style=abap}   
        // Load source image to Parser
        try (Parser parser = new Parser("source.jpg")){

            // Check if the file supports barcode extracting
            if (!parser.getFeatures().isBarcodes()) {

                // Extract barcodes from the file
                Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();

                // Iterate over barcodes
                for (PageBarcodeArea barcode : barcodes) {
                    // Print the page index
                    System.out.println("Page: " + barcode.getPage().getIndex());
                    // Print the barcode value
                    System.out.println("Value: " + barcode.getValue());
                }
            }
        }
        ```
        {{< /landing/code >}}

---
