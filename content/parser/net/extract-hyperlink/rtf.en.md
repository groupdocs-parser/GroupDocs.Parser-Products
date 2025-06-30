


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:26
draft: false
lang: en
format: Rtf
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "Extract hyperlinks from RTF files in C# apps"
head_description: "Use GroupDocs.Parser to detect and extract hyperlinks from RTF files in C# without additional tools or software."

############################# Header ############################
title: "Extract hyperlinks from RTF using C#" 
description: "Easily detect and extract URLs and hyperlinks from PDF, Word, Excel, and other document types using GroupDocs.Parser in your .NET applications."
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
       [GroupDocs.Parser](/parser/net/) is a versatile document parsing API for .NET developers. It supports extracting hyperlinks, text, images, and structured content from various file formats such as PDF, Word, Excel, HTML, and more—without relying on external software.

############################# Steps ############################
steps:
    enable: true
    title: "Steps to extract hyperlinks from Rtf in C#"
    content: |
      [GroupDocs.Parser](/parser/net/) enables .NET developers to extract hyperlinks from RTF files by following these simple steps:
      
      1. Load the RTF file using a Parser instance.
      2. Check if the document supports hyperlink extraction.
      3. Retrieve the list of hyperlinks from the document.
      4. Loop through the results and work with the extracted URLs.
   
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
        // Load the document containing hyperlinks using the Parser class
        using (Parser parser = new Parser("input.rtf")) {

            // Verify that the file supports hyperlink extraction
            if (!parser.Features.Hyperlinks)
            {
                Console.WriteLine("Hyperlink extraction is not available for the file");
                return;
            }

            // Retrieve and process the extracted hyperlinks
            IEnumerable<PageHyperlinkArea> hyperlinks = parser.GetHyperlinks();

            foreach (PageHyperlinkArea h in hyperlinks)
            {
                Console.WriteLine(h.Text);
                Console.WriteLine(h.Url);
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "Advanced document parsing capabilities"
  description: "In addition to hyperlink extraction, GroupDocs.Parser allows you to extract text, metadata, images, and structured data—supporting powerful data processing workflows."
  image: "/img/parser/features_extract-hyperlink.webp" # 500x500 px
  image_description: "Hyperlink detection and document parsing"
  features:
    # feature loop
    - title: "Hyperlink detection from documents"
      content: "Quickly extract URLs and link annotations from documents like PDFs, Word files, spreadsheets, and more."

    # feature loop
    - title: "Support for web and embedded links"
      content: "Detect and extract both standard web URLs and embedded document links across multiple formats."

    # feature loop
    - title: "Flexible parsing options"
      content: "Customize extraction settings for scanning specific sections or pages to improve performance and accuracy."
      
  code_samples:
    # code sample loop
    - title: "How to extract hyperlinks from a PDF using link options"
      content: |
        This code example shows how to extract all hyperlinks from a PDF file using custom options.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Initialize the Parser with the PDF document
        using (Parser parser = new Parser("input.docx"))
        {
            // Check if hyperlink extraction is supported
            if (!parser.Features.Hyperlinks)
            {
                return;
            }

            // Set link extraction options to narrow results
            PageAreaOptions options = new PageAreaOptions(new Rectangle(new Point(380, 90), new Size(150, 50)));

            // Extract hyperlink data from the document
            IEnumerable<PageHyperlinkArea> hyperlinks = parser.GetHyperlinks(options);

            // Handle the list of extracted links
            foreach (PageHyperlinkArea h in hyperlinks)
            {
                Console.WriteLine(h.Text);
                Console.WriteLine(h.Url);
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
    title: "Supported formats for hyperlink extraction"
    exclude: "RTF"
    description: "GroupDocs.Parser can extract hyperlinks from a wide variety of document types. See below for commonly supported formats."
    items: 
        # format loop 1
        - name: "Parse PDF"
          format: "PDF"
          link: "/parser/net/extract-hyperlink/pdf/"
          description: "(Portable Document Format)"
          
        # format loop 2
        - name: "Parse DOCX"
          format: "DOCX"
          link: "/parser/net/extract-hyperlink/docx/"
          description: "(Office 2007+ Word Document)"
          
        # format loop 3
        - name: "Parse PPTX"
          format: "PPTX"
          link: "/parser/net/extract-hyperlink/pptx/"
          description: "(Open XML presentation Format)"
          
        # format loop 4
        - name: "Parse XLSX"
          format: "XLSX"
          link: "/parser/net/extract-hyperlink/xlsx/"
          description: "(Open XML Workbook)"
          
        # format loop 5
        - name: "Parse TXT"
          format: "TXT"
          link: "/parser/net/extract-hyperlink/txt/"
          description: "(Text file)"
          
        # format loop 6
        - name: "Parse RTF"
          format: "RTF"
          link: "/parser/net/extract-hyperlink/rtf/"
          description: "(Rich Text Format)"
          
        # format loop 7
        - name: "Parse XML"
          format: "XML"
          link: "/parser/net/extract-hyperlink/xml/"
          description: "(eXtensible Markup Language)"
          
        # format loop 8
        - name: "Parse EPUB"
          format: "EPUB"
          link: "/parser/net/extract-hyperlink/epub/"
          description: "(Open eBook File)"
         
          

---