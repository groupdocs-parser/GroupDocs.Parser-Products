


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:24
draft: false
lang: uk
format: Rtf
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Витягування гіперпосилань з файлів RTF в додатках Java"
head_description: "Використовуйте GroupDocs.Parser для знаходження та витягування URL-адрес з документів RTF у проєктах Java—жодного додаткового програмного забезпечення не потрібно."

############################# Header ############################
title: "Витягування гіперпосилань з RTF за допомогою Java" 
description: "Витягніть веб-ліки та гіперпосилання з PDF, Word, Excel та інших документів, використовуючи GroupDocs.Parser у вашому Java середовищі."
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Завантажте безкоштовну версію"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "Про API GroupDocs.Parser for Java"
    link: "/parser/java/"
    link_title: "Дізнатися більше"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) — це надійний API для витягування вмісту, розроблений для розробників Java. Він пропонує інструменти для витягування гіперпосилань, структурованих даних, зображень та тексту з популярних форматів, таких як DOCX, XLSX, PDF, HTML та інших—все без необхідності в сторонніх плагінах.

############################# Steps ############################
steps:
    enable: true
    title: "Як витягувати гіперпосилання з Rtf в Java"
    content: |
      [GroupDocs.Parser](/parser/java/) спрощує витягування гіперпосилань з файлів RTF у додатках Java за допомогою цих основних етапів:
      
      1. Відкрийте файл RTF за допомогою екземпляра Parser.
      2. Переконайтесь, що витягування гіперпосилань доступне для формату файлу.
      3. Витягніть усі гіперпосилання за допомогою відповідного методу.
      4. Перегляньте результати та обробіть кожне посилання за потреби.
   
    code:
      platform: "net"
      copy_title: "Копіювати"
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
        copy_tip: "натисніть, щоб скопіювати"
        copy_done: "скопійовано"
      links:
        #  loop
        - title: "Більше прикладів"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java/"
        #  loop
        - title: "Документація"
          link: "https://docs.groupdocs.com/parser/java/"
          
      content: |
        ```java {style=abap}
        // Завантажте файл, що може містити гіперпосилання, за допомогою Parser
        try (Parser parser = new Parser("input.rtf")) {

            // Перевірте, чи підтримує формат документа витягування гіперпосилань
            if (!parser.getFeatures().isHyperlinks()) {
                System.out.println("Витягнення гіперпосилань недоступне для файлу");
                return;
            }

            // Витягніть і використайте дані з гіперпосиланнями з документа
            Iterable<PageHyperlinkArea> hyperlinks = parser.getHyperlinks();

            for (PageHyperlinkArea h : hyperlinks) {
                System.out.println(h.getText());
                System.out.println(h.getUrl());
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "Всебічні інструменти для парсингу документів"
  description: "Окрім витягування гіперпосилань, GroupDocs.Parser дозволяє вам збирати інший корисний вміст, такий як звичайний текст, вбудовані медіа та структуровані дані для використання в автоматизованих робочих процесах."
  image: "/img/parser/features_extract-hyperlink.webp" # 500x500 px
  image_description: "Витягування гіперпосилань та аналіз документів"
  features:
    # feature loop
    - title: "Точне виявлення посилань"
      content: "Збирайте всі типи гіперпосилань з різних макетів документів, включаючи клікабельний текст та приховані URL-адреси."

    # feature loop
    - title: "Підходить для документів та веб-контенту"
      content: "Витягуйте посилання з PDF, DOCX, XLSX, HTML та зображень, що містять вбудовані гіперпосилання."

    # feature loop
    - title: "Користувацька поведінка витягування"
      content: "Уточніть, як витягуються гіперпосилання, використовуючи такі параметри, як діапазони сторінок, типи посилань або фільтри вмісту."
      
  code_samples:
    # code sample loop
    - title: "Приклад: витягування гіперпосилань з PDF з користувацькими параметрами"
      content: |
        Цей приклад демонструє, як витягнути всі посилання з PDF-файлу, використовуючи налаштування витягування посилань.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Відкрийте PDF за допомогою класу Parser
        try (Parser parser = new Parser("input.docx"))
        {
            // Переконайтесь, що підтримка гіперпосилань увімкнена для цього документа
            if (!parser.getFeatures().isHyperlinks()) {
                return;
            }

            // Застосуйте параметри для фільтрації посилань
            PageAreaOptions options = new PageAreaOptions(new Rectangle(new Point(380, 90), new Size(150, 50)));

            // Використовуйте парсер для отримання даних з гіперпосиланнями
            Iterable<PageHyperlinkArea> hyperlinks = parser.getHyperlinks(options);

            // Перегляньте посилання та обробіть їх відповідно
            for (PageHyperlinkArea h : hyperlinks) {
                System.out.println(h.getText());
                System.out.println(h.getUrl());
            }
        }
        ```
        {{< /landing/code >}}


############################# Actions ############################

actions:
  enable: true
  title: "Готові розпочати?"
  description: "Спробуйте можливості GroupDocs.Parser безкоштовно або запитайте ліцензію"
  items:
    #  loop
    - title: "Завантаження Maven"
      link: "https://releases.groupdocs.com/parser/java/"
      color: "red"
        #  loop
    - title: "Ліцензування"
      link: "https://purchase.groupdocs.com/pricing/parser/java/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "Формати документів, що підтримують витягування гіперпосилань"
    exclude: "RTF"
    description: "За допомогою GroupDocs.Parser ви можете витягувати гіперпосилання з багатьох поширених форматів файлів. Нижче наведено список форматів, які зазвичай підтримуються."
    items: 
        # format loop 1
        - name: "Парсинг PDF"
          format: "PDF"
          link: "/parser/java/extract-hyperlink/pdf/"
          description: "(Формат портативного документа)"
          
        # format loop 2
        - name: "Парсинг DOCX"
          format: "DOCX"
          link: "/parser/java/extract-hyperlink/docx/"
          description: "(Документ Word Office 2007+)"
          
        # format loop 3
        - name: "Парсинг PPTX"
          format: "PPTX"
          link: "/parser/java/extract-hyperlink/pptx/"
          description: "(Формат відкритої XML-презентації)"
          
        # format loop 4
        - name: "Парсинг XLSX"
          format: "XLSX"
          link: "/parser/java/extract-hyperlink/xlsx/"
          description: "(Відкрите XML-робочий зошит)"
          
        # format loop 5
        - name: "Парсинг TXT"
          format: "TXT"
          link: "/parser/java/extract-hyperlink/txt/"
          description: "(Текстовий файл)"
          
        # format loop 6
        - name: "Парсинг RTF"
          format: "RTF"
          link: "/parser/java/extract-hyperlink/rtf/"
          description: "(Формат багатого тексту)"
          
        # format loop 7
        - name: "Парсинг XML"
          format: "XML"
          link: "/parser/java/extract-hyperlink/xml/"
          description: "(Мова розмітки eXtensible)"
          
        # format loop 8
        - name: "Парсинг EPUB"
          format: "EPUB"
          link: "/parser/java/extract-hyperlink/epub/"
          description: "(Відкритий файл eBook)"
         
          

---