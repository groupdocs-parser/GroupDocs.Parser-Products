


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:26
draft: false
lang: fa
format: Pdf
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "استخراج هایپرلینک‌ها از فایل‌های PDF در برنامه‌های C#"
head_description: "از GroupDocs.Parser برای شناسایی و استخراج هایپرلینک‌ها از فایل‌های PDF در C# بدون نیاز به ابزار یا نرم‌افزار اضافی استفاده کنید."

############################# Header ############################
title: "استخراج هایپرلینک‌ها از PDF با استفاده از C#" 
description: "URLها و هایپرلینک‌ها را از انواع اسناد مانند PDF، Word، Excel و ... با استفاده از GroupDocs.Parser در برنامه‌های .NET شناسایی و استخراج کنید."
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "نسخه رایگان را دانلود کنید"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "درباره API GroupDocs.Parser for .NET"
    link: "/parser/net/"
    link_title: "بیشتر بدانید"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/) یک API چندمنظوره برای تجزیه اسناد است که به توسعه‌دهندگان .NET خدمت می‌کند. این API قادر به استخراج هایپرلینک‌ها، متن، تصاویر و محتوای ساختاریافته از فرمت‌های مختلفی از جمله PDF، Word، Excel، HTML و غیره است—بدون نیاز به نرم‌افزار خارجی.

############################# Steps ############################
steps:
    enable: true
    title: "مراحل استخراج هایپرلینک‌ها از Pdf در C#"
    content: |
      [GroupDocs.Parser](/parser/net/) به توسعه‌دهندگان .NET این امکان را می‌دهد که هایپرلینک‌ها را از فایل‌های PDF با دنبال‌کردن مراحل ساده زیر استخراج کنند:
      
      1. فایل PDF را با استفاده از یک نمونه Parser بارگذاری کنید.
      2. بررسی کنید که آیا سند از استخراج هایپرلینک پشتیبانی می‌کند.
      3. لیست هایپرلینک‌ها را از سند بازیابی کنید.
      4. در نتایج حلقه بزنید و با URLهای استخراج‌شده کار کنید.
   
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
        // مدرکی که شامل هایپرلینک‌ها است را با استفاده از کلاس Parser بارگذاری کنید
        using (Parser parser = new Parser("input.pdf")) {

            // بررسی کنید که آیا فایل از استخراج هایپرلینک پشتیبانی می‌کند
            if (!parser.Features.Hyperlinks)
            {
                Console.WriteLine("استخراج هایپرلینک برای این فایل در دسترس نیست");
                return;
            }

            // لیست هایپرلینک‌های استخراج‌شده را بازیابی و پردازش کنید
            IEnumerable<PageHyperlinkArea> hyperlinks = parser.GetHyperlinks();

            foreach (PageHyperlinkArea h in hyperlinks)
            {
                Console.WriteLine(h.Text);
                Console.WriteLine(h.Url);
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "قابلیت‌های پیشرفته تجزیه اسناد"
  description: "علاوه بر استخراج هایپرلینک، GroupDocs.Parser به شما این امکان را می‌دهد که متن، متادیتا، تصاویر و داده‌های ساختاریافته را استخراج کنید—که از جریان‌های پردازش داده قدرتمند پشتیبانی می‌کند."
  image: "/img/parser/features_extract-hyperlink.webp" # 500x500 px
  image_description: "شناسایی هایپرلینک و تجزیه سند"
  features:
    # feature loop
    - title: "شناسایی هایپرلینک‌ها از اسناد"
      content: "به سرعت URLها و یادداشت‌های انوتیشن لینک را از اسنادی مانند PDFها، فایل‌های Word، صفحات‌گسترده و دیگر اسناد استخراج کنید."

    # feature loop
    - title: "پشتیبانی از لینک‌های وب و لینک‌های جاسازی‌شده"
      content: "شناسایی و استخراج هم URLهای وب و هم لینک‌های جاسازی‌شده در فرمت‌های مختلف."

    # feature loop
    - title: "گزینه‌های تجزیه انعطاف‌پذیر"
      content: "تنظیمات استخراج را برای اسکن بخش‌ها یا صفحات خاص سفارشی کنید تا عملکرد و دقت بهبود یابد."
      
  code_samples:
    # code sample loop
    - title: "چگونه هایپرلینک‌ها را از یک PDF با گزینه‌های لینک استخراج کنیم"
      content: |
        این مثال کد نشان می‌دهد که چگونه می‌توان همه هایپرلینک‌ها را از یک فایل PDF با استفاده از گزینه‌های سفارشی استخراج کرد.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  نمونه Parser را با سند PDF مقداردهی اولیه کنید
        using (Parser parser = new Parser("input.docx"))
        {
            // بررسی کنید که آیا استخراج هایپرلینک پشتیبانی می‌شود یا خیر
            if (!parser.Features.Hyperlinks)
            {
                return;
            }

            // گزینه‌های استخراج لینک را تنظیم کنید تا نتایج را محدود کنید
            PageAreaOptions options = new PageAreaOptions(new Rectangle(new Point(380, 90), new Size(150, 50)));

            // داده‌های هایپرلینک را از سند استخراج کنید
            IEnumerable<PageHyperlinkArea> hyperlinks = parser.GetHyperlinks(options);

            // لیست لینک‌های استخراج‌شده را مدیریت کنید
            foreach (PageHyperlinkArea h in hyperlinks)
            {
                Console.WriteLine(h.Text);
                Console.WriteLine(h.Url);
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
    title: "فرمت‌های پشتیبانی‌شده برای استخراج هایپرلینک"
    exclude: "PDF"
    description: "GroupDocs.Parser می‌تواند هایپرلینک‌ها را از انواع مختلفی از اسناد استخراج کند. فرمت‌های معمولی پشتیبانی‌شده در زیر آمده است."
    items: 
        # format loop 1
        - name: "تحلیل PDF"
          format: "PDF"
          link: "/parser/net/extract-hyperlink/pdf/"
          description: "(فرمت سند قابل حمل)"
          
        # format loop 2
        - name: "تحلیل DOCX"
          format: "DOCX"
          link: "/parser/net/extract-hyperlink/docx/"
          description: "(سند Word Office 2007+)"
          
        # format loop 3
        - name: "تحلیل PPTX"
          format: "PPTX"
          link: "/parser/net/extract-hyperlink/pptx/"
          description: "(فرمت ارائه Open XML)"
          
        # format loop 4
        - name: "تحلیل XLSX"
          format: "XLSX"
          link: "/parser/net/extract-hyperlink/xlsx/"
          description: "(دفتر کار Open XML)"
          
        # format loop 5
        - name: "تحلیل TXT"
          format: "TXT"
          link: "/parser/net/extract-hyperlink/txt/"
          description: "(فایل متنی)"
          
        # format loop 6
        - name: "تحلیل RTF"
          format: "RTF"
          link: "/parser/net/extract-hyperlink/rtf/"
          description: "(فرمت متن غنی)"
          
        # format loop 7
        - name: "تحلیل XML"
          format: "XML"
          link: "/parser/net/extract-hyperlink/xml/"
          description: "(زبان نشانه‌گذاری قابل توسعه)"
          
        # format loop 8
        - name: "تحلیل EPUB"
          format: "EPUB"
          link: "/parser/net/extract-hyperlink/epub/"
          description: "(فایل کتاب الکترونیکی Open)"
         
          

---