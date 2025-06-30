


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:40
draft: false
lang: en
format: Pdf
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "Extract tables from PDF files in C# apps"
head_description: "Use GroupDocs.Parser to locate and extract structured table data from PDF files in C# applications without extra dependencies."

############################# Header ############################
title: "Extract tables from PDF using C#" 
description: "Quickly identify and extract table structures from PDF, Word, Excel, and other file formats using GroupDocs.Parser in your .NET projects."
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Download Free Trial"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "About GroupDocs.Parser for .NET API"
    link: "/parser/net/"
    link_title: "Learn more"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/) is a comprehensive document parsing API built for .NET developers. It enables accurate extraction of text, tables, images, hyperlinks, and other structured elements from formats like PDF, DOCX, XLSX, PPTX, and many others — without the need for third-party software.

############################# Steps ############################
steps:
    enable: true
    title: "Steps to extract tables from Pdf in C#"
    content: |
      Follow these instructions to extract tables from PDF files using [GroupDocs.Parser](/parser/net/) within your .NET environment:
      
      1. Initialize a Parser instance and load your PDF document.
      2. Check if table extraction is supported for the input format.
      3. Extract table content from the file.
      4. Use the structured table data for reporting, automation, or analytics.
   
    code:
      platform: "net"
      copy_title: "Copy"
      install:
        command: |
        command: "dotnet add package GroupDocs.Parser"
        copy_tip: "click to copy"
        copy_done: "copied"
      links:
        #  loop
        - title: "More examples"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
        #  loop
        - title: "Documentation"
          link: "https://docs.groupdocs.com/parser/net/"
          
      content: |
        ```csharp {style=abap}
        // Open the document that contains table data using Parser
        using (Parser parser = new Parser("input.pdf")) {

            // Check if the format supports table recognition
            if (!parser.Features.Tables) {
                Console.WriteLine("Handle documents that do not support table parsing");
                return;
            }

            // Define how table structure should be recognized
            TemplateTableLayout layout = new TemplateTableLayout(
                new double[] { 50, 95, 275, 415, 485, 545 },
                new double[] { 325, 340, 365, 395 });

            // Specify extraction parameters for table data
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            //  Extract tables from the file content
            IEnumerable<PageTableArea> tables = parser.GetTables(options);

            //  Loop through each detected table
            foreach (PageTableArea t in tables)
            {
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "Powerful data extraction capabilities"
  description: "In addition to table parsing, GroupDocs.Parser can extract rich content such as text blocks, images, metadata, and other structured data to facilitate document automation."
  image: "/img/parser/features_extract-table.webp" # 500x500 px
  image_description: "Table recognition and content extraction"
  features:
    # feature loop
    - title: "Accurate multi-format table detection"
      content: "Extract tabular data from DOCX, XLSX, PDF, HTML, and similar formats with high precision."

    # feature loop
    - title: "Parse table structures from files"
      content: "Efficiently retrieve table data from documents and spreadsheets without formatting loss."

    # feature loop
    - title: "Flexible table extraction configuration"
      content: "Adjust layout detection, column alignment, and header/footer options for precise control over output."
      
  code_samples:
    # code sample loop
    - title: "How to extract tables from Excel spreadsheets"
      content: |
        This code sample shows how to read and iterate through table data in an XLSX file using GroupDocs.Parser.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Open the Excel file using the Parser API
        using (Parser parser = new Parser("input.xlsx"))
        {
            // Exit if tables cannot be extracted from the file
            if (!parser.Features.Tables)
            {
                return;
            }

            // Use layout rules to locate tabular content
            TemplateTableLayout layout = new TemplateTableLayout(
                    new double[] { 50, 95, 275, 415, 485, 545 },
                    new double[] { 325, 340, 365, 395 });

            // Set up extraction parameters for tables
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            // Perform the table extraction operation
            IEnumerable<PageTableArea> tables = parser.GetTables(options);

            // Go through each detected table structure
            foreach (PageTableArea t in tables)
            {
                // Iterate through each row in the table
                for (int row = 0; row < t.RowCount; row++)
                {
                    // Loop through the cells in each row
                    for (int column = 0; column < t.ColumnCount; column++)
                    {
                        // Access the current table cell
                        PageTableAreaCell cell = t[row, column];
                        if (cell != null)
                        {
                            // Display the text content of each cell
                            Console.Write(cell.Text);
                            Console.Write(" | ");
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
    - title: "Nuget download"
      link: "https://releases.groupdocs.com/parser/net/"
      color: "red"
        #  loop
    - title: "Licensing"
      link: "https://purchase.groupdocs.com/pricing/parser/net/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "Supported formats for table extraction"
    exclude: "PDF"
    description: "GroupDocs.Parser can extract table data from a variety of document types. Below are the most frequently used formats for structured table parsing."
    items: 
        # format loop 1
        - name: "Parse PDF"
          format: "PDF"
          link: "/parser/net/extract-table/pdf/"
          description: "(Portable Document Format)"
          
        # format loop 2
        - name: "Parse DOCX"
          format: "DOCX"
          link: "/parser/net/extract-table/docx/"
          description: "(Office 2007+ Word Document)"
          
        # format loop 3
        - name: "Parse PPTX"
          format: "PPTX"
          link: "/parser/net/extract-table/pptx/"
          description: "(Open XML presentation Format)"
          
        # format loop 4
        - name: "Parse XLSX"
          format: "XLSX"
          link: "/parser/net/extract-table/xlsx/"
          description: "(Open XML Workbook)"
          
        # format loop 5
        - name: "Parse TXT"
          format: "TXT"
          link: "/parser/net/extract-table/txt/"
          description: "(Text file)"
          
        # format loop 6
        - name: "Parse RTF"
          format: "RTF"
          link: "/parser/net/extract-table/rtf/"
          description: "(Rich Text Format)"
          
        # format loop 7
        - name: "Parse XML"
          format: "XML"
          link: "/parser/net/extract-table/xml/"
          description: "(eXtensible Markup Language)"
          
        # format loop 8
        - name: "Parse EPUB"
          format: "EPUB"
          link: "/parser/net/extract-table/epub/"
          description: "(Open eBook File)"
         
          

---