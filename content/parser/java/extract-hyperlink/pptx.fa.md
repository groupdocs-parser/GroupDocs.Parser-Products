


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:23
draft: false
lang: fa
format: Pptx
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "استخراج لینک‌های هایپر از فایل‌های PPTX در برنامه‌های Java"
head_description: "از GroupDocs.Parser برای یافتن و استخراج لینک‌های URL از اسناد PPTX در پروژه‌های Java استفاده کنید—بدون نیاز به نرم‌افزار اضافی."

############################# Header ############################
title: "استخراج لینک‌های هایپر از PPTX با Java" 
description: "لینک‌های وب و هایپرلینک‌ها را از پی‌دی‌اف‌ها، فایل‌های Word، صفحات Excel و دیگر اسناد با استفاده از GroupDocs.Parser در محیط Java خود استخراج کنید."
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
    title: "درباره API GroupDocs.Parser for Java"
    link: "/parser/java/"
    link_title: "بیشتر بدانید"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) یک API استخراج محتوا قدرتمند است که برای توسعه‌دهندگان Java طراحی شده است. این API ابزارهایی برای استخراج لینک‌های هایپر، داده‌های ساختاریافته، تصاویر و متن از فرمت‌های محبوب مانند DOCX، XLSX، PDF، HTML و بیشتر ارائه می‌دهد—بدون نیاز به پلاگین‌های خارجی.

############################# Steps ############################
steps:
    enable: true
    title: "نحوه استخراج لینک‌های هایپر از Pptx در Java"
    content: |
      [GroupDocs.Parser](/parser/java/) استخراج لینک‌های هایپر از فایل‌های PPTX را در برنامه‌های Java با این مراحل ساده تسهیل می‌کند:
      
      1. فایل PPTX را با استفاده از یک نمونه از Parser باز کنید.
      2. اطمینان حاصل کنید که استخراج لینک‌های هایپر برای فرمت فایل در دسترس است.
      3. همه لینک‌های هایپر را با استفاده از روش مناسب استخراج کنید.
      4. از نتایج عبور کنید و هر لینک را به‌دلخواه پردازش کنید.
   
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
        // فایلی که ممکن است شامل لینک‌های هایپر باشد را با استفاده از Parser بارگزاری کنید
        try (Parser parser = new Parser("input.pptx")) {

            // بررسی کنید که آیا فرمت سند از تجزیه لینک‌های هایپر پشتیبانی می‌کند
            if (!parser.getFeatures().isHyperlinks()) {
                System.out.println("استخراج لینک‌های هایپر برای این فایل در دسترس نیست");
                return;
            }

            // داده‌های لینک‌های هایپر را از سند استخراج و استفاده کنید
            Iterable<PageHyperlinkArea> hyperlinks = parser.getHyperlinks();

            for (PageHyperlinkArea h : hyperlinks) {
                System.out.println(h.getText());
                System.out.println(h.getUrl());
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "ابزارهای جامع تجزیه اسناد"
  description: "علاوه بر استخراج لینک‌های هایپر، GroupDocs.Parser به شما امکان می‌دهد سایر محتوای مفید مانند متن ساده، رسانه‌های جاسازی شده و داده‌های ساختاریافته را برای استفاده در گردش‌کارهای خودکار جمع‌آوری کنید."
  image: "/img/parser/features_extract-hyperlink.webp" # 500x500 px
  image_description: "استخراج لینک‌های هایپر و تجزیه و تحلیل اسناد"
  features:
    # feature loop
    - title: "تشخیص دقیق لینک"
      content: "همه انواع لینک‌های هایپر را از چیدمان‌های مختلف سند، از جمله متن قابل کلیک و URL های پنهان، ضبط کنید."

    # feature loop
    - title: "کار با اسناد و محتوای وب"
      content: "لینک‌ها را از فایل‌های PDF، DOCX، XLSX، HTML و تصاویری که شامل لینک‌های هایپر جاسازی شده هستند، استخراج کنید."

    # feature loop
    - title: "رفتار استخراج سفارشی"
      content: "چگونگی استخراج لینک‌های هایپر را با استفاده از گزینه‌هایی مانند محدوده صفحات، نوع لینک‌ها یا فیلترهای محتوا بهینه کنید."
      
  code_samples:
    # code sample loop
    - title: "مثال: استخراج لینک‌های هایپر از یک PDF با گزینه‌های سفارشی"
      content: |
        این نمونه نشان می‌دهد که چگونه می‌توان همه لینک‌ها را از یک فایل PDF با استفاده از تنظیمات استخراج لینک دریافت کرد.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  فایل PDF را با استفاده از کلاس Parser باز کنید
        try (Parser parser = new Parser("input.docx"))
        {
            // تأیید کنید که پشتیبانی از لینک‌های هایپر برای این سند فعال است
            if (!parser.getFeatures().isHyperlinks()) {
                return;
            }

            // گزینه‌ها را برای فیلتر لینک‌ها اعمال کنید
            PageAreaOptions options = new PageAreaOptions(new Rectangle(new Point(380, 90), new Size(150, 50)));

            // از تجزیه‌کننده برای دریافت داده‌های لینک‌های هایپر استفاده کنید
            Iterable<PageHyperlinkArea> hyperlinks = parser.getHyperlinks(options);

            // از طریق لینک‌ها عبور کنید و آن‌ها را به‌طور مناسب پردازش کنید
            for (PageHyperlinkArea h : hyperlinks) {
                System.out.println(h.getText());
                System.out.println(h.getUrl());
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
    title: "فرمت‌های مستنداتی که از استخراج لینک‌های هایپر پشتیبانی می‌کنند"
    exclude: "PPTX"
    description: "با GroupDocs.Parser، می‌توانید لینک‌های هایپر را از بسیاری از فرمت‌های فایل رایج استخراج کنید. در زیر فهرستی از فرمت‌هایی که معمولاً پشتیبانی می‌شوند، آمده است."
    items: 
        # format loop 1
        - name: "تحلیل PDF"
          format: "PDF"
          link: "/parser/java/extract-hyperlink/pdf/"
          description: "(فرمت سند قابل حمل)"
          
        # format loop 2
        - name: "تحلیل DOCX"
          format: "DOCX"
          link: "/parser/java/extract-hyperlink/docx/"
          description: "(سند Word Office 2007+)"
          
        # format loop 3
        - name: "تحلیل PPTX"
          format: "PPTX"
          link: "/parser/java/extract-hyperlink/pptx/"
          description: "(فرمت ارائه Open XML)"
          
        # format loop 4
        - name: "تحلیل XLSX"
          format: "XLSX"
          link: "/parser/java/extract-hyperlink/xlsx/"
          description: "(دفتر کار Open XML)"
          
        # format loop 5
        - name: "تحلیل TXT"
          format: "TXT"
          link: "/parser/java/extract-hyperlink/txt/"
          description: "(فایل متنی)"
          
        # format loop 6
        - name: "تحلیل RTF"
          format: "RTF"
          link: "/parser/java/extract-hyperlink/rtf/"
          description: "(فرمت متن غنی)"
          
        # format loop 7
        - name: "تحلیل XML"
          format: "XML"
          link: "/parser/java/extract-hyperlink/xml/"
          description: "(زبان نشانه‌گذاری قابل توسعه)"
          
        # format loop 8
        - name: "تحلیل EPUB"
          format: "EPUB"
          link: "/parser/java/extract-hyperlink/epub/"
          description: "(فایل کتاب الکترونیکی Open)"
         
          

---