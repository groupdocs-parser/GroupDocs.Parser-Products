


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:50
draft: false
lang: fa
format: Pptx
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "استخراج محتوا از فایل‌های PPTX در برنامه‌های Java"
head_description: "از GroupDocs.Parser برای تجزیه و بازیابی داده‌های ساختاری، متن، جداول و تصاویر از فایل‌های PPTX در Java استفاده کنید، بدون نیاز به ابزارهای خارجی."

############################# Header ############################
title: "استخراج داده از اسناد PPTX در Java" 
description: "با استفاده از GroupDocs.Parser در برنامه‌های Java خود، محتواهای ساختاری نظیر متن، متادیتا، جداول و گرافیک‌ها را به‌طور یکپارچه از اسناد PDF، Word، Excel و اسناد مبتنی بر تصویر استخراج کنید."
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "دریافت نسخه آزمایشی رایگان"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "چیست GroupDocs.Parser for Java؟"
    link: "/parser/java/"
    link_title: "بیشتر بدانید"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) یک API قدرتمند ساخته شده برای توسعه‌دهندگان Java است که قابلیت‌های پیشرفته تجزیه اسناد را ارائه می‌دهد. این امکان را برای شما فراهم می‌کند که داده‌های متنی، تصاویر، جداول، فیلدهای ساختاری و بارکدها را از فرمت‌های متنوعی مانند PDF، DOCX، XLSX، PPTX و غیره استخراج و پردازش کنید — همه این موارد بدون نیاز به نصب کتابخانه‌های اضافی.

############################# Steps ############################
steps:
    enable: true
    title: "چگونه داده‌ها را از Pptx با استفاده از Java استخراج کنیم"
    content: |
      برای استخراج اطلاعات مفید از اسناد PPTX در پروژه‌های Java خود با استفاده از [GroupDocs.Parser](/parser/java/)، این دستورالعمل‌ها را دنبال کنید:
      
      1. فایل PPTX را با یک شیء Parser باز کنید.
      2. از پارسر برای استخراج داده‌های مورد نیاز (متن، جداول، متادیتا و غیره) استفاده کنید.
      3. اطمینان حاصل کنید که خروجی صحیح و کامل است.
      4. محتوای تجزیه‌شده را در جریان داده‌ها، فرآیندهای تجاری یا برنامه‌های خود ادغام کنید.
   
    code:
      platform: "net"
      copy_title: "کپی"
      install:
        command: |
          <dependencies>
            <dependency>
              <groupId>com.groupdocs</groupId>
              <artifactId>groupdocs-parser</artifactId>
              <version>{0}</version>
            </dependency>
          </dependencies>

          <repositories>
            <repository>
              <id>repository.groupdocs.com</id>
              <name>GroupDocs Repository</name>
              <url>https://repository.groupdocs.com/repo/</url>
            </repository>
          </repositories>
        copy_tip: "برای کپی کلیک کنید"
        copy_done: "کپی شد"
      links:
        #  loop
        - title: "نمونه‌های بیشتر"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java/"
        #  loop
        - title: "مستندات"
          link: "https://docs.groupdocs.com/parser/java/"
          
      content: |
        ```java {style=abap}
        // مستندات ورودی خود را با Parser راه‌اندازی کنید
        try (Parser parser = new Parser("input.pptx"))
        {
            // تمام محتوای متنی موجود را از سند بازیابی کنید
            try (TextReader reader = parser.getText())
            {
                // اگر متنی پیدا نشود، مقدار برگردانده‌شده null خواهد بود
                // محتوای استخراج‌شده را در راه‌حل خود گنجانید
                System.out.println(reader == null ? 
                    "این فرمت ممکن است از استخراج متن پشتیبانی نکند" : reader.readToEnd());
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "قابلیت‌های چندمنظوره تجزیه اسناد"
  description: "GroupDocs.Parser تنها به استخراج متن محدود نمی‌شود — بلکه تجزیه کامل بارکدها، متادیتا، تصاویر، جداول و داده‌های دیگر را پشتیبانی می‌کند تا اتوماسیون هوشمند و برنامه‌های مبتنی بر داده را تقویت کند."
  image: "/img/parser/features_parse.webp" # 500x500 px
  image_description: "چشم‌انداز بصری از تجزیه و استخراج داده‌های اسناد"
  features:
    # feature loop
    - title: "استخراج از فرمت‌های فایل متعدد"
      content: "به داده‌هایی نظیر متن، جداول و رسانه از انواع فایل‌های پرکاربرد مانند PDF، Word، Excel، PowerPoint، HTML و غیره دسترسی پیدا کنید."

    # feature loop
    - title: "تجزیه محتوا از منابع دیجیتال و اسکن‌شده"
      content: "محتوا را هم از فایل‌های دیجیتال بومی و هم از تصاویر اسکن‌شده پردازش کنید و در صورت نیاز از OCR برای تفسیر متن embedded استفاده کنید."

    # feature loop
    - title: "گزینه‌های پیکربندی انعطاف‌پذیر"
      content: "تجزیه‌تان را با تنظیمات انتخاب صفحه، مناطق طرح‌نما و الگوهای فیلد سفارشی تنظیم کنید تا نیازهای خاص استخراج را برآورده کنید."
      
  code_samples:
    # code sample loop
    - title: "تجزیه PDF با استفاده از الگوی استخراج داده"
      content: |
        این نمونه نشان می‌دهد که چگونه می‌توان فیلدهای ساختاری را از یک PDF با استفاده از یک الگوی سفارشی از طریق GroupDocs.Parser استخراج کرد.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  PDF را با کلاس Parser باز کنید
        try (Parser parser = new Parser("input.pdf"))
        {
            // الگوی تجزیه را برای استخراج داده‌های تعریف‌شده اعمال کنید
            DocumentData data = parser.parseByTemplate(GetTemplate());

            // بررسی کنید که آیا استخراج بر مبنای الگو در دسترس است
            if (data == null) {
                return;
            }

            // با فیلدهای داده استخراج‌شده کار کنید
            for (int i = 0; i < data.getCount(); i++) {
                System.out.print(data.get(i).getName() + ": ");
                PageTextArea area = data.get(i).getPageArea() instanceof PageTextArea
                        ? (PageTextArea) data.get(i).getPageArea() : null;
                System.out.println(area == null ? "Not a template field" : area.getText());
            }
        }

        private static Template GetTemplate()
        {
            // تنظیمات تشخیص‌دهنده را برای استخراج بخش 'جزئیات' تعریف کنید
            TemplateTableParameters detailsTableParameters = 
                new TemplateTableParameters(new Rectangle(new Point(35, 320), new Size(530, 55)), null);

            TemplateItem[] templateItems = new TemplateItem[]
            {
                new TemplateTable(detailsTableParameters, "details", null)
            };

            Template template = new Template(java.util.Arrays.asList(templateItems));
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
    - title: "دانلود Maven"
      link: "https://releases.groupdocs.com/parser/java/"
      color: "red"
        #  loop
    - title: "مجوزدهی"
      link: "https://purchase.groupdocs.com/pricing/parser/java/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "نوع فایل‌های پشتیبانی‌شده برای استخراج محتوا"
    exclude: "PPTX"
    description: "GroupDocs.Parser با طیف گسترده‌ای از نوع فایل‌های اسناد و تصاویر سازگار است و استخراج اطلاعات از فرمت‌های متداول در سناریوهای تجزیه و اتوماسیون داده را ساده می‌سازد."
    items: 
        # format loop 1
        - name: "تحلیل PDF"
          format: "PDF"
          link: "/parser/java/parse/pdf/"
          description: "(فرمت سند قابل حمل)"
          
        # format loop 2
        - name: "تحلیل DOCX"
          format: "DOCX"
          link: "/parser/java/parse/docx/"
          description: "(سند Word Office 2007+)"
          
        # format loop 3
        - name: "تحلیل PPTX"
          format: "PPTX"
          link: "/parser/java/parse/pptx/"
          description: "(فرمت ارائه Open XML)"
          
        # format loop 4
        - name: "تحلیل XLSX"
          format: "XLSX"
          link: "/parser/java/parse/xlsx/"
          description: "(دفتر کار Open XML)"
          
        # format loop 5
        - name: "تحلیل TXT"
          format: "TXT"
          link: "/parser/java/parse/txt/"
          description: "(فایل متنی)"
          
        # format loop 6
        - name: "تحلیل RTF"
          format: "RTF"
          link: "/parser/java/parse/rtf/"
          description: "(فرمت متن غنی)"
          
        # format loop 7
        - name: "تحلیل XML"
          format: "XML"
          link: "/parser/java/parse/xml/"
          description: "(زبان نشانه‌گذاری قابل توسعه)"
          
        # format loop 8
        - name: "تحلیل EPUB"
          format: "EPUB"
          link: "/parser/java/parse/epub/"
          description: "(فایل کتاب الکترونیکی Open)"
         
          

---