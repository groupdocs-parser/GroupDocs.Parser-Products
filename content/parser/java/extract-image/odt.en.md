


---
############################# Static ############################
layout: "format"
date:  2025-06-26T17:35:43
draft: false
lang: en
format: Odt
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Extract images from ODT files in Java applications"
head_description: "With GroupDocs.Parser, you can extract images from ODT files in Java effortlessly, with no need for third-party tools."

############################# Header ############################
title: "Extract images from ODT using Java" 
description: "Retrieve embedded images from files such as PDF, Word, Excel, and more using GroupDocs.Parser in your Java development environment."
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
    title: "What is GroupDocs.Parser for Java?"
    link: "/parser/java/"
    link_title: "Learn more"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) is a feature-rich parsing API tailored for Java developers. It enables the extraction of images, text, links, and structured elements from various file formats including DOCX, XLSX, PDF, PNG, JPG, and many others — all without needing external libraries or applications.

############################# Steps ############################
steps:
    enable: true
    title: "How to extract images from Odt in Java"
    content: |
      Follow these steps to extract images from ODT documents using [GroupDocs.Parser](/parser/java/) in your Java application:
      
      1. Create a Parser instance and load the ODT file.
      2. Extract image data from the loaded document.
      3. Use or export the extracted images as needed.
   
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
        // Initialize parser and load the document with images using Parser
        try (Parser parser = new Parser("input.odt"))
        {
            // Collect all image elements embedded in the document
            Iterable<PageImageArea> images = parser.getImages();

            // Skip processing if the document has no images
            if (images == null) {
                return;
            }

            // Handle each image as required
            for (PageImageArea image : images) {
                System.out.println(String.format("Page: %d, R: %s, Type: %s", image.getPage().getIndex(), 
                    image.getRectangle(), image.getFileType()));
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "More document parsing capabilities"
  description: "In addition to image extraction, GroupDocs.Parser allows you to extract raw content like text, links, metadata, and structured data for processing and analysis."
  image: "/img/parser/features_extract-image.webp" # 500x500 px
  image_description: "Extract images and content from documents"
  features:
    # feature loop
    - title: "Works with a variety of formats"
      content: "Extract images from different document types including PDF, DOCX, PPTX, XLSX, and image formats like PNG, JPEG, and GIF."

    # feature loop
    - title: "Maintain image clarity and resolution"
      content: "All extracted images retain their original resolution and file type to ensure consistent quality and usability."

    # feature loop
    - title: "Flexible configuration options"
      content: "Customize the image extraction process by filtering images by type, size, page index, or file format."
      
  code_samples:
    # code sample loop
    - title: "Extract and save images from PDF files"
      content: |
        This example shows how to extract images from a PDF document and save them individually on your device.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Use Parser to open the PDF file
        try (Parser parser = new Parser("input.pdf"))
        {
            // Get the images from the document content
            Iterable<PageImageArea> images = parser.getImages();

            // Set output parameters like format (e.g., JPEG or PNG)
            ImageOptions options = new ImageOptions(ImageFormat.Png);

            // Save extracted images to a local directory
            int imageNumber = 0;
            for (PageImageArea image : images)
            {
                image.save(Constants.getOutputFilePath(String.format("%d.png", imageNumber)), options);
                imageNumber++;
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
    title: "File types supported for image extraction"
    exclude: "ODT"
    description: "GroupDocs.Parser supports image extraction across a broad array of documents and images. Explore the commonly supported formats below."
    items: 
        # format loop 1
        - name: "Parse PDF"
          format: "PDF"
          link: "/parser/java/extract-image/pdf/"
          description: "(Portable Document Format)"
          
        # format loop 2
        - name: "Parse DOCX"
          format: "DOCX"
          link: "/parser/java/extract-image/docx/"
          description: "(Office 2007+ Word Document)"
          
        # format loop 3
        - name: "Parse PPTX"
          format: "PPTX"
          link: "/parser/java/extract-image/pptx/"
          description: "(Open XML presentation Format)"
          
        # format loop 4
        - name: "Parse XLSX"
          format: "XLSX"
          link: "/parser/java/extract-image/xlsx/"
          description: "(Open XML Workbook)"
          
        # format loop 5
        - name: "Parse ODT"
          format: "ODT"
          link: "/parser/java/extract-image/odt/"
          description: "(OpenDocument text doc)"
          
        # format loop 6
        - name: "Parse ODS"
          format: "ODS"
          link: "/parser/java/extract-image/ods/"
          description: "(OpenDocument spreadsheet)"
          
        # format loop 7
        - name: "Parse ODP"
          format: "ODP"
          link: "/parser/java/extract-image/odp/"
          description: "(OpenDocument presentation)"
          
        # format loop 8
        - name: "Parse EPUB"
          format: "EPUB"
          link: "/parser/java/extract-image/epub/"
          description: "(Open eBook File)"
          
        # format loop 9
        - name: "Parse FB2"
          format: "FB2"
          link: "/parser/java/extract-image/fb2/"
          description: "(FictionBook eBook)"
         
          

---