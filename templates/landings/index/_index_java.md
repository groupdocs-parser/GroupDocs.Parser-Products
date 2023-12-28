---
############################# Static ############################
layout: "landing"
date: <% date "utcnow" %>
draft: false
#operation: <% get "Operation" %>
#parsertype: <% get "Parsertype" %>
#fileformat: <% get "Fileformat" %>
#productName: <% get "ProductName" %>
lang: <% lower ( get "lang") %>
#productCode: <% lower ( get "ProductCode") %>
#otherformats: <% get "OtherFormats" %>
#breadcrumb: Put <% get "Parsertype" %> parser on <% get "Fileformat" %> for <% get "ProgLang" %>
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "<% "{index-content.head_title}" %>"
head_description: "<% "{index-content.head_description}" %>"

############################# Header ############################
title: "<% "{index-content.title_1}" %><br><% "{index-content.java.title_2}" %>"
description: "<% "{index-content.description}" %>"
words:
  for: "<% "{index-content.words_for}" %>"

actions:
  main: "<% "{index-content.java.actions_main}" %>"
  main_link: "<% dict "products.java.main_link" %>"
  alt: "<% "{index-content.actions_alt}" %>"
  alt_link: "<% dict "products.java.alt_link" %>"
  title: "<% "{index-content.actions_title}" %>"
  description: "<% "{index-content.actions_description}" %>"

release:
  title: "<% "{index-content.release_title}" %>"
  notes: "<% "{index-content.release_notes}" %>"
  downloads: "<% "{index-content.release_downloads}" %>"

code:
  title: "<% "{index-content.java.code.title}" %>"
  more: "<% "{index-content.code_more}" %>"
  more_link: "<% dict "products.java.more_link" %>"
  install: |
    <dependency>
      <groupId>com.groupdocs</groupId>
      <artifactId>groupdocs-parser</artifactId>
      <version>{0}</version>
    </dependency>
  content: |
    ```java {style=abap}  
    // <% "{index-content.java.code.instance}" %>
    try (Parser parser = new Parser(filePath)) {
        // <% "{index-content.java.code.extract}" %>
        try (TextReader reader = parser.getText()) {
            // <% "{index-content.java.code.print_1}" %>
            // <% "{index-content.java.code.print_2}" %>
            if (reader == null) {
              System.out.println("<% "{index-content.java.code.not_supported}" %>");
            }
            else {
              System.out.println(reader.readToEnd()); 
            }
        }
    }    
    ```

############################# Overview ############################
overview:
  enable: true
  title: "<% "{index-content.overview_title}" %>"
  description: "<% "{index-content.java.overview_description}" %>"
  features:
    # feature loop
    - title: "<% "{index-content.java.overview_feature_1.title}" %>"
      content: "<% "{index-content.java.overview_feature_1.description}" %>"

    # feature loop
    - title: "<% "{index-content.java.overview_feature_2.title}" %>"
      content: "<% "{index-content.java.overview_feature_2.description}" %>"

    # feature loop
    - title: "<% "{index-content.java.overview_feature_3.title}" %>"
      content: "<% "{index-content.java.overview_feature_3.description}" %>"

############################# Platforms ############################
platforms:
  enable: true
  title: "<% "{index-content.platforms_title}" %>"
  description: "<% "{index-content.java.platforms_description}" %>"
  items:
    # platform loop
    - title: "Amazon"
      image: "amazon"
    # platform loop
    - title: "Docker"
      image: "docker"
    # platform loop
    - title: "Azure"
      image: "azure"
    # platform loop
    - title: "Eclipse"
      image: "eclipse"
    # platform loop
    - title: "IntelliJ"
      image: "intellij"
    # platform loop
    - title: "Windows"
      image: "windows"
    # platform loop
    - title: "Linux"
      image: "linux"
    # platform loop
    - title: "Maven"
      image: "maven"

############################# File formats ############################
formats:
  enable: true
  title: "<% "{index-content.formats_title}" %>"
  description: |
    <% "{index-content.java.formats_description}" %>
  groups:
    # group loop
    - color: "green"
      content: |
        ### <% "{index-content.formats_groups.title_1}" %>
        * **Word:**  DOCX, DOC, DOCM, DOT, DOTX, DOTM, RTF
        * **Excel:** XLSX, XLS, XLSM, XLSB, XLTM, XLT, XLTM, XLTX, XLAM, SXC, SpreadsheetML
        * **PowerPoint:** PPT, PPTX, PPS, PPSX, PPSM, POT, POTM, POTX, PPTM
    # group loop
    - color: "blue"
      content: |
        ### <% "{index-content.formats_groups.title_2}" %>
        * **<% "{index-content.formats_groups.format_portable}" %>:** PDF
        * **<% "{index-content.formats_groups.format_images}" %>:** JPG, BMP, PNG, TIFF, GIF, DICOM, WEBP
        * **<% "{index-content.formats_groups.format_other_office}" %>:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### <% "{index-content.formats_groups.title_3}" %>
        * **<% "{index-content.formats_groups.format_web}" %>:** HTML, MHTML
        * **<% "{index-content.formats_groups.format_archives}" %>:** ZIP, TAR, 7Z
        * **<% "{index-content.formats_groups.format_ebooks}" %>:** CHM, EPUB, FB2, MOBI

############################# Features ############################
features:
  enable: true
  title: "<% "{index-content.java.features.title}" %>"
  description: "<% "{index-content.java.features.description}" %>"

  items:
    # feature loop
    - icon: "text"
      title: "<% "{index-content.net.features.feature_1.title}" %>"
      content: "<% "{index-content.net.features.feature_1.content}" %>"

    # feature loop
    - icon: "image"
      title: "<% "{index-content.net.features.feature_2.title}" %>"
      content: "<% "{index-content.net.features.feature_2.content}" %>"

    # feature loop
    - icon: "qr"
      title: "<% "{index-content.net.features.feature_3.title}" %>"
      content: "<% "{index-content.net.features.feature_3.content}" %>"

    # feature loop
    - icon: "email"
      title: "<% "{index-content.net.features.feature_4.title}" %>"
      content: "<% "{index-content.net.features.feature_4.content}" %>"

    # feature loop
    - icon: "table"
      title: "<% "{index-content.net.features.feature_5.title}" %>"
      content: "<% "{index-content.net.features.feature_5.content}" %>"

    # feature loop
    - icon: "hyperlink"
      title: "<% "{index-content.net.features.feature_6.title}" %>"
      content: "<% "{index-content.net.features.feature_6.content}" %>"

    # feature loop
    - icon: "pdf"
      title: "<% "{index-content.net.features.feature_7.title}" %>"
      content: "<% "{index-content.net.features.feature_7.content}" %>"

    # feature loop
    - icon: "template"
      title: "<% "{index-content.net.features.feature_8.title}" %>"
      content: "<% "{index-content.net.features.feature_8.content}" %>"

    # feature loop
    - icon: "search"
      title: "<% "{index-content.net.features.feature_9.title}" %>"
      content: "<% "{index-content.net.features.feature_9.content}" %>"

############################# Code samples ############################
code_samples:
  enable: true
  title: "<% "{index-content.net.code-samples.title}" %>"
  description: "<% "{index-content.java.code-samples.description}" %>"
  items:
    # code sample loop
    - title: "<% "{index-content.java.code-samples.sample1.header}" %>"
      content: |
        <% "{index-content.java.code-samples.sample1.description}" %>
        {{< landing/code title="<% "{index-content.java.code-samples.sample1.title}" %>">}}
        ```java {style=abap}
        // <% "{index-content.java.code-samples.sample1.code.instance}" %>
        try (Parser parser = new Parser(Constants.SampleImagesPdf)) {
            // <% "{index-content.java.code-samples.sample1.code.extract}" %>
            Iterable<PageImageArea> images = parser.getImages();
            // <% "{index-content.java.code-samples.sample1.code.check_null}" %>
            if (images == null) {
                System.out.println("<% "{index-content.java.code-samples.sample1.code.not_supported}" %>");
                return;
            }
            // <% "{index-content.java.code-samples.sample1.code.iterate}" %>
            for (PageImageArea image : images) {
                // <% "{index-content.java.code-samples.sample1.code.print}" %>
                System.out.println(String.format("Page: %d, R: %s, Type: %s", image.getPage().getIndex(), image.getRectangle(), image.getFileType()));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "<% "{index-content.java.code-samples.sample2.header}" %>"
      content: |
        <% "{index-content.java.code-samples.sample2.description}" %>
        {{< landing/code title="<% "{index-content.java.code-samples.sample2.title}" %>">}}
        ```java {style=abap}   
        // <% "{index-content.java.code-samples.sample2.code.instance}" %>
        try (Parser parser = new Parser(Constants.SamplePdfWithBarcodes)) {
            // // <% "{index-content.java.code-samples.sample2.code.check}" %>
            if (!parser.getFeatures().isBarcodes()) {
                System.out.println("<% "{index-content.java.code-samples.sample2.code.not_supported}" %>");
                return;
            }

            // <% "{index-content.java.code-samples.sample2.code.scan}" %>
            Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();

            // <% "{index-content.java.code-samples.sample2.code.iterate}" %>
            for (PageBarcodeArea barcode : barcodes) {
                // <% "{index-content.java.code-samples.sample2.code.print_page_index}" %>
                System.out.println("Page: " + barcode.getPage().getIndex());
                // <% "{index-content.java.code-samples.sample2.code.print_value}" %>
                System.out.println("Value: " + barcode.getValue());
            }
        }
        ```
        {{< /landing/code >}}

---
