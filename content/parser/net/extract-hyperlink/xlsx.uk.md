


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:26
draft: false
lang: uk
format: Xlsx
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "Витягання гіперпосилань з файлів XLSX у додатках C#"
head_description: "Використовуйте GroupDocs.Parser для виявлення та витягання гіперпосилань з файлів XLSX у C# без додаткових інструментів чи програмного забезпечення."

############################# Header ############################
title: "Витягання гіперпосилань з XLSX за допомогою C#" 
description: "Виявляйте та витягайте URL-адреси та гіперпосилання з PDF, Word, Excel та інших типів документів, використовуючи GroupDocs.Parser у ваших додатках .NET."
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
       [GroupDocs.Parser](/parser/net/) — універсальний API для парсингу документів для розробників .NET. Він підтримує витягання гіперпосилань, тексту, зображень та структурованого контенту з різних форматів файлів, таких як PDF, Word, Excel, HTML та багато інших — без reliance на стороннє програмне забезпечення.

############################# Steps ############################
steps:
    enable: true
    title: "Кроки для витягання гіперпосилань з Xlsx в C#"
    content: |
      [GroupDocs.Parser](/parser/net/) дозволяє розробникам .NET витягувати гіперпосилання з файлів XLSX, дотримуючись цих простих кроків:
      
      1. Завантажте файл XLSX за допомогою екземпляра Parser.
      2. Перевірте, чи документ підтримує витягання гіперпосилань.
      3. Отримайте список гіперпосилань з документа.
      4. Обробіть результати та працюйте з витягнутими URL-адресами.
   
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
        // Завантажте документ, що містить гіперпосилання, за допомогою класу Parser
        using (Parser parser = new Parser("input.xlsx")) {

            // Перевірте, чи підтримує файл витягання гіперпосилань
            if (!parser.Features.Hyperlinks)
            {
                Console.WriteLine("Витягання гіперпосилань недоступне для файлу");
                return;
            }

            // Отримайте та обробіть витягнуті гіперпосилання
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
  title: "Розширені можливості парсингу документів"
  description: "Окрім витягання гіперпосилань, GroupDocs.Parser також дозволяє витягувати текст, метадані, зображення та структуровані дані — підтримуючи потужні робочі процеси обробки даних."
  image: "/img/parser/features_extract-hyperlink.webp" # 500x500 px
  image_description: "Виявлення гіперпосилань і парсинг документів"
  features:
    # feature loop
    - title: "Виявлення гіперпосилань з документів"
      content: "Швидко витягуйте URL-адреси та анотації посилань з документів, таких як PDF, файли Word, електронні таблиці та інші."

    # feature loop
    - title: "Підтримка веб і вбудованих посилань"
      content: "Виявляйте та витягуйте як стандартні веб URL, так і вбудовані посилання з документів у різних форматах."

    # feature loop
    - title: "Гнучкі параметри парсингу"
      content: "Налаштуйте параметри витягання для сканування конкретних секцій або сторінок для підвищення продуктивності та точності."
      
  code_samples:
    # code sample loop
    - title: "Як витягнути гіперпосилання з PDF, використовуючи параметри посилань"
      content: |
        Цей приклад коду показує, як витягувати всі гіперпосилання з PDF файлу, використовуючи користувацькі параметри.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Ініціалізуйте Parser з документом PDF
        using (Parser parser = new Parser("input.docx"))
        {
            // Перевірте, чи підтримується витягання гіперпосилань
            if (!parser.Features.Hyperlinks)
            {
                return;
            }

            // Встановіть параметри витягання посилань для звуження результатів
            PageAreaOptions options = new PageAreaOptions(new Rectangle(new Point(380, 90), new Size(150, 50)));

            // Витягніть дані гіперпосилань з документа
            IEnumerable<PageHyperlinkArea> hyperlinks = parser.GetHyperlinks(options);

            // Обробіть список витягнутих посилань
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
    title: "Підтримувані формати для витягання гіперпосилань"
    exclude: "XLSX"
    description: "GroupDocs.Parser може витягувати гіперпосилання з широкого спектра типів документів. Дивіться нижче список найпоширеніших форматов."
    items: 
        # format loop 1
        - name: "Парсинг PDF"
          format: "PDF"
          link: "/parser/net/extract-hyperlink/pdf/"
          description: "(Формат портативного документа)"
          
        # format loop 2
        - name: "Парсинг DOCX"
          format: "DOCX"
          link: "/parser/net/extract-hyperlink/docx/"
          description: "(Документ Word Office 2007+)"
          
        # format loop 3
        - name: "Парсинг PPTX"
          format: "PPTX"
          link: "/parser/net/extract-hyperlink/pptx/"
          description: "(Формат відкритої XML-презентації)"
          
        # format loop 4
        - name: "Парсинг XLSX"
          format: "XLSX"
          link: "/parser/net/extract-hyperlink/xlsx/"
          description: "(Відкрите XML-робочий зошит)"
          
        # format loop 5
        - name: "Парсинг TXT"
          format: "TXT"
          link: "/parser/net/extract-hyperlink/txt/"
          description: "(Текстовий файл)"
          
        # format loop 6
        - name: "Парсинг RTF"
          format: "RTF"
          link: "/parser/net/extract-hyperlink/rtf/"
          description: "(Формат багатого тексту)"
          
        # format loop 7
        - name: "Парсинг XML"
          format: "XML"
          link: "/parser/net/extract-hyperlink/xml/"
          description: "(Мова розмітки eXtensible)"
          
        # format loop 8
        - name: "Парсинг EPUB"
          format: "EPUB"
          link: "/parser/net/extract-hyperlink/epub/"
          description: "(Відкритий файл eBook)"
         
          

---