


---
############################# Static ############################
layout: "format"
date:  2025-06-26T17:35:42
draft: false
lang: en
format: Xlsx
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Extract hyperlinks from XLSX files in Java apps"
head_description: "Use GroupDocs.Parser to find and extract URL links from XLSX documents in Java projects—no extra software needed."

############################# Header ############################
title: "Extract hyperlinks from XLSX with Java" 
description: "Easily pull out web links and hyperlinks from PDFs, Word files, Excel sheets, and other documents using GroupDocs.Parser in your Java environment."
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
    title: "About GroupDocs.Parser for Java API"
    link: "/parser/java/"
    link_title: "Learn more"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) is a robust content extraction API designed for Java developers. It offers tools to extract hyperlinks, structured data, images, and text from popular formats like DOCX, XLSX, PDF, HTML, and more—all without needing any external plugins.

############################# Steps ############################
steps:
    enable: true
    title: "How to extract hyperlinks from Xlsx in Java"
    content: |
      [GroupDocs.Parser](/parser/java/) simplifies hyperlink extraction from XLSX files in Java applications with these basic steps:
      
      1. Open the XLSX file using an instance of Parser.
      2. Ensure hyperlink extraction is available for the file format.
      3. Extract all hyperlinks using the appropriate method.
      4. Loop through the results and process each link as needed.
   
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
        // Load the file that may contain hyperlinks using the Parser
        try (Parser parser = new Parser("input.xlsx")) {

            // Check whether the document format supports hyperlink parsing
            if (!parser.getFeatures().isHyperlinks()) {
                System.out.println("Hyperlink extraction is not available for the file");
                return;
            }

            // Extract and use hyperlink data from the document
            Iterable<PageHyperlinkArea> hyperlinks = parser.getHyperlinks();

            for (PageHyperlinkArea h : hyperlinks) {
                System.out.println(h.getText());
                System.out.println(h.getUrl());
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "Comprehensive document parsing tools"
  description: "Along with extracting hyperlinks, GroupDocs.Parser enables you to collect other useful content like plain text, embedded media, and structured data for use in automated workflows."
  image: "/img/parser/features_extract-hyperlink.webp" # 500x500 px
  image_description: "Hyperlink extraction and document analysis"
  features:
    # feature loop
    - title: "Accurate link detection"
      content: "Capture all types of hyperlinks from different document layouts, including clickable text and hidden URLs."

    # feature loop
    - title: "Works with documents and web content"
      content: "Pull links from PDF, DOCX, XLSX, HTML, and image files that contain embedded hyperlinks."

    # feature loop
    - title: "Custom extraction behavior"
      content: "Refine how hyperlinks are extracted using options like page ranges, link types, or content filters."
      
  code_samples:
    # code sample loop
    - title: "Example: extracting hyperlinks from a PDF with custom options"
      content: |
        This sample demonstrates how to extract all links from a PDF file using link extraction settings.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Open the PDF using the Parser class
        try (Parser parser = new Parser("input.docx"))
        {
            // Verify that hyperlink support is enabled for this document
            if (!parser.getFeatures().isHyperlinks()) {
                return;
            }

            // Apply options to filter the type of links
            PageAreaOptions options = new PageAreaOptions(new Rectangle(new Point(380, 90), new Size(150, 50)));

            // Use the parser to get hyperlink data
            Iterable<PageHyperlinkArea> hyperlinks = parser.getHyperlinks(options);

            // Iterate through the links and handle them accordingly
            for (PageHyperlinkArea h : hyperlinks) {
                System.out.println(h.getText());
                System.out.println(h.getUrl());
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
    title: "Document formats that support hyperlink extraction"
    exclude: "XLSX"
    description: "With GroupDocs.Parser, you can extract hyperlinks from many commonly used file formats. Below is a list of formats typically supported."
    items: 
        # format loop 1
        - name: "Parse PDF"
          format: "PDF"
          link: "/parser/java/extract-hyperlink/pdf/"
          description: "(Portable Document Format)"
          
        # format loop 2
        - name: "Parse DOCX"
          format: "DOCX"
          link: "/parser/java/extract-hyperlink/docx/"
          description: "(Office 2007+ Word Document)"
          
        # format loop 3
        - name: "Parse PPTX"
          format: "PPTX"
          link: "/parser/java/extract-hyperlink/pptx/"
          description: "(Open XML presentation Format)"
          
        # format loop 4
        - name: "Parse XLSX"
          format: "XLSX"
          link: "/parser/java/extract-hyperlink/xlsx/"
          description: "(Open XML Workbook)"
          
        # format loop 5
        - name: "Parse TXT"
          format: "TXT"
          link: "/parser/java/extract-hyperlink/txt/"
          description: "(Text file)"
          
        # format loop 6
        - name: "Parse RTF"
          format: "RTF"
          link: "/parser/java/extract-hyperlink/rtf/"
          description: "(Rich Text Format)"
          
        # format loop 7
        - name: "Parse XML"
          format: "XML"
          link: "/parser/java/extract-hyperlink/xml/"
          description: "(eXtensible Markup Language)"
          
        # format loop 8
        - name: "Parse EPUB"
          format: "EPUB"
          link: "/parser/java/extract-hyperlink/epub/"
          description: "(Open eBook File)"
         
          

---