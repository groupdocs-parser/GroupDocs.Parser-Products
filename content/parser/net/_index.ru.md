---
############################# Static ############################
layout: "landing"
date: 2024-02-13T17:01:03
draft: false
#operation: 
#parsertype: 
#fileformat: 
#productName: Java
lang: ru
#productCode: java
#otherformats: 
#breadcrumb: Put  parser on  for Java
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: ".NET, Java, облачные API и приложения для онлайн-анализа документов"
head_description: "Получите комплексное решение для анализа документов для .NET, Java и облачных приложений. Извлекайте данные из форматов документов онлайн с помощью простой функции перетаскивания."

############################# Header ############################
title: "Разбор документов<br>через API .NET"
description: "Извлекайте данные из документов и изображений на любой платформе, используя наши гибкие API и решения на базе приложений для программистов и конечных пользователей."
words:
  for: "для"

actions:
  main: "Бесплатная NuGet загрузка"
  main_link: "https://www.nuget.org/packages/GroupDocs.Parser"
  alt: "Лицензирование"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/net"
  title: "Готовы начать?"
  description: "Попробуйте функции GroupDocs.Parser бесплатно или запросите лицензию."

release:
  title: "Версия {0} выпущена"
  notes: "Посмотрите, что нового"
  downloads: "Загрузки"

code:
  title: "Извлечение текста из файлов PDF на C#"
  more: "Больше примеров"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET"
  install: "dotnet add package GroupDocs.Parser"
  content: |
    ```csharp {style=abap}   
    // Create an instance of Parser class
    using (var parser = new Parser(fileName))
    {
        // Extract a text into the reader
        using (var textReader = parser.GetText())
        {
            // Print a text from the document
            Console.WriteLine(textReader?.ReadToEnd());
        }
    }
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser: краткий обзор"
  description: "API для выполнения анализа документов в приложениях .NET"
  features:
    # feature loop
    - title: "Извлечение данных из документов"
      content: ".NET API позволяет извлекать текст, метаданные и изображения из широкого спектра форматов файлов, таких как документы Office, электронные письма, вложения и архивы. Этот мощный инструмент помогает вам эффективно получать доступ и обрабатывать ценную информацию, содержащуюся в этих файлах, для различных приложений, таких как анализ данных, индексирование поисковыми системами или системы управления контентом."

    # feature loop
    - title: "Разбор документов"
      content: "Извлекайте различные элементы, такие как гиперссылки, таблицы, QR-коды, штрих-коды и данные, из форм PDF. Также анализируйте любую желаемую информацию из документов, используя пользовательские шаблоны."

    # feature loop
    - title: "Настройка результатов"
      content: "API .NET позволяет получать данные в различных форматах, таких как необработанные, структурированные, HTML или Markdown. Кроме того, API предлагает функцию поиска определенных слов или фраз в тексте документов."

############################# Platforms ############################
platforms:
  enable: true
  title: "Независимость от платформы"
  description: "GroupDocs.Parser for .NET поддерживает следующие операционные системы, платформы и менеджеры пакетов."
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
    GroupDocs.Parser for .NET поддерживает операции со следующими [форматами файлов](https://docs.groupdocs.com/parser/net/supported-document-formats/).
  groups:
    # group loop
    - color: "green"
      content: |
        ### Microsoft Office форматы
        * **Word:**  DOCX, DOC, DOCM, DOT, DOTX, DOTM, RTF
        * **Excel:** XLSX, XLS, XLSM, XLSB, XLTM, XLT, XLTM, XLTX, XLAM, SXC, SpreadsheetML
        * **PowerPoint:** PPT, PPTX, PPS, PPSX, PPSM, POT, POTM, POTX, PPTM
    # group loop
    - color: "blue"
      content: |
        ### Изображения и другие форматы
        * **Portable:** PDF
        * **Изображений:** JPG, BMP, PNG, TIFF, GIF
        * **Другие форматы офисов:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### Другие форматы
        * **Интернет:** HTML, MHTML
        * **Архивы:** ZIP, TAR, 7Z
        * **Электронные книги:** CHM, EPUB, FB2, MOBI

############################# Features ############################
features:
  enable: true
  title: "Возможности GroupDocs.Parser"
  description: "Быстро и точно извлекайте данные из PDF, документов Office и изображений."

  items:
    # feature loop
    - icon: "text"
      title: "Извлечь текст"
      content: "Извлекайте текстовую информацию из файлов различных форматов, таких как офисные документы, файлы PDF и изображения, для удобства чтения и анализа."

    # feature loop
    - icon: "image"
      title: "Извлечение изображений"
      content: "Извлекайте визуальный контент из различных источников, таких как офисные документы и файлы PDF, для удобного доступа и использования."

    # feature loop
    - icon: "qr"
      title: "Сканировать QR-коды"
      content: "Обнаруживайте и декодируйте QR-коды, присутствующие в офисных документах, файлах PDF или визуальном контенте, для эффективного поиска информации."

    # feature loop
    - icon: "email"
      title: "Извлечение данных из вложений и архивов электронной почты"
      content: "Собирайте ценную информацию из сообщений электронной почты, вложенных файлов и источников сжатых данных для эффективного анализа и использования."

    # feature loop
    - icon: "table"
      title: "Извлечение таблиц"
      content: "Идентификация и извлечение табличных данных из документов PDF для организованного анализа и использования."

    # feature loop
    - icon: "hyperlink"
      title: "Извлечение гиперссылок"
      content: "Находите и извлекайте гиперссылки и адреса электронной почты в офисных документах или файлах PDF для эффективного доступа."

    # feature loop
    - icon: "pdf"
      title: "Анализ форм PDF"
      content: "PDF Формы представляют собой цифровые документы с заполняемыми полями для взаимодействия с пользователем, позволяющими вводить информацию в электронном виде. .NET API можно использовать для извлечения данных из этих форм для эффективной обработки."

    # feature loop
    - icon: "template"
      title: "Парсить данные по шаблонам"
      content: "Создавайте собственные шаблоны и используйте их с API .NET для анализа конкретной информации из файлов PDF, упрощая процессы извлечения данных."

    # feature loop
    - icon: "search"
      title: "Поиск текста в документах"
      content: "Быстро находите определенные слова или шаблоны в документах."

############################# Code samples ############################
code_samples:
  enable: true
  title: "Пример кода"
  description: "Некоторые варианты использования типичных операций GroupDocs.Parser for .NET"
  items:
    # code sample loop
    - title: "Извлечение изображений из документов PDF"
      content: |
        .NET API позволяет разработчикам C# легко извлекать изображения из документов, выполнив несколько простых шагов.
        {{< landing/code title="Извлечение изображений из документов PDF на C#.">}}
        ```csharp {style=abap}
        // Create an instance of Parser class
        using (var parser = new Parser(fileName))
        {
            // Extract images
            var images = parser.GetImages();

            // Check if images extraction is supported
            if (images != null)
            {
                var imageIndex = 0;

                // Iterate over images
                foreach (var image in images)
                {
                    // Save the image to the file
                    image.Save($"{++imageIndex}{image.FileType.Extension}");
                }
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Извлечение штрих-кодов из изображений"
      content: |
        .NET API позволяет разработчикам C# легко извлекать штрих-коды из документов, выполнив несколько простых шагов.
        {{< landing/code title="Извлечение штрих-кодов из изображений">}}
        ```csharp {style=abap}   
        // Create an instance of Parser class
        using (var parser = new Parser(fileName))
        {
            // Check if the file supports barcode extracting
            if (parser.Features.Barcodes)
            {
                // Extract barcodes from the file.
                var barcodes = parser.GetBarcodes();

                // Iterate over barcodes
                foreach (var barcode in barcodes)
                {
                    // Print the page index
                    Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                    // Print the barcode value
                    Console.WriteLine("Value: " + barcode.Value);
                }
            }
        }
        ```
        {{< /landing/code >}}

---
