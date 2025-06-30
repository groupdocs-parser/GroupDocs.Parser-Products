


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:33
draft: false
lang: fa
format: Pdf
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "استخراج تصاویر از فایل‌های PDF در برنامه‌های C#"
head_description: "از GroupDocs.Parser برای شناسایی و استخراج تصاویر از فایل‌های PDF در C# بدون نیاز به ابزارهای اضافی استفاده کنید."

############################# Header ############################
title: "استخراج تصاویر از PDF با استفاده از C#" 
description: "تصاویر embedded را از PDF ها، اسناد Word، شیت‌های Excel و سایر نوع فایل‌ها با استفاده از GroupDocs.Parser در برنامه‌های .NET خود پیدا و استخراج کنید."
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "دانلود نسخه رایگان"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "درباره API GroupDocs.Parser for .NET"
    link: "/parser/net/"
    link_title: "بیشتر بدانید"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/) یک کتابخانه قدرتمند برای تجزیه اسناد برای توسعه‌دهندگان .NET است. این امکان را به شما می‌دهد که تصاویر، متن، لینک‌های Hyperlink و داده‌های ساختاری را از فرمت‌های فایل محبوب مانند PDF، DOCX، XLSX، PPTX و دیگران استخراج کنید — بدون نیاز به برنامه‌های شخص ثالث.

############################# Steps ############################
steps:
    enable: true
    title: "مراحل استخراج تصاویر از Pdf در C#"
    content: |
      با [GroupDocs.Parser](/parser/net/)، می‌توانید تصاویر را از اسناد PDF در پروژه‌های .NET خود تنها با چند مرحله استخراج کنید:
      
      1. با فایل PDF Parser را راه‌اندازی کنید.
      2. عناصر تصویر را از سند بازیابی کنید.
      3. از تصاویر استخراج‌شده در جریان کاری خود به‌طور لازم استفاده کنید.
   
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
        // مدرکی که شامل تصاویر است را با استفاده از Parser باز کنید
        using (Parser parser = new Parser("input.pdf")) {

            // همه تصاویر embedded را از فایل استخراج کنید
            IEnumerable<PageImageArea> images = parser.GetImages();

            // مواردی را که در آن‌ها هیچ تصویری وجود ندارد مدیریت کنید
            if (images == null)
            {
                return;
            }

            // تصاویر استخراج‌شده را پردازش یا ذخیره کنید
            foreach (PageImageArea image in images)
            {
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Type: {2}", 
                    image.Page.Index, image.Rectangle, image.FileType));
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "استخراج جامع محتوای سند"
  description: "GroupDocs.Parser فراتر از استخراج تصاویر است — شما می‌توانید متن خام، لینک‌های Hyperlink، metadata و محتواهای ساختاری را برای سناریوهای اتوماسیون پیشرفته استخراج کنید."
  image: "/img/parser/features_extract-image.webp" # 500x500 px
  image_description: "جریان کار استخراج تصویر و تجزیه اسناد"
  features:
    # feature loop
    - title: "استخراج تصاویر از چندین فرمت"
      content: "تصاویر embedded را از انواع مختلف فرمت‌های فایل، از جمله DOCX، PDF، PPTX، XLSX و فایل‌های تصویری مانند PNG، JPG و TIFF استخراج کنید."

    # feature loop
    - title: "حفظ کیفیت تصویر اصلی"
      content: "تصاویر با دقت بالا استخراج می‌شوند و وضوح، فرمت و پروفایل رنگ اصلی آن‌ها حفظ می‌شود."

    # feature loop
    - title: "گزینه‌های استخراج پیشرفته"
      content: "استخراج تصویر را با فیلتر کردن بر اساس صفحه، فرمت یا وضوح سفارشی کنید و از چندین صفحه پشتیبانی کنید."
      
  code_samples:
    # code sample loop
    - title: "چگونه تصاویر را از یک سند PDF استخراج و ذخیره کنیم"
      content: |
        این مثال نشان می‌دهد که چگونه همه دارایی‌های تصویری را از یک فایل PDF استخراج کرده و آن‌ها را به سیستم فایل محلی ذخیره کنید.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  PDF را با استفاده از کلاس Parser بارگذاری کنید
        using (Parser parser = new Parser("input.pdf"))
        {
            // تصاویر embedded را از فایل استخراج کنید
            IEnumerable<PageImageArea> images = parser.GetImages();

            // فرمت خروجی و گزینه‌های تصویر (مانند PNG) را تنظیم کنید
            ImageOptions options = new ImageOptions(ImageFormat.Png);

            // تصاویر استخراج‌شده را در دیسک بنویسید
            int imageNumber = 0;
            foreach (PageImageArea image in images)
            {
                image.Save(imageNumber.ToString() + ".png", options);
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
    title: "فرمت‌های پشتیبانی‌شده برای استخراج تصویر"
    exclude: "PDF"
    description: "GroupDocs.Parser استخراج تصاویر دقیق از دامنه وسیعی از فرمت‌های اسناد و تصاویر را تسهیل می‌کند. لیست زیر شامل انواع رایج پشتیبانی‌شده است."
    items: 
        # format loop 1
        - name: "تحلیل PDF"
          format: "PDF"
          link: "/parser/net/extract-image/pdf/"
          description: "(فرمت سند قابل حمل)"
          
        # format loop 2
        - name: "تحلیل DOCX"
          format: "DOCX"
          link: "/parser/net/extract-image/docx/"
          description: "(سند Word Office 2007+)"
          
        # format loop 3
        - name: "تحلیل PPTX"
          format: "PPTX"
          link: "/parser/net/extract-image/pptx/"
          description: "(فرمت ارائه Open XML)"
          
        # format loop 4
        - name: "تحلیل XLSX"
          format: "XLSX"
          link: "/parser/net/extract-image/xlsx/"
          description: "(دفتر کار Open XML)"
          
        # format loop 5
        - name: "تحلیل ODT"
          format: "ODT"
          link: "/parser/net/extract-image/odt/"
          description: "(سند متنی OpenDocument)"
          
        # format loop 6
        - name: "تحلیل ODS"
          format: "ODS"
          link: "/parser/net/extract-image/ods/"
          description: "(برگه محاسباتی OpenDocument)"
          
        # format loop 7
        - name: "تحلیل ODP"
          format: "ODP"
          link: "/parser/net/extract-image/odp/"
          description: "(ارائه OpenDocument)"
          
        # format loop 8
        - name: "تحلیل EPUB"
          format: "EPUB"
          link: "/parser/net/extract-image/epub/"
          description: "(فایل کتاب الکترونیکی Open)"
          
        # format loop 9
        - name: "تحلیل FB2"
          format: "FB2"
          link: "/parser/net/extract-image/fb2/"
          description: "(کتاب الکترونیکی FictionBook)"
         
          

---