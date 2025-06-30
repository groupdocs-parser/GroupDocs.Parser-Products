


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:34
draft: false
lang: ru
format: Fb2
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "Извлечение изображений из файлов FB2 в приложениях C#"
head_description: "Используйте GroupDocs.Parser для обнаружения и извлечения изображений из файлов FB2 в C# без дополнительных инструментов."

############################# Header ############################
title: "Извлечение изображений из FB2 с использованием C#" 
description: "Определите и извлеките встроенные изображения из PDF, документов Word, таблиц Excel и других типов файлов с помощью GroupDocs.Parser в ваших приложениях .NET."
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
       [GroupDocs.Parser](/parser/net/) — это мощная библиотека для парсинга документов для разработчиков .NET. Она позволяет извлекать изображения, текст, гиперссылки и структурированные данные из популярных форматов файлов, таких как PDF, DOCX, XLSX, PPTX и других, без необходимости в сторонних приложениях.

############################# Steps ############################
steps:
    enable: true
    title: "Шаги для извлечения изображений из Fb2 в C#"
    content: |
      С [GroupDocs.Parser](/parser/net/) вы можете извлекать изображения из документов FB2 в ваших проектах .NET всего за несколько шагов:
      
      1. Инициализируйте Parser с файлом FB2.
      2. Извлеките элементы изображений из документа.
      3. Используйте извлеченные изображения по мере необходимости в вашем рабочем процессе.
   
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
        // Откройте документ, содержащий изображения, с помощью Parser
        using (Parser parser = new Parser("input.fb2")) {

            // Извлеките все встроенные изображения из файла
            IEnumerable<PageImageArea> images = parser.GetImages();

            // Обработайте случаи, когда изображения не найдены
            if (images == null)
            {
                return;
            }

            // Обработайте или сохраните полученные изображения
            foreach (PageImageArea image in images)
            {
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Type: {2}", 
                    image.Page.Index, image.Rectangle, image.FileType));
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "Комплексное извлечение содержания документов"
  description: "GroupDocs.Parser предлагает больше, чем просто извлечение изображений — вы также можете извлекать необработанный текст, гиперссылки, метаданные и структурированное содержимое для расширенных сценариев автоматизации."
  image: "/img/parser/features_extract-image.webp" # 500x500 px
  image_description: "Рабочий процесс извлечения изображений и парсинга документов"
  features:
    # feature loop
    - title: "Извлечение изображений из нескольких форматов"
      content: "Извлекайте встроенные изображения из различных форматов файлов, включая DOCX, PDF, PPTX, XLSX и графические файлы, такие как PNG, JPG и TIFF."

    # feature loop
    - title: "Сохранение оригинального качества изображений"
      content: "Изображения извлекаются с высокой точностью, сохраняя их оригинальное разрешение, формат и цветовой профиль."

    # feature loop
    - title: "Расширенные параметры извлечения"
      content: "Настройте извлечение изображений, фильтруя по странице, формату или разрешению, а также поддерживайте многополосные документы."
      
  code_samples:
    # code sample loop
    - title: "Как извлечь и сохранить изображения из документа PDF"
      content: |
        Этот пример демонстрирует, как извлечь все изображения из файла PDF и сохранить их в локальной файловой системе.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Загрузите PDF с помощью класса Parser
        using (Parser parser = new Parser("input.pdf"))
        {
            // Извлеките встроенные изображения из файла
            IEnumerable<PageImageArea> images = parser.GetImages();

            // Установите формат вывода и параметры изображений (например, PNG)
            ImageOptions options = new ImageOptions(ImageFormat.Png);

            // Запишите извлеченные изображения на диск
            int imageNumber = 0;
            foreach (PageImageArea image in images)
            {
                image.Save(imageNumber.ToString() + ".png", options);
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
    title: "Поддерживаемые форматы для извлечения изображений"
    exclude: "FB2"
    description: "GroupDocs.Parser обеспечивает точное извлечение изображений из широкого спектра документальных и графических форматов. Посмотрите ниже список часто поддерживаемых типов."
    items: 
        # format loop 1
        - name: "Парсинг PDF"
          format: "PDF"
          link: "/parser/net/extract-image/pdf/"
          description: "(Формат переносимого документа)"
          
        # format loop 2
        - name: "Парсинг DOCX"
          format: "DOCX"
          link: "/parser/net/extract-image/docx/"
          description: "(Документ Word 2007+)"
          
        # format loop 3
        - name: "Парсинг PPTX"
          format: "PPTX"
          link: "/parser/net/extract-image/pptx/"
          description: "(Формат презентации Open XML)"
          
        # format loop 4
        - name: "Парсинг XLSX"
          format: "XLSX"
          link: "/parser/net/extract-image/xlsx/"
          description: "(Рабочая книга Open XML)"
          
        # format loop 5
        - name: "Парсинг ODT"
          format: "ODT"
          link: "/parser/net/extract-image/odt/"
          description: "(Текстовый документ OpenDocument)"
          
        # format loop 6
        - name: "Парсинг ODS"
          format: "ODS"
          link: "/parser/net/extract-image/ods/"
          description: "(Электронная таблица OpenDocument)"
          
        # format loop 7
        - name: "Парсинг ODP"
          format: "ODP"
          link: "/parser/net/extract-image/odp/"
          description: "(Презентация OpenDocument)"
          
        # format loop 8
        - name: "Парсинг EPUB"
          format: "EPUB"
          link: "/parser/net/extract-image/epub/"
          description: "(Файл открытой электронной книги)"
          
        # format loop 9
        - name: "Парсинг FB2"
          format: "FB2"
          link: "/parser/net/extract-image/fb2/"
          description: "(Электронная книга FictionBook)"
         
          

---