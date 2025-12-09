---
############################# Static ############################
layout: "landing"
date: 2025-12-09T21:34:38
draft: false

lang: en
product: "Parser"
product_tag: "parser"
platform: "Python"
platform_tag: "python-net"

############################# Drop-down ############################
supported_platforms:
  items:
    # supported_platforms loop
    - title: ".NET"
      tag: "net"
    # supported_platforms loop
    - title: "Java"
      tag: "java"
    # supported_platforms loop
    - title: "Python"
      tag: "python-net"

############################# Head ############################
head_title: "GroupDocs.Parser for Python via .NET Document Parser SDK for Python"
head_description: "High‑performance Document Parser SDK for Python. Extract text, images, metadata, barcodes, tables and other data from PDF, Word, Excel, emails and 50+ document formats."

############################# Header ############################
title: "Document Parser SDK for Python"
description: "Add fast, accurate document parsing to your Python apps and extract text, images, metadata and structured data from documents and images."
words:
  for: "for"

actions:
  hidden: true # Hide version 0 is released
  main: "PyPI Download"
  main_link: "https://pypi.org/project/groupdocs-parser-net/"
  alt: "Licensing"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/python-net/"
  title: "Ready to get started?"
  description: "Try GroupDocs.Parser features for free or request a license"

release:
  enable: false
  title: "Version {0} released"
  notes: "See what’s new"
  downloads: "Downloads"

code:
  title: "Extract text using Python"
  more: "More examples"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Python-via-.NET/"
  install: "pip install groupdocs-parser-net"
  content: |
    ```python {style=abap}  
    from groupdocs.parser import Parser

    # Load the document
    with Parser("sample.pdf") as parser:
        # Extract text from the document
        text = parser.GetText()

        # Print all extracted text
        print(text)
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser at a glance"
  description: "Document Parser SDK for performing high‑accuracy document parsing in Python applications"
  features:
    # feature loop
    - title: "Extract data from documents"
      content: "GroupDocs.Parser for Python via .NET API enables you to retrieve text, metadata, and images from a wide range of file formats such as Office documents, emails, attachments, and archives. This powerful tool helps you efficiently access and process valuable information contained within these files for various applications like data analysis, search engine indexing, or content management systems."

    # feature loop
    - title: "Parse documents"
      content: "Extract various elements such as hyperlinks, tables, QR codes, barcodes and data from PDF forms. Also parse any desired information from documents using custom templates."

    # feature loop
    - title: "Customizing results"
      content: "Python API enables you to retrieve data in various formats such as raw, structured, HTML, or Markdown. Additionally, the API offers a search functionality for locating specific words or phrases within the text of documents."

############################# Platforms ############################
platforms:
  enable: true
  title: "Platform Independence"
  description: "GroupDocs.Parser for Python via .NET supports the following operating systems, frameworks and package managers"
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
    GroupDocs.Parser for Python via .NET supports operations with the following [file formats](https://docs.groupdocs.com/parser/python-net/supported-document-formats/).
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
  title: "GroupDocs.Parser for Python via .NET features"
  description: "Extract data from PDFs, Office documents, images and other formats swiftly and accurately with our Python Document Parser SDK"

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
      content: "Locate and extract hyperlinks and email addresses within office documents or PDF files for efficient access."

    # feature loop
    - icon: "pdf"
      title: "Parse PDF Forms"
      content: "PDF Forms are digital documents featuring fillable fields for user interaction, allowing them to input information electronically. Python API can be utilized to extract data from these forms for efficient processing."

    # feature loop
    - icon: "template"
      title: "Parse data by templates"
      content: "Create custom templates and utilize them with Python API to parse specific information from PDF files, simplifying data extraction processes."

    # feature loop
    - icon: "search"
      title: "Search a text in documents"
      content: "Quickly locate specific words or patterns within documents."


############################# Code samples ############################
code_samples:
  enable: true
  title: "Code samples"
  description: "Beyond basic text extraction, here are the most common use cases for quick text, image and metadata extraction."
  items:
    # code sample loop
    - title: "Search Text in a Document"
      content: |
        This example shows how to search for a specific phrase in a PDF document and print where it was found.
        {{< landing/code title="Search Text in a Document in Python">}}
        ```python {style=abap}
        from groupdocs.parser import Parser

        # Load the document
        with Parser("sample.pdf") as parser:
            # Print the page index and rectangle where the phrase was found
            for area in parser.Search("Total Amount"):
                # Print the page index and rectangle where the phrase was found
                print(f"Page {area.PageIndex}, Rectangle: {area.Rectangle}")
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Extract Images from a Document"
      content: |
        This example shows how to extract images from a PDF document and save them to a file.
        {{< landing/code title="Extract Images from a Document in Python">}}
        ```python {style=abap}    
        from groupdocs.parser import Parser

        # Load the document
        with Parser("sample.docx") as parser:
            # Extract images from the document
            images = parser.GetImages()

            # Save the images to a file
            index = 1
            for image in images:
                image.Save(f"image_{index}.png")
                index += 1
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Extract Metadata from a Document"
      content: |
        This example shows how to extract metadata from a PDF document and print it.
        {{< landing/code title="Extract Metadata from a Document in Python">}}
        ```python {style=abap}    
        from groupdocs.parser import Parser

        # Load the document
        with Parser("sample.pdf") as parser:
            # Extract metadata from the document
            metadata = parser.GetMetadata()

            # Print the metadata
            for item in metadata:
                print(f"{item.Name}: {item.Value}")
        ```
        {{< /landing/code >}}
---
