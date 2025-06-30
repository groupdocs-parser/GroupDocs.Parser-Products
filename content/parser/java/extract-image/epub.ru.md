


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:30
draft: false
lang: ru
format: Epub
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Извлечение изображений из файлов EPUB в приложениях Java"
head_description: "С помощью GroupDocs.Parser вы можете извлекать изображения из файлов EPUB в Java без необходимости в сторонних инструментах."

############################# Header ############################
title: "Извлечение изображений из EPUB с помощью Java" 
description: "Извлекайте встроенные изображения из файлов, таких как PDF, Word, Excel и других, используя GroupDocs.Parser в вашей среде разработки Java."
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Скачать Бесплатную Версию"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "Что такое GroupDocs.Parser for Java?"
    link: "/parser/java/"
    link_title: "Узнать больше"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) — это мощный API парсинга, разработанный для разработчиков Java. Он позволяет извлекать изображения, текст, ссылки и структурированные элементы из различных форматов файлов, включая DOCX, XLSX, PDF, PNG, JPG и многих других — без необходимости в дополнительных библиотеках или приложениях.

############################# Steps ############################
steps:
    enable: true
    title: "Как извлечь изображения из Epub в Java"
    content: |
      Следуйте этим шагам, чтобы извлечь изображения из документов EPUB с помощью [GroupDocs.Parser](/parser/java/) в вашем приложении Java:
      
      1. Создайте экземпляр Parser и загрузите файл EPUB.
      2. Извлеките данные изображений из загруженного документа.
      3. Используйте или экспортируйте извлеченные изображения по мере необходимости.
   
    code:
      platform: "net"
      copy_title: "Копировать"
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
        copy_tip: "Нажмите для копирования"
        copy_done: "Скопировано"
      links:
        #  loop
        - title: "Больше примеров"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java/"
        #  loop
        - title: "Документация"
          link: "https://docs.groupdocs.com/parser/java/"
          
      content: |
        ```java {style=abap}
        // Инициализируйте парсер и загрузите документ с изображениями, используя Parser
        try (Parser parser = new Parser("input.epub"))
        {
            // Соберите все элементы изображений, встроенные в документ
            Iterable<PageImageArea> images = parser.getImages();

            // Пропустите обработку, если в документе нет изображений
            if (images == null) {
                return;
            }

            // Обработайте каждое изображение по мере необходимости
            for (PageImageArea image : images) {
                System.out.println(String.format("Page: %d, R: %s, Type: %s", image.getPage().getIndex(), 
                    image.getRectangle(), image.getFileType()));
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "Дополнительные возможности парсинга документов"
  description: "В дополнение к извлечению изображений, GroupDocs.Parser позволяет извлекать сырой контент, такой как текст, ссылки, метаданные и структурированные данные для обработки и анализа."
  image: "/img/parser/features_extract-image.webp" # 500x500 px
  image_description: "Извлечение изображений и контента из документов"
  features:
    # feature loop
    - title: "Работа с разными форматами"
      content: "Извлекайте изображения из различных типов документов, включая PDF, DOCX, PPTX, XLSX, а также из форматов изображений, таких как PNG, JPEG и GIF."

    # feature loop
    - title: "Сохранение четкости и разрешения изображений"
      content: "Все извлеченные изображения сохраняют свое оригинальное разрешение и тип файла, обеспечивая постоянное качество и удобство использования."

    # feature loop
    - title: "Гибкие параметры конфигурации"
      content: "Настройте процесс извлечения изображений, фильтруя изображения по типу, размеру, индексу страницы или формату файла."
      
  code_samples:
    # code sample loop
    - title: "Извлечение и сохранение изображений из PDF файлов"
      content: |
        В этом примере показано, как извлечь изображения из PDF документа и сохранить их по отдельности на вашем устройстве.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Используйте Parser для открытия PDF файла
        try (Parser parser = new Parser("input.pdf"))
        {
            // Получите изображения из содержимого документа
            Iterable<PageImageArea> images = parser.getImages();

            // Установите параметры вывода, такие как формат (например, JPEG или PNG)
            ImageOptions options = new ImageOptions(ImageFormat.Png);

            // Сохраните извлеченные изображения в локальной директории
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
  title: "Готовы начать?"
  description: "Попробуйте функции GroupDocs.Parser бесплатно или запросите лицензию"
  items:
    #  loop
    - title: "Скачивание Maven"
      link: "https://releases.groupdocs.com/parser/java/"
      color: "red"
        #  loop
    - title: "Лицензирование"
      link: "https://purchase.groupdocs.com/pricing/parser/java/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "Поддерживаемые типы файлов для извлечения изображений"
    exclude: "EPUB"
    description: "GroupDocs.Parser поддерживает извлечение изображений из широкого спектра документов и изображений. Ознакомьтесь с общими поддерживаемыми форматами ниже."
    items: 
        # format loop 1
        - name: "Парсинг PDF"
          format: "PDF"
          link: "/parser/java/extract-image/pdf/"
          description: "(Формат переносимого документа)"
          
        # format loop 2
        - name: "Парсинг DOCX"
          format: "DOCX"
          link: "/parser/java/extract-image/docx/"
          description: "(Документ Word 2007+)"
          
        # format loop 3
        - name: "Парсинг PPTX"
          format: "PPTX"
          link: "/parser/java/extract-image/pptx/"
          description: "(Формат презентации Open XML)"
          
        # format loop 4
        - name: "Парсинг XLSX"
          format: "XLSX"
          link: "/parser/java/extract-image/xlsx/"
          description: "(Рабочая книга Open XML)"
          
        # format loop 5
        - name: "Парсинг ODT"
          format: "ODT"
          link: "/parser/java/extract-image/odt/"
          description: "(Текстовый документ OpenDocument)"
          
        # format loop 6
        - name: "Парсинг ODS"
          format: "ODS"
          link: "/parser/java/extract-image/ods/"
          description: "(Электронная таблица OpenDocument)"
          
        # format loop 7
        - name: "Парсинг ODP"
          format: "ODP"
          link: "/parser/java/extract-image/odp/"
          description: "(Презентация OpenDocument)"
          
        # format loop 8
        - name: "Парсинг EPUB"
          format: "EPUB"
          link: "/parser/java/extract-image/epub/"
          description: "(Файл открытой электронной книги)"
          
        # format loop 9
        - name: "Парсинг FB2"
          format: "FB2"
          link: "/parser/java/extract-image/fb2/"
          description: "(Электронная книга FictionBook)"
         
          

---