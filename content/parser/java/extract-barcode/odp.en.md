


---
############################# Static ############################
layout: "format"
date:  2025-06-26T17:35:41
draft: false
lang: en
format: Odp
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Read barcodes from ODP files in Java apps"
head_description: "With GroupDocs.Parser, extract barcode data from ODP documents using Java without any external tools."

############################# Header ############################
title: "Read barcodes from ODP using Java" 
description: "Extract barcode content from PDF, Word, Excel, and image files using GroupDocs.Parser in your Java applications."
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Download Free Trial"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "Overview of GroupDocs.Parser for Java API"
    link: "/parser/java/"
    link_title: "Learn more"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) provides a comprehensive solution for document parsing in Java. It enables developers to extract barcodes, text, images, and structured information from multiple file formats like PDF, Word, Excel, PowerPoint, and others—without needing third-party libraries.

############################# Steps ############################
steps:
    enable: true
    title: "How to read barcodes from Odp in Java"
    content: |
      With [GroupDocs.Parser](/parser/java/), Java developers can extract barcodes from ODP documents in just a few steps:
      
      1. Load the ODP document using Parser.
      2. Verify the document supports barcode extraction.
      3. Use the API to retrieve barcode data.
      4. Loop through the barcode results and apply them as needed.
   
    code:
      platform: "net"
      copy_title: "Copy"
      install:
        command: |
          <dependencies>
            <dependency>
              <groupId>com.groupdocs</groupId>
              <artifactId>groupdocs-parser</artifactId>
              <version>{0}</version>
            </dependency>
          </dependencies>

          <repositories>
            <repository>
              <id>repository.groupdocs.com</id>
              <name>GroupDocs Repository</name>
              <url>https://repository.groupdocs.com/repo/</url>
            </repository>
          </repositories>
        copy_tip: "click to copy"
        copy_done: "copied"
      links:
        #  loop
        - title: "More examples"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java/"
        #  loop
        - title: "Documentation"
          link: "https://docs.groupdocs.com/parser/java/"
          
      content: |
        ```java {style=abap}
        // Open a document containing barcodes using Parser
        try (Parser parser = new Parser("input.odp"))
        {
            // Check barcode support for the file
            if (!parser.getFeatures().isBarcodes())
            {
                System.out.println("Handle unsupported file types");
                return;
            }

            // Extract and use barcode data
            Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();
            for(PageBarcodeArea barcode : barcodes)
            {
                System.out.println("Page: " + barcode.getPage().getIndex());
                System.out.println("Value: " + barcode.getValue());
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "More parsing capabilities"
  description: "GroupDocs.Parser goes beyond barcode extraction—it also lets you extract plain text, images, and structured elements to support data-driven workflows."
  image: "/img/parser/features_extract-barcode.webp" # 500x500 px
  image_description: "Barcode and data extraction features"
  features:
    # feature loop
    - title: "Wide barcode format support"
      content: "Detect standard barcode formats including QR Code, Code 39, Data Matrix, EAN, Aztec, and others."

    # feature loop
    - title: "Read barcodes from multiple sources"
      content: "Extract barcode information from Office documents, PDFs, and image files like PNG, JPG, and BMP."

    # feature loop
    - title: "Custom barcode reading setup"
      content: "Fine-tune barcode extraction with options for targeting specific regions and multi-page files."
      
  code_samples:
    # code sample loop
    - title: "Example: extract barcodes from PDF with options"
      content: |
        This sample demonstrates barcode extraction from a PDF document using custom settings.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Initialize parser with PDF document
        try (Parser parser = new Parser("input.pdf"))
        {
            // Ensure the document supports barcode reading
            if (!parser.getFeatures().isBarcodes())
            {
                return;
            }

            // Apply filtering with barcode options
            BarcodeOptions options = new BarcodeOptions(QualityMode.Low, QualityMode.Low, "QR");

            // Extract barcodes using the parser
            Iterable<PageBarcodeArea> barcodes = parser.getBarcodes(options);

            // Handle each barcode result
            for (PageBarcodeArea barcode : barcodes)
            {
                System.out.println("Page: " + String.valueOf(barcode.getPage().getIndex()));
                System.out.println("Value: " + barcode.getValue());
            }
        }
        ```
        {{< /landing/code >}}


############################# Actions ############################

actions:
  enable: true
  title: "Ready to get started?"
  description: "Try GroupDocs.Parser features for free or request a license"
  items:
    #  loop
    - title: "Maven download"
      link: "https://releases.groupdocs.com/parser/java/"
      color: "red"
        #  loop
    - title: "Licensing"
      link: "https://purchase.groupdocs.com/pricing/parser/java/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "File formats supported for barcode reading"
    exclude: "ODP"
    description: "GroupDocs.Parser can read barcodes from many document and image types. Below are some of the commonly supported formats."
    items: 
        # format loop 1
        - name: "Parse PDF"
          format: "PDF"
          link: "/parser/java/extract-barcode/pdf/"
          description: "(Portable Document Format)"
          
        # format loop 2
        - name: "Parse DOCX"
          format: "DOCX"
          link: "/parser/java/extract-barcode/docx/"
          description: "(Office 2007+ Word Document)"
          
        # format loop 3
        - name: "Parse PPTX"
          format: "PPTX"
          link: "/parser/java/extract-barcode/pptx/"
          description: "(Open XML presentation Format)"
          
        # format loop 4
        - name: "Parse XLSX"
          format: "XLSX"
          link: "/parser/java/extract-barcode/xlsx/"
          description: "(Open XML Workbook)"
          
        # format loop 5
        - name: "Parse ODT"
          format: "ODT"
          link: "/parser/java/extract-barcode/odt/"
          description: "(OpenDocument text doc)"
          
        # format loop 6
        - name: "Parse ODS"
          format: "ODS"
          link: "/parser/java/extract-barcode/ods/"
          description: "(OpenDocument spreadsheet)"
          
        # format loop 7
        - name: "Parse ODP"
          format: "ODP"
          link: "/parser/java/extract-barcode/odp/"
          description: "(OpenDocument presentation)"
          
        # format loop 8
        - name: "Parse EPUB"
          format: "EPUB"
          link: "/parser/java/extract-barcode/epub/"
          description: "(Open eBook File)"
          
        # format loop 9
        - name: "Parse FB2"
          format: "FB2"
          link: "/parser/java/extract-barcode/fb2/"
          description: "(FictionBook eBook)"
         
          

---