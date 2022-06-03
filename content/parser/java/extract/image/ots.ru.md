---
############################# Static ############################
layout: "auto-gen-gist"
draft: false
path: "ru/parser/java/extract/image/ots/"
otherformats: DOC DOT DOCX DOCM DOTX DOTM TXT ODT OTT RTF PDF XHTML MHTML MD XML EPUB FB2 CHM XLS XLT XLSX XLSM XLSB XLTX XLTM ODS CSV XLAM PPT PPTX  PPS POT PPSX PPTM POTX PPSM ODP OTP PST OST EML EMLX MSG ONE 

############################# Head ############################
head_title: "Как извлечь изображения из Excel, Word, PDF и других документов с помощью Java?"
head_description: "GroupDocs.Parser Java API позволяет разработчикам программного обеспечения анализировать и извлекать изображения из документов PDF, DOC, DOCX, PPT, PPTX, XLS, XLSX, области страницы и электронных писем внутри приложений Java."

############################# Header ############################
title: "Java API для анализа и извлечения изображений из Excel, Word, PowerPoint, PDF и других страниц документов"
description: "GroupDocs.Parser Java API позволяет программистам извлекать изображения из документов PDF, DOC, DOCX, PPT, PPTX, EML, MSG, XLS, XLSX, CSV, ODT, RTF и EPUB или страниц документа внутри приложений Java."

######################### Download Button #######################
button:
    enable: true

############################# About ############################
about:
    enable: true
    title: "Узнайте, как извлекать изображения из документов или определенной страницы с помощью Java API?"
    content: |
       Изображение стоит тысячи слов, и его нельзя игнорировать в современном визуальном мире при создании привлекательного контента. Изображения могут быть отличным источником информации, а также привлекать внимание пользователя. Часто требуется получить изображения из документов, журналов или презентаций и использовать их в другом месте. GroupDocs.Parser для Java — это мощный API, который помогает разработчикам программного обеспечения и программистам создавать решения для анализа и извлечения изображений или другой информации из многочисленных типов документов. Он также поддерживает сохранение изображений в форматах PNG, JPEG, WebP, GIF, BMP и других. API включает поддержку некоторых популярных форматов документов, таких как PDF, форматы Microsoft Office: Word (DOC, DOCX), PowerPoint (PPT, PPTX), Excel (XLS, XLSX), форматы LibreOffice, электронные письма, электронные книги и многие другие. . Он также включает поддержку некоторых расширенных функций, связанных с анализом документов, извлечением простого и структурированного текста, поиском текста по ключевым словам, извлечением метаданных или изображений, контейнеров, а также вложений и многим другим.

############################# content ############################
steps:
    enable: true
    block:
    - title_left: "Как извлечь изображения из документов OTS"
      content_left: |
       В GroupDocs.Parser Java включены функции для извлечения изображений из документов OTS. В следующем примере кода Java показано, как можно легко извлечь изображения из документа OTS.

      title_right: "Получить изображения из документов через Java"
      content_right: |
        * Создайте экземпляр [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser) 
        * Проверьте, поддерживает ли документ извлечение изображений
        * Вызов метода [getImages()](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getImages()) извлекает все изображения из всего документа.
        * Извлечь все изображения из документа
        * Перебирать изображения и печатать тип изображения

      gisthash: "b13e690d2593f92081abd99948363e06"
      gistfile: "extract_images_form_documents.java"

    - title_left: "Извлечение изображений со страницы документов OTS"
      content_left: |
       Java API GroupDocs.Parser позволяет разработчикам программного обеспечения извлекать изображения из документов OTS с помощью пары строк кода. В приведенном ниже коде Java показано извлечение изображений из документа OTS. 

      title_right: "Как извлечь изображения файлов через Java"
      content_right: |
        * Создайте экземпляр [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser) 
        * Проверьте, поддерживает ли документ извлечение изображений
        * Получите информацию о документе, вызвав метод [getDocumentInfo](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getDocumentInfo()).
        * Проверить документ на наличие страниц
        * Перебирать страницы и печатать номер страницы
        * Вызов метода [getImages()](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getImages()) извлекает все изображения из всего документа.
        * Перебирать изображения и печатать тип изображения
     
      gisthash: "68450336a57c5d8df06b4ef1ea69b29f"
      gistfile: "extract_images_form_documents_page.java"
      
    - title_left: "Как извлечь изображения из области страницы документов OTS"
      content_left: |
       Java API GroupDocs.Parser обеспечивает полную поддержку извлечения из страницы документа OTS. Следующий код Java демонстрирует, как программисты могут извлекать изображения из области страницы документа OTS в своих собственных приложениях Java.

      title_right: "Извлекать изображения с помощью Java?"
      content_right: |
        * Создайте экземпляр [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser)  
        * Создайте параметры, которые используются для извлечения изображений
        * Проверьте документ на поддержку извлечения изображений
        * Вызовите метод [getImages()](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getImages()) для извлечения изображений из верхнего левого угла страницы.
        * Перебирать изображения и распечатывать URL-адрес изображений
     
      gisthash: "40143a56569ae88e7e7c972ccca041b5"
      gistfile: "extract_images_form_documents_page_area.java"

    - title_left: "Как извлечь изображения в файл через Java API"
      content_left: |
       Java API GroupDocs.Parser позволяет извлекать изображения из документа OTS и сохранять содержимое изображения в файл. Следующий код Java демонстрирует, как программисты могут извлекать изображения из файла по своему выбору в своих собственных приложениях Java.

      title_right: "Извлечение изображений из документа в файл"
      content_right: |
        * Создайте экземпляр [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser) 
        * Проверить документ на поддержку извлечения изображений
        * Вызов метода [getImages()](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getImages()) для извлечения изображений из верхнего левого угла страницы.
        * Создайте параметры для сохранения изображения в поддерживаемом формате файла
        * Перебирать изображения и распечатывать URL-адрес изображений
     
      gisthash: "6faeafc93e4412265b7439209828950b"
      gistfile: "images_saving_to_files.java"

    - title_left: "Системные Требования"
      content_left: |
        GroupDocs.Parser для Java поддерживается на всех основных платформах и операционных системах. Он может создавать документы в Microsoft Word, Excel, PowerPoint, Outlook, OpenOffice и более 50 других форматах. Для получения полного руководства по системным требованиям, пожалуйста, посетите системные требования перед выполнением приведенного ниже кода. Убедитесь, что в вашей системе установлены следующие предварительные требования:
        * Операционные системы: Microsoft Windows, Linux, MacOS
        * Поддержка версий Java: J2SE 7.0 (1.7), J2SE 8.0 (1.8) или выше
        * Получите последнюю версию Java API GroupDocs.Parser из GroupDocs [репозитория](https://repository.groupdocs.com/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs-parser)
        
      title_right: "Зачем использовать GroupDocs.Parser"
      content_right: |
        * Извлечение простого текста из любого из поддерживаемых документов.
        * Поддержка извлечения оглавления
        * Извлечение форматированного текста, метаданных, изображений, контейнеров и вложений.
        * Парсинг документов по пользовательским шаблонам.
        * Поиск текста с использованием ключевого слова или регулярного выражения.
        * Поддержка извлечения структурированного текста
        * Извлечение оглавления для некоторых поддерживаемых форматов документов.
        * Анализировать данные формы из PDF-документов.

demos:
    enable: true
        

more_formats:
    enable: true


back_to_top:
    enable: true
---