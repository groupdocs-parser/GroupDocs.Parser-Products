<% configRef "..\\configs\\index\\index_python-net.yml" %>
<% include "..\\data\\platform_data.md" %>
---
############################# Static ############################
layout: "landing"
date: <% date "utcnow" %>
draft: false

lang: <% lower ( get "lang") %>
product: "Parser"
product_tag: "parser"
platform: "Python"
platform_tag: "python-net"

############################# Drop-down ############################
supported_platforms:
  items:
    # supported_platforms loop
    - title: ".NET"
      tag: "net"
    # supported_platforms loop
    - title: "Java"
      tag: "java"
    # supported_platforms loop
    - title: "Python"
      tag: "python-net"

############################# Head ############################
head_title: "<% "{index-content-python-net.head_title}" %>"
head_description: "<% "{index-content-python-net.head_description}" %>"

############################# Header ############################
title: "<% "{index-content-python-net.title}" %>"
description: "<% "{index-content-python-net.description}" %>"
words:
  for: "<% "{index-content.words_for}" %>"

actions:
  hidden: true # Hide version 0 is released
  main: "<% "{index-content-python-net.actions_main}" %>"
  main_link: "<% get "PackageUrl" %>"
  alt: "<% "{index-content.actions.alt}" %>"
  alt_link: "<% get "PricesUrl" %>"
  title: "<% "{index-content.actions.title}" %>"
  description: "<% "{index-content.actions.description}" %>"

release:
  enable: false
  title: "<% "{index-content.release_title}" %>"
  notes: "<% "{index-content.release_notes}" %>"
  downloads: "<% "{index-content.release_downloads}" %>"

code:
  title: "<% "{index-content-python-net.code_title}" %>"
  more: "<% "{index-content.code_more}" %>"
  more_link: "<% dict "products.python-net.more_link" %>"
  install: "pip install groupdocs-parser-net"
  content: |
    ```python {style=abap}  
    from groupdocs.parser import Parser

    # <% "{index-content-python-net.code_comment_1}" %>
    with Parser("sample.pdf") as parser:
        # <% "{index-content-python-net.code_comment_2}" %>
        text = parser.GetText()

        # <% "{index-content-python-net.code_comment_3}" %>
        print(text)
    ```

############################# Overview ############################
overview:
  enable: true
  title: "<% "{index-content.overview_title}" %>"
  description: "<% "{index-content-python-net.overview_description}" %>"
  features:
    # feature loop
    - title: "<% "{index-content-python-net.overview_feature_1.title}" %>"
      content: "<% "{index-content-python-net.overview_feature_1.description}" %>"

    # feature loop
    - title: "<% "{index-content-python-net.overview_feature_2.title}" %>"
      content: "<% "{index-content-python-net.overview_feature_2.description}" %>"

    # feature loop
    - title: "<% "{index-content-python-net.overview_feature_3.title}" %>"
      content: "<% "{index-content-python-net.overview_feature_3.description}" %>"

############################# Platforms ############################
platforms:
  enable: true
  title: "<% "{index-content.platforms.title}" %>"
  description: "<% "{index-content-python-net.platforms_description}" %>"
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
    - title: "VS Code"
      image: "vs_code"
    # platform loop
    - title: "ReSharper"
      image: "resharper"
    # platform loop
    - title: "macOS"
      image: "finder"
    # platform loop
    - title: "Linux"
      image: "linux"
    # platform loop
    - title: "NuGet"
      image: "nuget"

############################# File formats ############################
formats:
  enable: true
  title: "<% "{index-content.formats_title}" %>"
  description: |
    <% "{index-content-python-net.formats_description}" %>
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
  title: "<% "{index-content-python-net.features.title}" %>"
  description: "<% "{index-content-python-net.features.description}" %>"

  items:
    # feature loop
    - icon: "text"
      title: "<% "{index-content-python-net.features.feature_1.title}" %>"
      content: "<% "{index-content-python-net.features.feature_1.content}" %>"

    # feature loop
    - icon: "image"
      title: "<% "{index-content-python-net.features.feature_2.title}" %>"
      content: "<% "{index-content-python-net.features.feature_2.content}" %>"

    # feature loop
    - icon: "qr"
      title: "<% "{index-content-python-net.features.feature_3.title}" %>"
      content: "<% "{index-content-python-net.features.feature_3.content}" %>"

    # feature loop
    - icon: "email"
      title: "<% "{index-content-python-net.features.feature_4.title}" %>"
      content: "<% "{index-content-python-net.features.feature_4.content}" %>"

    # feature loop
    - icon: "table"
      title: "<% "{index-content-python-net.features.feature_5.title}" %>"
      content: "<% "{index-content-python-net.features.feature_5.content}" %>"

    # feature loop
    - icon: "hyperlink"
      title: "<% "{index-content-python-net.features.feature_6.title}" %>"
      content: "<% "{index-content-python-net.features.feature_6.content}" %>"

    # feature loop
    - icon: "pdf"
      title: "<% "{index-content-python-net.features.feature_7.title}" %>"
      content: "<% "{index-content-python-net.features.feature_7.content}" %>"

    # feature loop
    - icon: "template"
      title: "<% "{index-content-python-net.features.feature_8.title}" %>"
      content: "<% "{index-content-python-net.features.feature_8.content}" %>"

    # feature loop
    - icon: "search"
      title: "<% "{index-content-python-net.features.feature_9.title}" %>"
      content: "<% "{index-content-python-net.features.feature_9.content}" %>"


############################# Code samples ############################
code_samples:
  enable: true
  title: "<% "{index-content.code_samples.title}" %>"
  description: "<% "{index-content-python-net.code_samples_description}" %>"
  items:
    # code sample loop
    - title: "<% "{index-content-python-net.code_sample_1_title}" %>"
      content: |
        <% "{index-content-python-net.code_sample_1_content}" %>
        {{< landing/code title="<% "{index-content-python-net.code_sample_1.title}" %>">}}
        ```python {style=abap}
        from groupdocs.parser import Parser

        # <% "{index-content-python-net.code_sample_1.comment_1}" %>
        with Parser("sample.pdf") as parser:
            # <% "{index-content-python-net.code_sample_1.comment_3}" %>
            for area in parser.Search("Total Amount"):
                # <% "{index-content-python-net.code_sample_1.comment_3}" %>
                print(f"Page {area.PageIndex}, Rectangle: {area.Rectangle}")
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "<% "{index-content-python-net.code_sample_2_title}" %>"
      content: |
        <% "{index-content-python-net.code_sample_2_content}" %>
        {{< landing/code title="<% "{index-content-python-net.code_sample_2.title}" %>">}}
        ```python {style=abap}    
        from groupdocs.parser import Parser

        # <% "{index-content-python-net.code_sample_2.comment_1}" %>
        with Parser("sample.docx") as parser:
            # <% "{index-content-python-net.code_sample_2.comment_2}" %>
            images = parser.GetImages()

            # <% "{index-content-python-net.code_sample_2.comment_3}" %>
            index = 1
            for image in images:
                image.Save(f"image_{index}.png")
                index += 1
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "<% "{index-content-python-net.code_sample_3_title}" %>"
      content: |
        <% "{index-content-python-net.code_sample_3_content}" %>
        {{< landing/code title="<% "{index-content-python-net.code_sample_3.title}" %>">}}
        ```python {style=abap}    
        from groupdocs.parser import Parser

        # <% "{index-content-python-net.code_sample_3.comment_1}" %>
        with Parser("sample.pdf") as parser:
            # <% "{index-content-python-net.code_sample_3.comment_2}" %>
            metadata = parser.GetMetadata()

            # <% "{index-content-python-net.code_sample_3.comment_3}" %>
            for item in metadata:
                print(f"{item.Name}: {item.Value}")
        ```
        {{< /landing/code >}}
---
