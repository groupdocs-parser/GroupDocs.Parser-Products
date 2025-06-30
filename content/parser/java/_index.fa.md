---
############################# Static ############################
layout: "landing"
date: 2025-06-30T10:26:00
draft: false

lang: fa
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
head_title: "برنامه‌های تحلیل اسناد GroupDocs.Parser for Java"
head_description: "راهکار جامع تحلیل اسناد برای برنامه‌های Java. استخراج داده‌ها از فرمت‌های اسنادی آنلاین با استفاده از ویژگی کشیدن و رها کردن ساده."

############################# Header ############################
title: "تحلیل اسناد از طریق API Java"
description: "استخراج داده‌ها از اسناد و تصاویر در هر پلتفرم با استفاده از API های انعطاف‌پذیر ما و راه‌حل‌های مبتنی بر برنامه برای برنامه‌نویسان و کاربران نهایی."
words:
  for: "برای"

actions:
  main: "دانلود Maven"
  main_link: "https://releases.groupdocs.com/java/repo/com/groupdocs/groupdocs-parser/"
  alt: "مجوز"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/java/"
  title: "آماده شروع کار هستید؟"
  description: "ویژگی‌های GroupDocs.Parser را به صورت رایگان امتحان کنید یا درخواست مجوز دهید."

release:
  title: "نسخه {0} منتشر شد"
  notes: "ببینید چه چیزهایی جدید است"
  downloads: "دانلودها"

code:
  title: "به‌سرعت محتوای سند را تحلیل کنید"
  more: "مثال‌های بیشتر"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java/"
  install: |
    <dependency>
      <groupId>com.groupdocs</groupId>
      <artifactId>groupdocs-parser</artifactId>
      <version>{0}</version>
    </dependency>
  content: |
    ```java {style=abap}  
    // فایل منبع را به نمونه Parser پاس دهید.
    try (Parser parser = new Parser("source.pdf"))
    {
        // متن سند را به TextReader پاس دهید.
        try (TextReader reader = parser.getText())
        {
            // متن سند را پردازش کنید.
            System.out.println(reader == null 
                ? "" 
                : reader.readToEnd());
        }
    }
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser در یک نظر"
  description: "API برای انجام تحلیل اسناد در برنامه‌های Java"
  features:
    # feature loop
    - title: "استخراج داده‌ها از اسناد"
      content: "GroupDocs.Parser for Java API به شما این امکان را می‌دهد که متن، متاداده و تصاویر را از دامنه وسیعی از فرمت‌های فایل استخراج کنید. این ابزار قوی به شما کمک می‌کند تا به‌طور مؤثر به اطلاعات ارزشمندی که در این فایل‌ها وجود دارد برای کاربردهای مختلفی همچون تحلیل داده، ایندکس‌سازی موتور جستجو یا سیستم‌های مدیریت محتوا دسترسی و پردازش کنید."

    # feature loop
    - title: "تحلیل اسناد"
      content: "استخراج عناصر مختلفی مانند هایپرلینک‌ها، جداول، بارکدها، بارکدهای QR و داده‌ها از فرم‌های PDF. همچنین می‌توانید هر اطلاعات دلخواهی را بر اساس الگوهای سفارشی استخراج کنید."

    # feature loop
    - title: "سفارشی‌سازی نتایج"
      content: "Java API به شما این امکان را می‌دهد که داده‌ها را در فرمت‌های مختلفی همچون خام، ساختاریافته، HTML یا Markdown استخراج کنید."

############################# Platforms ############################
platforms:
  enable: true
  title: "استقلال از پلتفرم"
  description: "GroupDocs.Parser for Java از سیستم‌عامل‌ها، فریم‌ورک‌ها و مدیران بسته های زیر پشتیبانی می‌کند."
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
  title: "فرمت‌های پشتیبانی شده"
  description: |
    GroupDocs.Parser for Java از عملیات روی [فرمت‌های فایل](https://docs.groupdocs.com/parser/java/supported-document-formats/) زیر پشتیبانی می‌کند.
  groups:
    # group loop
    - color: "green"
      content: |
        ### فرمت‌های Microsoft Office
        * **Word:** DOCX, DOC, DOCM, DOT, DOTX, DOTM, RTF
        * **Excel:** XLSX, XLS, XLSM, XLSB, XLTM, XLT, XLTM, XLTX, XLAM, SXC, SpreadsheetML
        * **PowerPoint:** PPT, PPTX, PPS, PPSX, PPSM, POT, POTM, POTX, PPTM
    # group loop
    - color: "blue"
      content: |
        ### تصاویر و سایر فرمت‌ها
        * **قابل حمل:** PDF 
        * **تصاویر:** JPG, BMP, PNG, TIFF, GIF
        * **سایر فرمت‌های اداری:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### سایر فرمت‌ها
        * **وب:** HTML, MHTML 
        * **آرشیوها:** ZIP, TAR, 7Z 
        * **کتاب‌های الکترونیکی:** CHM, EPUB, FB2, MOBI 
        
        

############################# Features ############################
features:
  enable: true
  title: "ویژگی‌های GroupDocs.Parser for Java"
  description: "استخراج داده‌ها از PDF ها، اسناد اداری و تصاویر به‌سرعت و به‌طور دقیق"

  items:
    # feature loop
    - icon: "text"
      title: "استخراج متن"
      content: "استخراج اطلاعات متنی از فرمت‌های مختلف فایل مانند اسناد اداری، فایل‌های PDF و تصاویر برای خوانایی و تحلیل آسان."

    # feature loop
    - icon: "image"
      title: "استخراج تصاویر"
      content: "بازیابی محتوای بصری از منابع مختلف مانند اسناد اداری و فایل‌های PDF برای دسترسی و استفاده راحت."

    # feature loop
    - icon: "qr"
      title: "اسکن بارکدهای QR"
      content: "شناسایی و رمزگشایی بارکدهای QR موجود در اسناد اداری، فایل‌های PDF یا محتوای بصری برای بازیابی اطلاعات مؤثر."

    # feature loop
    - icon: "email"
      title: "استخراج داده از پیوست‌های ایمیل و آرشیوها"
      content: "جمع‌آوری اطلاعات ارزشمند از پیام‌های ایمیل، پیوست‌های فایل و منابع داده‌های فشرده برای تحلیل و استفاده مؤثر."

    # feature loop
    - icon: "table"
      title: "استخراج جداول"
      content: "شناسایی و استخراج داده‌های جدولی از اسناد PDF برای تحلیل و استفاده سازمان‌یافته."

    # feature loop
    - icon: "hyperlink"
      title: "استخراج هایپرلینک‌ها"
      content: "شناسایی و استخراج هایپرلینک‌ها و آدرس‌های ایمیل موجود در اسناد اداری یا فایل‌های PDF برای دسترسی مؤثر."

    # feature loop
    - icon: "pdf"
      title: "تحلیل فرم‌های PDF"
      content: "فرم‌های PDF اسنادی دیجیتالی هستند که دارای فیلدهای قابل پر کردن برای تعامل کاربر می‌باشند، به آن‌ها این امکان را می‌دهد که اطلاعات را به‌صورت الکترونیکی وارد کنند. API .NET می‌تواند برای استخراج داده‌ها از این فرم‌ها به‌منظور پردازش مؤثر استفاده شود."

    # feature loop
    - icon: "template"
      title: "تحلیل داده با الگوها"
      content: "ایجاد الگوهای سفارشی و استفاده از آن‌ها با API .NET برای استخراج اطلاعات خاص از فایل‌های PDF، فرآیندهای استخراج داده را ساده می‌کند."

    # feature loop
    - icon: "search"
      title: "جستجوی متن در اسناد"
      content: "به‌سرعت کلمات یا الگوهای خاصی را در اسناد پیدا کنید."


############################# Code samples ############################
code_samples:
  enable: true
  title: "نمونه‌های کد"
  description: "برخی از نمونه‌های معمول GroupDocs.Parser for Java"
  items:
    # code sample loop
    - title: "استخراج تصاویر از اسناد PDF"
      content: |
        GroupDocs.Parser for Java فرآیند استخراج تصاویر را برای توسعه‌دهندگان Java از [اسناد](https://docs.groupdocs.com/parser/java/extract-images-from-documents/) آسان می‌کند:
        {{< landing/code title="استخراج تصاویر از اسناد PDF در Java">}}
        ```java {style=abap}
        // یک نمونه از کلاس Parser ایجاد کنید.
        try (Parser parser = new Parser("source.pdf"))
        {
            // تصاویر را استخراج کنید.
            Iterable<PageImageArea> images = parser.getImages();

            // بررسی کنید که آیا چیزی استخراج شده است.
            if (images == null) {
                return;
            }

            // بر روی تصاویر تکرار کنید.
            for (PageImageArea image : images) {
                // ایندکس صفحه، مستطیل و نوع تصویر را چاپ کنید.
                System.out.println(String.format("Page: %d, R: %s, Type: %s", 
                    image.getPage().getIndex(), image.getRectangle(), image.getFileType()));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "استخراج بارکدها از تصاویر"
      content: |
        از API Java ما برای استخراج [بارکدها](https://docs.groupdocs.com/parser/java/extract-barcodes-from-document/) از تصاویر استفاده کنید:
        {{< landing/code title="استخراج بارکدها از تصاویر در Java">}}
        ```java {style=abap}   
        // تصویر منبع را به Parser بارگذاری کنید.
        try (Parser parser = new Parser("source.jpg")){

            // بررسی کنید که آیا فایل از استخراج بارکد پشتیبانی می‌کند.
            if (!parser.getFeatures().isBarcodes()) {

                // بارکدها را از فایل استخراج کنید.
                Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();

                // بر روی بارکدها تکرار کنید.
                for (PageBarcodeArea barcode : barcodes) {
                    // ایندکس صفحه را چاپ کنید.
                    System.out.println("Page: " + barcode.getPage().getIndex());
                    // مقدار بارکد را چاپ کنید.
                    System.out.println("Value: " + barcode.getValue());
                }
            }
        }
        ```
        {{< /landing/code >}}

---
