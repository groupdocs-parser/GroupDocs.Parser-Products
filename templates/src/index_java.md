<% configRef "..\\configs\\index\\index_java.yml" %>
<% include "..\\data\\platform_data.md" %>
---
############################# Static ############################
layout: "landing"
date: <% date "utcnow" %>
draft: false

lang: <% lower ( get "lang") %>
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Drop-down ############################
supported_platforms:
  items:
    # supported_platforms loop
    - title: ".NET"
      tag: "net"
    # supported_platforms loop
    - title: "Java"
      tag: "java"

############################# Head ############################
head_title: "<% "{index-content-java.head_title}" %>"
head_description: "<% "{index-content-java.head_description}" %>"

############################# Header ############################
title: "<% "{index-content-java.title}" %>"
description: "<% "{index-content-java.description}" %>"
words:
  for: "<% "{index-content.words_for}" %>"

actions:
  main: "<% "{index-content-java.actions_main}" %>"
  main_link: "<% get "PackageUrl" %>"
  alt: "<% "{index-content.actions.alt}" %>"
  alt_link: "<% get "PricesUrl" %>"
  title: "<% "{index-content.actions.title}" %>"
  description: "<% "{index-content.actions.description}" %>"

release:
  title: "<% "{index-content.release_title}" %>"
  notes: "<% "{index-content.release_notes}" %>"
  downloads: "<% "{index-content.release_downloads}" %>"

code:
  title: "<% "{index-content-java.code_title}" %>"
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
    // <% "{index-content-java.code_comment_1}" %>
    try (Parser parser = new Parser("source.pdf"))
    {
        // <% "{index-content-java.code_comment_2}" %>
        try (TextReader reader = parser.getText())
        {
            // <% "{index-content-java.code_comment_3}" %>
            System.out.println(reader == null 
                ? "" 
                : reader.readToEnd());
        }
    }
    ```

############################# Overview ############################
overview:
  enable: true
  title: "<% "{index-content.overview_title}" %>"
  description: "<% "{index-content-java.overview_description}" %>"
  features:
    # feature loop
    - title: "<% "{index-content-java.overview_feature_1.title}" %>"
      content: "<% "{index-content-java.overview_feature_1.description}" %>"

    # feature loop
    - title: "<% "{index-content-java.overview_feature_2.title}" %>"
      content: "<% "{index-content-java.overview_feature_2.description}" %>"

    # feature loop
    - title: "<% "{index-content-java.overview_feature_3.title}" %>"
      content: "<% "{index-content-java.overview_feature_3.description}" %>"

############################# Platforms ############################
platforms:
  enable: true
  title: "<% "{index-content.platforms.title}" %>"
  description: "<% "{index-content-java.platforms_description}" %>"
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
    <% "{index-content-net.formats_description}" %>
  groups:
    # group loop
    - color: "green"
      content: |
        ### <% "{index-content.formats_groups.title_1}" %>
        * **Word:** DOCX, DOC, DOCM, DOT, DOTX, DOTM, RTF
        * **Excel:** XLSX, XLS, XLSM, XLSB, XLTM, XLT, XLTM, XLTX, XLAM, SXC, SpreadsheetML
        * **PowerPoint:** PPT, PPTX, PPS, PPSX, PPSM, POT, POTM, POTX, PPTM
    # group loop
    - color: "blue"
      content: |
        ### <% "{index-content.formats_groups.title_2}" %>
        * **<% "{index-content.formats_groups.format_portable}" %>:** PDF 
        * **<% "{index-content.formats_groups.format_images}" %>:** JPG, BMP, PNG, TIFF, GIF
        * **<% "{index-content.formats_groups.format_other_office}" %>:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### <% "{index-content.formats_groups.title_3}" %>
        * **<% "{index-content.formats_groups.format_other_web}" %>:** HTML, MHTML 
        * **<% "{index-content.formats_groups.format_other_archives}" %>:** ZIP, TAR, 7Z 
        * **<% "{index-content.formats_groups.format_other_ebooks}" %>:** CHM, EPUB, FB2, MOBI 
        
        

############################# Features ############################
features:
  enable: true
  title: "<% "{index-content-java.features.title}" %>"
  description: "<% "{index-content-java.features.description}" %>"

  items:
    # feature loop
    - icon: "text"
      title: "<% "{index-content-net.features.feature_1.title}" %>"
      content: "<% "{index-content-net.features.feature_1.content}" %>"

    # feature loop
    - icon: "image"
      title: "<% "{index-content-net.features.feature_2.title}" %>"
      content: "<% "{index-content-net.features.feature_2.content}" %>"

    # feature loop
    - icon: "qr"
      title: "<% "{index-content-net.features.feature_3.title}" %>"
      content: "<% "{index-content-net.features.feature_3.content}" %>"

    # feature loop
    - icon: "email"
      title: "<% "{index-content-net.features.feature_4.title}" %>"
      content: "<% "{index-content-net.features.feature_4.content}" %>"

    # feature loop
    - icon: "table"
      title: "<% "{index-content-net.features.feature_5.title}" %>"
      content: "<% "{index-content-net.features.feature_5.content}" %>"

    # feature loop
    - icon: "hyperlink"
      title: "<% "{index-content-net.features.feature_6.title}" %>"
      content: "<% "{index-content-net.features.feature_6.content}" %>"

    # feature loop
    - icon: "pdf"
      title: "<% "{index-content-net.features.feature_7.title}" %>"
      content: "<% "{index-content-net.features.feature_7.content}" %>"

    # feature loop
    - icon: "template"
      title: "<% "{index-content-net.features.feature_8.title}" %>"
      content: "<% "{index-content-net.features.feature_8.content}" %>"

    # feature loop
    - icon: "search"
      title: "<% "{index-content-net.features.feature_9.title}" %>"
      content: "<% "{index-content-net.features.feature_9.content}" %>"


############################# Code samples ############################
code_samples:
  enable: true
  title: "<% "{index-content.code_samples.title}" %>"
  description: "<% "{index-content-java.code_samples_description}" %>"
  items:
    # code sample loop
    - title: "<% "{index-content-java.code_title_sample_1}" %>"
      content: |
        <% "{index-content-java.code_samples_sample_1_content}" %>
        {{< landing/code title="<% "{index-content.code_samples.sample_1.code_title}" %>">}}
        ```java {style=abap}
        // <% "{index-content.code_samples.sample_1.comment_1}" %>
        try (Parser parser = new Parser("source.pdf"))
        {
            // <% "{index-content.code_samples.sample_1.comment_2}" %>
            Iterable<PageImageArea> images = parser.getImages();

            // <% "{index-content.code_samples.sample_1.comment_3}" %>
            if (images == null) {
                return;
            }

            // <% "{index-content.code_samples.sample_1.comment_4}" %>
            for (PageImageArea image : images) {
                // <% "{index-content.code_samples.sample_1.comment_5}" %>
                System.out.println(String.format("Page: %d, R: %s, Type: %s", image.getPage().getIndex(), image.getRectangle(), image.getFileType()));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "<% "{index-content-java.code_title_sample_2}" %>"
      content: |
        <% "{index-content-java.code_samples_sample_2_content}" %>
        {{< landing/code title="<% "{index-content.code_samples.sample_2.code_title}" %>">}}
        ```java {style=abap}   
        // <% "{index-content.code_samples.sample_2.comment_1}" %>
        try (Parser parser = new Parser("source.jpg")){

            // <% "{index-content.code_samples.sample_2.comment_2}" %>
            if (!parser.getFeatures().isBarcodes()) {

                // <% "{index-content.code_samples.sample_2.comment_3}" %>
                Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();

                // <% "{index-content.code_samples.sample_2.comment_4}" %>
                for (PageBarcodeArea barcode : barcodes) {
                    // <% "{index-content.code_samples.sample_2.comment_5}" %>
                    System.out.println("Page: " + barcode.getPage().getIndex());
                    // <% "{index-content.code_samples.sample_2.comment_6}" %>
                    System.out.println("Value: " + barcode.getValue());
                }
            }
        }
        ```
        {{< /landing/code >}}

---
