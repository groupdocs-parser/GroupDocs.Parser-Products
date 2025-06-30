


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:19
draft: false
lang: fa
format: Ods
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "استخراج بارکدها از فایل‌های ODS در برنامه‌های C#"
head_description: "از GroupDocs.Parser برای شناسایی و استخراج داده‌های بارکد از فایل‌های ODS در C# بدون نیاز به نرم‌افزار اضافی استفاده کنید."

############################# Header ############################
title: "استخراج بارکدها از ODS با استفاده از C#" 
description: "با استفاده از GroupDocs.Parser اطلاعات بارکد را از فایل‌های PDF، Word، Excel و تصاویر در برنامه‌های .NET شناسایی و استخراج کنید."
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "دانلود نسخه آزمایشی رایگان"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "درباره API GroupDocs.Parser for .NET"
    link: "/parser/net/"
    link_title: "بیشتر بدانید"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/) یک API قدرتمند برای تجزیه اسناد برای توسعه‌دهندگان .NET است. این امکان را فراهم می‌کند تا متن، تصاویر، محتوای ساختاری و بارکدها را از قالب‌های مختلف فایل شامل PDF، Word، Excel، PowerPoint و غیره استخراج کنید — بدون نیاز به ابزارهای خارجی.

############################# Steps ############################
steps:
    enable: true
    title: "مراحل استخراج بارکدها از Ods در C#"
    content: |
      [GroupDocs.Parser](/parser/net/) به شما این امکان را می‌دهد که داده‌های بارکد را از فایل‌های ODS در برنامه‌های .NET با پیروی از این مراحل ساده استخراج کنید:
      
      1. فایل ODS را با استفاده از یک نمونه Parser بارگذاری کنید.
      2. بررسی کنید که آیا سند از استخراج بارکد پشتیبانی می‌کند.
      3. فهرست بارکدها را از سند بازیابی کنید.
      4. نتایج را تکرار کنید و از مقادیر بارکد استخراج‌شده استفاده کنید.
   
    code:
      platform: "net"
      copy_title: "کپی"
      install:
        command: |
        command: "dotnet add package GroupDocs.Parser"
        copy_tip: "برای کپی کلیک کنید"
        copy_done: "کپی شد"
      links:
        #  loop
        - title: "نمونه‌های بیشتر"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
        #  loop
        - title: "مستندات"
          link: "https://docs.groupdocs.com/parser/net/"
          
      content: |
        ```csharp {style=abap}
        // سند حاوی بارکدها را با استفاده از کلاس Parser بارگذاری کنید
        using (Parser parser = new Parser("input.ods")) {

            // بررسی کنید که آیا فایل از استخراج بارکد پشتیبانی می‌کند
            if (!parser.Features.Barcodes) {
                Console.WriteLine("استخراج بارکد پشتیبانی نمی‌شود");
                return;
            }

            // بارکدهای استخراج‌شده را بازیابی و پردازش کنید
            IEnumerable<PageBarcodeArea> barcodes = parser.GetBarcodes();

            foreach (PageBarcodeArea barcode in barcodes) {
                Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                Console.WriteLine("Value: " + barcode.Value);
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "ویژگی‌های پیشرفته تجزیه اسناد"
  description: "فراتر از استخراج بارکد، GroupDocs.Parser به شما امکان می‌دهد تا متن ساده، تصاویر و داده‌های ساختاری را برای پشتیبانی از فرآیندهای خودکار و پردازش داده‌های پیشرفته استخراج کنید."
  image: "/img/parser/features_extract-barcode.webp" # 500x500 px
  image_description: "شناسایی بارکد و تجزیه اسناد"
  features:
    # feature loop
    - title: "پشتیبانی از فرمت‌های مختلف بارکد"
      content: "انواع رایج بارکد شامل QR Code، Code 128، Data Matrix، EAN، Aztec و بیشتر را شناسایی کنید."

    # feature loop
    - title: "استخراج بارکدها از اسناد و تصاویر"
      content: "بارکدها را از اسناد PDF، Word، Excel و فرمت‌های تصویری مانند JPEG، PNG و BMP بخوانید."

    # feature loop
    - title: "تنظیمات استخراج قابل تنظیم"
      content: "گزینه‌های شناسایی مانند مناطق اسکن و پردازش اسناد چند صفحه‌ای را پیکربندی کنید."
      
  code_samples:
    # code sample loop
    - title: "چگونه بارکدها را از یک PDF با استفاده از گزینه‌های بارکد استخراج کنیم"
      content: |
        این مثال نشان می‌دهد که چگونه بارکدها را از یک فایل PDF با استفاده از گزینه‌های خاص استخراج بارکد استخراج کنیم.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  فایل PDF را با کلاس Parser بارگذاری کنید
        using (Parser parser = new Parser("input.pdf"))
        {
            // تأیید کنید که استخراج بارکد پشتیبانی می‌شود
            if (!parser.Features.Barcodes)
            {
                return;
            }

            // از گزینه‌های بارکد برای فیلتر نتایج استفاده کنید
            BarcodeOptions options = new BarcodeOptions(QualityMode.Low, QualityMode.Low, "QR");

            // داده‌های بارکد را از سند بازیابی کنید
            IEnumerable<PageBarcodeArea> barcodes = parser.GetBarcodes(options);

            // فهرست بارکدهای استخراج‌شده را پردازش کنید
            foreach (PageBarcodeArea barcode in barcodes)
            {
                Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                Console.WriteLine("Value: " + barcode.Value);
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
    - title: "دانلود Nuget"
      link: "https://releases.groupdocs.com/parser/net/"
      color: "red"
        #  loop
    - title: "مجوزدهی"
      link: "https://purchase.groupdocs.com/pricing/parser/net/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "قالب‌های پشتیبانی‌شده برای استخراج بارکد"
    exclude: "ODS"
    description: "GroupDocs.Parser از شناسایی بارکد در مجموعه وسیعی از قالب‌های اسنادی و تصویری پشتیبانی می‌کند. در زیر، انواع فایل‌های رایج پشتیبانی‌شده را ببینید."
    items: 
        # format loop 1
        - name: "تحلیل PDF"
          format: "PDF"
          link: "/parser/net/extract-barcode/pdf/"
          description: "(فرمت سند قابل حمل)"
          
        # format loop 2
        - name: "تحلیل DOCX"
          format: "DOCX"
          link: "/parser/net/extract-barcode/docx/"
          description: "(سند Word Office 2007+)"
          
        # format loop 3
        - name: "تحلیل PPTX"
          format: "PPTX"
          link: "/parser/net/extract-barcode/pptx/"
          description: "(فرمت ارائه Open XML)"
          
        # format loop 4
        - name: "تحلیل XLSX"
          format: "XLSX"
          link: "/parser/net/extract-barcode/xlsx/"
          description: "(دفتر کار Open XML)"
          
        # format loop 5
        - name: "تحلیل ODT"
          format: "ODT"
          link: "/parser/net/extract-barcode/odt/"
          description: "(سند متنی OpenDocument)"
          
        # format loop 6
        - name: "تحلیل ODS"
          format: "ODS"
          link: "/parser/net/extract-barcode/ods/"
          description: "(برگه محاسباتی OpenDocument)"
          
        # format loop 7
        - name: "تحلیل ODP"
          format: "ODP"
          link: "/parser/net/extract-barcode/odp/"
          description: "(ارائه OpenDocument)"
          
        # format loop 8
        - name: "تحلیل EPUB"
          format: "EPUB"
          link: "/parser/net/extract-barcode/epub/"
          description: "(فایل کتاب الکترونیکی Open)"
          
        # format loop 9
        - name: "تحلیل FB2"
          format: "FB2"
          link: "/parser/net/extract-barcode/fb2/"
          description: "(کتاب الکترونیکی FictionBook)"
         
          

---