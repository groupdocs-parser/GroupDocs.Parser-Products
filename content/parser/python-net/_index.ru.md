---
############################# Static ############################
layout: "landing"
date: 2025-12-09T14:10:41
draft: false

lang: ru
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
head_description: "Высокопроизводительный Document Parser SDK для Python. Извлекайте текст, изображения, метаданные, штрихкоды, таблицы и другие данные из PDF, Word, Excel, электронных писем и более 50 форматов документов."

############################# Header ############################
title: "Document Parser SDK для Python"
description: "Добавьте быструю и точную обработку документов в ваши приложения Python и извлекайте текст, изображения, метаданные и структурированные данные из документов и изображений."
words:
  for: "для"

actions:
  hidden: true # Hide version 0 is released
  main: "PyPI Скачать"
  main_link: "https://pypi.org/project/groupdocs-parser-net/"
  alt: "Лицензирование"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/python-net/"
  title: "Готовы начать?"
  description: "Попробуйте функции GroupDocs.Parser бесплатно или запросите лицензию"

release:
  enable: false
  title: "Выпущена версия {0}"
  notes: "Посмотрите, что нового"
  downloads: "Загрузки"

code:
  title: "Извлеките текст с помощью Python"
  more: "Больше примеров"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
  install: "pip install groupdocs-parser-net"
  content: |
    ```python {style=abap}  
    from groupdocs.parser import Parser

    # Загрузить документ
    with Parser("sample.pdf") as parser:
        # Извлечь текст из документа
        text = parser.GetText()

        # Вывести весь извлеченный текст
        print(text)
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser в двух словах"
  description: "Document Parser SDK для выполнения высокоточной обработки документов в приложениях Python"
  features:
    # feature loop
    - title: "Извлечение данных из документов"
      content: "GroupDocs.Parser for Python via .NET API позволяет получать текст, метаданные и изображения из широкого спектра форматов файлов, таких как офисные документы, электронные письма, вложения и архивы. Этот мощный инструмент помогает эффективно получать доступ к ценной информации, содержащейся в этих файлах, и обрабатывать её для различных приложений, таких как анализ данных, индексирование поисковых систем или системы управления контентом."

    # feature loop
    - title: "Парсинг документов"
      content: "Извлекайте различные элементы, такие как гиперссылки, таблицы, QR‑коды, штрихкоды и данные из PDF‑форм. Также парсите любую необходимую информацию из документов с помощью пользовательских шаблонов."

    # feature loop
    - title: "Настройка результатов"
      content: "Python API позволяет получать данные в различных форматах, таких как необработанные, структурированные, HTML или Markdown. Кроме того, API предоставляет функцию поиска для нахождения конкретных слов или фраз в тексте документов."

############################# Platforms ############################
platforms:
  enable: true
  title: "Независимость от платформы"
  description: "GroupDocs.Parser for Python via .NET поддерживает следующие операционные системы, фреймворки и менеджеры пакетов"
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
  title: "Поддерживаемые форматы файлов"
  description: |
    GroupDocs.Parser for Python via .NET поддерживает работу со следующими [форматами файлов](https://docs.groupdocs.com/parser/python-net/supported-document-formats/).
  groups:
    # group loop
    - color: "green"
      content: |
        ### Форматы Microsoft Office
        * **Word:** DOCX, DOC, DOCM, DOT, DOTX, DOTM, RTF
        * **Excel:** XLSX, XLS, XLSM, XLSB, XLTM, XLT, XLTM, XLTX, XLAM, SXC, SpreadsheetML
        * **PowerPoint:** PPT, PPTX, PPS, PPSX, PPSM, POT, POTM, POTX, PPTM
    # group loop
    - color: "blue"
      content: |
        ### Изображения и другие форматы
        * **Переносимый:** PDF 
        * **Изображения:** JPG, BMP, PNG, TIFF, GIF
        * **Другие офисные форматы:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### Другие форматы
        * **Веб:** HTML, MHTML 
        * **Архивы:** ZIP, TAR, 7Z 
        * **Электронные книги:** CHM, EPUB, FB2, MOBI 

############################# Features ############################
features:
  enable: true
  title: "Возможности GroupDocs.Parser for Python via .NET"
  description: "Извлекайте данные из PDF, офисных документов, изображений и других форматов быстро и точно с помощью нашего Python Document Parser SDK"

  items:
    # feature loop
    - icon: "text"
      title: "Извлечение текста"
      content: "Извлекайте текстовую информацию из различных форматов файлов, таких как офисные документы, PDF‑файлы и изображения, для удобного чтения и анализа."

    # feature loop
    - icon: "image"
      title: "Извлечение изображений"
      content: "Получайте визуальное содержимое из различных источников, таких как офисные документы и PDF‑файлы, для удобного доступа и использования."

    # feature loop
    - icon: "qr"
      title: "Сканирование QR‑кодов"
      content: "Обнаруживайте и расшифровывайте QR‑коды, находящиеся в офисных документах, PDF‑файлах или визуальном контенте, для эффективного извлечения информации."

    # feature loop
    - icon: "email"
      title: "Извлечение данных из вложений электронной почты и архивов"
      content: "Собирайте ценную информацию из электронных писем, файлов‑вложений и сжатых источников данных для эффективного анализа и использования."

    # feature loop
    - icon: "table"
      title: "Извлечение таблиц"
      content: "Определяйте и извлекайте табличные данные из PDF‑документов для упорядоченного анализа и использования."

    # feature loop
    - icon: "hyperlink"
      title: "Извлечение гиперссылок"
      content: "Находите и извлекайте гиперссылки и адреса электронной почты в офисных документах или PDF‑файлах для удобного доступа."

    # feature loop
    - icon: "pdf"
      title: "Разбор PDF‑форм"
      content: "PDF‑формы — это цифровые документы с заполняемыми полями для взаимодействия с пользователем, позволяющие вводить информацию в электронном виде. API Python можно использовать для извлечения данных из этих форм для эффективной обработки."

    # feature loop
    - icon: "template"
      title: "Разбор данных по шаблонам"
      content: "Создайте пользовательские шаблоны и используйте их с API Python для разбора конкретной информации из PDF‑файлов, упрощая процессы извлечения данных."

    # feature loop
    - icon: "search"
      title: "Поиск текста в документах"
      content: "Быстро находите конкретные слова или шаблоны в документах."


############################# Code samples ############################
code_samples:
  enable: true
  title: "Примеры кода"
  description: "Помимо базового извлечения текста, ниже представлены типовые сценарии быстрого извлечения текста, изображений и метаданных."
  items:
    # code sample loop
    - title: "Поиск текста в документе"
      content: |
        В этом примере показано, как выполнить поиск конкретной фразы в PDF‑документе и вывести место её нахождения.
        {{< landing/code title="Поиск текста в документе на Python">}}
        ```python {style=abap}
        from groupdocs.parser import Parser

        # Загрузите документ
        with Parser("sample.pdf") as parser:
            # Выведите номер страницы и прямоугольник, где была найдена фраза
            for area in parser.Search("Total Amount"):
                # Выведите номер страницы и прямоугольник, где была найдена фраза
                print(f"Page {area.PageIndex}, Rectangle: {area.Rectangle}")
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Извлечение изображений из документа"
      content: |
        В этом примере показано, как извлечь изображения из PDF‑документа и сохранить их в файл.
        {{< landing/code title="Извлечение изображений из документа на Python">}}
        ```python {style=abap}    
        from groupdocs.parser import Parser

        # Загрузите документ
        with Parser("sample.docx") as parser:
            # Извлеките изображения из документа
            images = parser.GetImages()

            # Сохраните изображения в файл
            index = 1
            for image in images:
                image.Save(f"image_{index}.png")
                index += 1
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Извлечение метаданных из документа"
      content: |
        В этом примере показано, как извлечь метаданные из PDF‑документа и вывести их.
        {{< landing/code title="Извлечение метаданных из документа на Python">}}
        ```python {style=abap}    
        from groupdocs.parser import Parser

        # Загрузите документ
        with Parser("sample.pdf") as parser:
            # Извлеките метаданные из документа
            metadata = parser.GetMetadata()

            # Выведите метаданные
            for item in metadata:
                print(f"{item.Name}: {item.Value}")
        ```
        {{< /landing/code >}}
---
