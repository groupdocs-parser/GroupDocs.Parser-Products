---
############################# Static ############################
layout: "landing"
date: 2023-12-28T16:34:08
draft: false
#operation: 
#parsertype: 
#fileformat: 
#productName: Java
lang: en
#productCode: java
#otherformats: 
#breadcrumb: Put  parser on  for Java
product: "Parser"
product_tag: "parser"
platform: "Net"
platform_tag: "net"

############################# Head ############################
head_title: ".NET, Java, Cloud APIs & Online Document Parser Apps"
head_description: "Get all-in-one document parsing solution for .NET, Java and cloud-based applications. Extract data from document formats online using simple drag and drop feature"

############################# Header ############################
title: "Parse documents<br>via .NET API"
description: "Extract data from documents and images on any platform using our flexible APIs and app based solutions for programmers and end-users."
words:
  for: "for"

actions:
  main: "Free NuGet Download"
  main_link: "https://www.nuget.org/packages/GroupDocs.Parser"
  alt: "Licensing"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/net"
  title: "Ready to get started?"
  description: "Try GroupDocs.Parser features for free or request a license"

release:
  title: "Version {0} released"
  notes: "See what’s new"
  downloads: "Downloads"

code:
  title: "Extract text from PDF files in C#"
  more: "More examples"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET"
  install: "dotnet add package GroupDocs.Parser"
  content: |
    ```csharp {style=abap}   
    // Create an instance of Parser class
    using (Parser parser = new Parser(filePath)) {
        // Extract a text into the reader
        using (TextReader reader = parser.GetText()) {
            // Print a text from the document
            // If text extraction isn't supported, a reader is null
            if (reader == null) {
              Console.WriteLine("Text extraction isn't supported");
            } else {
              Console.WriteLine(reader.ReadToEnd());
            }
        }
    }
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser Overview"
  description: "API for performing document parsing in .NET applications"
  features:
    # feature loop
    - title: "Extract data from documents"
      content: ".NET API enables you to retrieve text, metadata, and images from a wide range of file formats such as Office documents, emails, attachments, and archives. This powerful tool helps you efficiently access and process valuable information contained within these files for various applications like data analysis, search engine indexing, or content management systems."

    # feature loop
    - title: "Parse documents"
      content: "Extract various elements such as hyperlinks, tables, QR codes, barcodes and data from PDF forms. Also parse any desired information from documents using custom templates."

    # feature loop
    - title: "Customizing results"
      content: ".NET API enables you to retrieve data in various formats such as raw, structured, HTML, or Markdown. Additionally, API offers a search functionality for locating specific words or phrases within the text of documents."

############################# Platforms ############################
platforms:
  enable: true
  title: "Platform independence"
  description: "GroupDocs.Parser for .NET supports the following operating systems, frameworks and package managers"
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
    - title: "VS Code"
      image: "vs_code"
    # platform loop
    - title: "ReSharper"
      image: "resharper"
    # platform loop
    - title: "macOS"
      image: "finder"
    # platform loop
    - title: "Linux"
      image: "linux"
    # platform loop
    - title: "NuGet"
      image: "nuget"

############################# File formats ############################
formats:
  enable: true
  title: "Supported file formats"
  description: |
    GroupDocs.Parser for .NET supports operations with the following [file formats](https://docs.groupdocs.com/parser/net/supported-document-formats/).
  groups:
    # group loop
    - color: "green"
      content: |
        ### Microsoft Office formats
        * **Word:**  DOCX, DOC, DOCM, DOT, DOTX, DOTM, RTF
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
        * **Ebooks:** CHM, EPUB, FB2, MOBI

############################# Features ############################
features:
  enable: true
  title: "GroupDocs.Parser features"
  description: "Extract data from PDFs, Office Documents, and Images swiftly and accurately."

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
  title: "Code sample"
  description: "Some use cases of typical GroupDocs.Parser for .NET operations"
  items:
    # code sample loop
    - title: "Extract images from PDF documents"
      content: |
        .NET API makes it easy for C# developers to extract images from documents by implementing a few easy steps.
        {{< landing/code title="Extract images from PDF documents in C#">}}
        ```csharp {style=abap}
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
        {{< /landing/code >}}
    # code sample loop
    - title: "Extract barcodes from images"
      content: |
        .NET API makes it easy for C# developers to extract barcodes from documents by implementing a few easy steps.
        {{< landing/code title="Extract barcodes from images">}}
        ```csharp {style=abap}   
        // Create an instance of Parser class
        using (Parser parser = new Parser(Constants.SamplePdfWithBarcodes)) {
            // Check if the file supports barcode extracting
            if (!parser.Features.Barcodes) {
                Console.WriteLine("The file doesn't support barcode extracting.");
                return;
            }

            // {index-content.net.code-samples.sample2.code.scan}
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
        {{< /landing/code >}}

---
