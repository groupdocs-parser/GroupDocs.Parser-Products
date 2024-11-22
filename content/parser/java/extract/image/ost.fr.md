---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:09
draft: false
otherformats: 

############################# Head ############################
head_title: "{head.title}"
head_description: "{head.description}"

############################# Header ############################
title: "{header.title}"
description: "{header.description}"
bg_image: "https://cms.admin.containerize.com/templates/aspose/App_Themes/V3/images/bg/header1.png"
bg_overlay: false
button:
    enable: true
    icon: "fas fa-arrow-down"
    label: "{header.button_label}"
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
              text: "{submenu.content_middle.button_text_1}"

            # button loop
            - link: "https://github.com/groupdocs-parser"
              text: "{submenu.content_middle.button_text_2}"

            # button loop
            - link: "https://products.groupdocs.app/parser/family"
              text: "{submenu.content_middle.button_text_3}"

            # button loop
            - link: "https://purchase.groupdocs.com/pricing/parser/java"
              text: "{submenu.content_middle.button_text_4}"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/java"
        link_buy: "https://purchase.groupdocs.com"

############################# About ############################
about:
    enable: true
    title: "{about.title}"
    content: |
        {about.h1}
        
        {about.h2}

############################# Steps ############################
steps:
    enable: true
    title_left: "{steps.title_left}"
    content_left: |
        {steps.content_left.description}
        
        * {steps.content_left.step_1}
        * {steps.content_left.step_2}
        * {steps.content_left.step_3}
        * {steps.content_left.step_4}

    title_right: "{steps.title_right}"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/java/extract-images-from-document/">{steps.content_right.step_1}</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-images-from-document-page/">{steps.content_right.step_2}</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-images-from-document-page-area/">{steps.content_right.step_3}</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-images-to-files/">{steps.content_right.step_4}</a>
         
    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="{steps.title_code}">}}

        ```java    
        // {steps.code.header}
        // {steps.code.instance}
        try (Parser parser = new Parser(Constants.SampleImagesPdf)) {
            // {steps.code.extract}
            Iterable<PageImageArea> images = parser.getImages();
            // {steps.code.check_null}
            if (images == null) {
                System.out.println("{steps.code.not_supported}");
                return;
            }
            // {steps.code.iterate}
            for (PageImageArea image : images) {
                // {steps.code.print}
                System.out.println(String.format("Page: %d, R: %s, Type: %s", image.getPage().getIndex(), image.getRectangle(), image.getFileType()));
            }
        }
        ```
     {{< /parser/code-parser >}}

############################# More ############################
more:
    enable: true
    title_left: "{more.title_left}"
    content_left: |
        {more.content_left.description}
        
        * {more.content_left.step_1}
        * {more.content_left.step_2}
        * {more.content_left.step_3}
        * {more.content_left.step_4}

    title_right: "{more.title_right}"
    content_right: |
        * {more.content_right.p1}    
        * {more.content_right.p2}    
        * {more.content_right.p3}    
        * {more.content_right.p4}    
        * {more.content_right.p5}    
        * {more.content_right.p6}    
        * {more.content_right.p7}    
        * {more.content_right.p8}   

############################# Demos ############################
demos:
    enable: true
    title: "{demos.title}"
    content: |
       {demos.h1}
       {demos.h2}
        
############################# About Formats ############################
about_formats:
    enable: true

############################# More Formats ############################
more_formats:
    enable: true
    title: "{more_formats.title}"
    content: |
        {more_formats.content}

############################# Back to top ###############################
back_to_top:
    enable: true
---