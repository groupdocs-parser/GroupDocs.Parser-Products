


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:30
draft: false
lang: uk
format: Pptx
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Витягування зображень з файлів PPTX в застосунках Java"
head_description: "З допомогою GroupDocs.Parser ви можете витягувати зображення з файлів PPTX в Java без зайвих зусиль, без потреби у сторонніх інструментах."

############################# Header ############################
title: "Витягування зображень з PPTX за допомогою Java" 
description: "Отримуйте вбудовані зображення з документів, таких як PDF, Word, Excel та інші, використовуючи GroupDocs.Parser у вашому середовищі розробки Java."
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Завантажити безкоштовну версію"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "Що таке GroupDocs.Parser for Java?"
    link: "/parser/java/"
    link_title: "Дізнатися більше"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) — це API для парсингу з розширеними можливостями, створений для розробників Java. Він забезпечує витягування зображень, тексту, посилань та структурованих елементів з різних форматів файлів, включаючи DOCX, XLSX, PDF, PNG, JPG та багато інших — усе без потреби у зовнішніх бібліотеках або застосунках.

############################# Steps ############################
steps:
    enable: true
    title: "Як витягувати зображення з Pptx в Java"
    content: |
      Дотримуйтесь цих кроків, щоб витягти зображення з документів PPTX за допомогою [GroupDocs.Parser](/parser/java/) у вашій програмі Java:
      
      1. Створіть екземпляр Parser та завантажте файл PPTX.
      2. Витягніть дані зображень з завантаженого документа.
      3. Використовуйте або експортні витягнуті зображення за потребою.
   
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
        // Ініціалізуйте парсер і завантажте документ з зображеннями за допомогою Parser
        try (Parser parser = new Parser("input.pptx"))
        {
            // Зберіть усі елементи зображень, вбудовані в документ
            Iterable<PageImageArea> images = parser.getImages();

            // Пропустіть обробку, якщо в документі немає зображень
            if (images == null) {
                return;
            }

            // Обработайте кожне зображення за потребою
            for (PageImageArea image : images) {
                System.out.println(String.format("Page: %d, R: %s, Type: %s", image.getPage().getIndex(), 
                    image.getRectangle(), image.getFileType()));
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "Інші можливості парсингу документів"
  description: "Окрім витягування зображень, GroupDocs.Parser дозволяє витягувати сирі дані, такі як текст, посилання, метадані та структуровані дані для обробки та аналізу."
  image: "/img/parser/features_extract-image.webp" # 500x500 px
  image_description: "Витягування зображень та вмісту з документів"
  features:
    # feature loop
    - title: "Працює з різноманітними форматами"
      content: "Витягуйте зображення з різних типів документів, включаючи PDF, DOCX, PPTX, XLSX, а також зображень форматів PNG, JPEG та GIF."

    # feature loop
    - title: "Збереження чіткості та роздільної здатності зображень"
      content: "Усі витягнуті зображення зберігають свою первісну роздільну здатність та тип файлу, щоб забезпечити послідовну якість та використання."

    # feature loop
    - title: "Гнучкі параметри налаштування"
      content: "Налаштуйте процес витягування зображень, фільтруючи зображення за типом, розміром, індексом сторінки або форматом файлу."
      
  code_samples:
    # code sample loop
    - title: "Витягти та зберегти зображення з PDF файлів"
      content: |
        Цей приклад демонструє, як витягувати зображення з PDF документа і зберігати їх окремо на вашому пристрої.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Використовуйте Parser для відкриття PDF файлу
        try (Parser parser = new Parser("input.pdf"))
        {
            // Отримайте зображення з вмісту документа
            Iterable<PageImageArea> images = parser.getImages();

            // Встановіть параметри виходу, такі як формат (наприклад, JPEG або PNG)
            ImageOptions options = new ImageOptions(ImageFormat.Png);

            // Збережіть витягнуті зображення у локальному каталозі
            int imageNumber = 0;
            for (PageImageArea image : images)
            {
                image.save(Constants.getOutputFilePath(String.format("%d.png", imageNumber)), options);
                imageNumber++;
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
    title: "Типи файлів, що підтримуються для витягування зображень"
    exclude: "PPTX"
    description: "GroupDocs.Parser підтримує витягування зображень з широкого спектра документів і зображень. Досліджуйте нижче поширені формати, що підтримуються."
    items: 
        # format loop 1
        - name: "Парсинг PDF"
          format: "PDF"
          link: "/parser/java/extract-image/pdf/"
          description: "(Формат портативного документа)"
          
        # format loop 2
        - name: "Парсинг DOCX"
          format: "DOCX"
          link: "/parser/java/extract-image/docx/"
          description: "(Документ Word Office 2007+)"
          
        # format loop 3
        - name: "Парсинг PPTX"
          format: "PPTX"
          link: "/parser/java/extract-image/pptx/"
          description: "(Формат відкритої XML-презентації)"
          
        # format loop 4
        - name: "Парсинг XLSX"
          format: "XLSX"
          link: "/parser/java/extract-image/xlsx/"
          description: "(Відкрите XML-робочий зошит)"
          
        # format loop 5
        - name: "Парсинг ODT"
          format: "ODT"
          link: "/parser/java/extract-image/odt/"
          description: "(Документ тексту OpenDocument)"
          
        # format loop 6
        - name: "Парсинг ODS"
          format: "ODS"
          link: "/parser/java/extract-image/ods/"
          description: "(Електронна таблиця OpenDocument)"
          
        # format loop 7
        - name: "Парсинг ODP"
          format: "ODP"
          link: "/parser/java/extract-image/odp/"
          description: "(Презентація OpenDocument)"
          
        # format loop 8
        - name: "Парсинг EPUB"
          format: "EPUB"
          link: "/parser/java/extract-image/epub/"
          description: "(Відкритий файл eBook)"
          
        # format loop 9
        - name: "Парсинг FB2"
          format: "FB2"
          link: "/parser/java/extract-image/fb2/"
          description: "(eBook формату FictionBook)"
         
          

---