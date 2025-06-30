


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:30
draft: false
lang: fa
format: Pptx
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "استخراج تصاویر از فایل‌های PPTX در برنامه‌های Java"
head_description: "با GroupDocs.Parser، می‌توانید تصاویر را به آسانی از فایل‌های PPTX در Java استخراج کنید، بدون نیاز به ابزارهای شخص ثالث."

############################# Header ############################
title: "استخراج تصاویر از PPTX با استفاده از Java" 
description: "تصاویر جاسازی شده در فایل‌هایی مانند PDF، Word، Excel و غیره را با استفاده از GroupDocs.Parser در محیط توسعه Java خود بازیابی کنید."
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
    title: "GroupDocs.Parser for Java چیست؟"
    link: "/parser/java/"
    link_title: "بیشتر بدانید"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) یک API قدرتمند و پر ویژگی برای پارس کردن فایل است که برای توسعه‌دهندگان Java بهینه‌سازی شده است. این امکان را فراهم می‌کند تا تصاویر، متن، پیوندها و عناصر ساختاری را از انواع فرمت‌های فایل شامل DOCX، XLSX، PDF، PNG، JPG و بسیاری دیگر استخراج کنید — بدون نیاز به کتابخانه‌ها یا برنامه‌های خارجی.

############################# Steps ############################
steps:
    enable: true
    title: "چگونه تصاویر را از Pptx در Java استخراج کنیم"
    content: |
      این مراحل را دنبال کنید تا تصاویر را از مستندات PPTX با استفاده از [GroupDocs.Parser](/parser/java/) در برنامه Java خود استخراج کنید:
      
      1. یک نمونه Parser ایجاد کرده و فایل PPTX را بارگذاری کنید.
      2. داده‌های تصویر را از سند بارگذاری‌شده استخراج کنید.
      3. تصاویر استخراج‌شده را به دلخواه استفاده یا صادر کنید.
   
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
        // نصب کننده را مقداردهی اولیه کرده و سند را با تصاویر با استفاده از Parser بارگذاری کنید.
        try (Parser parser = new Parser("input.pptx"))
        {
            // همه عناصر تصویری جاسازی شده در سند را جمع‌آوری کنید.
            Iterable<PageImageArea> images = parser.getImages();

            // پردازش را در صورت عدم وجود تصاویر در سند نادیده بگیرید.
            if (images == null) {
                return;
            }

            // هر تصویر را به دلخواه پردازش کنید.
            for (PageImageArea image : images) {
                System.out.println(String.format("Page: %d, R: %s, Type: %s", image.getPage().getIndex(), 
                    image.getRectangle(), image.getFileType()));
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "توانایی‌های بیشتر پارس کردن مستندات"
  description: "علاوه بر استخراج تصویر، GroupDocs.Parser این امکان را به شما می‌دهد تا محتواهای خام مانند متن، پیوندها، متادیتا و داده‌های ساختاری را برای پردازش و تحلیل استخراج کنید."
  image: "/img/parser/features_extract-image.webp" # 500x500 px
  image_description: "استخراج تصاویر و محتوا از مستندات"
  features:
    # feature loop
    - title: "همکاری با انواع مختلف فرمت‌ها"
      content: "استخراج تصاویر از انواع مختلف سندها از جمله PDF، DOCX، PPTX، XLSX و فرمت‌های تصویری مانند PNG، JPEG و GIF."

    # feature loop
    - title: "حفظ وضوح و کیفیت تصویر"
      content: "تمام تصاویر استخراج‌شده وضوح و نوع فایل اصلی خود را حفظ می‌کنند تا کیفیت و قابلیت استفاده پایدار بماند."

    # feature loop
    - title: "گزینه‌های پیکربندی انعطاف‌پذیر"
      content: "فرآیند استخراج تصویر را با فیلتر کردن تصاویر بر اساس نوع، اندازه، ایندکس صفحه یا فرمت فایل سفارشی کنید."
      
  code_samples:
    # code sample loop
    - title: "استخراج و ذخیره تصاویر از فایل‌های PDF"
      content: |
        این مثال نشان می‌دهد که چگونه می‌توان از یک سند PDF تصاویر را استخراج کرده و آن‌ها را به صورت جداگانه بر روی دستگاه خود ذخیره کرد.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  از Parser برای باز کردن فایل PDF استفاده کنید.
        try (Parser parser = new Parser("input.pdf"))
        {
            // تصاویر را از محتوای سند بگیرید.
            Iterable<PageImageArea> images = parser.getImages();

            // پارامترهای خروجی مانند فرمت (برای مثال، JPEG یا PNG) را تعیین کنید.
            ImageOptions options = new ImageOptions(ImageFormat.Png);

            // تصاویر استخراج‌شده را در یک دایرکتوری محلی ذخیره کنید.
            int imageNumber = 0;
            for (PageImageArea image : images)
            {
                image.save(Constants.getOutputFilePath(String.format("%d.png", imageNumber)), options);
                imageNumber++;
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
    title: "انواع فایل‌های پشتیبانی‌شده برای استخراج تصویر"
    exclude: "PPTX"
    description: "GroupDocs.Parser استخراج تصویر را در انواع مختلف مستندات و تصاویر پشتیبانی می‌کند. فرمت‌های رایج پشتیبانی‌شده در زیر را بررسی کنید."
    items: 
        # format loop 1
        - name: "تحلیل PDF"
          format: "PDF"
          link: "/parser/java/extract-image/pdf/"
          description: "(فرمت سند قابل حمل)"
          
        # format loop 2
        - name: "تحلیل DOCX"
          format: "DOCX"
          link: "/parser/java/extract-image/docx/"
          description: "(سند Word Office 2007+)"
          
        # format loop 3
        - name: "تحلیل PPTX"
          format: "PPTX"
          link: "/parser/java/extract-image/pptx/"
          description: "(فرمت ارائه Open XML)"
          
        # format loop 4
        - name: "تحلیل XLSX"
          format: "XLSX"
          link: "/parser/java/extract-image/xlsx/"
          description: "(دفتر کار Open XML)"
          
        # format loop 5
        - name: "تحلیل ODT"
          format: "ODT"
          link: "/parser/java/extract-image/odt/"
          description: "(سند متنی OpenDocument)"
          
        # format loop 6
        - name: "تحلیل ODS"
          format: "ODS"
          link: "/parser/java/extract-image/ods/"
          description: "(برگه محاسباتی OpenDocument)"
          
        # format loop 7
        - name: "تحلیل ODP"
          format: "ODP"
          link: "/parser/java/extract-image/odp/"
          description: "(ارائه OpenDocument)"
          
        # format loop 8
        - name: "تحلیل EPUB"
          format: "EPUB"
          link: "/parser/java/extract-image/epub/"
          description: "(فایل کتاب الکترونیکی Open)"
          
        # format loop 9
        - name: "تحلیل FB2"
          format: "FB2"
          link: "/parser/java/extract-image/fb2/"
          description: "(کتاب الکترونیکی FictionBook)"
         
          

---