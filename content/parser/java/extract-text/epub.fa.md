


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:45
draft: false
lang: fa
format: Epub
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "استخراج متن از فایل‌های EPUB در برنامه‌های Java"
head_description: "با استفاده از GroupDocs.Parser می‌توانید محتوای متن غیرساختاری یا ساختاری را از اسناد EPUB در Java استخراج کنید، بدون نیاز به وابستگی‌های خارجی."

############################# Header ############################
title: "استخراج متن از EPUB با استفاده از Java" 
description: "به‌خوبی متن‌های قابل خواندن یا ساختاری را از فایل‌هایی مانند PDF، Word، Excel و غیره با استفاده از GroupDocs.Parser در پروژه‌های توسعه Java خود استخراج کنید."
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "بارگیری نسخه رایگان"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "معرفی API GroupDocs.Parser for Java"
    link: "/parser/java/"
    link_title: "بیشتر بدانید"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) یک تجزیه‌کننده مستندات قوی و مقیاس‌پذیر است که برای توسعه‌دهندگان Java طراحی شده است. این ابزار قابلیت‌هایی برای استخراج دقیق متن، جدول‌ها، تصاویر و مؤلفه‌های ساختاری از فرمت‌های مختلف از جمله PDF، DOCX، XLSX، PPTX و دیگر فرمت‌ها، بدون نیاز به ابزارهای خارجی ارائه می‌دهد.

############################# Steps ############################
steps:
    enable: true
    title: "چگونه متن را از Epub با استفاده از Java بازیابی کنیم"
    content: |
      برای استخراج متن از فایل‌های EPUB با استفاده از [GroupDocs.Parser](/parser/java/) در پروژه Java خود مراحل زیر را دنبال کنید:
      
      1. فایل EPUB را با استفاده از کلاس Parser بارگذاری کنید.
      2. استخراج متن را از محتوای فایل انجام دهید.
      3. بررسی کنید که آیا متن با موفقیت بازیابی شده است یا خیر.
      4. از داده‌های متنی در سیستم‌های جستجو، تحلیل یا اتوماسیون استفاده کنید.
   
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
        // با Parser مستندات خود را اولیه‌سازی کنید
        try (Parser parser = new Parser("input.epub"))
        {
            // تمام داده‌های متنی را بخوانید و استخراج کنید
            try (TextReader reader = parser.getText())
            {
                // اگر محتویات متنی موجود نبود، مقدار null را بازگردانید
                // متن استخراج‌شده را در جریان کاری خود ادغام کنید
                System.out.println(reader == null ? 
                    "فرمت‌های استخراج متن غیرپشتیبانی را رد کنید" : reader.readToEnd());
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "عملکرد غنی استخراج متن"
  description: "GroupDocs.Parser فراتر از استخراج متن ساده عمل می‌کند و از بازیابی تصاویر، متاداده و داده‌های ساختاری برای بهبود وظایف پردازش محتوا پشتیبانی می‌کند."
  image: "/img/parser/features_extract-text.webp" # 500x500 px
  image_description: "استخراج و ساختاربندی محتوای متنی از اسناد"
  features:
    # feature loop
    - title: "عملکرد در فرمت‌های مختلف مستندات"
      content: "متن‌های خام و ساختاری را از فرمت‌های DOCX، XLSX، PPTX، PDF، HTML و فرمت‌های دیگر استخراج کنید."

    # feature loop
    - title: "استخراج متن از محتوای بصری و متنی"
      content: "متن را از اسناد اسکن‌شده، اسلایدها، صفحات گسترده و سایر نوع فایل‌ها استخراج کنید در حالی که ساختار منطقی را حفظ می‌نمایید."

    # feature loop
    - title: "کنترل دقیق بر فرآیند استخراج"
      content: "محدوده‌های صفحه، مناطق طرح و پارامترهای دقت را برای تجزیه متن بهینه تنظیم کنید."
      
  code_samples:
    # code sample loop
    - title: "نمونه: استخراج نواحی متنی از یک سند PPTX"
      content: |
        این نمونه نشان می‌دهد که چگونه بلوک‌های متنی همراه با مختصات فضایی آن‌ها را از یک ارائه PowerPoint با استفاده از GroupDocs.Parser استخراج کنید.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  فایل PPTX خود را با API Parser بارگذاری کنید
        try (Parser parser = new Parser("input.pptx"))
        {
            // تمام نواحی متنی مستطیلی را دریافت کنید
            IEnumerable<PageTextArea> areas = parser.GetTextAreas();

            // در صورت عدم پشتیبانی این ویژگی، خارج شوید
            if (areas == null)
            {
                return;
            }

            // از طریق نواحی متنی مطابق با صفحات تکرار کنید
            for (PageTextArea a : areas)
            {
                // هر بلوک متنی را با شماره صفحه و مستطیل محدودکننده‌اش پردازش کنید
                System.out.println(String.format("Page: %d, R: %s, Text: %s", a.getPage().getIndex(), a.getRectangle(), a.getText()));
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
    title: "نوع فایل‌های پشتیبانی شده برای استخراج متن"
    exclude: "EPUB"
    description: "GroupDocs.Parser قادر است محتوای متنی را از فرمت‌های مختلف فایل و تصویر استخراج کند. در زیر انواع رایجی که پشتیبانی می‌کند، آمده است."
    items: 
        # format loop 1
        - name: "تحلیل PDF"
          format: "PDF"
          link: "/parser/java/extract-text/pdf/"
          description: "(فرمت سند قابل حمل)"
          
        # format loop 2
        - name: "تحلیل DOCX"
          format: "DOCX"
          link: "/parser/java/extract-text/docx/"
          description: "(سند Word Office 2007+)"
          
        # format loop 3
        - name: "تحلیل PPTX"
          format: "PPTX"
          link: "/parser/java/extract-text/pptx/"
          description: "(فرمت ارائه Open XML)"
          
        # format loop 4
        - name: "تحلیل XLSX"
          format: "XLSX"
          link: "/parser/java/extract-text/xlsx/"
          description: "(دفتر کار Open XML)"
          
        # format loop 5
        - name: "تحلیل TXT"
          format: "TXT"
          link: "/parser/java/extract-text/txt/"
          description: "(فایل متنی)"
          
        # format loop 6
        - name: "تحلیل RTF"
          format: "RTF"
          link: "/parser/java/extract-text/rtf/"
          description: "(فرمت متن غنی)"
          
        # format loop 7
        - name: "تحلیل XML"
          format: "XML"
          link: "/parser/java/extract-text/xml/"
          description: "(زبان نشانه‌گذاری قابل توسعه)"
          
        # format loop 8
        - name: "تحلیل EPUB"
          format: "EPUB"
          link: "/parser/java/extract-text/epub/"
          description: "(فایل کتاب الکترونیکی Open)"
         
          

---