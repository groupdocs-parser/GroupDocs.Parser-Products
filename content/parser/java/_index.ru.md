---
############################# Static ############################
layout: "product"
date: 2021-04-27T09:31:06+03:00
draft: false

product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Java API для анализа текста, изображений и метаданных из PDF Word Excel HTML"
head_description: "API анализатора документов Java для извлечения текста, изображений, метаданных и кодировки из баз данных, Word, Excel, презентаций, файлов PDF, электронной почты, EPUB и ZIP.."

############################# Header ############################
title: "Java Парсер API для извлечения данных"
description: "Java API для анализа и извлечения изображений и текста с метаданными из документов, презентаций, архивов и электронных писем."
button:
    enable: true

############################# SubMenu ############################
submenu:
    enable: true
    
    left:
        img_alt: "GroupDocs.Parser for Java"
        image: "/border/groupdocs-parser-java.svg"
        product: "GroupDocs.Parser"
        platform: "Java"

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
            - link: "https://purchase.groupdocs.com/pricing/parser/java"
              text: "Pricing"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/java/"
        link_buy: "https://purchase.groupdocs.com"

############################# Обзор ############################
overview:
    enable: true
    content: |
      GroupDocs.Parser для Java — это API-интерфейс для извлечения текста, изображений и метаданных, поддерживающий более 50 популярных типов документов, помогающий создавать бизнес-приложения с функциями анализа необработанного, структурированного и форматированного текста. Он также поддерживает анализ документов с использованием предопределенных шаблонов и позволяет быстро и точно извлекать сложные данные из счетов-фактур и других типичных документов. GroupDocs.Parser для Java позволяет извлекать текст и метаданные из защищенных паролем файлов всех популярных форматов, включая документы обработки текста, электронные таблицы Excel, презентации PowerPoint, файлы OneNote, PDF и ZIP-архивы.
    tabs:
      enable: true     
      
      ## TAB ONE ##
      tab_one:
        description: |
          Ниже приводится обзор GroupDocs.Parser для Java:

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
          GroupDocs.Parser для Java поддерживает следующие [форматы файлов документов](https://docs.groupdocs.com/parser/java/supported-document-formats/):

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
                * **BOM**: UTF32 LE, UTF32 BE, UTF16 LE, UTF16 BE, UTF8 и UTF7
                * **Содержимое**: UTF32 LE, UTF32 BE, UTF16 LE, UTF16 BE, UTF8 и ANSI.

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
                * **Электронные таблицы**: XLS, XLSX, XLSM, XLSB, ODS, XLT, XLTM, XLTX
                * **Презентации**: PPT, PPTX, PPTM, ODP, POT, POTM, POTX, PPS, PPSX, PPSM
                * **Переносимый документ**: PDF, POT, POTM, POTX
                * **Электронная книга**: CHM, EPUB, FB2
                * **Разметка**: HTML
      ## TAB THREE ##
      tab_three:
        description: |
          GroupDocs.Parser for Java поддерживает следующие Операционные системы:
        
        left:
          enable: true
          table:
            # table loop
            - icon: "fab fa-windows"
              title: "Операционные системы"
              content: |
                * Рабочий стол Microsoft Windows
                * Сервер Microsoft Windows
                * линукс
                * MacOS

            # table loop
            - icon: "fas fa-code"
              title: "Поддерживаемые платформы"
              content: |
                * Java 7 (1.7) и выше

        right:
          enable: true
          table:
            # table loop
            - icon: "fas fa-cogs"
              title: "Среды разработки"
              content: |
                * NetBeans
                * IntelliJ ИДЕЯ
                * Затмение
            # table loop
            - icon: "fas fa-tools"
              title: "Инструмент автоматизации сборки"
              content: |
                * Мавен

############################# Функции ############################
features:
    enable: true
    title: "GroupDocs.Parser for Java Функции"

    feature:
      # feature loop
      - icon: "fas fa-copy"
        content: "Статистический подсчет вхождений слов для одного или нескольких документов"

      # feature loop
      - icon: "fas fa-eye"
        content: "Извлечение текста и метаданных из электронных таблиц Excel и шаблонов презентаций PowerPoint"

      # feature loop
      - icon: "fas fa-code"
        content: "Определите тип носителя защищенных паролем XML-документов и извлеките из них текст"

      # feature loop
      - icon: "fas fa-cloud"
        content: "Программное извлечение форматированного текста из презентации PowerPoint, электронных писем и вложений"

      # feature loop
      - icon: "fas fa-remove-format"
        content: "Изгнать текст с одной или нескольких страниц документа OneNote"

      # feature loop
      - icon: "fas fa-comment-slash"
        content: "Извлечение необработанного текста из простого файла PDF или документа портфолио PDF"

      # feature loop
      - icon: "fas fa-location-arrow"
        content: "Извлечение данных из документов PDF, MS Word, Excel и презентаций"

      # feature loop
      - icon: "fas fa-border-all"
        content: "Извлечение необработанного или форматированного текста из ячеек, строк и столбцов электронной таблицы Excel"

      # feature loop
      - icon: "fas fa-wrench"
        content: "Соберите необработанный текст или текст в формате HTML из документа Word и извлеките выделенный текст из документов"

      # feature loop
      - icon: "fas fa-columns"
        content: "Получить данные из форм PDF и получить отформатированную таблицу из документа PDF или Word"

      # feature loop
      - icon: "fas fa-file-word"
        content: "Извлечение отдельного предложения или всего текста из файлов EPUB, CHM, Markdown и FB2"

      # feature loop
      - icon: "fas fa-print"
        content: "Извлеките текстовую область из документов для анализа и вытащите текст с неповрежденной структурой содержимого"

      # feature loop
      - icon: "fas fa-file-archive"
        content: "Получить метаданные из поддерживаемых форматов документов"

      # feature loop
      - icon: "fas fa-lock"
        content: "Извлечение всех или выбранных изображений из поддерживаемых форматов и поворот извлеченных изображений"

      # feature loop
      - icon: "fas fa-fill-drip"
        content: "Получение данных из контейнера электронной почты (веб-сервер Exchange, POP3, IMAP)"

      # feature loop
      - icon: "fas fa-heading"
        content: "Найти простой текст, целое слово и регулярное выражение в документах"

      # feature loop
      - icon: "fas fa-project-diagram"
        content: "Подготовка шаблона документа, извлечение данных из документа и анализ полей и таблиц данных"

      # feature loop
      - icon: "fas fa-cube"
        content: "Поиск и извлечение выделенных выражений в документах"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Вытягивание текста с помощью средства форматирования простого текста (простого и ASCII) или пользовательского форматирования с кромками, углами и пересечениями"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Извлечение и форматирование текста (шрифт, гиперссылки, заголовки, списки и таблицы) с помощью Markdown Formatter"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Получить текст с помощью HTML Formatter и применить форматирование к абзацам, гиперссылкам, шрифтам, заголовкам, спискам и таблицам"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Перемещение макета таблицы и обнаружение таблиц в прямоугольной области с помощью разделителей столбцов"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Извлечение текста из фигур, объектов WordArt и текстовых полей в форматах файлов Microsoft Office"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Extract Text from Email Servers and База данныхs via JDBC"

    больше_функций:
      # more_feature_loop
      - title: "Получить текст с помощью форматирования обычного текста или HTML"
        content: |
          С помощью GroupDocs.Parser для Java вы можете применять различные средства форматирования к тексту и HTML. Вы можете извлечь текст с помощью Plain Text Formatter как для простого, так и для ASCII. Вы также можете получить текст с помощью HTML Formatter и применить форматирование к абзацу, гиперссылке, шрифту, заголовкам, спискам и таблицам.

############################# Support ############################
support:
    enable: true

############################# Solutions ############################
solutions:
    enable: true
    title: "GroupDocs.Parser предлагает API для просмотра документов для других популярных сред разработки."

    solution:
        # solution loop
        - img_alt: "GroupDocs.Parser for .NET"
          image: "/border/groupdocs-parser-net.svg"
          product: "GroupDocs.Parser"
          platform: ".NET"
          link: "/parser/net/"

############################# Back to top ###############################
back_to_top:
  enable: true
---