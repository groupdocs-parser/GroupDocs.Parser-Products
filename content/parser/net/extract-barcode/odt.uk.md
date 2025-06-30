


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:20
draft: false
lang: uk
format: Odt
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "Витягуйте штрих-коди з файлів ODT в програмах C#"
head_description: "Скористайтеся GroupDocs.Parser, щоб виявити та витягти дані штрих-кодів з файлів ODT в C# без додаткового програмного забезпечення."

############################# Header ############################
title: "Витягуйте штрих-коди з ODT за допомогою C#" 
description: "Виявляйте та витягайте інформацію про штрих-коди з PDF, Word, Excel та графічних файлів за допомогою GroupDocs.Parser у ваших .NET програмах."
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Завантажте безкоштовну версію"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "Про API GroupDocs.Parser for .NET"
    link: "/parser/net/"
    link_title: "Дізнатися більше"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/) — це потужний API для розбору документів для розробників .NET. Він дозволяє витягувати текст, зображення, структурований контент і штрих-коди з різних форматових файлів, включаючи PDF, Word, Excel, PowerPoint та інші — все це без залежності від зовнішніх інструментів.

############################# Steps ############################
steps:
    enable: true
    title: "Кроки для витягування штрих-кодів з Odt в C#"
    content: |
      [GroupDocs.Parser](/parser/net/) дозволяє витягувати дані штрих-кодів з файлів ODT в програмах .NET, слідуючи цим простим крокам:
      
      1. Завантажте файл ODT за допомогою екземпляра Parser.
      2. Перевірте, чи документ підтримує витягування штрих-кодів.
      3. Отримайте список штрих-кодів з документа.
      4. Ітерація через результати та використання витягнутих значень штрих-кодів.
   
    code:
      platform: "net"
      copy_title: "Копіювати"
      install:
        command: |
        command: "dotnet add package GroupDocs.Parser"
        copy_tip: "натисніть, щоб скопіювати"
        copy_done: "скопійовано"
      links:
        #  loop
        - title: "Більше прикладів"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
        #  loop
        - title: "Документація"
          link: "https://docs.groupdocs.com/parser/net/"
          
      content: |
        ```csharp {style=abap}
        // Завантажте документ, що містить штрих-коди, за допомогою класу Parser
        using (Parser parser = new Parser("input.odt")) {

            // Перевірте, чи підтримує файл витягування штрих-кодів
            if (!parser.Features.Barcodes) {
                Console.WriteLine("Витягування штрих-кодів не підтримується");
                return;
            }

            // Отримайте та обробіть витягнуті штрих-коди
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
  title: "Розширені можливості розбору документів"
  description: "Окрім витягування штрих-кодів, GroupDocs.Parser дозволяє витягувати простий текст, зображення та структуровані дані для підтримки розширеної автоматизації та обробки даних."
  image: "/img/parser/features_extract-barcode.webp" # 500x500 px
  image_description: "Визнання штрих-кодів та розбір документів"
  features:
    # feature loop
    - title: "Підтримка кількох форматів штрих-кодів"
      content: "Визначайте загальні типи штрих-кодів, включаючи QR-код, Code 128, Data Matrix, EAN, Aztec та інші."

    # feature loop
    - title: "Витягування штрих-кодів з документів і зображень"
      content: "Читання штрих-кодів з PDF, Word, Excel документів і графічних форматів, таких як JPEG, PNG та BMP."

    # feature loop
    - title: "Налаштовувані параметри витягування"
      content: "Конфігуруйте параметри виявлення, такі як області сканування та обробка багатосторінкових документів."
      
  code_samples:
    # code sample loop
    - title: "Як витягувати штрих-коди з PDF, використовуючи параметри штрих-коду"
      content: |
        Цей приклад демонструє, як витягувати штрих-коди з PDF файлу, використовуючи специфічні опції витягування штрих-кодів.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Завантажте PDF файл з класом Parser
        using (Parser parser = new Parser("input.pdf"))
        {
            // Підтвердіть, що підтримується витягування штрих-кодів
            if (!parser.Features.Barcodes)
            {
                return;
            }

            // Використовуйте параметри штрих-коду для фільтрації результатів
            BarcodeOptions options = new BarcodeOptions(QualityMode.Low, QualityMode.Low, "QR");

            // Отримайте дані штрих-кодів з документа
            IEnumerable<PageBarcodeArea> barcodes = parser.GetBarcodes(options);

            // Обробіть список отриманих штрих-кодів
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
  title: "Готові розпочати?"
  description: "Спробуйте можливості GroupDocs.Parser безкоштовно або запитайте ліцензію"
  items:
    #  loop
    - title: "Завантаження Nuget"
      link: "https://releases.groupdocs.com/parser/net/"
      color: "red"
        #  loop
    - title: "Ліцензування"
      link: "https://purchase.groupdocs.com/pricing/parser/net/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "Підтримувані формати для витягування штрих-кодів"
    exclude: "ODT"
    description: "GroupDocs.Parser підтримує виявлення штрих-кодів у широкому діапазоні документів і графічних форматів. Нижче наведені поширено підтримувані типи файлів."
    items: 
        # format loop 1
        - name: "Парсинг PDF"
          format: "PDF"
          link: "/parser/net/extract-barcode/pdf/"
          description: "(Формат портативного документа)"
          
        # format loop 2
        - name: "Парсинг DOCX"
          format: "DOCX"
          link: "/parser/net/extract-barcode/docx/"
          description: "(Документ Word Office 2007+)"
          
        # format loop 3
        - name: "Парсинг PPTX"
          format: "PPTX"
          link: "/parser/net/extract-barcode/pptx/"
          description: "(Формат відкритої XML-презентації)"
          
        # format loop 4
        - name: "Парсинг XLSX"
          format: "XLSX"
          link: "/parser/net/extract-barcode/xlsx/"
          description: "(Відкрите XML-робочий зошит)"
          
        # format loop 5
        - name: "Парсинг ODT"
          format: "ODT"
          link: "/parser/net/extract-barcode/odt/"
          description: "(Документ тексту OpenDocument)"
          
        # format loop 6
        - name: "Парсинг ODS"
          format: "ODS"
          link: "/parser/net/extract-barcode/ods/"
          description: "(Електронна таблиця OpenDocument)"
          
        # format loop 7
        - name: "Парсинг ODP"
          format: "ODP"
          link: "/parser/net/extract-barcode/odp/"
          description: "(Презентація OpenDocument)"
          
        # format loop 8
        - name: "Парсинг EPUB"
          format: "EPUB"
          link: "/parser/net/extract-barcode/epub/"
          description: "(Відкритий файл eBook)"
          
        # format loop 9
        - name: "Парсинг FB2"
          format: "FB2"
          link: "/parser/net/extract-barcode/fb2/"
          description: "(eBook формату FictionBook)"
         
          

---