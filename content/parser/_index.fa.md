---
############################# Static ############################
layout: "family"
date:  2025-12-09T14:52:35
draft: false

product: "Parser"
product_tag: "parser"

lang: fa

############################# Head ############################
head_title: "SDKهای تجزیه‌کننده اسناد برای PDF، Word و Excel | GroupDocs"
head_description: "SDK تجزیه‌کننده اسناد برای استخراج متن، تصویر، متادیتا، بارکدها و جدول‌ها از PDF، Word، Excel، ایمیل‌ها و بیش از 50 فرمت دیگر اسناد برای برنامه‌های .NET، Java و Python."

############################# Header ############################
title: "SDK تجزیه‌کننده اسناد"
description:  |
  SDK تجزیه‌کننده اسناد کاربرپسند برای توسعه‌دهندگان جهت استخراج متن، تصویر، بارکد، متادیتا و جدول‌ها از بیش از 50 فرمت سند و تصویر.

  تجزیه‌کردن اسناد با عملکرد بالا را با کمترین کدنویسی در برنامه‌های .NET، Java و Python خود ادغام کنید.

  از قالب‌های انعطاف‌پذیر و APIهای پیشرفته استفاده کنید تا قوانین تجزیه را سفارشی کنید و خروجی‌های داده‌ای ساختار یافته و تمیز ارائه دهید.

############################# Supported Platforms ###############################
supported_platforms:
  enable: true
  head_title: "پلتفرم خود را انتخاب کنید"
  title: "استقلال پلتفرم"
  description: "GroupDocs.Parser کتابخانه از سیستم‌عامل‌ها و چارچوب‌های زیر پشتیبانی می‌کند:"
  details_link_title: "اطلاعات بیشتر"

  items:
    # items loop
    - title: ".NET"
      description: GroupDocs.Parser for .NET 
      color: "blue"
      tag: "net"
      link: "/parser/net/"
      features_link: "https://docs.groupdocs.com/parser/net/system-requirements/"
      features:
          # features loop
          - rows: "3"
            content: |
                    .NET Framework 4.6.2 or higher <br> .NET Core 2.0 or higher <br> .NET 6.0 or higher
      
          # features loop
          - rows: "1"
            content: |
                    Windows <br> Linux <br> Mac OS
      
          # features loop
          - rows: "4"
            content: |
                    Microsoft Visual Studio <br> JetBrains Rider <br> Microsoft Visual Code
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats
      

    # items loop
    - title: "Java"
      description: GroupDocs.Parser for Java
      color: "red"
      tag: "java"
      link: "/parser/java/"
      features_link: "https://docs.groupdocs.com/parser/java/system-requirements/"
      features:
          # features loop
          - rows: "3"
            content: |
                    Java 8 or higher <br> Kotlin
      
          # features loop
          - rows: "1"
            content: |
                    Windows <br> Linux <br> Mac OS
      
          # features loop
          - rows: "4"
            content: |
                    IntelliJ IDEA <br> Eclipse <br> NetBeans
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats


    # items loop
    - title: "Python"
      description: GroupDocs.Parser for Python
      color: "yellow"
      tag: "python-net"
      link: "/parser/python-net/"
      features_link: "https://docs.groupdocs.com/parser/python-net/system-requirements/"
      features:
          # features loop
          - rows: "3"
            content: |
                    Python 3.5+
      
          # features loop
          - rows: "1"
            content: |
                    Windows <br> Linux <br> macOS
      
          # features loop
          - rows: "4"
            content: |
                    PyCharm, VS Code, Jupyter Notebook
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats                    

############################# Features ###############################
features:
  enable: true
  title: "GroupDocs.Parser در یک نگاه"
  description: "SDK قدرتمند تجزیه‌کننده اسناد برای استخراج داده‌های ساختاریافته و غیرساختاریافته از PDFها، اسناد Office، تصاویر، ایمیل‌ها و آرشیوها."

  items:
    # items loop
    - icon: "text"
      title: "استخراج متن"
      content: "استخراج اطلاعات متنی از فرمت‌های مختلف فایل"

    # items loop
    - icon: "image"
      title: "استخراج تصاویر"
      content: "دریافت محتوای تصویری از منابع مختلف"

    # items loop
    - icon: "template"
      title: "تحلیل داده‌ها با قالب‌ها"
      content: "ایجاد قالب‌های سفارشی و استفاده از آن‌ها برای تجزیه اطلاعات خاص"

    # items loop
    - icon: "pdf"
      title: "تجزیه فرم‌های PDF"
      content: "فرم‌های PDF اسناد دیجیتالی هستند که شامل فیلدهای قابل پر شدن برای تعامل کاربر می‌باشند"

############################# Code Samples ###############################
code_samples:
  enable: true
  title: "GroupDocs.Parser نمونه‌های کد"
  description: "برخی موارد استفاده از عملیات‌های معمول GroupDocs.Parser در C# و Java و Python"

  items:
    # items loop
    - title: "چگونگی استخراج متن از اسناد PDF"
      content: "API GroupDocs.Parser استخراج متن از اسناد را با اجرای چند مرحله آسان می‌کند."
      samples:
          # samples loop
          - language: "C#"
            color: "blue"
            content: |
              ```csharp {style=abap}  
                // یک نمونه از کلاس Parser را با عبور فایل مورد نظر ایجاد کنید
                using (var parser = new Parser("source.pdf"))
                {
                    // استخراج متن
                    using (var textReader = parser.GetText())
                    {
                        // پردازش متن استخراج‌شده
                        Console.WriteLine(textReader?.ReadToEnd());
                    }
                }     
              ```
          # samples loop
          - language: "Java"
            color: "red"
            content: |
              ```java {style=abap}
                // یک نمونه از کلاس Parser را با عبور فایل مورد نظر ایجاد کنید
                try (Parser parser = new Parser("source.pdf"))
                {
                    // استخراج متن
                    try (TextReader reader = parser.getText())
                    {
                        // پردازش متن استخراج‌شده
                        System.out.println(reader == null 
                                ? "" 
                                : reader.readToEnd());
                    }
                }  
              ```
          # samples loop
          - language: "Python"
            color: "green"
            content: |
              ```python {style=abap}
                from groupdocs.parser import Parser

                # یک نمونه از کلاس Parser را با عبور فایل مورد نظر ایجاد کنید
                with Parser("source.pdf") as parser:
                    # استخراج متن
                    text = parser.get_text()

                    # پردازش متن استخراج‌شده
                    print(text)
              ```
############################# Supported Formats ###############################
formats:
  enable: true
  title: "پشتیبانی از بیش از 50 فرمت سند و تصویر"
  description: "GroupDocs.Parser SDK تجزیه‌کننده اسناد امکان انجام عملیات تجزیه را در اسناد Office، PDFها، تصاویر، ایمیل‌ها، آرشیوها و موارد دیگر فراهم می‌کند."

############################# Metrics ###############################
metrics:
  enable: true
  title: "دست‌آوردهای GroupDocs.Parser"
  description: "معیارهای کلیدی دستاوردهای کتابخانه ما را کشف کنید"

  items:
    # items loop
    - number: "50+"
      title: "قالب‌های پشتیبانی‌شده"
      content: "GroupDocs.Parser عملیات‌ها را با بیش از ۵۰ قالب فایل محبوب پشتیبانی می‌کند."

    # items loop
    - number: "1600k"
      title: "دانلودهای NuGet"
      content: "پکیج NuGet GroupDocs.Parser برای .NET بیش از 1,600,000 بار دانلود شده است."

    # items loop
    - number: "18k"
      title: "دانلودهای Maven"
      content: "GroupDocs.Parser در Maven 18,000 بار دانلود شده است. ویژگی‌های قدرتمند تجزیه‌وتحلیل Java."

    # items loop
    - number: "140+"
      title: "مشتریان خوشحال"
      content: "شرکت‌های مشهور و توسعه‌دهندگان فردی به‌طور یکسان محصولات GroupDocs را برای ساخت راه‌حل‌های نوآورانه ترجیح می‌دهند."


############################# Customers ###############################
customers:
  enable: true
  title: "مشتریان خوشحال ما"
  description: "GroupDocs کتابخانه‌ها توسط برندهای مشهور و معتبر جهانی در سراسر جهان مورد استفاده قرار می‌گیرند."

  items:
    # items loop
    - title: "BenQ Corporation"
      logo: "benq"
      
    # items loop
    - title: "Nasdaq Stock Market"
      logo: "nasdaq"
      
    # items loop
    - title: "AT&T Inc."
      logo: "att"
      
    # items loop
    - title: "Customer logo AstraZeneca"
      logo: "astrazeneca"
      
    # items loop
    - title: "Central Bank of Argentina"
      logo: "argentinacentralbank"
      
    # items loop
    - title: "Roche Holding AG"
      logo: "roche"
      
    # items loop
    - title: "Capita"
      logo: "capita"
      
    # items loop
    - title: "Axa S.A."
      logo: "axa"
      
    # items loop
    - title: "Instructure Inc."
      logo: "instructure"
      
    # items loop
    - title: "Wipro"
      logo: "wipro"


############################# Actions ###############################
actions:
  enable: true
  title: "آیا آماده شروع هستید؟"
  description: "امکانات GroupDocs.Parser را به‌صورت رایگان روی پلتفرم خود امتحان کنید"

  items:
    # items loop
    - title: ".NET"
      color: "blue"
      link: "/parser/net/"

    # items loop
    - title: "Java"
      color: "red"
      link: "/parser/java/"

############################# FAQ ###############################
faq:
  enable: true
  title: "سوالات متداول"
  description: "پاسخ‌های اکثر سوالات متداول."

  items:
    # items loop
    - question: "آیا کتابخانه GroupDocs.Parser برای دست‌کاری اسناد به نرم‌افزارهای شخص ثالث دیگری نیاز دارد؟"
      answer: "GroupDocs.Parser نیازی به نصب هیچ نرم‌افزار خارجی مانند Adobe Acrobat، Microsoft Office یا سایر برنامه‌ها ندارد."

    # items loop
    - question: "آیا می‌توانم قبل از خرید کتابخانه GroupDocs.Parser را امتحان کنم؟"
      answer: "بله، می‌توانید GroupDocs.Parser را بدون خرید لایسنس امتحان کنید. پس از نصب بدون لایسنس، کتابخانه در حالت آزمایشی کار می‌کند. در این حالت، برچسب‌های آزمایشی به سند خروجی اضافه می‌شود و سند به سه صفحهٔ اول محدود می‌شود. اگر می‌خواهید GroupDocs.Parser را بدون محدودیت‌های نسخه آزمایشی تست کنید، می‌توانید یک لایسنس موقت ۳۰ روزه نیز درخواست کنید. برای جزئیات بیشتر، [مشاهده کنید](https://purchase.groupdocs.com/temporary-license/)."

    # items loop
    - question: "چه نوع لایسنس‌هایی ارائه می‌کنید؟"
      answer: "ما چندین نوع لایسنس ارائه می‌دهیم که متناسب با نیازهای توسعه‌دهندگان یا شرکت‌های خاص باشد. انواع لایسنس بر اساس تعداد توسعه‌دهندگان، تعداد مکان‌های سایت توسعه‌دهنده، و این که آیا نیاز به ارائه SDK/API ما به مشتریان نهایی دارید یا نه، تعیین می‌شود. به‌علاوه، می‌توانید لایسنس‌های متره (Metered) براساس استفاده ماهانه از محصول را انتخاب کنید. برای اطلاعات بیشتر، [اینجا](https://purchase.groupdocs.com/pricing/parser/net/)."

############################# Cloud Links ###############################
cloud_links:
  enable: true
  title: "GroupDocs.Parser APIهای پارسر سند با کد کم"
  description: "قابلیت‌های پارس سند را با استفاده از API REST مبتنی بر ابر و SDKهای ما به هر برنامه‌ای اضافه کنید."
  
  items:
    # items loop
    - title: "GroupDocs.Parser Cloud for cURL"
      content: "دستورات cURL برای API ابری پارسر سند RESTful جهت پردازش اسناد در انواع گسترده‌ای از فرمت‌های محبوب پشتیبانی‌شده."
      icon: "groupdocs_parser-for-curl"
      link: "https://products.groupdocs.cloud/parser/curl"

    # items loop
    - title: "GroupDocs.Parser Cloud for .NET"
      content: "استخراج تصاویر، متن، اطلاعات سند یا حتی پارس هر سندی با الگوی تعریف‌شده توسط کاربر در برنامه‌های Microsoft .NET شما."
      icon: "groupdocs_parser-for-net"
      link: "https://products.groupdocs.cloud/parser/net"

    # items loop
    - title: "GroupDocs.Parser Cloud for Java"
      content: "SDK ابری برای توسعه‌دهندگان Java جهت پارس سند، استخراج اطلاعات سند و داده‌ها در برنامه‌های مبتنی بر Java."
      icon: "groupdocs_parser-for-java"
      link: "https://products.groupdocs.cloud/parser/java"

############################# App links ###############################
app_links:
  enable: true
  title: "GroupDocs.Parser برنامه‌های بدون کد پارسر سند"
  description: "برنامه‌های وب پارسر سند که به شما امکان استخراج داده از بیش از ۵۰ فرمت محبوب را مستقیماً در مرورگر شما می‌دهند."

  items:
    # items loop
    - title: "GroupDocs.Parser Total"
      content: "اپلیکیشن آنلاین رایگان برای پارس Word، Excel، PowerPoint، PDF و بیش از ۵۰ نوع سند دیگر."
      icon: "groupdocs_parser-app"
      link: "https://products.groupdocs.app/parser/total"

    # items loop
    - title: "GroupDocs.Parser DOCX"
      content: "پارس اسناد Word مستقیماً از مرورگر وب شما برای استخراج تصاویر، متن یا متاداده."
      icon: "groupdocs_words-app"
      link: "https://products.groupdocs.app/parser/docx"

    # items loop
    - title: "GroupDocs.Parser PDF"
      content: "اپلیکیشن رایگان پارس PDF که روی هر پلتفرم یا دستگاهی بدون هیچ محدودیتی کار می‌کند."
      icon: "groupdocs_pdf-app"
      link: "https://products.groupdocs.app/parser/pdf"


      


---