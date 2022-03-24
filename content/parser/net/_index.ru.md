---
############################# Static ############################
layout: "product"
date: 2021-04-27T09:31:06+03:00
draft: false

product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "API парсинга .NET, извлечение метаданных текстовых изображений из PDF Word Excel"
head_description: "API анализа документов C# .NET для извлечения текста, изображений, метаданных и кодирования из баз данных, PDF, Word, Excel, презентаций, Интернета, электронной почты, форматов файлов EPUB и zip.."

############################# Header ############################
title: ".NET API для извлечения данных документа"
description: "Извлекайте изображения, необработанный или форматированный текст и метаданные из документов, электронных таблиц, презентаций, электронных писем и архивов из приложений .NET."
button:
    enable: true

############################# SubMenu ############################
submenu:
    enable: true
    
    left:
        img_alt: "GroupDocs.Parser for .NET"
        image: "/border/groupdocs-parser-net.svg"
        product: "GroupDocs.Parser"
        platform: ".NET"

    middle:
        button:
            # button loop
            - link: "#overview"
              text: "Обзор"

            # button loop
            - link: "#features"
              text: "Функции"

            # button loop
            - link: "#support"
              text: "Support"

            # button loop
            - link: "https://products.groupdocs.app/parser"
              text: "Live Demo"

            # button loop
            - link: "https://purchase.groupdocs.com/pricing/parser/net"
              text: "Pricing"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/net/"
        link_buy: "https://purchase.groupdocs.com"

############################# Обзор ############################
overview:
    enable: true
    content: |
      GroupDocs.Parser для .NET — это API извлечения текста, метаданных и изображений для бизнес-приложений, разработанных с использованием C#, ASP.NET и других технологий .NET. Он поддерживает извлечение необработанного, форматированного и структурированного текста, а также метаданных из файлов поддерживаемых форматов. С помощью GroupDocs.Parser для .NET ваши приложения также могут выполнять синтаксический анализ защищенных паролем документов для популярных форматов, таких как документы обработки Word, электронные таблицы Excel, презентации PowerPoint, OneNote, файлы PDF и ZIP-архивы.
    tabs:
      enable: true
      
      ## TAB ONE ##
      tab_one:
        description: |
          Ниже приведен обзор GroupDocs.Parser для .NET:
      
        left:
          enable: true
          icon: "fas fa-tools"
          title: "Функции"
          content: |
            * Извлечь изображения
            * Извлечь необработанный текст
            * Извлечь форматированный текст
            * Извлечь структурированный текст
            * Извлечь метаданные
            * Извлечение из файлов в ZIP-файле
            * Извлечь путем поиска
            * Извлечь с помощью Text Formatters
            * Определить стандарт кодирования
            * Определить тип носителя
        
        right:
          enable: true
          icon: "fab fa-html5"
          title: "API"
          content: |
            * Получает входной файл
            * Извлекает необработанный или форматированный текст
            * Извлекает метаданные
      
      ## TAB TWO ##
      tab_two:
        description: |
          GroupDocs.Parser для .NET поддерживает следующие [форматы файлов документов](https://docs.groupdocs.com/parser/net/supported-document-formats/):

        left:
          enable: true
          table:
            # table loop
            - title: "Извлечение текста"
              content: |
                * **Текст**: DOC, DOCX, DOT, DOTM, DOTX, DOCM, RTF, ODT, OTT, TXT, MD, WordprocessingML (XML)
                * **Таблицы**: XLS, XLSX, CSV, XLSM, XLSB, ODS, SpreadsheetML (XML), XLT, XLTX, XLTM, OTS, XLA, XLAM, TSV
                * **Презентации**: PPT, PPTX, PPTM, PPS, PPSX, PPSM, POT, POTX, POTM, ODP, OTP
                * **OneNote**: ОДИН
                * **Электронная почта**: MSG, EML, EMLX, PST, OST, MS EXCHANGE SERVER, POP, IMAP
                * **Электронное издание**: EPUB, FB2
                * **Переносимый документ**: PDF, портфолио PDF, зашифрованный PDF
                * **На основе DOM**: XML, HTML, XHTML, MHTML
                * **Сжатие и упаковка**: ZIP, CHM
                * **База данных**: ADO.NET

            # table loop
            - title: "Обнаружение кодирования"
              content: |
                * **BOM**: UTF32 LE, UTF32 BE, UTF16 LE, UTF16 BE, UTF8, and UTF7
                * **Content**: UTF32 LE, UTF32 BE, UTF16 LE, UTF16 BE, UTF8, and ANSI

        right:
          enable: true
          table:
            # table loop
            - title: "Извлечение метаданных"
              content: |
                * **Текст**: DOC, DOCX, DOT, DOTX, DOTM, OTT, ODT
                * **Электронные таблицы**: XLS, XLSX, XLT, XLTX, XLTM, XLA, XLAM, OTS, ODS
                * **Презентации**: PPT, PPTX, POT, POTX, POTM, PPSM, PPTM, OTP, ODP
                * **Электронная почта**: MSG, EML, EMLX
                * **Электронное издание**: EPUB, FB2
                * **Другое**: PDF

            # table loop
            - title: "Text & Извлечение метаданных"
              content: |
                * **Шаблон**: DOTX, POTX
                * **Шаблон с поддержкой макросов**: DOTM, POTM, PPSM, PPTM
                * **Шаблон OpenDocument**: OTT

            # table loop
            - title: "Извлечение изображения"
              content: |
                * **Текст**: DOC, DOCX, DOCM, RTF, DOT, DOTM, DOTX, ODT
                * **Таблицы**: XLS, XLSX, XLSM, XLSB, ODS, XLT, XLTM, XLTX
                * **Презентации**: PPT, PPTX, PPTM, ODP, POT, POTM, POTX, PPS, PPSX, PPSM
                * **Переносимый документ**: PDF, POT, POTM, POTX
                * **Электронная книга**: CHM, EPUB, FB2
                * **Разметка**: HTML

      ## TAB THREE ##
      tab_three:
        description: |
          GroupDocs.Parser for .NET поддерживает следующие Операционные системы Менеджер пакетовs:
        
        left:
          enable: true
          table:
            # table loop
            - icon: "fab fa-windows"
              title: "Операционные системы"
              content: |
                * Рабочий стол Windows
                * Windows-сервер
                * Windows Azure
                * линукс

            # table loop
            - icon: "fas fa-code"
              title: "Поддерживаемые платформы"
              content: |
                * .NET Framework 2.0 или выше
                * Монофреймворк 1.2 или выше
                * .NET Стандарт 2.0
                * .NET Core 2.0

        right:
          enable: true
          table:
            # table loop
            - icon: "fas fa-box"
              title: "Менеджер пакетов"
              content: |
                * NuGet

            # table loop
            - icon: "fas fa-tools"
              title: "Среды разработки"
              content: |
                * Microsoft Visual Studio
                * Xamarin.Android
                * Xamarin.IOS
                * Xamarin.Mac
                * МоноДевелопмент

############################# Функции ############################
features:
    enable: true
    title: "GroupDocs.Parser for .NET Функции"

    feature:
      # feature loop
      - icon: "fas fa-copy"
        content: "Статистический подсчет встречаемости слов в одном или нескольких файлах"

      # feature loop
      - icon: "fas fa-eye"
        content: "Извлечение текста и метаданных из листов Excel и шаблонов презентаций"

      # feature loop
      - icon: "fas fa-bolt"
        content: "Извлечение текстового содержимого из файла или потока без установки Document Reader"
      
      # feature loop
      - icon: "fas fa-file-powerpoint"
        content: "Получить отформатированный текст из документа, используя режим быстрого или стандартного извлечения текста"

      # feature loop
      - icon: "fas fa-code"
        content: "Определить тип носителя XML-документов, защищенных паролем, и извлечь из них текст"

      # feature loop
      - icon: "fas fa-cloud"
        content: "Программное получение форматированного текста из электронных писем и вложений"

      # feature loop
      - icon: "fas fa-remove-format"
        content: "Вытягивание текста из одной или нескольких страниц документа OneNote"

      # feature loop
      - icon: "fas fa-comment-slash"
        content: "Извлечение данных из документов PDF, MS Word, Excel и презентаций"

      # feature loop
      - icon: "fas fa-location-arrow"
        content: "Извлечение данных из форм PDF и извлечение текста из простого файла PDF или документа портфолио PDF"

      # feature loop
      - icon: "fas fa-border-all"
        content: "Получить отформатированный текст из презентации PowerPoint или вытеснить текст из определенного слайда"

      # feature loop
      - icon: "fas fa-wrench"
        content: "Сбор необработанного или форматированного текста из ячеек, строк и столбцов электронной таблицы Excel"

      # feature loop
      - icon: "fas fa-columns"
        content: "Извлечение необработанного или HTML-форматированного текста из документа Word"

      # feature loop
      - icon: "fas fa-file-word"
        content: "HTML Formatter поддерживает форматирование абзаца, гиперссылки, шрифта, заголовков, списков и таблиц"

      # feature loop
      - icon: "fas fa-envelope"
        content: "Извлечение отдельного предложения или всего текста из файлов EPUB, CHM, Markdown и FB2"

      # feature loop
      - icon: "fas fa-print"
        content: "Выдержка из содержания базы данных, документов PDF, EPUB, CHM и Word Processing"

      # feature loop
      - icon: "fas fa-file-archive"
        content: "Вытащить текст с неповрежденной структурой содержимого и извлечь выделенный текст из документов"

      # feature loop
      - icon: "fas fa-lock"
        content: "Получить текстовую область из документов для анализа и извлечь метаданные из поддерживаемых форматов документов"

      # feature loop
      - icon: "fas fa-file-code"
        content: "Получить все или выбранные изображения из поддерживаемых форматов и повернуть извлеченные изображения"
      
      # feature loop
      - icon: "fas fa-fill-drip"
        content: "Извлечение текста из файлов в Zip-архивах и контейнерах OST и обнаружение типов файлов элементов ZIP-контейнеров"

      # feature loop
      - icon: "fas fa-file-excel"
        content: "Получить данные из контейнера электронной почты (веб-сервер Exchange, POP3, IMAP)"

      # feature loop
      - icon: "fas fa-heading"
        content: "Поиск простого текста, всего слова и регулярного выражения в документах"

      # feature loop
      - icon: "fas fa-project-diagram"
        content: "Подготовка шаблона документа, извлечение данных из документа и анализ полей и таблиц данных"

      # feature loop
      - icon: "fas fa-cube"
        content: "Поиск и извлечение выделенных выражений в документах"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Получить текст с помощью форматирования обычного текста (Простой и ASCII) или с помощью форматирования Markdown"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Markdown Formatter поддерживает форматирование шрифта, гиперссылок, заголовков, списков и таблиц"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Выполнение пользовательского форматирования с помощью краев, углов и пересечений для форматирования обычного текста"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Перемещение макета таблицы и обнаружение таблиц в прямоугольной области с помощью разделителей столбцов"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Извлечение текста из фигур, объектов WordArt и текстовых полей в форматах файлов Microsoft Office"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Извлечь изображенияв файлы — сохранение в форматах JPG, PNG, GIF, BMP, PNG или WEBP"

    больше_функций:
      # more_feature_loop
      - title: "Извлечение текста из документа"
        content: |
          Использовать GroupDocs.Parser for .NET API для извлечения текста из документа очень просто и достигается с помощью всего нескольких строк кода:

          ```cs
          using(Parser parser = new Parser("sample.docx"))
          {
            // Извлечь текст в ридер
            using(TextReader reader = parser.GetText())
            {
              // Распечатать текст из документа
              // Если извлечение текста не поддерживается, считыватель имеет значение null
              Console.WriteLine(reader == null ? "Text extraction isn't supported." : reader.ReadToEnd());
            }
          }
          ```

############################# Support ############################
support:
    enable: true

############################# Solutions ############################
solutions:
    enable: true
    title: "GroupDocs.Parser предлагает API для просмотра документов для других популярных сред разработки."

    solution:
        # solution loop
        - img_alt: "GroupDocs.Parser for Java"
          image: "/border/groupdocs-parser-java.svg"
          product: "GroupDocs.Parser"
          platform: "Java"
          link: "/parser/java/"

############################# Back to top ###############################
back_to_top:
  enable: true
---