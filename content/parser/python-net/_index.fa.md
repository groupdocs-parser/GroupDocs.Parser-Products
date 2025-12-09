---
############################# Static ############################
layout: "landing"
date: 2025-12-09T21:34:38
draft: false

lang: fa
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
head_title: "GroupDocs.Parser for Python via .NET SDK تجزیه‌کننده سند برای Python"
head_description: "SDK تجزیه‌کننده سند با عملکرد بالا برای Python. استخراج متن، تصاویر، متاداده، بارکدها، جداول و سایر داده‌ها از PDF، Word، Excel، ایمیل‌ها و 50+ قالب سند."

############################# Header ############################
title: "SDK تجزیه‌کننده سند برای Python"
description: "تجزیه سریع و دقیق اسناد را به برنامه‌های Python خود اضافه کنید و متن، تصاویر، متاداده و داده‌های ساختاریافته را از اسناد و تصاویر استخراج کنید."
words:
  for: "برای"

actions:
  hidden: true # Hide version 0 is released
  main: "دانلود PyPI"
  main_link: "https://pypi.org/project/groupdocs-parser-net/"
  alt: "مجوزدهی"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/python-net/"
  title: "آیا آماده شروع هستید؟"
  description: "امکانات GroupDocs.Parser را به‌صورت رایگان امتحان کنید یا یک مجوز درخواست کنید"

release:
  enable: false
  title: "نسخه {0} منتشر شد"
  notes: "جدیدهای نسخه را ببینید"
  downloads: "دانلودها"

code:
  title: "استخراج متن با استفاده از پایتون"
  more: "مثال‌های بیشتر"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Python-via-.NET/"
  install: "pip install groupdocs-parser-net"
  content: |
    ```python {style=abap}  
    from groupdocs.parser import Parser

    # بارگذاری سند
    with Parser("sample.pdf") as parser:
        # استخراج متن از سند
        text = parser.GetText()

        # چاپ تمام متن استخراج‌شده
        print(text)
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser در یک نگاه"
  description: "SDK تجزیه‌کننده سند برای انجام تجزیه دقیق اسناد در برنامه‌های Python"
  features:
    # feature loop
    - title: "استخراج داده‌ها از اسناد"
      content: "GroupDocs.Parser for Python via .NET API به شما امکان می‌دهد متن، متاداده و تصاویر را از انواع گسترده‌ای از قالب‌های فایل مانند اسناد Office، ایمیل‌ها، پیوست‌ها و آرشیوها بازیابی کنید. این ابزار قدرتمند به شما کمک می‌کند تا به‌صورت کارآمد به اطلاعات ارزشمند موجود در این فایل‌ها دسترسی پیدا کرده و آن‌ها را برای کاربردهای مختلفی مانند تحلیل داده، ایندکسیابی موتورهای جستجو یا سیستم‌های مدیریت محتوا پردازش کنید."

    # feature loop
    - title: "تجزیه اسناد"
      content: "عناصر مختلفی مانند هایپرلینک‌ها، جداول، کدهای QR، بارکدها و داده‌ها را از فرم‌های PDF استخراج کنید. همچنین می‌توانید هر اطلاعات دلخواهی را از اسناد با استفاده از قالب‌های سفارشی تجزیه کنید."

    # feature loop
    - title: "سفارشی‌سازی نتایج"
      content: "Python API به شما امکان می‌دهد داده‌ها را در قالب‌های مختلفی مانند خام، ساختاریافته، HTML یا Markdown بازیابی کنید. علاوه بر این، این API امکان جستجو برای یافتن کلمات یا عبارات خاص در متن اسناد را فراهم می‌کند."

############################# Platforms ############################
platforms:
  enable: true
  title: "استقلال پلتفرم"
  description: "GroupDocs.Parser for Python via .NET از سیستم‌عامل‌ها، چارچوب‌ها و مدیرهای بستهٔ زیر پشتیبانی می‌کند"
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
    GroupDocs.Parser for Python via .NET عملیات را با [فرمت‌های فایل](https://docs.groupdocs.com/parser/python-net/supported-document-formats/) زیر پشتیبانی می‌کند.
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
  title: "امکانات GroupDocs.Parser for Python via .NET"
  description: "داده‌ها را از PDFها، اسناد Office، تصاویر و سایر قالب‌ها به‌سرعت و با دقت با Python Document Parser SDK ما استخراج کنید."

  items:
    # feature loop
    - icon: "text"
      title: "استخراج متن"
      content: "اطلاعات متنی را از انواع قالب‌های فایل مانند اسناد Office، فایل‌های PDF و تصاویر استخراج کنید تا خوانایی و تجزیه و تحلیل آسان باشد."

    # feature loop
    - icon: "image"
      title: "استخراج تصاویر"
      content: "محتوای بصری را از منابع متنوعی مانند اسناد Office و فایل‌های PDF بازیابی کنید تا به‌راحتی دسترسی و استفاده شود."

    # feature loop
    - icon: "qr"
      title: "اسکن کدهای QR"
      content: "کدهای QR موجود در اسناد Office، فایل‌های PDF یا محتوای بصری را شناسایی و رمزگشایی کنید تا بازیابی اطلاعات به‌صورت کارآمد انجام شود."

    # feature loop
    - icon: "email"
      title: "استخراج داده‌ها از پیوست‌های ایمیل و آرشیوها"
      content: "اطلاعات ارزشمند را از پیام‌های ایمیل، پیوست‌های فایل و منابع داده فشرده جمع‌آوری کنید تا تجزیه و تحلیل و استفاده مؤثری داشته باشید."

    # feature loop
    - icon: "table"
      title: "استخراج جداول"
      content: "داده‌های جدول‌بندی شده را از اسناد PDF شناسایی و استخراج کنید تا برای تجزیه و تحلیل و استفاده سازمان‌یافته به کار رود."

    # feature loop
    - icon: "hyperlink"
      title: "استخراج هایپرلینک‌ها"
      content: "در اسناد office یا فایل‌های PDF، پیوندهای ابرمتن و آدرس‌های ایمیل را شناسایی و استخراج کنید تا دسترسی کارآمد شود."

    # feature loop
    - icon: "pdf"
      title: "تجزیه فرم‌های PDF"
      content: "فرم‌های PDF اسناد دیجیتالی هستند که شامل فیلدهای قابل پر شدن برای تعامل کاربر می‌باشند و امکان وارد کردن اطلاعات به صورت الکترونیکی را فراهم می‌کنند. Python API می‌تواند برای استخراج داده‌ها از این فرم‌ها جهت پردازش کارآمد مورد استفاده قرار گیرد."

    # feature loop
    - icon: "template"
      title: "تجزیه داده‌ها با الگوها"
      content: "الگوهای سفارشی ایجاد کنید و با استفاده از Python API برای تجزیه اطلاعات خاص از فایل‌های PDF به کار ببرید تا فرآیند استخراج داده‌ها ساده شود."

    # feature loop
    - icon: "search"
      title: "جستجوی متن در اسناد"
      content: "به‌سرعت کلمات یا الگوهای خاص را در اسناد پیدا کنید."


############################# Code samples ############################
code_samples:
  enable: true
  title: "نمونه‌های کد"
  description: "فراتر از استخراج متن پایه، در ادامه رایج‌ترین موارد استفاده برای استخراج سریع متن، تصویر و فراداده آورده شده است."
  items:
    # code sample loop
    - title: "جستجوی متن در یک سند"
      content: |
        این مثال نشان می‌دهد چگونه یک عبارت خاص را در سند PDF جستجو کرده و مکان یافتن آن را چاپ کنید.
        {{< landing/code title="جستجوی متن در یک سند با Python">}}
        ```python {style=abap}
        from groupdocs.parser import Parser

        # سند را بارگذاری کنید
        with Parser("sample.pdf") as parser:
            # اندیس صفحه و مستطیل مکان یافتن عبارت را چاپ کنید
            for area in parser.Search("Total Amount"):
                # اندیس صفحه و مستطیل مکان یافتن عبارت را چاپ کنید
                print(f"Page {area.PageIndex}, Rectangle: {area.Rectangle}")
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "استخراج تصاویر از یک سند"
      content: |
        این مثال نشان می‌دهد چگونه تصاویر را از سند PDF استخراج کرده و در فایلی ذخیره کنید.
        {{< landing/code title="استخراج تصاویر از یک سند با Python">}}
        ```python {style=abap}    
        from groupdocs.parser import Parser

        # سند را بارگذاری کنید
        with Parser("sample.docx") as parser:
            # تصاویر را از سند استخراج کنید
            images = parser.GetImages()

            # تصاویر را در یک فایل ذخیره کنید
            index = 1
            for image in images:
                image.Save(f"image_{index}.png")
                index += 1
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "استخراج فراداده از یک سند"
      content: |
        این مثال نشان می‌دهد چگونه فراداده را از سند PDF استخراج کرده و چاپ کنید.
        {{< landing/code title="استخراج فراداده از یک سند با Python">}}
        ```python {style=abap}    
        from groupdocs.parser import Parser

        # سند را بارگذاری کنید
        with Parser("sample.pdf") as parser:
            # فراداده را از سند استخراج کنید
            metadata = parser.GetMetadata()

            # فراداده را چاپ کنید
            for item in metadata:
                print(f"{item.Name}: {item.Value}")
        ```
        {{< /landing/code >}}
---
