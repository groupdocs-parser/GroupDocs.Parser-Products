


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:40
draft: false
lang: fa
format: Xlsx
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "استخراج جداول از فایل‌های XLSX در برنامه‌های C#"
head_description: "از GroupDocs.Parser برای شناسایی و استخراج داده‌های جدول ساختاری از فایل‌های XLSX در برنامه‌های C# بدون وابستگی‌های اضافی استفاده کنید."

############################# Header ############################
title: "استخراج جداول از XLSX با استفاده از C#" 
description: "به سرعت ساختارهای جدول را از PDF، Word، Excel و سایر فرمت‌های فایل با استفاده از GroupDocs.Parser در پروژه‌های .NET خود شناسایی و استخراج کنید."
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
       [GroupDocs.Parser](/parser/net/) یک API جامع برای تجزیه اسناد است که برای توسعه‌دهندگان .NET ساخته شده است. این API امکان استخراج دقیق متن، جداول، تصاویر، پیوندهای هایپر و سایر عناصر ساختاری را از فرمت‌هایی مانند PDF، DOCX، XLSX، PPTX و بسیاری دیگر فراهم می‌کند — بدون نیاز به نرم‌افزارهای ثالث.

############################# Steps ############################
steps:
    enable: true
    title: "مراحل استخراج جداول از Xlsx در C#"
    content: |
      برای استخراج جداول از فایل‌های XLSX با استفاده از [GroupDocs.Parser](/parser/net/) در محیط .NET خود این دستورالعمل‌ها را دنبال کنید:
      
      1. یک نمونه Parser را مقداردهی اولیه کرده و سند XLSX خود را بارگذاری کنید.
      2. بررسی کنید که آیا استخراج جدول برای فرمت ورودی پشتیبانی می‌شود.
      3. محتوای جدول را از فایل استخراج کنید.
      4. از داده‌های جدول ساختاری برای گزارش‌دهی، اتوماسیون یا آنالیز استفاده کنید.
   
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
        // مدرکی که شامل داده‌های جدول است را با استفاده از Parser باز کنید
        using (Parser parser = new Parser("input.xlsx")) {

            // بررسی کنید که آیا فرمت از شناسایی جدول پشتیبانی می‌کند
            if (!parser.Features.Tables) {
                Console.WriteLine("مدارک را مدیریت کنید که از تجزیه جدول پشتیبانی نمی‌کنند");
                return;
            }

            // تعریف کنید که چگونه ساختار جدول شناسایی شود
            TemplateTableLayout layout = new TemplateTableLayout(
                new double[] { 50, 95, 275, 415, 485, 545 },
                new double[] { 325, 340, 365, 395 });

            // پارامترهای استخراج برای داده‌های جدول را مشخص کنید
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            //  جداول را از محتوای فایل استخراج کنید
            IEnumerable<PageTableArea> tables = parser.GetTables(options);

            //  در هر جدول شناسایی شده حلقه بزنید
            foreach (PageTableArea t in tables)
            {
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "قابلیت‌های قدرتمند استخراج داده"
  description: "علاوه بر تجزیه جدول، GroupDocs.Parser می‌تواند محتوای غنی مانند بلوک‌های متنی، تصاویر، متاداده و سایر داده‌های ساختاری را برای تسهیل در اتوماسیون اسناد استخراج کند."
  image: "/img/parser/features_extract-table.webp" # 500x500 px
  image_description: "شناسایی جدول و استخراج محتوا"
  features:
    # feature loop
    - title: "تشخیص دقیق جدول در چند فرمت"
      content: "داده‌های جدولی را از DOCX، XLSX، PDF، HTML و فرمت‌های مشابه با دقت بالا استخراج کنید."

    # feature loop
    - title: "تجزیه ساختارهای جدول از فایل‌ها"
      content: "با دقت داده‌های جدول را از اسناد و صفحات گسترده بدون از دست دادن فرمت بازیابی کنید."

    # feature loop
    - title: "پیکربندی سفارشی استخراج جدول"
      content: "تشخیص چیدمان، تراز ستون‌ها و گزینه‌های سرصفحه/پاورقی را برای کنترل دقیق خروجی تنظیم کنید."
      
  code_samples:
    # code sample loop
    - title: "چگونه جداول را از صفحات گسترده Excel استخراج کنیم"
      content: |
        این نمونه کد نشان می‌دهد که چگونه می‌توان داده‌های جدول را در یک فایل XLSX با استفاده از GroupDocs.Parser خواند و به آنها دسترسی پیدا کرد.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  فایل Excel را با استفاده از API Parser باز کنید
        using (Parser parser = new Parser("input.xlsx"))
        {
            // اگر نمی‌توان جداول را از فایل استخراج کرد خارج شوید
            if (!parser.Features.Tables)
            {
                return;
            }

            // از قوانین چیدمان برای مکان‌یابی محتویات جدولی استفاده کنید
            TemplateTableLayout layout = new TemplateTableLayout(
                    new double[] { 50, 95, 275, 415, 485, 545 },
                    new double[] { 325, 340, 365, 395 });

            // پارامترهای استخراج برای جداول را تنظیم کنید
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            // عملیات استخراج جدول را انجام دهید
            IEnumerable<PageTableArea> tables = parser.GetTables(options);

            // در هر ساختار جدول شناسایی شده بروید
            foreach (PageTableArea t in tables)
            {
                // در هر ردیف جدول حلقه بزنید
                for (int row = 0; row < t.RowCount; row++)
                {
                    // در سلول‌های هر ردیف حلقه بزنید
                    for (int column = 0; column < t.ColumnCount; column++)
                    {
                        // به سلول فعلی جدول دسترسی پیدا کنید
                        PageTableAreaCell cell = t[row, column];
                        if (cell != null)
                        {
                            // محتوای متنی هر سلول را نمایش دهید
                            Console.Write(cell.Text);
                            Console.Write(" | ");
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
    title: "فرمت‌های پشتیبانی شده برای استخراج جدول"
    exclude: "XLSX"
    description: "GroupDocs.Parser می‌تواند داده‌های جدول را از انواع مختلف فایل‌ها استخراج کند. در زیر فرمت‌های پرکاربرد برای تجزیه جدول‌های ساختاری آمده است."
    items: 
        # format loop 1
        - name: "تحلیل PDF"
          format: "PDF"
          link: "/parser/net/extract-table/pdf/"
          description: "(فرمت سند قابل حمل)"
          
        # format loop 2
        - name: "تحلیل DOCX"
          format: "DOCX"
          link: "/parser/net/extract-table/docx/"
          description: "(سند Word Office 2007+)"
          
        # format loop 3
        - name: "تحلیل PPTX"
          format: "PPTX"
          link: "/parser/net/extract-table/pptx/"
          description: "(فرمت ارائه Open XML)"
          
        # format loop 4
        - name: "تحلیل XLSX"
          format: "XLSX"
          link: "/parser/net/extract-table/xlsx/"
          description: "(دفتر کار Open XML)"
          
        # format loop 5
        - name: "تحلیل TXT"
          format: "TXT"
          link: "/parser/net/extract-table/txt/"
          description: "(فایل متنی)"
          
        # format loop 6
        - name: "تحلیل RTF"
          format: "RTF"
          link: "/parser/net/extract-table/rtf/"
          description: "(فرمت متن غنی)"
          
        # format loop 7
        - name: "تحلیل XML"
          format: "XML"
          link: "/parser/net/extract-table/xml/"
          description: "(زبان نشانه‌گذاری قابل توسعه)"
          
        # format loop 8
        - name: "تحلیل EPUB"
          format: "EPUB"
          link: "/parser/net/extract-table/epub/"
          description: "(فایل کتاب الکترونیکی Open)"
         
          

---