


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:49
draft: false
lang: en
format: Docx
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Extract content from DOCX files in Java applications"
head_description: "Leverage GroupDocs.Parser to parse and retrieve structured data, text, tables, and images from DOCX files in Java, without needing external tools."

############################# Header ############################
title: "Extract data from DOCX documents in Java" 
description: "Seamlessly extract structured content such as text, metadata, tables, and graphics from PDFs, Word, Excel, and image-based documents using GroupDocs.Parser in your Java apps."
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
       [GroupDocs.Parser](/parser/java/) is a robust API built for Java developers, offering advanced document parsing functionality. It allows you to extract and process textual data, images, tables, structured fields, and barcodes from numerous formats like PDF, DOCX, XLSX, PPTX, and more — all without installing extra libraries.

############################# Steps ############################
steps:
    enable: true
    title: "How to extract data from Docx using Java"
    content: |
      To extract useful information from DOCX documents in your Java projects using [GroupDocs.Parser](/parser/java/), follow these instructions:
      
      1. Open the DOCX file with a Parser object.
      2. Use the parser to retrieve the required data (text, tables, metadata, etc.).
      3. Ensure the output is correct and complete.
      4. Integrate the parsed content into your data flow, business processes, or applications.
   
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
        // Initialize your Parser with the input document
        try (Parser parser = new Parser("input.docx"))
        {
            // Retrieve all available text content from the document
            try (TextReader reader = parser.getText())
            {
                // If no text is found, the return value will be null
                // Incorporate the extracted content into your solution
                System.out.println(reader == null ? 
                    "This format may not support text extraction" : reader.readToEnd());
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "Versatile document parsing functionality"
  description: "GroupDocs.Parser does more than just text extraction—it supports full parsing of barcodes, metadata, images, tables and other data to power intelligent automation and data-driven applications."
  image: "/img/parser/features_parse.webp" # 500x500 px
  image_description: "Visual overview of document data parsing and extraction"
  features:
    # feature loop
    - title: "Extract from multiple file formats"
      content: "Access data like text, tables, and media from widely used file types such as PDF, Word, Excel, PowerPoint, HTML, and others."

    # feature loop
    - title: "Parse content from digital and scanned sources"
      content: "Process content from both native digital files and scanned images, using OCR when necessary to interpret embedded text."

    # feature loop
    - title: "Flexible configuration options"
      content: "Tailor your parsing with settings for page selection, layout zones, and custom field templates to meet specific extraction needs."
      
  code_samples:
    # code sample loop
    - title: "Parsing PDF using a data extraction template"
      content: |
        This sample shows how to extract structured fields from a PDF using a custom template via GroupDocs.Parser.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Open the PDF using the Parser class
        try (Parser parser = new Parser("input.pdf"))
        {
            // Apply the parsing template to extract defined data
            DocumentData data = parser.parseByTemplate(GetTemplate());

            // Check if the template-based extraction is available
            if (data == null) {
                return;
            }

            // Work with the extracted data fields
            for (int i = 0; i < data.getCount(); i++) {
                System.out.print(data.get(i).getName() + ": ");
                PageTextArea area = data.get(i).getPageArea() instanceof PageTextArea
                        ? (PageTextArea) data.get(i).getPageArea() : null;
                System.out.println(area == null ? "Not a template field" : area.getText());
            }
        }

        private static Template GetTemplate()
        {
            // Define detector settings for extracting the 'Details' section
            TemplateTableParameters detailsTableParameters = 
                new TemplateTableParameters(new Rectangle(new Point(35, 320), new Size(530, 55)), null);

            TemplateItem[] templateItems = new TemplateItem[]
            {
                new TemplateTable(detailsTableParameters, "details", null)
            };

            Template template = new Template(java.util.Arrays.asList(templateItems));
            return template;
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
    title: "File types supported for content extraction"
    exclude: "DOCX"
    description: "GroupDocs.Parser is compatible with a wide range of document and image file types, making it easy to extract information from commonly used formats in parsing and data automation scenarios."
    items: 
        # format loop 1
        - name: "Parse PDF"
          format: "PDF"
          link: "/parser/java/parse/pdf/"
          description: "(Portable Document Format)"
          
        # format loop 2
        - name: "Parse DOCX"
          format: "DOCX"
          link: "/parser/java/parse/docx/"
          description: "(Office 2007+ Word Document)"
          
        # format loop 3
        - name: "Parse PPTX"
          format: "PPTX"
          link: "/parser/java/parse/pptx/"
          description: "(Open XML presentation Format)"
          
        # format loop 4
        - name: "Parse XLSX"
          format: "XLSX"
          link: "/parser/java/parse/xlsx/"
          description: "(Open XML Workbook)"
          
        # format loop 5
        - name: "Parse TXT"
          format: "TXT"
          link: "/parser/java/parse/txt/"
          description: "(Text file)"
          
        # format loop 6
        - name: "Parse RTF"
          format: "RTF"
          link: "/parser/java/parse/rtf/"
          description: "(Rich Text Format)"
          
        # format loop 7
        - name: "Parse XML"
          format: "XML"
          link: "/parser/java/parse/xml/"
          description: "(eXtensible Markup Language)"
          
        # format loop 8
        - name: "Parse EPUB"
          format: "EPUB"
          link: "/parser/java/parse/epub/"
          description: "(Open eBook File)"
         
          

---