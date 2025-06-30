


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:20
draft: false
lang: ru
format: Epub
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "Извлечение штрих-кодов из файлов EPUB в приложениях C#"
head_description: "Используйте GroupDocs.Parser для обнаружения и извлечения данных штрих-кодов из файлов EPUB в C# без использования дополнительного ПО."

############################# Header ############################
title: "Извлечение штрих-кодов из EPUB с использованием C#" 
description: "Определяйте и извлекайте информацию о штрих-кодах из файлов PDF, Word, Excel и изображений с помощью GroupDocs.Parser в ваших приложениях .NET."
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
       [GroupDocs.Parser](/parser/net/) — мощный API для парсинга документов для разработчиков .NET. Он позволяет извлекать текст, изображения, структурированные данные и штрих-коды из различных форматов файлов, включая PDF, Word, Excel, PowerPoint и другие, без зависимости от внешних инструментов.

############################# Steps ############################
steps:
    enable: true
    title: "Шаги для извлечения штрих-кодов из Epub в C#"
    content: |
      [GroupDocs.Parser](/parser/net/) позволяет извлекать данные штрих-кодов из файлов EPUB в приложениях .NET, следуя этим простым шагам:
      
      1. Загрузите файл EPUB с использованием экземпляра Parser.
      2. Убедитесь, что документ поддерживает извлечение штрих-кодов.
      3. Получите список штрих-кодов из документа.
      4. Итерация по результатам и использование извлеченных значений штрих-кодов.
   
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
        // Загрузите документ, содержащий штрих-коды, с помощью класса Parser
        using (Parser parser = new Parser("input.epub")) {

            // Убедитесь, что файл поддерживает извлечение штрих-кодов
            if (!parser.Features.Barcodes) {
                Console.WriteLine("Извлечение штрих-кодов не поддерживается");
                return;
            }

            // Получите и обработайте извлеченные штрих-коды
            IEnumerable<PageBarcodeArea> barcodes = parser.GetBarcodes();

            foreach (PageBarcodeArea barcode in barcodes) {
                Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                Console.WriteLine("Value: " + barcode.Value);
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "Расширенные функции парсинга документов"
  description: "Помимо извлечения штрих-кодов, GroupDocs.Parser позволяет извлекать обычный текст, изображения и структурированные данные для поддержки сложной автоматизации и рабочих процессов обработки данных."
  image: "/img/parser/features_extract-barcode.webp" # 500x500 px
  image_description: "Распознавание штрих-кодов и парсинг документов"
  features:
    # feature loop
    - title: "Поддержка множества форматов штрих-кодов"
      content: "Распознавайте распространенные типы штрих-кодов, включая QR-код, Code 128, Data Matrix, EAN, Aztec и другие."

    # feature loop
    - title: "Извлечение штрих-кодов из документов и изображений"
      content: "Чтение штрих-кодов из документов PDF, Word, Excel и изображений форматов JPEG, PNG и BMP."

    # feature loop
    - title: "Настраиваемые параметры извлечения"
      content: "Настройте параметры обнаружения, такие как области сканирования и обработка многостраничных документов."
      
  code_samples:
    # code sample loop
    - title: "Как извлечь штрих-коды из PDF с использованием параметров штрих-кодов"
      content: |
        Этот пример демонстрирует, как извлечь штрих-коды из PDF-файла с использованием определенных параметров извлечения штрих-кодов.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Загрузите PDF-файл с классом Parser
        using (Parser parser = new Parser("input.pdf"))
        {
            // Подтвердите поддержку извлечения штрих-кодов
            if (!parser.Features.Barcodes)
            {
                return;
            }

            // Используйте параметры штрих-кодов для фильтрации результатов
            BarcodeOptions options = new BarcodeOptions(QualityMode.Low, QualityMode.Low, "QR");

            // Получите данные штрих-кодов из документа
            IEnumerable<PageBarcodeArea> barcodes = parser.GetBarcodes(options);

            // Обработайте список извлеченных штрих-кодов
            foreach (PageBarcodeArea barcode in barcodes)
            {
                Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                Console.WriteLine("Value: " + barcode.Value);
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
    title: "Поддерживаемые форматы для извлечения штрих-кодов"
    exclude: "EPUB"
    description: "GroupDocs.Parser поддерживает обнаружение штрих-кодов в широком диапазоне форматов документов и изображений. См. ниже список наиболее часто поддерживаемых типов файлов."
    items: 
        # format loop 1
        - name: "Парсинг PDF"
          format: "PDF"
          link: "/parser/net/extract-barcode/pdf/"
          description: "(Формат переносимого документа)"
          
        # format loop 2
        - name: "Парсинг DOCX"
          format: "DOCX"
          link: "/parser/net/extract-barcode/docx/"
          description: "(Документ Word 2007+)"
          
        # format loop 3
        - name: "Парсинг PPTX"
          format: "PPTX"
          link: "/parser/net/extract-barcode/pptx/"
          description: "(Формат презентации Open XML)"
          
        # format loop 4
        - name: "Парсинг XLSX"
          format: "XLSX"
          link: "/parser/net/extract-barcode/xlsx/"
          description: "(Рабочая книга Open XML)"
          
        # format loop 5
        - name: "Парсинг ODT"
          format: "ODT"
          link: "/parser/net/extract-barcode/odt/"
          description: "(Текстовый документ OpenDocument)"
          
        # format loop 6
        - name: "Парсинг ODS"
          format: "ODS"
          link: "/parser/net/extract-barcode/ods/"
          description: "(Электронная таблица OpenDocument)"
          
        # format loop 7
        - name: "Парсинг ODP"
          format: "ODP"
          link: "/parser/net/extract-barcode/odp/"
          description: "(Презентация OpenDocument)"
          
        # format loop 8
        - name: "Парсинг EPUB"
          format: "EPUB"
          link: "/parser/net/extract-barcode/epub/"
          description: "(Файл открытой электронной книги)"
          
        # format loop 9
        - name: "Парсинг FB2"
          format: "FB2"
          link: "/parser/net/extract-barcode/fb2/"
          description: "(Электронная книга FictionBook)"
         
          

---