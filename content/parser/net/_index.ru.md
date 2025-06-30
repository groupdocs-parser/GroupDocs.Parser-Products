---
############################# Static ############################
layout: "landing"
date: 2025-06-30T10:26:00
draft: false

lang: ru
product: "Parser"
product_tag: "parser"
platform: "Net"
platform_tag: "net"

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
head_title: "Приложения для парсинга документов GroupDocs.Parser for .NET"
head_description: "Получите универсальное решение для парсинга документов для приложений .NET. Извлекайте данные из форматов документов онлайн с помощью простого функционала перетаскивания."

############################# Header ############################
title: "Парсите документы через API .NET"
description: "Извлекайте данные из документов и изображений на любой платформе, используя наши гибкие API и решения на базе приложений для программистов и конечных пользователей."
words:
  for: "для"

actions:
  main: "Скачать Nuget"
  main_link: "https://www.nuget.org/packages/GroupDocs.Parser"
  alt: "Лицензирование"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/net/"
  title: "Готовы приступить к работе?"
  description: "Попробуйте функции GroupDocs.Parser бесплатно или запросите лицензию"

release:
  title: "Версия {0} выпущена"
  notes: "Смотрите, что нового"
  downloads: "Скачивания"

code:
  title: "Быстрый парсинг содержимого документа"
  more: "Больше примеров"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
  install: "dotnet add package GroupDocs.Parser"
  content: |
    ```csharp {style=abap}   
    // Передайте исходный файл экземпляру Parser
    using (var parser = new Parser("source.pdf"))
    {
        // Передайте текст документа экземпляру TextReader
        using (var textReader = parser.GetText())
        {
            // Обработайте текст документа
            Console.WriteLine(textReader?.ReadToEnd());
        }
    }  
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser в кратком изложении"
  description: "API для парсинга документов в приложениях .NET"
  features:
    # feature loop
    - title: "Извлечение данных из документов"
      content: "GroupDocs.Parser for .NET API позволяет извлекать текст, метаданные и изображения из широкого диапазона форматов файлов, таких как офисные документы, электронные письма, вложения и архивы. Этот мощный инструмент помогает эффективно получать и обрабатывать ценные данные, содержащиеся в этих файлах для различных приложений, таких как анализ данных, индексация поисковых систем или системы управления контентом."

    # feature loop
    - title: "Парсинг документов"
      content: "Извлечение различных элементов, таких как гиперссылки, таблицы, QR-коды, штрих-коды и данные из форм PDF. Также можно парсить любую необходимую информацию из документов с помощью пользовательских шаблонов."

    # feature loop
    - title: "Настройка результатов"
      content: ".NET API позволяет извлекать данные в различных форматах, таких как необработанные, структурированные, HTML или Markdown. Дополнительно API предлагает функциональность поиска для нахождения конкретных слов или фраз в тексте документов."

############################# Platforms ############################
platforms:
  enable: true
  title: "Независимость платформы"
  description: "GroupDocs.Parser for .NET поддерживает следующие операционные системы, фреймворки и менеджеры пакетов."
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
    - title: "VS Code"
      image: "vs_code"
    # platform loop
    - title: "ReSharper"
      image: "resharper"
    # platform loop
    - title: "macOS"
      image: "finder"
    # platform loop
    - title: "Linux"
      image: "linux"
    # platform loop
    - title: "NuGet"
      image: "nuget"

############################# File formats ############################
formats:
  enable: true
  title: "Поддерживаемые форматы файлов"
  description: |
    GroupDocs.Parser for .NET поддерживает операции с следующими [форматами файлов](https://docs.groupdocs.com/parser/net/supported-document-formats/).
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
  title: "GroupDocs.Parser for .NET функции"
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
  description: "Некоторые случаи использования типичных операций GroupDocs.Parser for .NET"
  items:
    # code sample loop
    - title: "Извлечение изображений из PDF-документов"
      content: |
        GroupDocs.Parser for .NET облегчает разработчикам C# извлечение изображений из [документов](https://docs.groupdocs.com/parser/net/extract-images-from-documents/):
        {{< landing/code title="Извлечение изображений из PDF-документов на C#">}}
        ```csharp {style=abap}
        // Создайте экземпляр класса Parser
        using (var parser = new Parser("source.pptx"))
        {
            // Извлеките изображения
            var images = parser.GetImages();

            // Проверьте, извлечено ли что-то
            if (images == null)
            {
                return;
            }
            // Итерация по изображениям
            foreach (PageImageArea image in images)
            {
                // Выведите индекс страницы, прямоугольник и тип изображения
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Type: {2}", 
                    image.Page.Index, image.Rectangle, image.FileType));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Извлечение штрих-кодов из изображений"
      content: |
        Используйте наш .NET API для извлечения [штрих-кодов](https://docs.groupdocs.com/parser/net/extract-barcodes-from-document/) из изображений:
        {{< landing/code title="Извлечение штрих-кодов из изображений на C#">}}
        ```csharp {style=abap}   
        // Загрузите исходное изображение в Parser
        using (var parser = new Parser("source.jpg"))
        {
            // Проверьте, поддерживает ли файл извлечение штрих-кодов
            if (parser.Features.Barcodes)
            {
                // Извлеките штрих-коды из файла
                var barcodes = parser.GetBarcodes();

                // Итерация по штрих-кодам
                foreach (var barcode in barcodes)
                {
                    // Выведите индекс страницы
                    Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                    // Выведите значение штрих-кода
                    Console.WriteLine("Value: " + barcode.Value);
                }
            }
        }
        ```
        {{< /landing/code >}}

---
