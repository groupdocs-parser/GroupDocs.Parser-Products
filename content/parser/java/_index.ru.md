---
############################# Static ############################
layout: "landing"
date: 2025-06-30T10:26:00
draft: false

lang: ru
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Drop-down ############################
supported_platforms:
  items:
    # supported_platforms loop
    - title: ".NET"
      tag: "net"
    # supported_platforms loop
    - title: "Java"
      tag: "java"

############################# Head ############################
head_title: "Приложения для парсинга документов GroupDocs.Parser for Java"
head_description: "Получите универсальное решение для парсинга документов для приложений Java. Извлекайте данные из форматов документов онлайн с помощью простого функционала перетаскивания."

############################# Header ############################
title: "Парсите документы через API Java"
description: "Извлекайте данные из документов и изображений на любой платформе, используя наши гибкие API и решения на базе приложений для программистов и конечных пользователей."
words:
  for: "для"

actions:
  main: "Скачать Maven"
  main_link: "https://releases.groupdocs.com/java/repo/com/groupdocs/groupdocs-parser/"
  alt: "Лицензирование"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/java/"
  title: "Готовы приступить к работе?"
  description: "Попробуйте функции GroupDocs.Parser бесплатно или запросите лицензию"

release:
  title: "Версия {0} выпущена"
  notes: "Смотрите, что нового"
  downloads: "Скачивания"

code:
  title: "Быстро получите содержимое документа"
  more: "Больше примеров"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java/"
  install: |
    <dependency>
      <groupId>com.groupdocs</groupId>
      <artifactId>groupdocs-parser</artifactId>
      <version>{0}</version>
    </dependency>
  content: |
    ```java {style=abap}  
    // Передайте исходный файл экземпляру Parser
    try (Parser parser = new Parser("source.pdf"))
    {
        // Передайте текст документа экземпляру TextReader
        try (TextReader reader = parser.getText())
        {
            // Обработайте текст документа
            System.out.println(reader == null 
                ? "" 
                : reader.readToEnd());
        }
    }
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser в кратком изложении"
  description: "API для парсинга документов в приложениях Java"
  features:
    # feature loop
    - title: "Извлечение данных из документов"
      content: "GroupDocs.Parser for Java API позволяет извлекать текст, метаданные и изображения из широкого диапазона форматов файлов, таких как офисные документы, электронные письма, вложения и архивы. Этот мощный инструмент помогает эффективно получать и обрабатывать ценные данные, содержащиеся в этих файлах для различных приложений, таких как анализ данных, индексация поисковых систем или системы управления контентом."

    # feature loop
    - title: "Парсинг документов"
      content: "Извлечение различных элементов, таких как гиперссылки, таблицы, QR-коды, штрих-коды и данные из форм PDF. Также можно парсить любую необходимую информацию из документов с помощью пользовательских шаблонов."

    # feature loop
    - title: "Настройка результатов"
      content: "Java API позволяет извлекать данные в различных форматах, таких как необработанные, структурированные, HTML или Markdown. Дополнительно API предлагает функциональность поиска для нахождения конкретных слов или фраз в тексте документов."

############################# Platforms ############################
platforms:
  enable: true
  title: "Независимость платформы"
  description: "GroupDocs.Parser for Java поддерживает следующие операционные системы, фреймворки и менеджеры пакетов."
  items:
    # platform loop
    - title: "Amazon"
      image: "amazon"
    # platform loop
    - title: "Docker"
      image: "docker"
    # platform loop
    - title: "Azure"
      image: "azure"
    # platform loop
    - title: "Eclipse"
      image: "eclipse"
    # platform loop
    - title: "IntelliJ"
      image: "intellij"
    # platform loop
    - title: "Windows"
      image: "windows"
    # platform loop
    - title: "Linux"
      image: "linux"
    # platform loop
    - title: "Maven"
      image: "maven"

############################# File formats ############################
formats:
  enable: true
  title: "Поддерживаемые форматы файлов"
  description: |
    GroupDocs.Parser for Java поддерживает операции с следующими [форматами файлов](https://docs.groupdocs.com/parser/java/supported-document-formats/).
  groups:
    # group loop
    - color: "green"
      content: |
        ### Форматы Microsoft Office
        * **Word:** DOCX, DOC, DOCM, DOT, DOTX, DOTM, RTF
        * **Excel:** XLSX, XLS, XLSM, XLSB, XLTM, XLT, XLTM, XLTX, XLAM, SXC, SpreadsheetML
        * **PowerPoint:** PPT, PPTX, PPS, PPSX, PPSM, POT, POTM, POTX, PPTM
    # group loop
    - color: "blue"
      content: |
        ### Изображения и другие форматы
        * **Портативные:** PDF 
        * **Изображения:** JPG, BMP, PNG, TIFF, GIF
        * **Другие офисные форматы:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### Другие форматы
        * **Веб:** HTML, MHTML 
        * **Архивы:** ZIP, TAR, 7Z 
        * **Электронные книги:** CHM, EPUB, FB2, MOBI 
        
        

############################# Features ############################
features:
  enable: true
  title: "GroupDocs.Parser for Java функции"
  description: "Быстро и точно извлекайте данные из PDF, офисных документов и изображений"

  items:
    # feature loop
    - icon: "text"
      title: "Извлечение текста"
      content: "Извлечение текстовой информации из различных форматов файлов, таких как офисные документы, PDF-файлы и изображения для удобства чтения и анализа."

    # feature loop
    - icon: "image"
      title: "Извлечение изображений"
      content: "Получение визуального контента из различных источников, таких как офисные документы, PDF-файлы для удобства доступа и использования."

    # feature loop
    - icon: "qr"
      title: "Сканирование QR-кодов"
      content: "Выявление и расшифровка QR-кодов, присутствующих в офисных документах, PDF-файлах или визуальном контенте для успешного получения информации."

    # feature loop
    - icon: "email"
      title: "Извлечение данных из вложений электронной почты и архивов"
      content: "Сбор ценной информации из электронных писем, вложений файлов и сжатых источников данных для дальнейшего анализа и использования."

    # feature loop
    - icon: "table"
      title: "Извлечение таблиц"
      content: "Определение и извлечение табличных данных из PDF-документов для систематизированного анализа и использования."

    # feature loop
    - icon: "hyperlink"
      title: "Извлечение гиперссылок"
      content: "Поиск и извлечение гиперссылок и адресов электронной почты в офисных документах или PDF-файлах для эффективного доступа."

    # feature loop
    - icon: "pdf"
      title: "Парсинг PDF-форм"
      content: "PDF-формы - это цифровые документы с заполняемыми полями для взаимодействия с пользователем, позволяющие электронно вводить информацию. API .NET может быть использован для извлечения данных из этих форм для эффективной обработки."

    # feature loop
    - icon: "template"
      title: "Парсинг данных по шаблонам"
      content: "Создавайте пользовательские шаблоны и используйте их с API .NET для парсинга конкретной информации из PDF-файлов, упрощая процессы извлечения данных."

    # feature loop
    - icon: "search"
      title: "Поиск текста в документах"
      content: "Быстро находите конкретные слова или паттерны в документах."


############################# Code samples ############################
code_samples:
  enable: true
  title: "Примеры кода"
  description: "Некоторые случаи использования типичных операций GroupDocs.Parser for Java"
  items:
    # code sample loop
    - title: "Извлечение изображений из PDF-документов"
      content: |
        GroupDocs.Parser for Java облегчает разработчикам Java извлечение изображений из [документов](https://docs.groupdocs.com/parser/java/extract-images-from-documents/):
        {{< landing/code title="Извлечение изображений из PDF-документов на Java">}}
        ```java {style=abap}
        // Создайте экземпляр класса Parser
        try (Parser parser = new Parser("source.pdf"))
        {
            // Извлеките изображения
            Iterable<PageImageArea> images = parser.getImages();

            // Проверьте, извлечено ли что-то
            if (images == null) {
                return;
            }

            // Итерация по изображениям
            for (PageImageArea image : images) {
                // Выведите индекс страницы, прямоугольник и тип изображения
                System.out.println(String.format("Page: %d, R: %s, Type: %s", 
                    image.getPage().getIndex(), image.getRectangle(), image.getFileType()));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Извлечение штрих-кодов из изображений"
      content: |
        Используйте наш Java API для извлечения [штрих-кодов](https://docs.groupdocs.com/parser/java/extract-barcodes-from-document/) из изображений:
        {{< landing/code title="Извлечение штрих-кодов из изображений на Java">}}
        ```java {style=abap}   
        // Загрузите исходное изображение в Parser
        try (Parser parser = new Parser("source.jpg")){

            // Проверьте, поддерживает ли файл извлечение штрих-кодов
            if (!parser.getFeatures().isBarcodes()) {

                // Извлеките штрих-коды из файла
                Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();

                // Итерация по штрих-кодам
                for (PageBarcodeArea barcode : barcodes) {
                    // Выведите индекс страницы
                    System.out.println("Page: " + barcode.getPage().getIndex());
                    // Выведите значение штрих-кода
                    System.out.println("Value: " + barcode.getValue());
                }
            }
        }
        ```
        {{< /landing/code >}}

---
