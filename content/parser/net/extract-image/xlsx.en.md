


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:33
draft: false
lang: en
format: Xlsx
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "Extract images from XLSX files in C# apps"
head_description: "Use GroupDocs.Parser to detect and extract images from XLSX files in C# without additional tools."

############################# Header ############################
title: "Extract images from XLSX using C#" 
description: "Easily locate and extract embedded images from PDFs, Word documents, Excel sheets, and other file types using GroupDocs.Parser in your .NET apps."
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
       [GroupDocs.Parser](/parser/net/) is a robust document parsing library for .NET developers. It allows you to extract images, text, hyperlinks, and structured data from popular file formats like PDF, DOCX, XLSX, PPTX, and others — all without needing any third-party applications.

############################# Steps ############################
steps:
    enable: true
    title: "Steps to extract images from Xlsx in C#"
    content: |
      With [GroupDocs.Parser](/parser/net/), you can extract images from XLSX documents in your .NET projects in just a few steps:
      
      1. Initialize the Parser with the XLSX file.
      2. Retrieve image elements from the document.
      3. Use the extracted images as needed in your workflow.
   
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
        // Open the document containing images using Parser
        using (Parser parser = new Parser("input.xlsx")) {

            // Extract all embedded images from the file
            IEnumerable<PageImageArea> images = parser.GetImages();

            // Handle cases where no images are found
            if (images == null)
            {
                return;
            }

            // Process or save the retrieved images
            foreach (PageImageArea image in images)
            {
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Type: {2}", 
                    image.Page.Index, image.Rectangle, image.FileType));
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "Comprehensive document content extraction"
  description: "GroupDocs.Parser offers more than just image extraction — you can also extract raw text, hyperlinks, metadata, and structured content for advanced automation scenarios."
  image: "/img/parser/features_extract-image.webp" # 500x500 px
  image_description: "Image extraction and document parsing workflow"
  features:
    # feature loop
    - title: "Extract images from multiple formats"
      content: "Pull out embedded images from a variety of file formats, including DOCX, PDF, PPTX, XLSX, and image files like PNG, JPG, and TIFF."

    # feature loop
    - title: "Preserve original image quality"
      content: "Images are extracted with high fidelity, maintaining their original resolution, format, and color profile."

    # feature loop
    - title: "Advanced extraction options"
      content: "Customize image extraction with filtering by page, format, or resolution, and support for multi-page documents."
      
  code_samples:
    # code sample loop
    - title: "How to extract and save images from a PDF document"
      content: |
        This example demonstrates how to extract all image assets from a PDF file and save them to the local file system.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Load the PDF using the Parser class
        using (Parser parser = new Parser("input.pdf"))
        {
            // Extract embedded images from the file
            IEnumerable<PageImageArea> images = parser.GetImages();

            // Set output format and image options (e.g., PNG)
            ImageOptions options = new ImageOptions(ImageFormat.Png);

            // Write the extracted images to disk
            int imageNumber = 0;
            foreach (PageImageArea image in images)
            {
                image.Save(imageNumber.ToString() + ".png", options);
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
    title: "Supported formats for image extraction"
    exclude: "XLSX"
    description: "GroupDocs.Parser enables accurate image extraction from a wide range of document and image formats. Check the list below for commonly supported types."
    items: 
        # format loop 1
        - name: "Parse PDF"
          format: "PDF"
          link: "/parser/net/extract-image/pdf/"
          description: "(Portable Document Format)"
          
        # format loop 2
        - name: "Parse DOCX"
          format: "DOCX"
          link: "/parser/net/extract-image/docx/"
          description: "(Office 2007+ Word Document)"
          
        # format loop 3
        - name: "Parse PPTX"
          format: "PPTX"
          link: "/parser/net/extract-image/pptx/"
          description: "(Open XML presentation Format)"
          
        # format loop 4
        - name: "Parse XLSX"
          format: "XLSX"
          link: "/parser/net/extract-image/xlsx/"
          description: "(Open XML Workbook)"
          
        # format loop 5
        - name: "Parse ODT"
          format: "ODT"
          link: "/parser/net/extract-image/odt/"
          description: "(OpenDocument text doc)"
          
        # format loop 6
        - name: "Parse ODS"
          format: "ODS"
          link: "/parser/net/extract-image/ods/"
          description: "(OpenDocument spreadsheet)"
          
        # format loop 7
        - name: "Parse ODP"
          format: "ODP"
          link: "/parser/net/extract-image/odp/"
          description: "(OpenDocument presentation)"
          
        # format loop 8
        - name: "Parse EPUB"
          format: "EPUB"
          link: "/parser/net/extract-image/epub/"
          description: "(Open eBook File)"
          
        # format loop 9
        - name: "Parse FB2"
          format: "FB2"
          link: "/parser/net/extract-image/fb2/"
          description: "(FictionBook eBook)"
         
          

---