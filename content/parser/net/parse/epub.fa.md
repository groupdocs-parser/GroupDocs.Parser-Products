


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:53
draft: false
lang: fa
format: Epub
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "پارسر داده‌ها از فایل‌های EPUB در برنامه‌های C#"
head_description: "از GroupDocs.Parser برای استخراج متن، تصاویر، جداول و داده‌های دیگر از فایل‌های EPUB در C# بدون نیاز به ابزارهای شخص ثالث استفاده کنید."

############################# Header ############################
title: "استخراج اسناد EPUB با استفاده از C#" 
description: "با استفاده از GroupDocs.Parser به‌طور کارآمد متن، متادیتا، جداول و تصاویر را از فایل‌های PDF، Word، Excel و تصاویر استخراج کنید در پروژه‌های .NET خود."
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
       [GroupDocs.Parser](/parser/net/) یک API جامع پارسر اسنادی است که برای توسعه‌دهندگان .NET طراحی شده است. این API قابلیت استخراج متن ساده و ساختار یافته، متادیتا، تصاویر، جداول و بارکدها را از فرمت‌های محبوبی همچون PDF، DOCX، XLSX، PPTX و غیره پشتیبانی می‌کند — همه اینها بدون نیاز به نرم‌افزارهای اضافی.

############################# Steps ############################
steps:
    enable: true
    title: "مراحل استخراج داده از Epub در C#"
    content: |
      این مراحل را دنبال کنید تا محتوا را از اسناد EPUB در برنامه‌های .NET خود با استفاده از [GroupDocs.Parser](/parser/net/) پارس کنید:
      
      1. سند EPUB را با استفاده از یک نمونه Parser بارگذاری کنید.
      2. محتوای مورد نظر مانند متن، جداول یا متادیتا را استخراج کنید.
      3. بررسی کنید که داده‌های استخراج‌شده معتبر است.
      4. از خروجی پارس‌شده در پردازش‌های بعدی، اتوماسیون یا سیستم‌های کسب‌وکار خود استفاده کنید.
   
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
        // سند خود را به Parser بارگذاری کنید
        using (Parser parser = new Parser("input.epub")) {

            // تمام محتوای متنی را از فایل استخراج کنید
            using (TextReader reader = parser.GetText()) 
            {
                // اگر متن موجود نباشد، نتیجه نال خواهد بود
                // متن استخراج‌شده را در برنامه خود استفاده کنید
                Console.WriteLine(reader == null ? 
                    "استخراج متن برای این فرمت پشتیبانی نمی‌شود" : reader.ReadToEnd());
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "قابلیت‌های جامع پارس اسناد"
  description: "GroupDocs.Parser بیش از فقط خواندن متن را امکان‌پذیر می‌کند — این API از استخراج بارکد، پارس تصاویر، دسترسی به متادیتا و پردازش داده‌های ساختار یافته برای اتوماسیون و تحلیل داده‌های پیشرفته پشتیبانی می‌کند."
  image: "/img/parser/features_parse.webp" # 500x500 px
  image_description: "قابلیت‌های استخراج محتوا و پارس اسناد"
  features:
    # feature loop
    - title: "پشتیبانی از انواع محتواهای مختلف فایل"
      content: "داده‌ها را شامل متن، تصاویر، جداول و فیلدها از فرمت‌های اسنادی مانند PDF، Word، Excel، HTML و بیشتر استخراج کنید."

    # feature loop
    - title: "کار با فایل‌های اسکن‌شده و دیجیتالی"
      content: "داده‌ها را از اسناد اسکن‌شده و فایل‌های دیجیتالی استخراج کنید، با پشتیبانی از OCR و استخراج آگاه به طرح."

    # feature loop
    - title: "پارامترهای استخراج قابل تنظیم"
      content: "منطق پارس را با گزینه‌های انعطاف‌پذیر مانند انتخاب محدوده صفحه، هدف‌گذاری حوزه و الگوهای تشخیص فیلد تنظیم کنید."
      
  code_samples:
    # code sample loop
    - title: "نحوه پارس PDF با استفاده از الگوها"
      content: |
        این مثال نشان می‌دهد که چگونه می‌توان داده‌های ساختار یافته را از یک PDF با استفاده از یک الگوی پارس پیش‌تعریف‌شده با GroupDocs.Parser استخراج کرد.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  فایل PDF را با کلاس Parser بارگذاری کنید
        using (Parser parser = new Parser("input.pdf"))
        {
            // سند را بر اساس الگو پارس کنید
            DocumentData data = parser.ParseByTemplate(GetTemplate());

            // بررسی کنید که آیا استخراج فرم پشتیبانی می‌شود
            if (data == null)
            {
                return;
            }

            // فیلدهای به‌دست‌آمده را پردازش کنید
            for (int i = 0; i < data.Count; i++)
            {
                Console.Write(data[i].Name + ": ");
                PageTextArea area = data[i].PageArea as PageTextArea;
                Console.WriteLine(area == null ? "Not a template field" : area.Text);
            }
        }

        private static Template GetTemplate()
        {
            // پارامترهای تشخیص برای جدول 'جزئیات' بسازید
            TemplateTableParameters detailsTableParameters = 
                new TemplateTableParameters(new Rectangle(new Point(35, 320), new Size(530, 55)), null);

            TemplateItem[] templateItems = new TemplateItem[]
            {
                new TemplateTable(detailsTableParameters, "details", null)
            };

            Template template = new Template(templateItems);
            return template;
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
    title: "فرمت‌های پشتیبانی‌شده برای استخراج داده"
    exclude: "EPUB"
    description: "GroupDocs.Parser امکان پارس کردن در مجموعه وسیعی از فرمت‌های اسنادی و تصویری را فراهم می‌کند. فرمت‌های فایل‌های پشتیبانی‌شده که به‌طور معمول در گردش‌کارهای استخراج داده استفاده می‌شوند را بررسی کنید."
    items: 
        # format loop 1
        - name: "تحلیل PDF"
          format: "PDF"
          link: "/parser/net/parse/pdf/"
          description: "(فرمت سند قابل حمل)"
          
        # format loop 2
        - name: "تحلیل DOCX"
          format: "DOCX"
          link: "/parser/net/parse/docx/"
          description: "(سند Word Office 2007+)"
          
        # format loop 3
        - name: "تحلیل PPTX"
          format: "PPTX"
          link: "/parser/net/parse/pptx/"
          description: "(فرمت ارائه Open XML)"
          
        # format loop 4
        - name: "تحلیل XLSX"
          format: "XLSX"
          link: "/parser/net/parse/xlsx/"
          description: "(دفتر کار Open XML)"
          
        # format loop 5
        - name: "تحلیل TXT"
          format: "TXT"
          link: "/parser/net/parse/txt/"
          description: "(فایل متنی)"
          
        # format loop 6
        - name: "تحلیل RTF"
          format: "RTF"
          link: "/parser/net/parse/rtf/"
          description: "(فرمت متن غنی)"
          
        # format loop 7
        - name: "تحلیل XML"
          format: "XML"
          link: "/parser/net/parse/xml/"
          description: "(زبان نشانه‌گذاری قابل توسعه)"
          
        # format loop 8
        - name: "تحلیل EPUB"
          format: "EPUB"
          link: "/parser/net/parse/epub/"
          description: "(فایل کتاب الکترونیکی Open)"
         
          

---