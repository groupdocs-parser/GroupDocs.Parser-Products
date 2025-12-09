---
############################# Static ############################
layout: "landing"
date: 2025-12-09T14:10:41
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
    # supported_platforms loop
    - title: "Python"
      tag: "python-net"

############################# Head ############################
head_title: "GroupDocs.Parser for Java Document Parser SDK для Java"
head_description: "Высокопроизводительный SDK для разбора документов для Java. Извлекает текст, изображения, метаданные, штрихкоды, таблицы и другие данные из PDF, Word, Excel, электронных писем и более 50 форматов документов."

############################# Header ############################
title: "Document Parser SDK для Java"
description: "Добавьте быстрое и точное разбор документов в ваши приложения Java и извлекайте текст, изображения, метаданные и структурированные данные из документов и изображений."
words:
  for: "для"

actions:
  main: "Maven Скачать"
  main_link: "https://releases.groupdocs.com/java/repo/com/groupdocs/groupdocs-parser/"
  alt: "Лицензирование"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/java/"
  title: "Готовы начать?"
  description: "Попробуйте функции GroupDocs.Parser бесплатно или запросите лицензию"

release:
  title: "Выпущена версия {0}"
  notes: "Посмотрите, что нового"
  downloads: "Загрузки"

code:
  title: "Быстро разбирайте содержимое документов с помощью SDK"
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
    // Передайте исходный файл в экземпляр Parser
    try (Parser parser = new Parser("source.pdf"))
    {
        // Передайте текст документа в TextReader
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
  title: "GroupDocs.Parser в двух словах"
  description: "Document Parser SDK для выполнения высокоточного разбора документов в приложениях Java"
  features:
    # feature loop
    - title: "Извлечение данных из документов"
      content: "GroupDocs.Parser for Java API позволяет получать текст, метаданные и изображения из широкого спектра форматов файлов, таких как офисные документы, электронные письма, вложения и архивы. Этот мощный инструмент поможет вам эффективно получать доступ к ценнейшей информации, содержащейся в этих файлах, и обрабатывать её для различных задач, например анализа данных, индексации поисковых систем или систем управления контентом."

    # feature loop
    - title: "Разбор документов"
      content: "Извлекайте различные элементы, такие как гиперссылки, таблицы, QR‑коды, штрихкоды и данные из PDF‑форм. Также разбирайте любую необходимую информацию из документов с помощью пользовательских шаблонов."

    # feature loop
    - title: "Настройка результатов"
      content: "Java API позволяет получать данные в различных форматах, таких как необработанный, структурированный, HTML или Markdown. Кроме того, API предоставляет возможность поиска конкретных слов или фраз в тексте документов."

############################# Platforms ############################
platforms:
  enable: true
  title: "Независимость от платформы"
  description: "GroupDocs.Parser for Java поддерживает следующие операционные системы, фреймворки и менеджеры пакетов"
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
    GroupDocs.Parser for Java поддерживает работу со следующими [форматами файлов](https://docs.groupdocs.com/parser/java/supported-document-formats/).
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
        * **Переносимый:** PDF 
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
  title: "GroupDocs.Parser for Java возможности"
  description: "Извлекайте данные из PDF, офисных документов, изображений и других форматов быстро и точно с помощью нашего Java Document Parser SDK"

  items:
    # feature loop
    - icon: "text"
      title: "Извлечение текста"
      content: "Извлекайте текстовую информацию из различных форматов файлов, таких как офисные документы, PDF‑файлы и изображения, для удобного чтения и анализа."

    # feature loop
    - icon: "image"
      title: "Извлечение изображений"
      content: "Получайте визуальное содержимое из разнообразных источников, таких как офисные документы и PDF‑файлы, для удобного доступа и использования."

    # feature loop
    - icon: "qr"
      title: "Сканирование QR‑кодов"
      content: "Обнаруживайте и декодируйте QR‑коды, находящиеся в офисных документах, PDF‑файлах или визуальном контенте, для эффективного получения информации."

    # feature loop
    - icon: "email"
      title: "Извлечение данных из вложений электронных писем и архивов"
      content: "Собирайте ценную информацию из электронных сообщений, вложений файлов и сжатых источников данных для эффективного анализа и использования."

    # feature loop
    - icon: "table"
      title: "Извлечение таблиц"
      content: "Определяйте и извлекайте табличные данные из PDF‑документов для структурированного анализа и использования."

    # feature loop
    - icon: "hyperlink"
      title: "Извлечение гиперссылок"
      content: "Находите и извлекайте гиперссылки и адреса электронной почты в офисных документах или PDF‑файлах для удобного доступа."

    # feature loop
    - icon: "pdf"
      title: "Разбор PDF‑форм"
      content: "PDF‑формы — это цифровые документы с заполняемыми полями для взаимодействия с пользователем, позволяющие вводить информацию электронно. .NET API можно использовать для извлечения данных из этих форм для эффективной обработки."

    # feature loop
    - icon: "template"
      title: "Разбор данных по шаблонам"
      content: "Создавайте пользовательские шаблоны и используйте их с .NET API для разбора конкретной информации из PDF‑файлов, упрощая процессы извлечения данных."

    # feature loop
    - icon: "search"
      title: "Поиск текста в документах"
      content: "Быстро находите определённые слова или шаблоны в документах."


############################# Code samples ############################
code_samples:
  enable: true
  title: "Примеры кода"
  description: "Некоторые примеры использования типовых операций GroupDocs.Parser for Java"
  items:
    # code sample loop
    - title: "Извлечение изображений из PDF‑документов"
      content: |
        GroupDocs.Parser for Java упрощает Java разработчикам извлечение изображений из [документов](https://docs.groupdocs.com/parser/java/extract-images-from-documents/):
        {{< landing/code title="Извлечение изображений из PDF‑документов на Java">}}
        ```java {style=abap}
        // Создайте экземпляр класса Parser
        try (Parser parser = new Parser("source.pdf"))
        {
            // Извлеките изображения
            Iterable<PageImageArea> images = parser.getImages();

            // Проверьте, извлечено ли что‑то
            if (images == null) {
                return;
            }

            // Итерируйтесь по изображениям
            for (PageImageArea image : images) {
                // Выведите индекс страницы, прямоугольник и тип изображения
                System.out.println(String.format("Page: %d, R: %s, Type: %s", 
                    image.getPage().getIndex(), image.getRectangle(), image.getFileType()));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Извлечение штрихкодов из изображений"
      content: |
        Используйте наш API Java для извлечения [штрихкоды](https://docs.groupdocs.com/parser/java/extract-barcodes-from-document/) из изображений:
        {{< landing/code title="Извлечение штрих‑кодов из изображений на Java">}}
        ```java {style=abap}   
        // Загрузите исходное изображение в Parser
        try (Parser parser = new Parser("source.jpg")){

            // Проверьте, поддерживает ли файл извлечение штрих‑кодов
            if (!parser.getFeatures().isBarcodes()) {

                // Извлеките штрих‑коды из файла
                Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();

                // Итерируйтесь по штрих‑кодам
                for (PageBarcodeArea barcode : barcodes) {
                    // Выведите индекс страницы
                    System.out.println("Page: " + barcode.getPage().getIndex());
                    // Выведите значение штрих‑кода
                    System.out.println("Value: " + barcode.getValue());
                }
            }
        }
        ```
        {{< /landing/code >}}

---
