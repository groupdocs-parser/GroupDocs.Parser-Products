


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:26
draft: false
lang: ru
format: Pptx
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "Извлечение гиперссылок из файлов PPTX в приложениях C#"
head_description: "Используйте GroupDocs.Parser для обнаружения и извлечения гиперссылок из файлов PPTX в C# без дополнительных инструментов или программного обеспечения."

############################# Header ############################
title: "Извлечение гиперссылок из PPTX с использованием C#" 
description: "Обнаруживайте и извлекайте URLs и гиперссылки из PDF, Word, Excel и других типов документов с помощью GroupDocs.Parser в ваших приложениях .NET."
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Скачать бесплатную пробную версию"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "О API GroupDocs.Parser for .NET"
    link: "/parser/net/"
    link_title: "Узнать больше"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/) — это универсальный API для разбора документов, предназначенный для разработчиков .NET. Он поддерживает извлечение гиперссылок, текста, изображений и структурированных данных из различных форматов файлов, таких как PDF, Word, Excel, HTML и других без использования стороннего программного обеспечения.

############################# Steps ############################
steps:
    enable: true
    title: "Шаги для извлечения гиперссылок из Pptx в C#"
    content: |
      [GroupDocs.Parser](/parser/net/) позволяет разработчикам .NET извлекать гиперссылки из файлов PPTX в несколько простых шагов:
      
      1. Загрузите файл PPTX с помощью экземпляра Parser.
      2. Проверьте, поддерживает ли документ извлечение гиперссылок.
      3. Извлеките список гиперссылок из документа.
      4. Просмотрите результаты и работайте с извлеченными URL-адресами.
   
    code:
      platform: "net"
      copy_title: "Копировать"
      install:
        command: |
        command: "dotnet add package GroupDocs.Parser"
        copy_tip: "Нажмите для копирования"
        copy_done: "Скопировано"
      links:
        #  loop
        - title: "Больше примеров"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
        #  loop
        - title: "Документация"
          link: "https://docs.groupdocs.com/parser/net/"
          
      content: |
        ```csharp {style=abap}
        // Загрузите документ, содержащий гиперссылки, с помощью класса Parser
        using (Parser parser = new Parser("input.pptx")) {

            // Убедитесь, что файл поддерживает извлечение гиперссылок
            if (!parser.Features.Hyperlinks)
            {
                Console.WriteLine("Извлечение гиперссылок недоступно для данного файла");
                return;
            }

            // Получите и обработайте извлеченные гиперссылки
            IEnumerable<PageHyperlinkArea> hyperlinks = parser.GetHyperlinks();

            foreach (PageHyperlinkArea h in hyperlinks)
            {
                Console.WriteLine(h.Text);
                Console.WriteLine(h.Url);
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "Расширенные возможности разбора документов"
  description: "В дополнение к извлечению гиперссылок, GroupDocs.Parser позволяет извлекать текст, метаданные, изображения и структурированные данные — поддерживая мощные рабочие процессы обработки данных."
  image: "/img/parser/features_extract-hyperlink.webp" # 500x500 px
  image_description: "Обнаружение гиперссылок и разбор документов"
  features:
    # feature loop
    - title: "Обнаружение гиперссылок в документах"
      content: "Быстро извлекайте URLs и аннотации ссылок из таких документов, как PDF, Word-файлы, электронные таблицы и других."

    # feature loop
    - title: "Поддержка веб и встроенных ссылок"
      content: "Обнаруживайте и извлекайте как стандартные веб-URLs, так и встроенные ссылки из документов в различных форматах."

    # feature loop
    - title: "Гибкие параметры разбора"
      content: "Настраивайте параметры извлечения для сканирования специфических разделов или страниц для повышения производительности и точности."
      
  code_samples:
    # code sample loop
    - title: "Как извлечь гиперссылки из PDF с использованием параметров ссылок"
      content: |
        Этот пример кода демонстрирует, как извлечь все гиперссылки из PDF файла с использованием пользовательских параметров.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Инициализируйте Parser с документом PDF
        using (Parser parser = new Parser("input.docx"))
        {
            // Проверьте, поддерживается ли извлечение гиперссылок
            if (!parser.Features.Hyperlinks)
            {
                return;
            }

            // Установите параметры извлечения ссылок для уточнения результатов
            PageAreaOptions options = new PageAreaOptions(new Rectangle(new Point(380, 90), new Size(150, 50)));

            // Извлеките данные о гиперссылках из документа
            IEnumerable<PageHyperlinkArea> hyperlinks = parser.GetHyperlinks(options);

            // Обработайте список извлеченных ссылок
            foreach (PageHyperlinkArea h in hyperlinks)
            {
                Console.WriteLine(h.Text);
                Console.WriteLine(h.Url);
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
    - title: "Скачивание Nuget"
      link: "https://releases.groupdocs.com/parser/net/"
      color: "red"
        #  loop
    - title: "Лицензирование"
      link: "https://purchase.groupdocs.com/pricing/parser/net/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "Поддерживаемые форматы для извлечения гиперссылок"
    exclude: "PPTX"
    description: "GroupDocs.Parser может извлекать гиперссылки из широкого спектра типов документов. Ниже представлены обычно поддерживаемые форматы."
    items: 
        # format loop 1
        - name: "Парсинг PDF"
          format: "PDF"
          link: "/parser/net/extract-hyperlink/pdf/"
          description: "(Формат переносимого документа)"
          
        # format loop 2
        - name: "Парсинг DOCX"
          format: "DOCX"
          link: "/parser/net/extract-hyperlink/docx/"
          description: "(Документ Word 2007+)"
          
        # format loop 3
        - name: "Парсинг PPTX"
          format: "PPTX"
          link: "/parser/net/extract-hyperlink/pptx/"
          description: "(Формат презентации Open XML)"
          
        # format loop 4
        - name: "Парсинг XLSX"
          format: "XLSX"
          link: "/parser/net/extract-hyperlink/xlsx/"
          description: "(Рабочая книга Open XML)"
          
        # format loop 5
        - name: "Парсинг TXT"
          format: "TXT"
          link: "/parser/net/extract-hyperlink/txt/"
          description: "(Текстовый файл)"
          
        # format loop 6
        - name: "Парсинг RTF"
          format: "RTF"
          link: "/parser/net/extract-hyperlink/rtf/"
          description: "(Формат Rich Text)"
          
        # format loop 7
        - name: "Парсинг XML"
          format: "XML"
          link: "/parser/net/extract-hyperlink/xml/"
          description: "(Расширяемый язык разметки)"
          
        # format loop 8
        - name: "Парсинг EPUB"
          format: "EPUB"
          link: "/parser/net/extract-hyperlink/epub/"
          description: "(Файл открытой электронной книги)"
         
          

---