


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:16
draft: false
lang: fa
format: Epub
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "خواندن بارکدها از فایل‌های EPUB در برنامه‌های Java"
head_description: "با GroupDocs.Parser، داده‌های بارکد را از اسناد EPUB با استفاده از Java بدون نیاز به ابزارهای خارجی استخراج کنید."

############################# Header ############################
title: "خواندن بارکدها از EPUB با استفاده از Java" 
description: "محتوای بارکد را از فایل‌های PDF، Word، Excel و تصاویر با استفاده از GroupDocs.Parser در برنامه‌های Java خود استخراج کنید."
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "دانلود نسخه آزمایشی رایگان"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "بررسی اجمالی API GroupDocs.Parser for Java"
    link: "/parser/java/"
    link_title: "بیشتر بدانید"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) یک راه‌حل جامع برای تجزیه اسناد در Java ارائه می‌دهد. این امکان را برای توسعه‌دهندگان فراهم می‌کند تا بارکدها، متن، تصاویر و اطلاعات ساختار یافته را از فرمت‌های مختلف فایل مانند PDF، Word، Excel، PowerPoint و دیگر فرمت‌ها استخراج کنند—بدون نیاز به کتابخانه‌های خارجی.

############################# Steps ############################
steps:
    enable: true
    title: "چگونه بارکدها را از Epub در Java بخوانیم"
    content: |
      با [GroupDocs.Parser](/parser/java/)، توسعه‌دهندگان Java می‌توانند بارکدها را از اسناد EPUB در چند مرحله استخراج کنند:
      
      1. سند EPUB را با استفاده از Parser بارگذاری کنید.
      2. بررسی کنید که آیا سند از استخراج بارکد پشتیبانی می‌کند.
      3. از API برای بازیابی داده‌های بارکد استفاده کنید.
      4. نتایج بارکد را مرور کرده و طبق نیاز خود اعمال کنید.
   
    code:
      platform: "net"
      copy_title: "کپی"
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
        copy_tip: "برای کپی کلیک کنید"
        copy_done: "کپی شد"
      links:
        #  loop
        - title: "نمونه‌های بیشتر"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java/"
        #  loop
        - title: "مستندات"
          link: "https://docs.groupdocs.com/parser/java/"
          
      content: |
        ```java {style=abap}
        // یک سند حاوی بارکدها را با استفاده از Parser باز کنید
        try (Parser parser = new Parser("input.epub"))
        {
            // پشتیبانی بارکد برای فایل را بررسی کنید
            if (!parser.getFeatures().isBarcodes())
            {
                System.out.println("مدیریت فرمت‌های فایل غیرمعتبر");
                return;
            }

            // داده‌های بارکد را استخراج و استفاده کنید
            Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();
            for(PageBarcodeArea barcode : barcodes)
            {
                System.out.println("Page: " + barcode.getPage().getIndex());
                System.out.println("Value: " + barcode.getValue());
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "قابلیت‌های بیشتر تجزیه"
  description: "GroupDocs.Parser فراتر از استخراج بارکد می‌رود و همچنین امکان استخراج متن ساده، تصاویر و عناصر ساختاریافته را برای پشتیبانی از جریان‌های کاری مبتنی بر داده فراهم می‌کند."
  image: "/img/parser/features_extract-barcode.webp" # 500x500 px
  image_description: "قابلیت‌های استخراج بارکد و داده"
  features:
    # feature loop
    - title: "پشتیبانی از فرمت‌های وسیع بارکد"
      content: "شناسایی فرمت‌های استاندارد بارکد از جمله QR Code، Code 39، Data Matrix، EAN، Aztec و دیگران."

    # feature loop
    - title: "خواندن بارکدها از منابع مختلف"
      content: "استخراج اطلاعات بارکد از اسناد Office، PDF و فایل‌های تصویری مانند PNG، JPG و BMP."

    # feature loop
    - title: "تنظیمات سفارشی خواندن بارکد"
      content: "تنظیم دقیق استخراج بارکد با گزینه‌هایی برای هدف قرار دادن مناطق خاص و فایل‌های چند صفحه‌ای."
      
  code_samples:
    # code sample loop
    - title: "مثال: استخراج بارکدها از PDF با گزینه‌ها"
      content: |
        این نمونه استخراج بارکد را از یک سند PDF با استفاده از تنظیمات سفارشی نشان می‌دهد.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  تجزیه‌گر را با سند PDF راه‌اندازی کنید
        try (Parser parser = new Parser("input.pdf"))
        {
            // اطمینان حاصل کنید که سند از خواندن بارکد پشتیبانی می‌کند
            if (!parser.getFeatures().isBarcodes())
            {
                return;
            }

            // اعمال فیلتر با گزینه‌های بارکد
            BarcodeOptions options = new BarcodeOptions(QualityMode.Low, QualityMode.Low, "QR");

            // بارکدها را با استفاده از تجزیه‌گر استخراج کنید
            Iterable<PageBarcodeArea> barcodes = parser.getBarcodes(options);

            // به هر نتیجه بارکد رسیدگی کنید
            for (PageBarcodeArea barcode : barcodes)
            {
                System.out.println("Page: " + String.valueOf(barcode.getPage().getIndex()));
                System.out.println("Value: " + barcode.getValue());
            }
        }
        ```
        {{< /landing/code >}}


############################# Actions ############################

actions:
  enable: true
  title: "آماده شروع هستید؟"
  description: "امکانات GroupDocs.Parser را به صورت رایگان امتحان کنید یا درخواست مجوز دهید"
  items:
    #  loop
    - title: "دانلود Maven"
      link: "https://releases.groupdocs.com/parser/java/"
      color: "red"
        #  loop
    - title: "مجوزدهی"
      link: "https://purchase.groupdocs.com/pricing/parser/java/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "فرمت‌های فایل پشتیبانی‌شده برای خواندن بارکد"
    exclude: "EPUB"
    description: "GroupDocs.Parser می‌تواند بارکدها را از انواع مستندات و تصاویر بخواند. در زیر برخی از فرمت‌های معمولی پشتیبانی شده آورده شده‌اند."
    items: 
        # format loop 1
        - name: "تحلیل PDF"
          format: "PDF"
          link: "/parser/java/extract-barcode/pdf/"
          description: "(فرمت سند قابل حمل)"
          
        # format loop 2
        - name: "تحلیل DOCX"
          format: "DOCX"
          link: "/parser/java/extract-barcode/docx/"
          description: "(سند Word Office 2007+)"
          
        # format loop 3
        - name: "تحلیل PPTX"
          format: "PPTX"
          link: "/parser/java/extract-barcode/pptx/"
          description: "(فرمت ارائه Open XML)"
          
        # format loop 4
        - name: "تحلیل XLSX"
          format: "XLSX"
          link: "/parser/java/extract-barcode/xlsx/"
          description: "(دفتر کار Open XML)"
          
        # format loop 5
        - name: "تحلیل ODT"
          format: "ODT"
          link: "/parser/java/extract-barcode/odt/"
          description: "(سند متنی OpenDocument)"
          
        # format loop 6
        - name: "تحلیل ODS"
          format: "ODS"
          link: "/parser/java/extract-barcode/ods/"
          description: "(برگه محاسباتی OpenDocument)"
          
        # format loop 7
        - name: "تحلیل ODP"
          format: "ODP"
          link: "/parser/java/extract-barcode/odp/"
          description: "(ارائه OpenDocument)"
          
        # format loop 8
        - name: "تحلیل EPUB"
          format: "EPUB"
          link: "/parser/java/extract-barcode/epub/"
          description: "(فایل کتاب الکترونیکی Open)"
          
        # format loop 9
        - name: "تحلیل FB2"
          format: "FB2"
          link: "/parser/java/extract-barcode/fb2/"
          description: "(کتاب الکترونیکی FictionBook)"
         
          

---