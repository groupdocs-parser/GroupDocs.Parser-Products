---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:11
draft: false
otherformats: 

############################# Head ############################
head_title: "Extract Tables from PDF, DOCX, PPTX, XLSX, EPUB & More via Java API"
head_description: "GroupDocs.Parser Java API enables progreammers to extract tables from PDF, DOC, DOCX, PPT, PPTX, EML, MSG, XLS, XLSX, CSV, ODT, RTF & many other documents types inside Java Apps."

############################# Header ############################
title: "Extract Tables from Excel, Word, PDF & PowerPoint Documents via Java API"
description: "GroupDocs.Parser Java API allows programmers to extract tables from PDF, DOC, DOCX, PPT, PPTX, EML, MSG, XLS, XLSX, CSV, ODT, RTF & EPUB documents or pages."
bg_image: "https://cms.admin.containerize.com/templates/aspose/App_Themes/V3/images/bg/header1.png"
bg_overlay: false
button:
    enable: true
    icon: "fas fa-arrow-down"
    label: "Download Free Trial"
    link: "https://downloads.groupdocs.com/parser/java"

############################# SubMenu ############################
submenu:
    enable: true

    left:
        img_alt: "GroupDocs.Parser for Java"
        image: "https://cms.admin.containerize.com/templates/groupdocs/images/product-logos/90x90-noborder/groupdocs-parser-java.png"
        product: "GroupDocs.Parser"
        platform: "Java"

    middle:
        button:

            # button loop
            - link: "https://apireference.groupdocs.com/parser/java"
              text: "API Reference"

            # button loop
            - link: "https://github.com/groupdocs-parser"
              text: "Code Examples"

            # button loop
            - link: "https://products.groupdocs.app/parser/family"
              text: "Live Demos"

            # button loop
            - link: "https://purchase.groupdocs.com/pricing/parser/java"
              text: "Pricing"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/java"
        link_buy: "https://purchase.groupdocs.com"

############################# About ############################
about:
    enable: true
    title: "How to Extract Tables from EML files via Java API?"
    content: |
        Table is the collection of cells arranged in rows and columns. Tables play a very important role in storing as well as organizing detailed or complicated data allowing the users to easily read and view it. Tables can be used in many ways, such as making lists, comparing information, align data, group information, highlight trends or patterns in data and many more. GroupDocs.Parser for Java is a useufly API that allows software programmers to develop solution for extracting tables, text and images from various kinds of supported documents formats, such as such as PDF, Emails, Ebooks, Word (DOC, DOCX), PowerPoint (PPT, PPTX), Excel (XLS, XLSX), Emails (EML, MSG) formats and many more. The Java API has included several important features for working with tables, such as extract all tables from a documents, extract table from a particular page, get table cell data, get total number of a table rows and columns, get row height, print data of a table and may more.
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: "Extract tables from EML in Java"
    content_left: |
        [GroupDocs.Parser for Java](/parser/java/) makes it easy for Java developers to extract tables from a EML file by implementing a few easy steps.
        
        * Instantiate [Parser](https://reference.groupdocs.com/parser/java/com.groupdocs.parser/parser/) object for the initial document;
        * Check if the document supports table extraction;
        * Instantiate [PageTableAreaOptions](https://reference.groupdocs.com/parser/java/com.groupdocs.parser.options/pagetableareaoptions/) and [TemplateTableLayout](https://reference.groupdocs.com/parser/java/com.groupdocs.parser.templates/templatetablelayout/) classes to set the layout of tables
        * Call [getTables](https://reference.groupdocs.com/parser/java/com.groupdocs.parser/parser/#getTables-com.groupdocs.parser.options.PageTableAreaOptions-) method and obtain collection of [PageTableArea](https://reference.groupdocs.com/parser/java/com.groupdocs.parser.data/pagetablearea/) objects;

    title_right: "Learn more about the tables extraction"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/java/extract-tables-from-document/">How to extract tables from document</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-tables-from-document-page/">How to extract tables from document page</a>
 
    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="How to extract tables from EML file using Java example code">}}

        ```java    
        // Extract tables from EML file using GroupDocs.Parser API
        // Create an instance of Parser class
        try (Parser parser = new Parser(Constants.SampleInvoicePagesPdf)) {
            // Check if the document supports table extraction
            if (!parser.getFeatures().isTables()) {
                System.out.println("Document isn't supports tables extraction.");
                return;
            }
            // Create the layout of tables
            TemplateTableLayout layout = new TemplateTableLayout(
                    java.util.Arrays.asList(new Double[]{50.0, 95.0, 275.0, 415.0, 485.0, 545.0}),
                    java.util.Arrays.asList(new Double[]{325.0, 340.0, 365.0, 395.0}));
            // Create the options for table extraction
            PageTableAreaOptions options = new PageTableAreaOptions(layout);
            // Extract tables from the document.
            Iterable<PageTableArea> tables = parser.getTables(options);
            // Iterate over tables
            for (PageTableArea t : tables) {
                // Iterate over rows
                for (int row = 0; row < t.getRowCount(); row++) {
                    // Iterate over columns
                    for (int column = 0; column < t.getColumnCount(); column++) {
                        // Get the table cell
                        PageTableAreaCell cell = t.getCell(row, column);
                        if (cell != null) {
                            // Print the table cell text
                            System.out.print(cell.getText());
                            System.out.print(" | ");
                        }
                    }
                    System.out.println();
                }
                System.out.println();
            }
        }
        ```
     {{< /parser/code-parser >}}

############################# More ############################
more:
    enable: true
    title_left: "System Requirements"
    content_left: |
        GroupDocs.Parser for Java APIs are supported on all major platforms and operating systems. Before executing the code below, please make sure that you have the following prerequisites installed on your system.
        
        * Operating Systems: Microsoft Windows, Linux, MacOS
        * Development Environments: NetBeans, Intellij IDEA, Eclipse, etc.
        * Frameworks
        * Download the latest version of GroupDocs.Parser for Java from [Maven](https://repository.groupdocs.com/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs-parser)

    title_right: "Why Use GroupDocs.Parser for Java"
    content_right: |
        * Plain text extraction support from any supported documents    
        * Documents parsing via user-defined templates    
        * Fully support structured text extraction    
        * Text searching via keyword as well as regular expression    
        * Extract formatted text, metadata, images, containers, and attachments    
        * Extract table of contents for some supported document formats    
        * Parse form data from PDF documents    
        * Extract hyperlinks from the document   

############################# About Formats ############################
about_formats:
    enable: true

############################# More Formats ############################
more_formats:
    enable: true
    title: "Extract Tables From Other Document Formats"
    content: |
        Java documents parse & tables extraction API for file formats and images. Extract data for some of the popular file formats as stated below.

############################# Back to top ###############################
back_to_top:
    enable: true
---