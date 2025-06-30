


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:40
draft: false
lang: ru
format: Pptx
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "Извлечение таблиц из файлов PPTX в приложениях C#"
head_description: "Используйте GroupDocs.Parser, чтобы находить и извлекать структурированные данные таблиц из файлов PPTX в приложениях C# без дополнительных зависимостей."

############################# Header ############################
title: "Извлечение таблиц из PPTX с использованием C#" 
description: "Быстро идентифицируйте и извлекайте структуры таблиц из PDF, Word, Excel и других форматов файлов, используя GroupDocs.Parser в ваших проектах .NET."
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Скачать бесплатную версию"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "О API GroupDocs.Parser for .NET"
    link: "/parser/net/"
    link_title: "Узнать больше"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/) — это комплексный API для парсинга документов, разработанный для разработчиков .NET. Он обеспечивает точное извлечение текста, таблиц, изображений, гиперссылок и других структурированных элементов из форматов, таких как PDF, DOCX, XLSX, PPTX и многих других — без необходимости в стороннем программном обеспечении.

############################# Steps ############################
steps:
    enable: true
    title: "Шаги для извлечения таблиц из Pptx в C#"
    content: |
      Следуйте этим инструкциям, чтобы извлечь таблицы из файлов PPTX с использованием [GroupDocs.Parser](/parser/net/) в вашей среде .NET:
      
      1. Инициализируйте экземпляр Parser и загрузите ваш документ PPTX.
      2. Проверьте, поддерживается ли извлечение таблиц для входного формата.
      3. Извлеките содержимое таблицы из файла.
      4. Используйте структурированные данные таблицы для отчетности, автоматизации или аналитики.
   
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
        // Откройте документ, содержащий данные таблицы, с помощью Parser
        using (Parser parser = new Parser("input.pptx")) {

            // Проверьте, поддерживает ли формат распознавание таблиц
            if (!parser.Features.Tables) {
                Console.WriteLine("Обработайте документы, которые не поддерживают парсинг таблиц");
                return;
            }

            // Определите, как должна распознаваться структура таблицы
            TemplateTableLayout layout = new TemplateTableLayout(
                new double[] { 50, 95, 275, 415, 485, 545 },
                new double[] { 325, 340, 365, 395 });

            // Уточните параметры извлечения для данных таблицы
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            //  Извлеките таблицы из содержимого файла
            IEnumerable<PageTableArea> tables = parser.GetTables(options);

            //  Переберите каждую обнаруженную таблицу
            foreach (PageTableArea t in tables)
            {
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "Мощные возможности извлечения данных"
  description: "Помимо парсинга таблиц, GroupDocs.Parser может извлекать содержимое, такое как текстовые блоки, изображения, метаданные и другие структурированные данные для упрощения автоматизации документов."
  image: "/img/parser/features_extract-table.webp" # 500x500 px
  image_description: "Распознавание таблиц и извлечение содержимого"
  features:
    # feature loop
    - title: "Точная многопрофильная детекция таблиц"
      content: "Извлеките табличные данные из форматов DOCX, XLSX, PDF, HTML и аналогичных с высокой точностью."

    # feature loop
    - title: "Парсинг структур таблиц из файлов"
      content: "Эффективно получайте данные таблиц из документов и таблиц без потери форматирования."

    # feature loop
    - title: "Гибкая настройка извлечения таблиц"
      content: "Настройте детекцию макета, выравнивание колонок и параметры заголовков/колонтитулов для точного контроля над выходными данными."
      
  code_samples:
    # code sample loop
    - title: "Как извлечь таблицы из Excel-таблиц"
      content: |
        Этот образец кода демонстрирует, как читать и перебрать данные таблицы в файле XLSX с помощью GroupDocs.Parser.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Откройте файл Excel с помощью API Parser
        using (Parser parser = new Parser("input.xlsx"))
        {
            // Завершите, если таблицы не могут быть извлечены из файла
            if (!parser.Features.Tables)
            {
                return;
            }

            // Используйте правила макета для нахождения табличного содержимого
            TemplateTableLayout layout = new TemplateTableLayout(
                    new double[] { 50, 95, 275, 415, 485, 545 },
                    new double[] { 325, 340, 365, 395 });

            // Настройте параметры извлечения для таблиц
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            // Проведите операцию извлечения таблицы
            IEnumerable<PageTableArea> tables = parser.GetTables(options);

            // Просмотрите каждую обнаруженную структуру таблицы
            foreach (PageTableArea t in tables)
            {
                // Переберите каждую строку в таблице
                for (int row = 0; row < t.RowCount; row++)
                {
                    // Переберите ячейки в каждой строке
                    for (int column = 0; column < t.ColumnCount; column++)
                    {
                        // Получите доступ к текущей ячейке таблицы
                        PageTableAreaCell cell = t[row, column];
                        if (cell != null)
                        {
                            // Выведите текстовое содержимое каждой ячейки
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
    title: "Поддерживаемые форматы для извлечения таблиц"
    exclude: "PPTX"
    description: "GroupDocs.Parser может извлекать данные таблиц из различных типов документов. Ниже приведены наиболее часто используемые форматы для структурированного парсинга таблиц."
    items: 
        # format loop 1
        - name: "Парсинг PDF"
          format: "PDF"
          link: "/parser/net/extract-table/pdf/"
          description: "(Формат переносимого документа)"
          
        # format loop 2
        - name: "Парсинг DOCX"
          format: "DOCX"
          link: "/parser/net/extract-table/docx/"
          description: "(Документ Word 2007+)"
          
        # format loop 3
        - name: "Парсинг PPTX"
          format: "PPTX"
          link: "/parser/net/extract-table/pptx/"
          description: "(Формат презентации Open XML)"
          
        # format loop 4
        - name: "Парсинг XLSX"
          format: "XLSX"
          link: "/parser/net/extract-table/xlsx/"
          description: "(Рабочая книга Open XML)"
          
        # format loop 5
        - name: "Парсинг TXT"
          format: "TXT"
          link: "/parser/net/extract-table/txt/"
          description: "(Текстовый файл)"
          
        # format loop 6
        - name: "Парсинг RTF"
          format: "RTF"
          link: "/parser/net/extract-table/rtf/"
          description: "(Формат Rich Text)"
          
        # format loop 7
        - name: "Парсинг XML"
          format: "XML"
          link: "/parser/net/extract-table/xml/"
          description: "(Расширяемый язык разметки)"
          
        # format loop 8
        - name: "Парсинг EPUB"
          format: "EPUB"
          link: "/parser/net/extract-table/epub/"
          description: "(Файл открытой электронной книги)"
         
          

---