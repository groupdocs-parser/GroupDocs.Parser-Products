


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:45
draft: false
lang: ru
format: Docx
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Извлечение текста из файлов DOCX в приложениях Java"
head_description: "Используйте GroupDocs.Parser для извлечения неструктурированного или структурированного текстового содержимого из документов DOCX в Java, без каких-либо внешних зависимостей."

############################# Header ############################
title: "Извлечение текста из DOCX с помощью Java" 
description: "Бесшовно извлекайте читаемый или структурированный текст из файлов, таких как PDF, Word, Excel и других, используя GroupDocs.Parser в ваших проектах разработки Java."
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Скачать бесплатную версию"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "Представляем API GroupDocs.Parser for Java"
    link: "/parser/java/"
    link_title: "Узнать больше"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) — это надежный и масштабируемый парсер документов, разработанный для разработчиков Java. Он предоставляет возможности для точного извлечения текста, таблиц, изображений и структурированных компонентов из различных форматов, включая PDF, DOCX, XLSX, PPTX и другие — без зависимости от внешних утилит.

############################# Steps ############################
steps:
    enable: true
    title: "Как извлечь текст из Docx с помощью Java"
    content: |
      Следуйте шагам ниже, чтобы извлечь текст из файлов DOCX с помощью [GroupDocs.Parser](/parser/java/) в вашем проекте Java:
      
      1. Загрузите документ DOCX с помощью класса Parser.
      2. Выполните извлечение текста из содержимого файла.
      3. Проверьте, был ли успешно извлечен текст.
      4. Используйте текстовые данные в системах поиска, аналитики или автоматизации.
   
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
        // Инициализируйте Parser с вашим документом
        try (Parser parser = new Parser("input.docx"))
        {
            // Прочитайте и извлеките все текстовые данные
            try (TextReader reader = parser.getText())
            {
                // Верните null, если текстовое содержимое отсутствует
                // Интегрируйте извлеченный текст в ваш рабочий процесс
                System.out.println(reader == null ? 
                    "Пропустите неподдерживаемые форматы извлечения текста" : reader.readToEnd());
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "Функционал извлечения структурированного текста"
  description: "GroupDocs.Parser предлагает не только простое извлечение текста — поддерживает получение изображений, метаданных и структурированных данных для улучшения задач обработки содержимого."
  image: "/img/parser/features_extract-text.webp" # 500x500 px
  image_description: "Извлечение и структурирование текстового содержимого из документов"
  features:
    # feature loop
    - title: "Работает с множеством форматов документов"
      content: "Извлечение как неструктурированного, так и структурированного текста из DOCX, XLSX, PPTX, PDF, HTML и других форматов."

    # feature loop
    - title: "Извлечение текста из визуального и текстового контента"
      content: "Парсинг текста из сканированных документов, слайдов, таблиц и других типов файлов с сохранением логической структуры."

    # feature loop
    - title: "Детальный контроль над процессом извлечения"
      content: "Настройка диапазонов страниц, зон макета и параметров точности для тонкой настройки извлечения текста."
      
  code_samples:
    # code sample loop
    - title: "Пример: Извлечение текстовых областей из документа PPTX"
      content: |
        Этот пример демонстрирует извлечение текстовых блоков вместе с их пространственными координатами из презентации PowerPoint с использованием GroupDocs.Parser.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Загрузите ваш файл PPTX с помощью API Parser
        try (Parser parser = new Parser("input.pptx"))
        {
            // Получите все прямоугольные текстовые зоны
            IEnumerable<PageTextArea> areas = parser.GetTextAreas();

            // Выходите, если эта функция не поддерживается
            if (areas == null)
            {
                return;
            }

            // Обходите текстовые области по страницам
            for (PageTextArea a : areas)
            {
                // Обрабатывайте каждый текстовый блок с его номером страницы и ограничивающей прямоугольной областью
                System.out.println(String.format("Page: %d, R: %s, Text: %s", a.getPage().getIndex(), a.getRectangle(), a.getText()));
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
    title: "Поддерживаемые типы файлов для извлечения текста"
    exclude: "DOCX"
    description: "GroupDocs.Parser способен извлекать текстовое содержимое из многочисленных файловых и графических форматов. Ниже приведены самые распространенные типы, которые он поддерживает."
    items: 
        # format loop 1
        - name: "Парсинг PDF"
          format: "PDF"
          link: "/parser/java/extract-text/pdf/"
          description: "(Формат переносимого документа)"
          
        # format loop 2
        - name: "Парсинг DOCX"
          format: "DOCX"
          link: "/parser/java/extract-text/docx/"
          description: "(Документ Word 2007+)"
          
        # format loop 3
        - name: "Парсинг PPTX"
          format: "PPTX"
          link: "/parser/java/extract-text/pptx/"
          description: "(Формат презентации Open XML)"
          
        # format loop 4
        - name: "Парсинг XLSX"
          format: "XLSX"
          link: "/parser/java/extract-text/xlsx/"
          description: "(Рабочая книга Open XML)"
          
        # format loop 5
        - name: "Парсинг TXT"
          format: "TXT"
          link: "/parser/java/extract-text/txt/"
          description: "(Текстовый файл)"
          
        # format loop 6
        - name: "Парсинг RTF"
          format: "RTF"
          link: "/parser/java/extract-text/rtf/"
          description: "(Формат Rich Text)"
          
        # format loop 7
        - name: "Парсинг XML"
          format: "XML"
          link: "/parser/java/extract-text/xml/"
          description: "(Расширяемый язык разметки)"
          
        # format loop 8
        - name: "Парсинг EPUB"
          format: "EPUB"
          link: "/parser/java/extract-text/epub/"
          description: "(Файл открытой электронной книги)"
         
          

---