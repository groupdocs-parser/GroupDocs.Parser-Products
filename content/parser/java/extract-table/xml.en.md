


---
############################# Static ############################
layout: "format"
date:  2025-06-26T17:35:44
draft: false
lang: en
format: Xml
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Retrieve tables from XML documents in Java apps"
head_description: "Extract structured tabular data from XML files in Java applications using GroupDocs.Parser—no external tools needed."

############################# Header ############################
title: "Retrieve table data from XML using Java" 
description: "Seamlessly detect and extract tables from formats like PDF, DOCX, and XLSX with GroupDocs.Parser in your Java workflows."
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
    title: "Introduction to GroupDocs.Parser for Java API"
    link: "/parser/java/"
    link_title: "Learn more"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) is a feature-rich content extraction API for Java platforms. It allows developers to accurately parse tables, text, graphics, links, and structured data from PDFs, Word documents, Excel sheets, PowerPoint presentations, and more—without requiring third-party plugins.

############################# Steps ############################
steps:
    enable: true
    title: "How to retrieve tables from Xml in Java"
    content: |
      To parse tables from XML documents using [GroupDocs.Parser](/parser/java/), follow these easy steps in your Java environment:
      
      1. Create a Parser instance and load the target XML file.
      2. Verify that the file supports structured table extraction.
      3. Use the API to retrieve table elements from the document.
      4. Leverage the extracted data in analytics, reporting, or automation systems.
   
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
        // Load the input document with Parser that includes table elements
        try (Parser parser = new Parser("input.xml"))
        {
            // Verify that the document type allows table recognition
            if (!parser.getFeatures().isTables()) {
                System.out.println("Add logic for files that don’t support tables");
                return;
            }

            // Define rules for interpreting table structure
            TemplateTableLayout layout = new TemplateTableLayout(
                    java.util.Arrays.asList(new Double[]{50.0, 95.0, 275.0, 415.0, 485.0, 545.0}),
                    java.util.Arrays.asList(new Double[]{325.0, 340.0, 365.0, 395.0}));

            // Set parameters to extract tables
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            //  Run table extraction on the loaded document
            Iterable<PageTableArea> tables = parser.getTables(options);

            //  Process each extracted table from the result
            for (PageTableArea t : tables) {
            {
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "Advanced content extraction tools"
  description: "Beyond reading tables, GroupDocs.Parser supports capturing plain text, visual elements, embedded metadata, and structured objects to enhance document processing tasks."
  image: "/img/parser/features_extract-table.webp" # 500x500 px
  image_description: "Extracting structured content and tabular data"
  features:
    # feature loop
    - title: "Precise table parsing across formats"
      content: "Support for extracting tables from standard document types like PDF, Word, Excel, and HTML with high accuracy."

    # feature loop
    - title: "Read tabular structures from diverse sources"
      content: "Retrieve table data from spreadsheets, documents, and reports while preserving the structure and alignment."

    # feature loop
    - title: "Customizable table extraction settings"
      content: "Control layout detection, manage headers and footers, and fine-tune extraction with flexible configuration options."
      
  code_samples:
    # code sample loop
    - title: "Sample: extract tables from an Excel document"
      content: |
        This example shows how to extract and loop through table content in an Excel (XLSX) file using GroupDocs.Parser.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Initialize Parser with the Excel file
        try (Parser parser = new Parser("input.pdf"))
        {
            // Exit if table extraction isn’t supported for this format
            if (!parser.getFeatures().isTables())
            {
                return;
            }

            // Apply rules to locate table layout
            TemplateTableLayout layout = new TemplateTableLayout(
                    java.util.Arrays.asList(new Double[]{50.0, 95.0, 275.0, 415.0, 485.0, 545.0}),
                    java.util.Arrays.asList(new Double[]{325.0, 340.0, 365.0, 395.0}));

            // Configure settings for table extraction
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            // Invoke the extraction process
            Iterable<PageTableArea> tables = parser.getTables(options);

            // Loop over all parsed table structures
            for (PageTableArea t : tables)
            {
                // Iterate over each row within the table
                for (int row = 0; row < t.getRowCount(); row++)
                {
                    // Process each cell in the current row
                    for (int column = 0; column < t.getColumnCount(); column++) 
                    {
                        // Access and read the current cell's content
                        PageTableAreaCell cell = t.getCell(row, column);
                        if (cell != null)
                        {
                            // Output the textual value of each table cell
                            System.out.print(cell.getText());
                            System.out.print(" | ");
                        }
                    }
                }
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
    title: "Document types supported for table extraction"
    exclude: "XML"
    description: "GroupDocs.Parser provides reliable table detection across multiple file types. Here's a list of the most widely supported document formats for extracting tables."
    items: 
        # format loop 1
        - name: "Parse PDF"
          format: "PDF"
          link: "/parser/java/extract-table/pdf/"
          description: "(Portable Document Format)"
          
        # format loop 2
        - name: "Parse DOCX"
          format: "DOCX"
          link: "/parser/java/extract-table/docx/"
          description: "(Office 2007+ Word Document)"
          
        # format loop 3
        - name: "Parse PPTX"
          format: "PPTX"
          link: "/parser/java/extract-table/pptx/"
          description: "(Open XML presentation Format)"
          
        # format loop 4
        - name: "Parse XLSX"
          format: "XLSX"
          link: "/parser/java/extract-table/xlsx/"
          description: "(Open XML Workbook)"
          
        # format loop 5
        - name: "Parse TXT"
          format: "TXT"
          link: "/parser/java/extract-table/txt/"
          description: "(Text file)"
          
        # format loop 6
        - name: "Parse RTF"
          format: "RTF"
          link: "/parser/java/extract-table/rtf/"
          description: "(Rich Text Format)"
          
        # format loop 7
        - name: "Parse XML"
          format: "XML"
          link: "/parser/java/extract-table/xml/"
          description: "(eXtensible Markup Language)"
          
        # format loop 8
        - name: "Parse EPUB"
          format: "EPUB"
          link: "/parser/java/extract-table/epub/"
          description: "(Open eBook File)"
         
          

---