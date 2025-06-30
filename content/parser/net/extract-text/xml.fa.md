


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:47
draft: false
lang: fa
format: Xml
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "استخراج متن از فایل‌های XML در اپلیکیشن‌های C#"
head_description: "از GroupDocs.Parser برای استخراج متن ساده یا ساختاریافته از فایل‌های XML در اپلیکیشن‌های C# بدون نیاز به ابزارهای خارجی استفاده کنید."

############################# Header ############################
title: "استخراج متن از XML با استفاده از C#" 
description: "به‌سرعت متن قابل خواندن و ساختاریافته را از فایل‌های PDF، Word، Excel و سایر انواع فایل با استفاده از GroupDocs.Parser در راه‌حل‌های .NET خود استخراج کنید."
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "داستان رایگان را دانلود کنید"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "درباره API GroupDocs.Parser for .NET"
    link: "/parser/net/"
    link_title: "بیشتر بدانید"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/) یک API با عملکرد بالا برای تجزیه اسناد برای توسعه‌دهندگان .NET است. این API استخراج متن، تصاویر، جداول و محتوای ساختاریافته از چندین فرمت فایل از جمله PDF، DOCX، XLSX، PPTX و بیشتر را بدون وابستگی به کتابخانه‌های شخص ثالث آسان می‌کند.

############################# Steps ############################
steps:
    enable: true
    title: "مراحل استخراج متن از Xml در C#"
    content: |
      شما می‌توانید متن تمیز و ساختاریافته را از اسناد XML در اپلیکیشن‌های .NET با دنبال کردن این مراحل با [GroupDocs.Parser](/parser/net/) استخراج کنید:
      
      1. اسناد XML را با استفاده از یک نمونه Parser باز کنید.
      2. متن را از محتوای فایل استخراج کنید.
      3. نتیجه را بررسی کنید تا اطمینان حاصل شود که استخراج متن موفقیت‌آمیز بود.
      4. از متن استخراج شده در منطق کسب‌وکار، ایندکس‌گذاری یا پایپ‌لاین‌های داده خود استفاده کنید.
   
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
        // مدارک خود را به Parser بارگذاری کنید
        using (Parser parser = new Parser("input.xml")) {

            // تمام محتوای متنی را از فایل استخراج کنید
            using (TextReader reader = parser.GetText()) 
            {
                // اگر متن موجود نیست، نتیجه null خواهد بود
                // از متن استخراج شده در اپلیکیشن خود استفاده کنید
                Console.WriteLine(reader == null ? 
                    "استخراج متن برای این فرمت پشتیبانی نمی‌شود" : reader.ReadToEnd());
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "ویژگی‌های جامع استخراج محتوا"
  description: "علاوه بر متن ساده، GroupDocs.Parser می‌تواند تصاویر، عناصر ساختاریافته و متا دیتا را استخراج کند تا از تجزیه و تحلیل محتوا، تبدیل و اتوماسیون پشتیبانی کند."
  image: "/img/parser/features_extract-text.webp" # 500x500 px
  image_description: "شناسایی متن و تجزیه اسناد ساختاریافته"
  features:
    # feature loop
    - title: "استخراج متن از انواع فایل‌های مختلف"
      content: "متن ساده یا ساختاریافته را از فرمت‌هایی مانند PDF، DOCX، XLSX، PPTX، HTML و دیگر فرمت‌ها دریافت کنید."

    # feature loop
    - title: "پردازش متن از اسناد و تصاویر"
      content: "متن را از تصاویر اسکن‌شده، ارائه‌ها، صفحه‌گسترده‌ها و اسناد دیجیتال در حالی که ساختار حفظ می‌شود، استخراج کنید."

    # feature loop
    - title: "پیکربندی پیشرفته استخراج متن"
      content: "نحوه شناسایی متن را سفارشی کنید—محدوده‌های صفحه، مناطق چیدمان را تعریف کنید و خروجی را برای حداکثر دقت تنظیم نمایید."
      
  code_samples:
    # code sample loop
    - title: "چگونه مناطق متنی را از یک فایل PPTX استخراج کنیم"
      content: |
        این نمونه کد نشان می‌دهد که چگونه محتویات متنی را همراه با مختصات ناحیه از یک فایل پاورپوینت با استفاده از GroupDocs.Parser بازیابی کنید.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  ارائه پاورپوینت را با Parser بارگذاری کنید
        using (Parser parser = new Parser("input.pptx"))
        {
            // تمام مستطیل‌های مناطق متنی را از سند استخراج کنید
            IEnumerable<PageTextArea> areas = parser.GetTextAreas();

            // اگر استخراج ناحیه متنی در دسترس نیست، خارج شوید
            if (areas == null)
            {
                return;
            }

            // در هر صفحه از نواحی متنی عبور کنید
            foreach (PageTextArea a in areas)
            {
                // به ایندکس صفحه، مستطیل ناحیه و مقدار متن دسترسی پیدا کنید
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Text: {2}", a.Page.Index, a.Rectangle, a.Text));
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
    title: "فرمت‌های پشتیبانی‌شده برای استخراج متن"
    exclude: "XML"
    description: "GroupDocs.Parser استخراج متن را از مجموعه وسیعی از انواع مدارک و تصاویر ممکن می‌سازد. فرمت‌های معمول پشتیبانی شده در زیر را بررسی کنید."
    items: 
        # format loop 1
        - name: "تحلیل PDF"
          format: "PDF"
          link: "/parser/net/extract-text/pdf/"
          description: "(فرمت سند قابل حمل)"
          
        # format loop 2
        - name: "تحلیل DOCX"
          format: "DOCX"
          link: "/parser/net/extract-text/docx/"
          description: "(سند Word Office 2007+)"
          
        # format loop 3
        - name: "تحلیل PPTX"
          format: "PPTX"
          link: "/parser/net/extract-text/pptx/"
          description: "(فرمت ارائه Open XML)"
          
        # format loop 4
        - name: "تحلیل XLSX"
          format: "XLSX"
          link: "/parser/net/extract-text/xlsx/"
          description: "(دفتر کار Open XML)"
          
        # format loop 5
        - name: "تحلیل TXT"
          format: "TXT"
          link: "/parser/net/extract-text/txt/"
          description: "(فایل متنی)"
          
        # format loop 6
        - name: "تحلیل RTF"
          format: "RTF"
          link: "/parser/net/extract-text/rtf/"
          description: "(فرمت متن غنی)"
          
        # format loop 7
        - name: "تحلیل XML"
          format: "XML"
          link: "/parser/net/extract-text/xml/"
          description: "(زبان نشانه‌گذاری قابل توسعه)"
          
        # format loop 8
        - name: "تحلیل EPUB"
          format: "EPUB"
          link: "/parser/net/extract-text/epub/"
          description: "(فایل کتاب الکترونیکی Open)"
         
          

---