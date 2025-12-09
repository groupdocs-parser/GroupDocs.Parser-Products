---
############################# Static ############################
layout: "landing"
date: 2025-12-09T21:34:38
draft: false

lang: uk
product: "Parser"
product_tag: "parser"
platform: "Python"
platform_tag: "python-net"

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
head_title: "GroupDocs.Parser for Python via .NET Document Parser SDK для Python"
head_description: "Високопродуктивний Document Parser SDK для Python. Вилучайте текст, зображення, метадані, штрих‑коди, таблиці та інші дані з PDF, Word, Excel, електронних листів та понад 50 форматів документів."

############################# Header ############################
title: "Document Parser SDK для Python"
description: "Додайте швидкий і точний аналіз документів у ваші застосунки Python і вилучайте текст, зображення, метадані та структуровані дані з документів і зображень."
words:
  for: "для"

actions:
  hidden: true # Hide version 0 is released
  main: "PyPI Завантажити"
  main_link: "https://pypi.org/project/groupdocs-parser-net/"
  alt: "Ліцензування"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/python-net/"
  title: "Готові розпочати?"
  description: "Спробуйте функції GroupDocs.Parser безкоштовно або запитайте ліцензію"

release:
  enable: false
  title: "Випущено версію {0}"
  notes: "Перегляньте, що нового"
  downloads: "Завантаження"

code:
  title: "Вилучити текст за допомогою Python"
  more: "Більше прикладів"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Python-via-.NET/"
  install: "pip install groupdocs-parser-net"
  content: |
    ```python {style=abap}  
    from groupdocs.parser import Parser

    # Завантажити документ
    with Parser("sample.pdf") as parser:
        # Вилучити текст з документа
        text = parser.GetText()

        # Вивести весь вилучений текст
        print(text)
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser на перший погляд"
  description: "Document Parser SDK для високоточного аналізу документів у застосунках Python"
  features:
    # feature loop
    - title: "Вилучення даних з документів"
      content: "GroupDocs.Parser for Python via .NET API дозволяє отримувати текст, метадані та зображення з широкого спектру форматів файлів, таких як офісні документи, електронні листи, вкладення та архіви. Цей потужний інструмент допомагає ефективно отримувати доступ і обробляти цінну інформацію, що міститься у цих файлах, для різних застосувань, таких як аналіз даних, індексація пошукових систем або системи керування контентом."

    # feature loop
    - title: "Аналіз документів"
      content: "Вилучайте різні елементи, такі як гіперпосилання, таблиці, QR‑коди, штрих‑коди та дані з PDF‑форм. Також аналізуйте будь‑яку необхідну інформацію з документів за допомогою користувацьких шаблонів."

    # feature loop
    - title: "Налаштування результатів"
      content: "Python API дозволяє отримувати дані в різних форматах, таких як необроблені, структуровані, HTML або Markdown. Крім того, API пропонує функцію пошуку для знаходження конкретних слів або фраз у тексті документів."

############################# Platforms ############################
platforms:
  enable: true
  title: "Платформна незалежність"
  description: "GroupDocs.Parser for Python via .NET підтримує наступні операційні системи, фреймворки та менеджери пакетів"
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
    GroupDocs.Parser for Python via .NET підтримує роботу з наступними [форматами файлів](https://docs.groupdocs.com/parser/python-net/supported-document-formats/).
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
  title: "Функції GroupDocs.Parser for Python via .NET"
  description: "Швидко та точно витягайте дані з PDF, офісних документів, зображень та інших форматів за допомогою нашого Python Document Parser SDK"

  items:
    # feature loop
    - icon: "text"
      title: "Вилучення тексту"
      content: "Вилучайте текстову інформацію з різних форматів файлів, таких як офісні документи, PDF‑файли та зображення, для зручного читання та аналізу."

    # feature loop
    - icon: "image"
      title: "Вилучення зображень"
      content: "Отримуйте візуальний контент з різноманітних джерел, таких як офісні документи, PDF‑файли, для зручного доступу та використання."

    # feature loop
    - icon: "qr"
      title: "Сканування QR‑кодів"
      content: "Виявляйте та розшифровуйте QR‑коди, що містяться в офісних документах, PDF‑файлах або візуальному контенті, для ефективного отримання інформації."

    # feature loop
    - icon: "email"
      title: "Вилучення даних з вкладень електронних листів та архівів"
      content: "Збирайте цінну інформацію з електронних листів, вкладень файлів та стиснених даних для ефективного аналізу та використання."

    # feature loop
    - icon: "table"
      title: "Вилучення таблиць"
      content: "Ідентифікуйте та вилучайте табличні дані з PDF‑документів для впорядкованого аналізу та використання."

    # feature loop
    - icon: "hyperlink"
      title: "Вилучення гіперпосилань"
      content: "Знаходьте та вилучайте гіперпосилання та електронні адреси в офісних документах або PDF‑файлах для зручного доступу."

    # feature loop
    - icon: "pdf"
      title: "Розбір PDF‑форм"
      content: "PDF‑форми — це цифрові документи з заповнюваними полями для взаємодії користувачів, що дозволяє вводити інформацію електронно. API Python можна використовувати для вилучення даних з цих форм для ефективної обробки."

    # feature loop
    - icon: "template"
      title: "Розбір даних за шаблонами"
      content: "Створюйте користувацькі шаблони та використовуйте їх разом з API Python для розбору конкретної інформації з PDF‑файлів, спрощуючи процеси вилучення даних."

    # feature loop
    - icon: "search"
      title: "Пошук тексту в документах"
      content: "Швидко знаходьте конкретні слова чи шаблони в документах."


############################# Code samples ############################
code_samples:
  enable: true
  title: "Зразки коду"
  description: "Окрім базового вилучення тексту, ось найпоширеніші випадки використання для швидкого вилучення тексту, зображень та метаданих."
  items:
    # code sample loop
    - title: "Пошук тексту в документі"
      content: |
        Цей приклад демонструє, як шукати певну фразу у PDF‑документі та виводити, де вона була знайдена.
        {{< landing/code title="Пошук тексту в документі на Python">}}
        ```python {style=abap}
        from groupdocs.parser import Parser

        # Завантажте документ
        with Parser("sample.pdf") as parser:
            # Виведіть індекс сторінки та прямокутник, де була знайдена фраза
            for area in parser.Search("Total Amount"):
                # Виведіть індекс сторінки та прямокутник, де була знайдена фраза
                print(f"Page {area.PageIndex}, Rectangle: {area.Rectangle}")
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Вилучення зображень з документа"
      content: |
        Цей приклад показує, як вилучати зображення з PDF‑документа та зберігати їх у файл.
        {{< landing/code title="Вилучення зображень з документа на Python">}}
        ```python {style=abap}    
        from groupdocs.parser import Parser

        # Завантажте документ
        with Parser("sample.docx") as parser:
            # Вилучіть зображення з документа
            images = parser.GetImages()

            # Збережіть зображення у файл
            index = 1
            for image in images:
                image.Save(f"image_{index}.png")
                index += 1
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Вилучення метаданих з документа"
      content: |
        Цей приклад демонструє, як вилучити метадані з PDF‑документа та вивести їх.
        {{< landing/code title="Вилучення метаданих з документа на Python">}}
        ```python {style=abap}    
        from groupdocs.parser import Parser

        # Завантажте документ
        with Parser("sample.pdf") as parser:
            # Вилучіть метадані з документа
            metadata = parser.GetMetadata()

            # Виведіть метадані
            for item in metadata:
                print(f"{item.Name}: {item.Value}")
        ```
        {{< /landing/code >}}
---
