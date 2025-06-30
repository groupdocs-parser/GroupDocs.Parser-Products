


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:34
draft: false
lang: uk
format: Pptx
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "Витягнення зображень з файлів PPTX у додатках C#"
head_description: "Використовуйте GroupDocs.Parser для виявлення та витягування зображень з файлів PPTX у C# без додаткових інструментів."

############################# Header ############################
title: "Витягнення зображень з PPTX за допомогою C#" 
description: "Локалізуйте і витягуйте вбудовані зображення з PDF, документів Word, таблиць Excel та інших типів файлів за допомогою GroupDocs.Parser у ваших додатках .NET."
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Скачати безкоштовну версію"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "Про API GroupDocs.Parser for .NET"
    link: "/parser/net/"
    link_title: "Дізнатися більше"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/) — це потужна бібліотека для парсингу документів для розробників .NET. Вона дозволяє витягувати зображення, текст, гіперпосилання та структуровані дані з популярних форматів файлів, таких як PDF, DOCX, XLSX, PPTX та інших — все без потреби в сторонніх додатках.

############################# Steps ############################
steps:
    enable: true
    title: "Кроки для витягнення зображень з Pptx у C#"
    content: |
      З [GroupDocs.Parser](/parser/net/), ви можете витягувати зображення з документів PPTX у своїх проектах .NET всього за кілька кроків:
      
      1. Ініціалізуйте Parser з файлом PPTX.
      2. Отримайте елементи зображень з документа.
      3. Використовуйте витягнуті зображення за потребою у вашому робочому процесі.
   
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
        // Відкрийте документ, що містить зображення, за допомогою Parser
        using (Parser parser = new Parser("input.pptx")) {

            // Витягніть всі вбудовані зображення з файлу
            IEnumerable<PageImageArea> images = parser.GetImages();

            // Обробіть випадки, коли зображення не знайдено
            if (images == null)
            {
                return;
            }

            // Обробіть або збережіть отримані зображення
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
  title: "Комплексне витягнення вмісту документів"
  description: "GroupDocs.Parser пропонує більше, ніж просто витягнення зображень — ви також можете витягувати сирий текст, гіперпосилання, метадані та структурований вміст для складніших сценаріїв автоматизації."
  image: "/img/parser/features_extract-image.webp" # 500x500 px
  image_description: "Процес витягнення зображень та парсингу документів"
  features:
    # feature loop
    - title: "Витягнення зображень з кількох форматів"
      content: "Витягніть вбудовані зображення з різноманітних форматів файлів, включаючи DOCX, PDF, PPTX, XLSX та графічні файли, такі як PNG, JPG та TIFF."

    # feature loop
    - title: "Збереження оригінальної якості зображення"
      content: "Зображення витягуються з високою точністю, зберігаючи свою оригінальну роздільну здатність, формат та колірний профіль."

    # feature loop
    - title: "Розширені параметри витягнення"
      content: "Налаштуйте витягнення зображень з фільтрацією за сторінкою, форматом або роздільною здатністю, з підтримкою багатосторінкових документів."
      
  code_samples:
    # code sample loop
    - title: "Як витягнути та зберегти зображення з PDF-документа"
      content: |
        Цей приклад демонструє, як витягнути всі активи зображення з PDF-файлу та зберегти їх у локальній файловій системі.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Завантажте PDF за допомогою класу Parser
        using (Parser parser = new Parser("input.pdf"))
        {
            // Витягніть вбудовані зображення з файлу
            IEnumerable<PageImageArea> images = parser.GetImages();

            // Встановіть формат виходу та параметри зображення (наприклад, PNG)
            ImageOptions options = new ImageOptions(ImageFormat.Png);

            // Запишіть витягнуті зображення на диск
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
    title: "Підтримувані формати для витягнення зображень"
    exclude: "PPTX"
    description: "GroupDocs.Parser забезпечує точне витягнення зображень з широкого спектра документів та графічних форматів. Перегляньте список нижче для загально підтримуваних типів."
    items: 
        # format loop 1
        - name: "Парсинг PDF"
          format: "PDF"
          link: "/parser/net/extract-image/pdf/"
          description: "(Формат портативного документа)"
          
        # format loop 2
        - name: "Парсинг DOCX"
          format: "DOCX"
          link: "/parser/net/extract-image/docx/"
          description: "(Документ Word Office 2007+)"
          
        # format loop 3
        - name: "Парсинг PPTX"
          format: "PPTX"
          link: "/parser/net/extract-image/pptx/"
          description: "(Формат відкритої XML-презентації)"
          
        # format loop 4
        - name: "Парсинг XLSX"
          format: "XLSX"
          link: "/parser/net/extract-image/xlsx/"
          description: "(Відкрите XML-робочий зошит)"
          
        # format loop 5
        - name: "Парсинг ODT"
          format: "ODT"
          link: "/parser/net/extract-image/odt/"
          description: "(Документ тексту OpenDocument)"
          
        # format loop 6
        - name: "Парсинг ODS"
          format: "ODS"
          link: "/parser/net/extract-image/ods/"
          description: "(Електронна таблиця OpenDocument)"
          
        # format loop 7
        - name: "Парсинг ODP"
          format: "ODP"
          link: "/parser/net/extract-image/odp/"
          description: "(Презентація OpenDocument)"
          
        # format loop 8
        - name: "Парсинг EPUB"
          format: "EPUB"
          link: "/parser/net/extract-image/epub/"
          description: "(Відкритий файл eBook)"
          
        # format loop 9
        - name: "Парсинг FB2"
          format: "FB2"
          link: "/parser/net/extract-image/fb2/"
          description: "(eBook формату FictionBook)"
         
          

---