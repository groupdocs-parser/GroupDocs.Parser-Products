---
############################# Static ############################
layout: "landing"
date: 2025-12-09T14:10:41
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
    # supported_platforms loop
    - title: "Python"
      tag: "python-net"

############################# Head ############################
head_title: "GroupDocs.Parser for .NET Document Parser SDK для .NET"
head_description: "Высокопроизводительный Document Parser SDK для .NET. Извлекайте текст, изображения, метаданные, штрихкоды, таблицы и другие данные из PDF, Word, Excel, электронных писем и более 50 форматов документов."

############################# Header ############################
title: "Document Parser SDK для .NET"
description: "Добавьте быстрое и точное парсирование документов в ваши приложения .NET и извлекайте текст, изображения, метаданные и структурированные данные из документов и изображений."
words:
  for: "для"

actions:
  main: "Nuget Скачать"
  main_link: "https://www.nuget.org/packages/GroupDocs.Parser"
  alt: "Лицензирование"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/net/"
  title: "Готовы начать?"
  description: "Попробуйте функции GroupDocs.Parser бесплатно или запросите лицензию"

release:
  title: "Выпущена версия {0}"
  notes: "Посмотрите, что нового"
  downloads: "Загрузки"

code:
  title: "Быстро разбирайте содержимое документов с помощью SDK"
  more: "Больше примеров"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
  install: "dotnet add package GroupDocs.Parser"
  content: |
    ```csharp {style=abap}   
    // Передайте исходный файл в экземпляр Parser
    using (var parser = new Parser("source.pdf"))
    {
        // Передайте текст документа в TextReader
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
  title: "GroupDocs.Parser в двух словах"
  description: "Document Parser SDK для выполнения высокоточного парсирования документов в приложениях .NET"
  features:
    # feature loop
    - title: "Извлечение данных из документов"
      content: "GroupDocs.Parser for .NET API позволяет получать текст, метаданные и изображения из широкого спектра форматов файлов, таких как офисные документы, электронные письма, вложения и архивы. Этот мощный инструмент помогает эффективно получать доступ и обрабатывать ценную информацию, содержащуюся в этих файлах, для различных приложений, таких как аналитика данных, индексация поисковых систем или системы управления контентом."

    # feature loop
    - title: "Разбор документов"
      content: "Извлекайте различные элементы, такие как гиперссылки, таблицы, QR‑коды, штрихкоды и данные из PDF‑форм. Также разбирайте любую необходимую информацию из документов с помощью пользовательских шаблонов."

    # feature loop
    - title: "Настройка результатов"
      content: ".NET API позволяет получать данные в различных форматах, таких как сырой, структурированный, HTML или Markdown. Кроме того, API предоставляет функцию поиска для обнаружения конкретных слов или фраз в тексте документов."

############################# Platforms ############################
platforms:
  enable: true
  title: "Независимость от платформы"
  description: "GroupDocs.Parser for .NET поддерживает следующие операционные системы, фреймворки и менеджеры пакетов"
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
    GroupDocs.Parser for .NET поддерживает работу со следующими [форматами файлов](https://docs.groupdocs.com/parser/net/supported-document-formats/).
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
  title: "Функции GroupDocs.Parser for .NET"
  description: "Извлекайте данные из PDF, офисных документов, изображений и других форматов быстро и точно с помощью нашего .NET Document Parser SDK"

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
  description: "Некоторые типичные сценарии использования GroupDocs.Parser for .NET"
  items:
    # code sample loop
    - title: "Извлечение изображений из PDF‑документов"
      content: |
        GroupDocs.Parser for .NET упрощает C#‑разработчикам извлечение изображений из [документов](https://docs.groupdocs.com/parser/net/extract-images-from-documents/):
        {{< landing/code title="Извлечение изображений из PDF‑документов на C#">}}
        ```csharp {style=abap}
        // Создайте экземпляр класса Parser
        using (var parser = new Parser("source.pptx"))
        {
            // Извлеките изображения
            var images = parser.GetImages();

            // Проверьте, извлечено ли что‑то
            if (images == null)
            {
                return;
            }
            // Итерируйтесь по изображениям
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
    - title: "Извлечение штрихкодов из изображений"
      content: |
        Используйте наш .NET API для извлечения [штрихкодов](https://docs.groupdocs.com/parser/net/extract-barcodes-from-document/) из изображений:
        {{< landing/code title="Извлечение штрих‑кодов из изображений на C#">}}
        ```csharp {style=abap}   
        // Загрузите исходное изображение в Parser
        using (var parser = new Parser("source.jpg"))
        {
            // Проверьте, поддерживает ли файл извлечение штрих‑кодов
            if (parser.Features.Barcodes)
            {
                // Извлеките штрих‑коды из файла
                var barcodes = parser.GetBarcodes();

                // Итерируйтесь по штрих‑кодам
                foreach (var barcode in barcodes)
                {
                    // Выведите индекс страницы
                    Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                    // Выведите значение штрих‑кода
                    Console.WriteLine("Value: " + barcode.Value);
                }
            }
        }
        ```
        {{< /landing/code >}}

---
