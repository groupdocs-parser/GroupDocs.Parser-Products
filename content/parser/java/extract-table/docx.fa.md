


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:38
draft: false
lang: fa
format: Docx
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "دریافت جداول از اسناد DOCX در برنامه‌های Java"
head_description: "استخراج داده‌های جدولی ساختار‌یافته از فایل‌های DOCX در برنامه‌های Java با استفاده از GroupDocs.Parser—بدون نیاز به ابزارهای خارجی."

############################# Header ############################
title: "دریافت داده‌های جدولی از DOCX با استفاده از Java" 
description: "به‌راحتی جداول را از فرمت‌هایی مانند PDF، DOCX و XLSX با GroupDocs.Parser در جریان‌های کاری Java خود تشخیص داده و استخراج کنید."
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
    title: "معرفی API GroupDocs.Parser for Java"
    link: "/parser/java/"
    link_title: "بیشتر بدانید"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) یک API استخراج محتوای غنی برای پلتفرم‌های Java است. این ابزار به توسعه‌دهندگان اجازه می‌دهد تا به‌دقت جداول، متن، گرافیک، لینک‌ها و داده‌های ساختار‌یافته را از PDFها، اسناد Word، صفحات Excel، ارائه‌های PowerPoint و بیشتر استخراج کنند—بدون نیاز به پلاگین‌های شخص ثالث.

############################# Steps ############################
steps:
    enable: true
    title: "چگونه جداول را از Docx در Java استخراج کنیم"
    content: |
      برای استخراج جداول از اسناد DOCX با استفاده از [GroupDocs.Parser](/parser/java/)، مراحل زیر را در محیط Java خود دنبال کنید:
      
      1. یک نمونه از Parser را ایجاد کرده و فایل هدف DOCX را بارگذاری کنید.
      2. تأیید کنید که فایل از استخراج جدول ساختار‌یافته پشتیبانی می‌کند.
      3. از API برای استخراج المان‌های جدول از سند استفاده کنید.
      4. از داده‌های استخراج‌شده در تحلیل، گزارش‌گیری یا سیستم‌های اتوماسیون استفاده کنید.
   
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
        // بارگذاری سند ورودی با Parser که شامل المان‌های جدول است.
        try (Parser parser = new Parser("input.docx"))
        {
            // تأیید کنید که نوع سند اجازه شناسایی جدول را می‌دهد.
            if (!parser.getFeatures().isTables()) {
                System.out.println("منطق لازم برای فایل‌هایی که از جداول پشتیبانی نمی‌کنند را اضافه کنید.");
                return;
            }

            // قوانینی برای تفسیر ساختار جدول تعریف کنید.
            TemplateTableLayout layout = new TemplateTableLayout(
                    java.util.Arrays.asList(new Double[]{50.0, 95.0, 275.0, 415.0, 485.0, 545.0}),
                    java.util.Arrays.asList(new Double[]{325.0, 340.0, 365.0, 395.0}));

            // پارامترهایی برای استخراج جداول تنظیم کنید.
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            //  عملیات استخراج جدول را بر روی سند بارگذاری‌شده اجرا کنید.
            Iterable<PageTableArea> tables = parser.getTables(options);

            //  هر جدول استخراج‌شده را از نتیجه پردازش کنید.
            for (PageTableArea t : tables) 
            {
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "ابزارهای پیشرفته استخراج محتوا"
  description: "فراتر از خواندن جداول، GroupDocs.Parser از ثبت متن ساده، عناصر بصری، متادیتای شما و اشیای ساختار‌یافته برای بهبود وظایف پردازش سند پشتیبانی می‌کند."
  image: "/img/parser/features_extract-table.webp" # 500x500 px
  image_description: "استخراج محتوای ساختار‌یافته و داده‌های جدولی"
  features:
    # feature loop
    - title: "تجزیه دقیق جدول در فرمت‌های مختلف"
      content: "پشتیبانی از استخراج جداول از انواع مستندات استاندارد مانند PDF، Word، Excel و HTML با دقت بالا."

    # feature loop
    - title: "خواندن ساختارهای جدولی از منابع مختلف"
      content: "استخراج داده‌های جدول از صفحات گسترده، اسناد و گزارش‌ها در حالی که ساختار و تراز را حفظ می‌کند."

    # feature loop
    - title: "تنظیمات استخراج جدول قابل تنظیم"
      content: "تشخیص لایه، مدیریت سرصفحات و پاورقی‌ها و تنظیم دقیق استخراج با گزینه‌های پیکربندی منعطف."
      
  code_samples:
    # code sample loop
    - title: "نمونه: استخراج جداول از یک سند Excel"
      content: |
        این مثال نشان می‌دهد که چگونه می‌توان محتویات جدول را در یک فایل Excel (XLSX) با استفاده از GroupDocs.Parser استخراج و مرور کرد.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  مقداردهی اولیه Parser با فایل Excel.
        try (Parser parser = new Parser("input.pdf"))
        {
            // در صورتی که استخراج جدول برای این سند پشتیبانی نشود، خارج شوید.
            if (!parser.getFeatures().isTables())
            {
                return;
            }

            // قوانینی برای یافتن لایه جدول اعمال کنید.
            TemplateTableLayout layout = new TemplateTableLayout(
                    java.util.Arrays.asList(new Double[]{50.0, 95.0, 275.0, 415.0, 485.0, 545.0}),
                    java.util.Arrays.asList(new Double[]{325.0, 340.0, 365.0, 395.0}));

            // تنظیمات را برای استخراج جدول پیکربندی کنید.
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            // فرآیند استخراج را فراخوانی کنید.
            Iterable<PageTableArea> tables = parser.getTables(options);

            // بر روی تمام ساختارهای جدول تجزیه شده مرور کنید.
            for (PageTableArea t : tables)
            {
                // بر روی هر ردیف در جدول تکرار کنید.
                for (int row = 0; row < t.getRowCount(); row++)
                {
                    // هر سلول در ردیف فعلی را پردازش کنید.
                    for (int column = 0; column < t.getColumnCount(); column++) 
                    {
                        // به محتوای سلول فعلی دسترسی پیدا کرده و آن را بخوانید.
                        PageTableAreaCell cell = t.getCell(row, column);
                        if (cell != null)
                        {
                            // مقدار متنی هر سلول جدول را خروجی دهید.
                            System.out.print(cell.getText());
                            System.out.print(" | ");
                        }
                    }
                }
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
    title: "انواع اسناد پشتیبانی شده برای استخراج جداول"
    exclude: "DOCX"
    description: "GroupDocs.Parser تشخیص جدول مطمئن را در چندین نوع فایل ارائه می‌دهد. در اینجا فهرستی از قالب‌های مستندات به‌طور گسترده‌ای پشتیبانی شده برای استخراج جداول آورده شده است."
    items: 
        # format loop 1
        - name: "تحلیل PDF"
          format: "PDF"
          link: "/parser/java/extract-table/pdf/"
          description: "(فرمت سند قابل حمل)"
          
        # format loop 2
        - name: "تحلیل DOCX"
          format: "DOCX"
          link: "/parser/java/extract-table/docx/"
          description: "(سند Word Office 2007+)"
          
        # format loop 3
        - name: "تحلیل PPTX"
          format: "PPTX"
          link: "/parser/java/extract-table/pptx/"
          description: "(فرمت ارائه Open XML)"
          
        # format loop 4
        - name: "تحلیل XLSX"
          format: "XLSX"
          link: "/parser/java/extract-table/xlsx/"
          description: "(دفتر کار Open XML)"
          
        # format loop 5
        - name: "تحلیل TXT"
          format: "TXT"
          link: "/parser/java/extract-table/txt/"
          description: "(فایل متنی)"
          
        # format loop 6
        - name: "تحلیل RTF"
          format: "RTF"
          link: "/parser/java/extract-table/rtf/"
          description: "(فرمت متن غنی)"
          
        # format loop 7
        - name: "تحلیل XML"
          format: "XML"
          link: "/parser/java/extract-table/xml/"
          description: "(زبان نشانه‌گذاری قابل توسعه)"
          
        # format loop 8
        - name: "تحلیل EPUB"
          format: "EPUB"
          link: "/parser/java/extract-table/epub/"
          description: "(فایل کتاب الکترونیکی Open)"
         
          

---