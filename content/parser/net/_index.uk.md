---
############################# Static ############################
layout: "landing"
date: 2025-12-09T14:10:41
draft: false

lang: uk
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
head_description: "Високопродуктивний Document Parser SDK для .NET. Витягайте текст, зображення, метадані, штрих‑коди, таблиці та інші дані з PDF, Word, Excel, електронних листів і понад 50 форматів документів."

############################# Header ############################
title: "Document Parser SDK для .NET"
description: "Додайте швидке та точне розпарсування документів у ваші застосунки .NET і витягайте текст, зображення, метадані та структуровані дані з документів і зображень."
words:
  for: "для"

actions:
  main: "Nuget Завантажити"
  main_link: "https://www.nuget.org/packages/GroupDocs.Parser"
  alt: "Ліцензування"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/net/"
  title: "Готові розпочати?"
  description: "Спробуйте функції GroupDocs.Parser безкоштовно або запитайте ліцензію"

release:
  title: "Випущено версію {0}"
  notes: "Перегляньте, що нового"
  downloads: "Завантаження"

code:
  title: "Швидко розпарсити вміст документу за допомогою SDK"
  more: "Більше прикладів"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
  install: "dotnet add package GroupDocs.Parser"
  content: |
    ```csharp {style=abap}   
    // Передайте вихідний файл до екземпляра Parser
    using (var parser = new Parser("source.pdf"))
    {
        // Передайте текст документа до TextReader
        using (var textReader = parser.GetText())
        {
            // Обробіть текст документа
            Console.WriteLine(textReader?.ReadToEnd());
        }
    }  
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser на перший погляд"
  description: "Document Parser SDK для виконання високоточного розпарсування документів у застосунках .NET"
  features:
    # feature loop
    - title: "Витяг даних з документів"
      content: "GroupDocs.Parser for .NET API дозволяє отримувати текст, метадані та зображення з широкого спектра форматів файлів, таких як офісні документи, електронні листи, вкладення та архіви. Цей потужний інструмент допомагає ефективно отримувати та обробляти цінну інформацію, що міститься у цих файлах, для різноманітних застосувань, таких як аналіз даних, індексування пошукових систем або системи управління контентом."

    # feature loop
    - title: "Розпарсування документів"
      content: "Витягайте різноманітні елементи, такі як гіперпосилання, таблиці, QR‑коди, штрих‑коди та дані з PDF‑форм. Також розпарсуйте будь‑яку потрібну інформацію з документів, використовуючи власні шаблони."

    # feature loop
    - title: "Налаштування результатів"
      content: ".NET API дозволяє отримувати дані у різних форматах, таких як сирий, структурований, HTML або Markdown. Крім того, API пропонує функціональність пошуку для знаходження конкретних слів чи виразів у тексті документів."

############################# Platforms ############################
platforms:
  enable: true
  title: "Платформна незалежність"
  description: "GroupDocs.Parser for .NET підтримує наступні операційні системи, фреймворки та менеджери пакетів"
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
  title: "Підтримувані формати файлів"
  description: |
    GroupDocs.Parser for .NET підтримує роботу з наступними [форматами файлів](https://docs.groupdocs.com/parser/net/supported-document-formats/).
  groups:
    # group loop
    - color: "green"
      content: |
        ### Формати Microsoft Office
        * **Word:** DOCX, DOC, DOCM, DOT, DOTX, DOTM, RTF
        * **Excel:** XLSX, XLS, XLSM, XLSB, XLTM, XLT, XLTM, XLTX, XLAM, SXC, SpreadsheetML
        * **PowerPoint:** PPT, PPTX, PPS, PPSX, PPSM, POT, POTM, POTX, PPTM
    # group loop
    - color: "blue"
      content: |
        ### Зображення та інші формати
        * **Портативний:** PDF 
        * **Зображення:** JPG, BMP, PNG, TIFF, GIF
        * **Інші офісні формати:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### Інші формати
        * **Веб:** HTML, MHTML 
        * **Архіви:** ZIP, TAR, 7Z 
        * **Електронні книги:** CHM, EPUB, FB2, MOBI 
        
        

############################# Features ############################
features:
  enable: true
  title: "Функції GroupDocs.Parser for .NET"
  description: "Витягайте дані з PDF, офісних документів, зображень та інших форматів швидко та точно за допомогою нашого .NET Document Parser SDK"

  items:
    # feature loop
    - icon: "text"
      title: "Витяг тексту"
      content: "Витягайте текстову інформацію з різних форматів файлів, таких як офісні документи, PDF‑файли та зображення, для легкої читабельності та аналізу."

    # feature loop
    - icon: "image"
      title: "Витяг зображень"
      content: "Отримуйте візуальний контент з різноманітних джерел, таких як офісні документи, PDF‑файли, для зручного доступу та використання."

    # feature loop
    - icon: "qr"
      title: "Сканувати QR‑коди"
      content: "Виявляйте та розшифровуйте QR‑коди, що містяться в офісних документах, PDF‑файлах або візуальному контенті, для ефективного отримання інформації."

    # feature loop
    - icon: "email"
      title: "Витяг даних з вкладень електронної пошти та архівів"
      content: "Збирайте цінну інформацію з електронних листів, вкладень файлів та стиснених джерел даних для ефективного аналізу та використання."

    # feature loop
    - icon: "table"
      title: "Витягнути таблиці"
      content: "Визначайте та витягайте табличні дані з PDF‑документів для упорядкованого аналізу та використання."

    # feature loop
    - icon: "hyperlink"
      title: "Витягнути гіперпосилання"
      content: "Знаходьте та витягайте гіперпосилання та електронні адреси в офісних документах або PDF‑файлах для ефективного доступу."

    # feature loop
    - icon: "pdf"
      title: "Обробляти PDF‑форми"
      content: "PDF‑форми — це цифрові документи з полями, які можна заповнювати, для взаємодії користувачів, що дозволяє їм вводити інформацію електронно. .NET API можна використати для витягування даних із цих форм з метою ефективної обробки."

    # feature loop
    - icon: "template"
      title: "Обробляти дані за шаблонами"
      content: "Створюйте власні шаблони та використовуйте їх за допомогою .NET API для розбору конкретної інформації з PDF‑файлів, спрощуючи процеси витягування даних."

    # feature loop
    - icon: "search"
      title: "Шукати текст у документах"
      content: "Швидко знаходьте конкретні слова або шаблони в документах."


############################# Code samples ############################
code_samples:
  enable: true
  title: "Зразки коду"
  description: "Декілька прикладів використання типових операцій GroupDocs.Parser for .NET"
  items:
    # code sample loop
    - title: "Витягнути зображення з PDF‑документів"
      content: |
        GroupDocs.Parser for .NET спрощує C# розробникам витягування зображень з [документів](https://docs.groupdocs.com/parser/net/extract-images-from-documents/):
        {{< landing/code title="Витягнути зображення з PDF‑документів у C#">}}
        ```csharp {style=abap}
        // Створіть екземпляр класу Parser
        using (var parser = new Parser("source.pptx"))
        {
            // Витягніть зображення
            var images = parser.GetImages();

            // Перевірте, чи щось витягнуто
            if (images == null)
            {
                return;
            }
            // Переберіть зображення
            foreach (PageImageArea image in images)
            {
                // Виведіть індекс сторінки, прямокутник і тип зображення
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Type: {2}", 
                    image.Page.Index, image.Rectangle, image.FileType));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Витягнути штрихкоди з зображень"
      content: |
        Використайте наш API .NET для витягування [штрихкодів](https://docs.groupdocs.com/parser/net/extract-barcodes-from-document/) з зображень:
        {{< landing/code title="Витягнути штрихкоди з зображень у C#">}}
        ```csharp {style=abap}   
        // Завантажте вихідне зображення у Parser
        using (var parser = new Parser("source.jpg"))
        {
            // Перевірте, чи файл підтримує витягування штрихкодів
            if (parser.Features.Barcodes)
            {
                // Витягніть штрихкоди з файлу
                var barcodes = parser.GetBarcodes();

                // Переберіть штрихкоди
                foreach (var barcode in barcodes)
                {
                    // Виведіть індекс сторінки
                    Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                    // Виведіть значення штрихкоду
                    Console.WriteLine("Value: " + barcode.Value);
                }
            }
        }
        ```
        {{< /landing/code >}}

---
