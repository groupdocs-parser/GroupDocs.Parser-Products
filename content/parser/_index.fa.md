---
############################# Static ############################
layout: "family"
date:  2025-06-30T10:26:00
draft: false

product: "Parser"
product_tag: "parser"

lang: fa

############################# Head ############################
head_title: "برنامه‌های تحلیل اسناد .NET، جاوا، API های ابری و برنامه‌های آنلاین"
head_description: "راهکار جامع تحلیل اسناد برای برنامه‌های .NET، جاوا و برنامه‌های مبتنی بر ابر. استخراج داده‌ها از فرمت‌های اسنادی آنلاین با استفاده از ویژگی کشیدن و رها کردن ساده."

############################# Header ############################
title: "راهکار تحلیل اسناد"
description:  |
  API قوی برای استخراج داده‌ها از فرمت‌های مختلف فایل.

  تحلیل اسناد با حداقل تلاش کدنویسی.

  سفارشی کردن نتایج تحلیل.

############################# Supported Platforms ###############################
supported_platforms:
  enable: true
  head_title: "پلتفرم خود را انتخاب کنید"
  title: "استقلال از پلتفرم"
  description: "کتابخانه GroupDocs.Parser از سیستم‌عامل‌ها و فریم‌ورک‌های زیر پشتیبانی می‌کند:"
  details_link_title: "بیشتر بدانید"

  items:
    # items loop
    - title: ".NET"
      description: GroupDocs.Parser .NET 
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
      description: GroupDocs.Parser Java
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

############################# Features ###############################
features:
  enable: true
  title: "GroupDocs.Parser در یک نظر"
  description: "API برای پردازش داده‌ها در قالب‌های PDF، Word، Excel و بیشتر"

  items:
    # items loop
    - icon: "text"
      title: "استخراج متن"
      content: "استخراج اطلاعات متنی از فرمت‌های مختلف فایل"

    # items loop
    - icon: "image"
      title: "استخراج تصاویر"
      content: "بازیابی محتوای بصری از منابع مختلف"

    # items loop
    - icon: "template"
      title: "تحلیل داده با الگوها"
      content: "ایجاد قالب‌های سفارشی و استفاده از آن‌ها برای استخراج اطلاعات خاص"

    # items loop
    - icon: "pdf"
      title: "تحلیل فرم‌های PDF"
      content: "فرم‌های PDF اسنادی دیجیتالی هستند که دارای فیلدهای قابل پر کردن برای تعامل کاربر می‌باشند."

############################# Code Samples ###############################
code_samples:
  enable: true
  title: "نمونه‌های کد GroupDocs.Parser"
  description: "برخی از موارد کاربرد عملیات معمول GroupDocs.Parser در C# و جاوا"

  items:
    # items loop
    - title: "چگونه متن را از اسناد PDF استخراج کنیم"
      content: "API GroupDocs.Parser روند استخراج متن از اسناد را با اجرای چند مرحله آسان می‌سازد."
      samples:
          # samples loop
          - language: "C#"
            color: "blue"
            content: |
                    <code class="language-csharp" data-lang="csharp">

                        // یک نمونه از کلاس Parser ایجاد کنید و فایل مطلوب را به آن پاس دهید.
                        using (var parser = new Parser("source.pdf"))
                        {
                            // متن را استخراج کنید.
                            using (var textReader = parser.GetText())
                            {
                                // متن استخراج‌شده را پردازش کنید.
                                Console.WriteLine(textReader?.ReadToEnd());
                            }
                        }     
                        
                    </code>

          # samples loop
          - language: "Java"
            color: "red"
            content: |
                    <code class="language-java" data-lang="java">

                        // یک نمونه از کلاس Parser ایجاد کنید و فایل مطلوب را به آن پاس دهید.
                        try (Parser parser = new Parser("source.pdf"))
                        {
                            // متن را استخراج کنید.
                            try (TextReader reader = parser.getText())
                            {
                                // متن استخراج‌شده را پردازش کنید.
                                System.out.println(reader == null 
                                        ? "" 
                                        : reader.readToEnd());
                            }
                        }  

                    </code>


############################# Supported Formats ###############################
formats:
  enable: true
  title: "پشتیبانی از بیش از 50 فرمت فایل"
  description: "GroupDocs.Parser عملیات پارس را در خانواده‌های مختلف فرمت‌ها امکان‌پذیر می‌سازد."

############################# Metrics ###############################
metrics:
  enable: true
  title: "دستاوردهای GroupDocs.Parser"
  description: "شاخص‌های کلیدی موفقیت‌های کتابخانه ما را کشف کنید."

  items:
    # items loop
    - number: "50+"
      title: "فرمت‌های پشتیبانی‌شده"
      content: "GroupDocs.Parser با بیش از 50 فرمت فایل محبوب کار می‌کند."

    # items loop
    - number: "1600k"
      title: "نصب‌های NuGet"
      content: "بسته NuGet GroupDocs.Parser برای .NET بیش از 1,600,000 بار دانلود شده است."

    # items loop
    - number: "18k"
      title: "نصب‌های Maven"
      content: "GroupDocs.Parser در Maven دارای 18,000 نصب است. ویژگی‌های قدرتمند پارس جاوا."

    # items loop
    - number: "140+"
      title: "مشتریان خوشحال"
      content: "شرکت‌های معروف و توسعه‌دهندگان فردی محصولات GroupDocs را برای ایجاد راه‌حل‌های نوآورانه انتخاب می‌کنند."


############################# Customers ###############################
customers:
  enable: true
  title: "مشتریان خوشحال ما"
  description: "کتابخانه‌های GroupDocs توسط برندهای معتبر و شناخته‌شده در سراسر جهان مورد استفاده قرار می‌گیرند."

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
  title: "آماده شروع کار هستید؟"
  description: "ویژگی‌های GroupDocs.Parser را بر روی پلتفرم خود به صورت رایگان امتحان کنید."

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
  description: "پاسخ به رایج‌ترین سوالات."

  items:
    # items loop
    - question: "آیا کتابخانه GroupDocs.Parser به نرم‌افزارهای شخص ثالث دیگری برای ویرایش اسناد نیاز دارد؟"
      answer: "GroupDocs.Parser نیازی به نصب نرم‌افزارهای خارجی مانند Adobe Acrobat، Microsoft Office یا هر نرم‌افزار دیگر ندارد."

    # items loop
    - question: "آیا می‌توانم قبل از خرید، کتابخانه GroupDocs.Parser را امتحان کنم؟"
      answer: "بله، می‌توانید GroupDocs.Parser را بدون خرید مجوز امتحان کنید. پس از نصب بدون مجوز، کتابخانه در حالت آزمایشی کار می‌کند. در این حالت، نشان‌های آزمایشی به سند حاصل افزوده می‌شود و به سه صفحه اول محدود می‌شود. اگر می‌خواهید GroupDocs.Parser را بدون محدودیت‌های نسخه آزمایشی تست کنید، می‌توانید یک مجوز موقت 30 روزه درخواست کنید. برای جزئیات بیشتر، [مشاهده کنید](https://purchase.groupdocs.com/temporary-license/)."

    # items loop
    - question: "چه نوع مجوزهایی دارید؟"
      answer: "ما چندین نوع مجوز ارائه می‌دهیم که نیازهای توسعه‌دهندگان خاص یا شرکت‌ها را برآورده می‌کند. نوع مجوزها به تعداد توسعه‌دهندگان، تعداد مکان‌های سایت توسعه‌دهندگان و اینکه آیا نیاز دارید SDK/API ما را به مشتریان نهایی خود ارائه دهید بستگی دارد. به‌عنوان مثال، می‌توانید مجوزهای متری را بر اساس استفاده ماهیانه از محصول انتخاب کنید. برای اطلاعات بیشتر، [اینجا را مشاهده کنید](https://purchase.groupdocs.com/pricing/parser/net/)."

############################# Cloud Links ###############################
cloud_links:
  enable: true
  title: "API های کم‌کد GroupDocs.Parser"
  description: "قابلیت‌های ویرایش‌گر اسناد را در هر برنامه‌ای با استفاده از API REST مبتنی بر ابر ما ادغام کنید."
  
  items:
    # items loop
    - title: "GroupDocs.Parser Cloud for cURL"
      content: "دستورات cURL برای API ابری ویرایش‌گر اسناد RESTful برای تحلیل اسناد در بازه وسیعی از فرمت‌های پشتیبانی‌شده محبوب."
      icon: "groupdocs_parser-for-curl"
      link: "https://products.groupdocs.cloud/parser/curl"

    # items loop
    - title: "GroupDocs.Parser Cloud for .NET"
      content: "استخراج تصاویر، متن، اطلاعات سند یا حتی تحلیل هر سند با الگوی تعریف‌شده توسط کاربر در برنامه‌های Microsoft .NET شما."
      icon: "groupdocs_parser-for-net"
      link: "https://products.groupdocs.cloud/parser/net"

    # items loop
    - title: "GroupDocs.Parser Cloud for Java"
      content: "SDK ابری برای توسعه‌دهندگان جاوا برای تحلیل اسناد، استخراج اطلاعات سند و داده‌ها در برنامه‌های مبتنی بر جاوا."
      icon: "groupdocs_parser-for-java"
      link: "https://products.groupdocs.cloud/parser/java"

############################# App links ###############################
app_links:
  enable: true
  title: "برنامه‌های بدون کد GroupDocs.Parser"
  description: "برنامه تحت وبی که به شما امکان می‌دهد تا تحلیل را در بیش از 50 نوع فایل محبوب به‌صورت مستقیم در مرورگر خود انجام دهید."

  items:
    # items loop
    - title: "GroupDocs.Parser Total"
      content: "برنامه آنلاین رایگان برای تحلیل Word، Excel، PowerPoint، PDF و بیش از 50 نوع سند دیگر."
      icon: "groupdocs_parser-app"
      link: "https://products.groupdocs.app/parser/total"

    # items loop
    - title: "GroupDocs.Parser DOCX"
      content: "تحلیل اسناد Word به‌صورت مستقیم از مرورگر وب خود برای استخراج تصاویر، متن یا متاداده."
      icon: "groupdocs_words-app"
      link: "https://products.groupdocs.app/parser/docx"

    # items loop
    - title: "GroupDocs.Parser PDF"
      content: "برنامه تحلیل PDF رایگان که بر روی هر پلتفرم یا دستگاهی بدون هیچ محدودیتی کار می‌کند."
      icon: "groupdocs_pdf-app"
      link: "https://products.groupdocs.app/parser/pdf"


      


---