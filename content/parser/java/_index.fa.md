---
############################# Static ############################
layout: "landing"
date: 2025-12-09T14:10:41
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
    # supported_platforms loop
    - title: "Python"
      tag: "python-net"

############################# Head ############################
head_title: "GroupDocs.Parser for Java SDK تجزیه‌گر سند برای Java"
head_description: "SDK تجزیه‌گر سند با عملکرد بالا برای Java. متن، تصاویر، فراداده، بارکدها، جداول و سایر داده‌ها را از PDF، Word، Excel، ایمیل‌ها و بیش از 50 فرمت سند استخراج کنید."

############################# Header ############################
title: "SDK تجزیه‌گر سند برای Java"
description: "قابلیت تجزیه سریع و دقیق اسناد را به برنامه‌های Java خود اضافه کنید و متن، تصاویر، فراداده و داده‌های ساختار یافته را از اسناد و تصاویر استخراج کنید."
words:
  for: "برای"

actions:
  main: "Maven دانلود"
  main_link: "https://releases.groupdocs.com/java/repo/com/groupdocs/groupdocs-parser/"
  alt: "مجوزدهی"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/java/"
  title: "آیا آماده شروع هستید؟"
  description: "امکانات GroupDocs.Parser را به‌صورت رایگان امتحان کنید یا یک مجوز درخواست کنید"

release:
  title: "نسخه {0} منتشر شد"
  notes: "جدیدهای نسخه را ببینید"
  downloads: "دانلودها"

code:
  title: "به‌سرعت محتوای سند را با SDK تجزیه کنید"
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
    // فایل منبع را به نمونه Parser پاس دهید
    try (Parser parser = new Parser("source.pdf"))
    {
        // متن سند را به TextReader پاس دهید
        try (TextReader reader = parser.getText())
        {
            // متن سند را پردازش کنید
            System.out.println(reader == null 
                ? "" 
                : reader.readToEnd());
        }
    }
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser در یک نگاه"
  description: "SDK تجزیه‌گر سند برای انجام تجزیه دقیق اسناد در برنامه‌های Java"
  features:
    # feature loop
    - title: "استخراج داده‌ها از اسناد"
      content: "API GroupDocs.Parser for Java به شما امکان می‌دهد تا متن، فراداده و تصاویر را از طیف وسیعی از قالب‌های فایل مانند اسناد Office، ایمیل‌ها، پیوست‌ها و بایگانی‌ها بازیابی کنید. این ابزار قدرتمند به شما کمک می‌کند تا به‌صورت کارآمد به اطلاعات ارزشمند موجود در این فایل‌ها دسترسی پیدا کنید و آنها را برای کاربردهای مختلفی مانند تحلیل داده، ایندکس‌گذاری موتورهای جستجو یا سیستم‌های مدیریت محتوا پردازش نمایید."

    # feature loop
    - title: "تجزیه اسناد"
      content: "عناصر مختلفی مانند پیوندها، جداول، کدهای QR، بارکدها و داده‌ها را از فرم‌های PDF استخراج کنید. همچنین با استفاده از قالب‌های سفارشی، هر اطلاعات مورد نظر را از اسناد تجزیه کنید."

    # feature loop
    - title: "سفارشی‌سازی نتایج"
      content: "Java API به شما امکان می‌دهد داده‌ها را در قالب‌های مختلفی مانند خام، ساختار یافته، HTML یا Markdown بازیابی کنید. علاوه بر این، API قابلیت جستجو برای یافتن کلمات یا عبارات خاص در متن اسناد را فراهم می‌کند."

############################# Platforms ############################
platforms:
  enable: true
  title: "استقلال پلتفرم"
  description: "GroupDocs.Parser for Java سیستم‌عامل‌ها، چارچوب‌ها و مدیران بسته زیر را پشتیبانی می‌کند"
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
  title: "قالب‌های فایل پشتیبانی شده"
  description: |
    GroupDocs.Parser for Java عملیات با [قالب‌های فایل](https://docs.groupdocs.com/parser/java/supported-document-formats/) زیر را پشتیبانی می‌کند.
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
        ### تصاویر و فرمت‌های دیگر
        * **قابل حمل:** PDF 
        * **تصاویر:** JPG, BMP, PNG, TIFF, GIF
        * **قالب‌های دیگر آفیس:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### فرمت‌های دیگر
        * **وب:** HTML, MHTML 
        * **آرشیوها:** ZIP, TAR, 7Z 
        * **کتاب‌های الکترونیکی:** CHM, EPUB, FB2, MOBI 
        
        

############################# Features ############################
features:
  enable: true
  title: "قابلیت‌های GroupDocs.Parser for Java"
  description: "داده‌ها را از PDFها، اسناد Office، تصاویر و سایر فرمت‌ها به‌سرعت و با دقت با Java Document Parser SDK ما استخراج کنید."

  items:
    # feature loop
    - icon: "text"
      title: "استخراج متن"
      content: "اطلاعات متنی را از فرمت‌های مختلف فایل مانند اسناد آفیس، فایل‌های PDF و تصاویر استخراج کنید تا قابلیت خواندن و تحلیل آسان را داشته باشید."

    # feature loop
    - icon: "image"
      title: "استخراج تصاویر"
      content: "محتوای تصویری را از منابع متنوعی مانند اسناد آفیس و فایل‌های PDF بازیابی کنید برای دسترسی و استفاده راحت."

    # feature loop
    - icon: "qr"
      title: "اسکن کدهای QR"
      content: "کدهای QR موجود در اسناد آفیس، فایل‌های PDF یا محتوای تصویری را شناسایی و رمزگشایی کنید برای بازیابی مؤثر اطلاعات."

    # feature loop
    - icon: "email"
      title: "استخراج داده‌ها از پیوست‌های ایمیل و آرشیوها"
      content: "اطلاعات ارزشمند را از پیام‌های ایمیل، پیوست‌های فایل و منابع داده فشرده جمع‌آوری کنید تا برای تجزیه و تحلیل و بهره‌برداری مؤثر به کار رود."

    # feature loop
    - icon: "table"
      title: "استخراج جداول"
      content: "داده‌های جدولی را از اسناد PDF شناسایی و استخراج کنید برای تجزیه و تحلیل منظم و استفاده."

    # feature loop
    - icon: "hyperlink"
      title: "استخراج پیوندهای ابرمتنی"
      content: "پیوندهای ابرمتنی و آدرس‌های ایمیل را در اسناد آفیس یا فایل‌های PDF پیدا کرده و استخراج کنید برای دسترسی کارآمد."

    # feature loop
    - icon: "pdf"
      title: "تجزیه فرم‌های PDF"
      content: "فرم‌های PDF اسناد دیجیتالی هستند که دارای فیلدهای قابل پرکردن برای تعامل کاربر می‌باشند و به آنها امکان وارد کردن اطلاعات به‌صورت الکترونیکی را می‌دهند. می‌توان از API .NET برای استخراج داده‌ها از این فرم‌ها جهت پردازش کارآمد استفاده کرد."

    # feature loop
    - icon: "template"
      title: "تجزیه داده‌ها با قالب‌ها"
      content: "قالب‌های سفارشی ایجاد کنید و با استفاده از API .NET، اطلاعات خاصی را از فایل‌های PDF تجزیه کنید، که فرآیند استخراج داده‌ها را ساده می‌کند."

    # feature loop
    - icon: "search"
      title: "جستجوی متن در اسناد"
      content: "به‌سرعت کلمات یا الگوهای خاص را در اسناد پیدا کنید."


############################# Code samples ############################
code_samples:
  enable: true
  title: "نمونه‌های کد"
  description: "برخی موارد استفاده رایج از عملیات GroupDocs.Parser for Java"
  items:
    # code sample loop
    - title: "استخراج تصاویر از اسناد PDF"
      content: |
        GroupDocs.Parser for Java برای توسعه‌دهندگان Java استخراج تصاویر از [اسناد](https://docs.groupdocs.com/parser/java/extract-images-from-documents/) را آسان می‌کند:
        {{< landing/code title="استخراج تصاویر از اسناد PDF در Java">}}
        ```java {style=abap}
        // یک نمونه از کلاس Parser ایجاد کنید
        try (Parser parser = new Parser("source.pdf"))
        {
            // استخراج تصاویر
            Iterable<PageImageArea> images = parser.getImages();

            // بررسی کنید آیا چیزی استخراج شده است
            if (images == null) {
                return;
            }

            // تکرار بر روی تصاویر
            for (PageImageArea image : images) {
                // چاپ شاخص صفحه، مستطیل و نوع تصویر
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
        // بارگذاری تصویر منبع به Parser
        try (Parser parser = new Parser("source.jpg")){

            // بررسی کنید آیا فایل از استخراج بارکد پشتیبانی می‌کند
            if (!parser.getFeatures().isBarcodes()) {

                // استخراج بارکدها از فایل
                Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();

                // تکرار بر روی بارکدها
                for (PageBarcodeArea barcode : barcodes) {
                    // چاپ شاخص صفحه
                    System.out.println("Page: " + barcode.getPage().getIndex());
                    // چاپ مقدار بارکد
                    System.out.println("Value: " + barcode.getValue());
                }
            }
        }
        ```
        {{< /landing/code >}}

---
