


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:41
draft: false
lang: uk
format: Rtf
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "Витяг таблиць з файлів RTF в застосунках C#"
head_description: "Використовуйте GroupDocs.Parser для знаходження та витягнення структурованих даних таблиць з файлів RTF в застосунках C# без додаткових залежностей."

############################# Header ############################
title: "Витяг таблиць з RTF за допомогою C#" 
description: "Швидко визначайте та витягуйте структури таблиць з PDF, Word, Excel та інших форматів файлів, використовуючи GroupDocs.Parser у ваших проектах .NET."
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Завантажити безкоштовну версію"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "Про API GroupDocs.Parser for .NET"
    link: "/parser/net/"
    link_title: "Дізнатися більше"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/) — це універсальний API для парсингу документів, створений для розробників .NET. Він дозволяє точно витягувати текст, таблиці, зображення, гіперпосилання та інші структуровані елементи з форматів, таких як PDF, DOCX, XLSX, PPTX та багатьох інших — без необхідності у сторонньому програмному забезпеченні.

############################# Steps ############################
steps:
    enable: true
    title: "Кроки для витягнення таблиць з Rtf в C#"
    content: |
      Дотримуйтесь цих інструкцій, щоб витягти таблиці з файлів RTF за допомогою [GroupDocs.Parser](/parser/net/) у вашому середовищі .NET:
      
      1. Ініціалізуйте екземпляр Parser та завантажте ваш документ RTF.
      2. Перевірте, чи підтримується витягнення таблиць для вхідного формату.
      3. Витягніть вміст таблиці з файлу.
      4. Використовуйте структуровані дані таблиці для звітування, автоматизації або аналітики.
   
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
        // Відкрийте документ, що містить дані таблиці, використовуючи Parser
        using (Parser parser = new Parser("input.rtf")) {

            // Перевірте, чи підтримує формат розпізнавання таблиць
            if (!parser.Features.Tables) {
                Console.WriteLine("Обробляйте документи, що не підтримують парсинг таблиць");
                return;
            }

            // Визначте, як слід розпізнавати структуру таблиці
            TemplateTableLayout layout = new TemplateTableLayout(
                new double[] { 50, 95, 275, 415, 485, 545 },
                new double[] { 325, 340, 365, 395 });

            // Вкажіть параметри витягнення для даних таблиці
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            //  Витягніть таблиці з вмісту файлу
            IEnumerable<PageTableArea> tables = parser.GetTables(options);

            //  Перебирайте кожну виявлену таблицю
            foreach (PageTableArea t in tables)
            {
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "Потужні можливості витягнення даних"
  description: "Крім парсингу таблиць, GroupDocs.Parser може витягувати багатий контент, такий як текстові блоки, зображення, метадані та інші структуровані дані для автоматизації документів."
  image: "/img/parser/features_extract-table.webp" # 500x500 px
  image_description: "Розпізнавання таблиць і витягнення вмісту"
  features:
    # feature loop
    - title: "Точне виявлення таблиць у кількох форматах"
      content: "Витягуйте табличні дані з DOCX, XLSX, PDF, HTML та аналогічних форматів з високою точністю."

    # feature loop
    - title: "Парсинг структур таблиць з файлів"
      content: "Ефективно отримуйте дані таблиць з документів та електронних таблиць без втрати форматування."

    # feature loop
    - title: "Гнучка конфігурація витягнення таблиць"
      content: "Налаштовуйте виявлення макета, вирівнювання стовпців та параметри заголовка/підзаголовка для точного контролю за вихідними даними."
      
  code_samples:
    # code sample loop
    - title: "Як витягнути таблиці з Excel електронних таблиць"
      content: |
        Цей кодовий приклад демонструє, як читати та перебирати дані таблиці в файлі XLSX за допомогою GroupDocs.Parser.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Відкрийте файл Excel за допомогою API Parser
        using (Parser parser = new Parser("input.xlsx"))
        {
            // Вийдіть, якщо таблиці не можуть бути витягнені з файлу
            if (!parser.Features.Tables)
            {
                return;
            }

            // Використовуйте правила макета для знаходження табличного контенту
            TemplateTableLayout layout = new TemplateTableLayout(
                    new double[] { 50, 95, 275, 415, 485, 545 },
                    new double[] { 325, 340, 365, 395 });

            // Налаштуйте параметри витягнення для таблиць
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            // Виконайте операцію витягнення таблиці
            IEnumerable<PageTableArea> tables = parser.GetTables(options);

            // Перегляньте кожну виявлену структуру таблиці
            foreach (PageTableArea t in tables)
            {
                // Перебирання кожного рядка в таблиці
                for (int row = 0; row < t.RowCount; row++)
                {
                    // Цикл по клітинам в кожному рядку
                    for (int column = 0; column < t.ColumnCount; column++)
                    {
                        // Отримайте доступ до клітини поточної таблиці
                        PageTableAreaCell cell = t[row, column];
                        if (cell != null)
                        {
                            // Відобразіть текстовий вміст кожної клітини
                            Console.Write(cell.Text);
                            Console.Write(" | ");
                        }
                    }
                }
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
    title: "Підтримувані формати для витягнення таблиць"
    exclude: "RTF"
    description: "GroupDocs.Parser може витягувати дані таблиць з різних типів документів. Нижче наведено найбільш поширені формати для структурованого парсингу таблиць."
    items: 
        # format loop 1
        - name: "Парсинг PDF"
          format: "PDF"
          link: "/parser/net/extract-table/pdf/"
          description: "(Формат портативного документа)"
          
        # format loop 2
        - name: "Парсинг DOCX"
          format: "DOCX"
          link: "/parser/net/extract-table/docx/"
          description: "(Документ Word Office 2007+)"
          
        # format loop 3
        - name: "Парсинг PPTX"
          format: "PPTX"
          link: "/parser/net/extract-table/pptx/"
          description: "(Формат відкритої XML-презентації)"
          
        # format loop 4
        - name: "Парсинг XLSX"
          format: "XLSX"
          link: "/parser/net/extract-table/xlsx/"
          description: "(Відкрите XML-робочий зошит)"
          
        # format loop 5
        - name: "Парсинг TXT"
          format: "TXT"
          link: "/parser/net/extract-table/txt/"
          description: "(Текстовий файл)"
          
        # format loop 6
        - name: "Парсинг RTF"
          format: "RTF"
          link: "/parser/net/extract-table/rtf/"
          description: "(Формат багатого тексту)"
          
        # format loop 7
        - name: "Парсинг XML"
          format: "XML"
          link: "/parser/net/extract-table/xml/"
          description: "(Мова розмітки eXtensible)"
          
        # format loop 8
        - name: "Парсинг EPUB"
          format: "EPUB"
          link: "/parser/net/extract-table/epub/"
          description: "(Відкритий файл eBook)"
         
          

---