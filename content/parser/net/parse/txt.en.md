


---
############################# Static ############################
layout: "format"
date:  2025-06-26T17:35:46
draft: false
lang: en
format: Txt
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "Parse data from TXT files in C# apps"
head_description: "Use GroupDocs.Parser to extract text, images, tables, and other data from TXT files in C# without relying on third-party tools."

############################# Header ############################
title: "Parse TXT documents using C#" 
description: "Efficiently extract text, metadata, tables, and images from PDF, Word, Excel, and image files using GroupDocs.Parser in your .NET projects."
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
       [GroupDocs.Parser](/parser/net/) is a feature-rich document parsing API designed for .NET developers. It supports extracting plain and structured text, metadata, images, tables, and barcodes from popular formats like PDF, DOCX, XLSX, PPTX, and more — all without additional software dependencies.

############################# Steps ############################
steps:
    enable: true
    title: "Steps to extract data from Txt in C#"
    content: |
      Follow these steps to parse content from TXT documents in your .NET apps using [GroupDocs.Parser](/parser/net/):
      
      1. Load the TXT document using a Parser instance.
      2. Extract the desired content such as text, tables, or metadata.
      3. Verify that the extracted data is valid.
      4. Use the parsed output in your downstream processing, automation, or business systems.
   
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
        // Load your document into Parser
        using (Parser parser = new Parser("input.txt")) {

            // Extract all text content from the file
            using (TextReader reader = parser.GetText()) 
            {
                // If the text is unavailable, the result will be null
                // Use the extracted text in your application
                Console.WriteLine(reader == null ? 
                    "Text extraction is unsupported for this format" : reader.ReadToEnd());
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "Comprehensive document parsing capabilities"
  description: "GroupDocs.Parser enables more than just barcode reading — it supports full-text extraction, image parsing, metadata access, and structured data processing for advanced automation and data analysis."
  image: "/img/parser/features_parse.webp" # 500x500 px
  image_description: "Document content extraction and parsing capabilities"
  features:
    # feature loop
    - title: "Support for diverse file content types"
      content: "Extract data including text, images, tables, and fields from document formats like PDF, Word, Excel, HTML, and more."

    # feature loop
    - title: "Work with both scanned and digital files"
      content: "Parse data from scanned documents and born-digital files alike, with support for OCR and layout-aware extraction."

    # feature loop
    - title: "Configurable extraction parameters"
      content: "Adjust parsing logic with flexible options like page range selection, region targeting, and field detection templates."
      
  code_samples:
    # code sample loop
    - title: "How to parse PDF using templates"
      content: |
        This example shows how to extract structured data from a PDF using a predefined parsing template with GroupDocs.Parser.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Load the PDF file with the Parser class
        using (Parser parser = new Parser("input.pdf"))
        {
            // Parse the document by the template
            DocumentData data = parser.ParseByTemplate(GetTemplate());

            // Check if form extraction is supported
            if (data == null)
            {
                return;
            }

            // Process obtained fields
            for (int i = 0; i < data.Count; i++)
            {
                Console.Write(data[i].Name + ": ");
                PageTextArea area = data[i].PageArea as PageTextArea;
                Console.WriteLine(area == null ? "Not a template field" : area.Text);
            }
        }

        private static Template GetTemplate()
        {
            // Create detector parameters for 'Details' table
            TemplateTableParameters detailsTableParameters = 
                new TemplateTableParameters(new Rectangle(new Point(35, 320), new Size(530, 55)), null);

            TemplateItem[] templateItems = new TemplateItem[]
            {
                new TemplateTable(detailsTableParameters, "details", null)
            };

            Template template = new Template(templateItems);
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
    title: "Supported formats for data extraction"
    exclude: "TXT"
    description: "GroupDocs.Parser enables parsing across a broad set of document and image formats. Explore the supported file types commonly used in data extraction workflows."
    items: 
        # format loop 1
        - name: "Parse PDF"
          format: "PDF"
          link: "/parser/net/parse/pdf/"
          description: "(Portable Document Format)"
          
        # format loop 2
        - name: "Parse DOCX"
          format: "DOCX"
          link: "/parser/net/parse/docx/"
          description: "(Office 2007+ Word Document)"
          
        # format loop 3
        - name: "Parse PPTX"
          format: "PPTX"
          link: "/parser/net/parse/pptx/"
          description: "(Open XML presentation Format)"
          
        # format loop 4
        - name: "Parse XLSX"
          format: "XLSX"
          link: "/parser/net/parse/xlsx/"
          description: "(Open XML Workbook)"
          
        # format loop 5
        - name: "Parse TXT"
          format: "TXT"
          link: "/parser/net/parse/txt/"
          description: "(Text file)"
          
        # format loop 6
        - name: "Parse RTF"
          format: "RTF"
          link: "/parser/net/parse/rtf/"
          description: "(Rich Text Format)"
          
        # format loop 7
        - name: "Parse XML"
          format: "XML"
          link: "/parser/net/parse/xml/"
          description: "(eXtensible Markup Language)"
          
        # format loop 8
        - name: "Parse EPUB"
          format: "EPUB"
          link: "/parser/net/parse/epub/"
          description: "(Open eBook File)"
         
          

---