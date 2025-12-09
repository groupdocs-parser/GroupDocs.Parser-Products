---
############################# Static ############################
layout: "landing"
date: 2025-12-09T14:10:41
draft: false

lang: uk
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

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
head_title: "GroupDocs.Parser for Java Document Parser SDK для Java"
head_description: "Високопродуктивний Document Parser SDK для Java. Витягайте текст, зображення, метадані, штрихкоди, таблиці та інші дані з PDF, Word, Excel, електронних листів та понад 50 форматів документів."

############################# Header ############################
title: "Document Parser SDK для Java"
description: "Додайте швидкий, точний аналіз документів до ваших застосунків Java та витягайте текст, зображення, метадані та структуровані дані з документів і зображень."
words:
  for: "для"

actions:
  main: "Maven Завантажити"
  main_link: "https://releases.groupdocs.com/java/repo/com/groupdocs/groupdocs-parser/"
  alt: "Ліцензування"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/java/"
  title: "Готові розпочати?"
  description: "Спробуйте функції GroupDocs.Parser безкоштовно або запитайте ліцензію"

release:
  title: "Випущено версію {0}"
  notes: "Перегляньте, що нового"
  downloads: "Завантаження"

code:
  title: "Швидко розбирати вміст документу за допомогою SDK"
  more: "Більше прикладів"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java/"
  install: |
    <dependency>
      <groupId>com.groupdocs</groupId>
      <artifactId>groupdocs-parser</artifactId>
      <version>{0}</version>
    </dependency>
  content: |
    ```java {style=abap}  
    // Передайте вихідний файл до інстанції Parser
    try (Parser parser = new Parser("source.pdf"))
    {
        // Передайте текст документа до TextReader
        try (TextReader reader = parser.getText())
        {
            // Обробіть текст документа
            System.out.println(reader == null 
                ? "" 
                : reader.readToEnd());
        }
    }
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser на перший погляд"
  description: "Document Parser SDK для виконання високоточного аналізу документів у застосунках Java"
  features:
    # feature loop
    - title: "Витягувати дані з документів"
      content: "API GroupDocs.Parser for Java дозволяє отримувати текст, метадані та зображення з широкого спектру форматів файлів, таких як офісні документи, електронні листи, вкладення та архіви. Цей потужний інструмент допомагає ефективно отримувати доступ і обробляти цінну інформацію, що міститься у цих файлах, для різних застосувань, таких як аналіз даних, індексація пошукових систем або системи управління контентом."

    # feature loop
    - title: "Розбір документів"
      content: "Видобувайте різні елементи, такі як гіперпосилання, таблиці, QR‑коди, штрих‑коди та дані з PDF‑форм. Також розбирайте будь‑яку потрібну інформацію з документів за допомогою користувацьких шаблонів."

    # feature loop
    - title: "Налаштування результатів"
      content: "Java API дозволяє отримувати дані у різних форматах, таких як необроблені, структуровані, HTML або Markdown. Крім того, API пропонує функцію пошуку для знаходження окремих слів або фраз у тексті документів."

############################# Platforms ############################
platforms:
  enable: true
  title: "Платформна незалежність"
  description: "GroupDocs.Parser for Java підтримує наступні операційні системи, фреймворки та менеджери пакетів"
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
    - title: "Eclipse"
      image: "eclipse"
    # platform loop
    - title: "IntelliJ"
      image: "intellij"
    # platform loop
    - title: "Windows"
      image: "windows"
    # platform loop
    - title: "Linux"
      image: "linux"
    # platform loop
    - title: "Maven"
      image: "maven"

############################# File formats ############################
formats:
  enable: true
  title: "Підтримувані формати файлів"
  description: |
    GroupDocs.Parser for Java підтримує роботу з наступними [форматами файлів](https://docs.groupdocs.com/parser/java/supported-document-formats/).
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
  title: "GroupDocs.Parser for Java функції"
  description: "Видобувайте дані з PDF‑файлів, офісних документів, зображень та інших форматів швидко та точно за допомогою нашого Java Document Parser SDK"

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
  description: "Декілька прикладів типових операцій GroupDocs.Parser for Java"
  items:
    # code sample loop
    - title: "Видобути зображення з PDF‑документів"
      content: |
        GroupDocs.Parser for Java полегшує Java розробникам видобуток зображень з [документів](https://docs.groupdocs.com/parser/java/extract-images-from-documents/):
        {{< landing/code title="Витягнути зображення з PDF‑документів у Java">}}
        ```java {style=abap}
        // Створіть екземпляр класу Parser
        try (Parser parser = new Parser("source.pdf"))
        {
            // Витягніть зображення
            Iterable<PageImageArea> images = parser.getImages();

            // Перевірте, чи щось витягнуто
            if (images == null) {
                return;
            }

            // Переберіть зображення
            for (PageImageArea image : images) {
                // Виведіть індекс сторінки, прямокутник і тип зображення
                System.out.println(String.format("Page: %d, R: %s, Type: %s", 
                    image.getPage().getIndex(), image.getRectangle(), image.getFileType()));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Видобути штрих‑коди з зображень"
      content: |
        Використовуйте наш API Java для вилучення [штрих-кодів](https://docs.groupdocs.com/parser/java/extract-barcodes-from-document/) з зображень:
        {{< landing/code title="Витягнути штрихкоди з зображень у Java">}}
        ```java {style=abap}   
        // Завантажте вихідне зображення у Parser
        try (Parser parser = new Parser("source.jpg")){

            // Перевірте, чи файл підтримує витягування штрихкодів
            if (!parser.getFeatures().isBarcodes()) {

                // Витягніть штрихкоди з файлу
                Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();

                // Переберіть штрихкоди
                for (PageBarcodeArea barcode : barcodes) {
                    // Виведіть індекс сторінки
                    System.out.println("Page: " + barcode.getPage().getIndex());
                    // Виведіть значення штрихкоду
                    System.out.println("Value: " + barcode.getValue());
                }
            }
        }
        ```
        {{< /landing/code >}}

---
