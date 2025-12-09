---
############################# Static ############################
layout: "landing"
date: 2025-12-09T14:10:41
draft: false

lang: fa
product: "Parser"
product_tag: "parser"
platform: "Net"
platform_tag: "net"

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
head_title: "GroupDocs.Parser for .NET Document Parser SDK برای .NET"
head_description: "SDK تجزیه‌گر سند با عملکرد بالا برای .NET. متن، تصاویر، فراداده، بارکدها، جداول و سایر داده‌ها را از PDF، Word، Excel، ایمیل‌ها و بیش از 50 فرمت سند استخراج می‌کند."

############################# Header ############################
title: "Document Parser SDK برای .NET"
description: "تحلیل سریع و دقیق اسناد را به برنامه‌های .NET خود اضافه کنید و متن، تصاویر، فراداده و داده‌های ساختاریافته را از اسناد و تصاویر استخراج کنید."
words:
  for: "برای"

actions:
  main: "Nuget دانلود"
  main_link: "https://www.nuget.org/packages/GroupDocs.Parser"
  alt: "مجوزدهی"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/net/"
  title: "آیا آماده شروع هستید؟"
  description: "امکانات GroupDocs.Parser را به‌صورت رایگان امتحان کنید یا یک مجوز درخواست کنید"

release:
  title: "نسخه {0} منتشر شد"
  notes: "جدیدهای نسخه را ببینید"
  downloads: "دانلودها"

code:
  title: "به‌سرعت محتوای سند را با SDK تجزیه کنید"
  more: "مثال‌های بیشتر"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
  install: "dotnet add package GroupDocs.Parser"
  content: |
    ```csharp {style=abap}   
    // فایل منبع را به نمونه Parser پاس دهید
    using (var parser = new Parser("source.pdf"))
    {
        // متن سند را به TextReader پاس دهید
        using (var textReader = parser.GetText())
        {
            // متن سند را پردازش کنید
            Console.WriteLine(textReader?.ReadToEnd());
        }
    }  
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser در یک نگاه"
  description: "Document Parser SDK برای انجام تجزیه دقیق اسناد در برنامه‌های .NET"
  features:
    # feature loop
    - title: "استخراج داده‌ها از اسناد"
      content: "GroupDocs.Parser for .NET API به شما امکان می‌دهد متن، فراداده و تصاویر را از طیف گسترده‌ای از فرمت‌های فایل مانند اسناد آفیس، ایمیل‌ها، پیوست‌ها و آرشیوها بازیابی کنید. این ابزار قدرتمند به شما کمک می‌کند تا به‌صورت کارآمد به اطلاعات ارزشمند موجود در این فایل‌ها دسترسی پیدا کنید و آنها را برای برنامه‌های مختلفی مانند تحلیل داده، ایندکس‌سازی موتورهای جستجو یا سیستم‌های مدیریت محتوا پردازش کنید."

    # feature loop
    - title: "تجزیه اسناد"
      content: "عناصر مختلفی مانند پیوندها، جداول، کدهای QR، بارکدها و داده‌ها را از فرم‌های PDF استخراج کنید. همچنین می‌توانید با استفاده از قالب‌های سفارشی، هر اطلاعات دلخواهی را از اسناد تجزیه کنید."

    # feature loop
    - title: "سفارشی‌سازی نتایج"
      content: ".NET API به شما امکان می‌دهد داده‌ها را در قالب‌های مختلفی مانند خام، ساختار یافته، HTML یا Markdown بازیابی کنید. علاوه بر این، API امکان جستجو برای یافتن کلمات یا عبارات خاص در متن اسناد را فراهم می‌کند."

############################# Platforms ############################
platforms:
  enable: true
  title: "استقلال پلتفرم"
  description: "GroupDocs.Parser for .NET سیستم‌عامل‌ها، چارچوب‌ها و مدیران بسته زیر را پشتیبانی می‌کند"
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
  title: "قالب‌های فایل پشتیبانی شده"
  description: |
    GroupDocs.Parser for .NET عملیات با [قالب‌های فایل](https://docs.groupdocs.com/parser/net/supported-document-formats/) زیر را پشتیبانی می‌کند.
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
  title: "ویژگی‌های GroupDocs.Parser for .NET"
  description: "با استفاده از .NET Document Parser SDK ما، داده‌ها را از PDFها، اسناد آفیس، تصاویر و سایر فرمت‌ها به‌سرعت و به‌دقت استخراج کنید"

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
  description: "برخی موارد استفاده رایج برای عملیات GroupDocs.Parser for .NET"
  items:
    # code sample loop
    - title: "استخراج تصاویر از اسناد PDF"
      content: |
        GroupDocs.Parser for .NET کار را برای توسعه‌دهندگان C# آسان می‌کند تا تصاویر را از [اسناد](https://docs.groupdocs.com/parser/net/extract-images-from-documents/) استخراج کنند:
        {{< landing/code title="استخراج تصاویر از اسناد PDF در C#">}}
        ```csharp {style=abap}
        // یک نمونه از کلاس Parser ایجاد کنید
        using (var parser = new Parser("source.pptx"))
        {
            // استخراج تصاویر
            var images = parser.GetImages();

            // بررسی کنید آیا چیزی استخراج شده است
            if (images == null)
            {
                return;
            }
            // تکرار بر روی تصاویر
            foreach (PageImageArea image in images)
            {
                // چاپ شاخص صفحه، مستطیل و نوع تصویر
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Type: {2}", 
                    image.Page.Index, image.Rectangle, image.FileType));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "استخراج بارکدها از تصاویر"
      content: |
        از API .NET ما برای استخراج [بارکدها](https://docs.groupdocs.com/parser/net/extract-barcodes-from-document/) از تصاویر استفاده کنید:
        {{< landing/code title="استخراج بارکدها از تصاویر در C#">}}
        ```csharp {style=abap}   
        // بارگذاری تصویر منبع به Parser
        using (var parser = new Parser("source.jpg"))
        {
            // بررسی کنید آیا فایل از استخراج بارکد پشتیبانی می‌کند
            if (parser.Features.Barcodes)
            {
                // استخراج بارکدها از فایل
                var barcodes = parser.GetBarcodes();

                // تکرار بر روی بارکدها
                foreach (var barcode in barcodes)
                {
                    // چاپ شاخص صفحه
                    Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                    // چاپ مقدار بارکد
                    Console.WriteLine("Value: " + barcode.Value);
                }
            }
        }
        ```
        {{< /landing/code >}}

---
