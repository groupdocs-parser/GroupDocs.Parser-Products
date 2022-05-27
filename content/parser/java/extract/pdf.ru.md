---
############################# Static ############################
layout: "auto-gen-gist"
draft: false
path: "ru/parser/java/extract/pdf/"
otherformats: DOC DOT DOCX DOCM DOTX DOTM TXT ODT OTT RTF PDF  MHTML MD XML EPUB FB2 CHM XLS XLT XLSX XLSM XLSB XLTX XLTM ODS CSV OTS XLA XLAM PPT PPTX  PPS POT PPSX PPTM POTX PPSM ODP OTP PST OST EML EMLX MSG ONE 

############################# Head ############################
head_title: "Извлечение гиперссылок из документов, страниц или области страницы через Java API"
head_description: "GroupDocs.Parser Java API позволяет разработчикам извлекать гиперссылки из документов, страниц документов или определенных областей страниц Excel, PowerPoint, PDF, Outlook и т. д."

############################# Header ############################
title: "Java API для извлечения гиперссылок из документов, страниц или определенной области страницы"
description: "Java API GroupDocs.Parser упрощает работу разработчиков, позволяя им извлекать гиперссылки из документов, страницы документа или определенной области страницы PDF, DOCX, PPTX, EML, MSG, XLS, XLSX, CSV, RTF, EPUB и многих других."

######################### Download Button #######################
button:
    enable: true

############################# About ############################
about:
    enable: true
    title: "Как выполнить извлечение гиперссылок из различных документов с помощью Java?"
    content: |
       На этой веб-странице объясняется, как анализировать и извлекать гиперссылки из различных типов документов, страниц документа или определенной области страницы, используя всего пару строк кода Java. Гиперссылка может быть очень полезна для навигации между страницами или веб-сайтами и может указывать на весь документ или на определенную часть документа, графику, звуки, адреса электронной почты и многое другое. GroupDocs.Parser для Java — это очень мощный API, который позволяет разработчикам программного обеспечения анализировать документы и извлекать текст, а также метаданные из различных популярных документов в своих собственных Java-приложениях. Он включает несколько расширенных функций для извлечения текста и гиперссылок из различных типов документов, таких как PDF, электронные письма, электронные книги, форматы Microsoft Office: Word (DOC, DOCX), PowerPoint (PPT, PPTX), Excel (XLS, XLSX), форматы LibreOffice. и многое другое.

############################# content ############################
steps:
    enable: true
    block:
    - title_left: "Как извлечь гиперссылки из документов PDF"
      content_left: |
       В GroupDocs.Parser Java включены функции для извлечения гиперссылок из документов PDF. В следующем примере кода Java показано, как можно извлечь гиперссылки из документа PDF. 

      title_right: "Извлечение гиперссылок через Java"
      content_right: |
        * Создайте экземпляр [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser)
        * Проверьте, поддерживает ли документ извлечение гиперссылок
        * Извлечь гиперссылки из документа
        * Вызов метода [GetHyperlinks](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getHyperlinks()) извлекает все гиперссылки из всего документа.
        * Итерация по гиперссылкам и печать URL-адреса гиперссылки

      gisthash: "036de701f5f17a02dd2353ee547afd5b"
      gistfile: "extract_hyperlinks_form_documents.java"

    - title_left: "Как извлечь гиперссылки со страницы документов PDF"
      content_left: |
       GroupDocs.Parser .NET позволяет разработчикам программного обеспечения извлекать гиперссылки из документов PDF с помощью пары строк кода. В приведенном ниже коде C# .NET показано извлечение гиперссылок внутри документа PDF.

      title_right: "Извлечение гиперссылок через Java"
      content_right: |
        * Создайте экземпляр [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser)
        * Проверьте, поддерживает ли документ извлечение гиперссылок
        * Get document info by calling [getDocumentInfo](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getDocumentInfo()) method.
        * Перебирать страницы и печатать номер страницы
        * Извлечь гиперссылки из документа
        * Вызов метода [GetHyperlinks](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getHyperlinks()) извлекает все гиперссылки из всего документа.
        * Итерация по гиперссылкам и печать URL-адреса гиперссылки
     
      gisthash: "bcca6319f2287edb7295443c1def46ee"
      gistfile: "extract_hyperlinks_form_documents_page.java"
      
    - title_left: "Извлечение гиперссылок из PDF области страницы документов"
      content_left: |
       GroupDocs.Parser Java API обеспечивает полную поддержку извлечения гиперссылок со страницы документа PDF. В следующем коде Java показано, как программисты могут извлекать гиперссылки из области страницы документа PDF в своих собственных приложениях Java.

      title_right: "Как извлечь гиперссылки с помощью Java?"
      content_right: |
        * Создайте экземпляр [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser) 
        * Проверить документ на наличие поддержки извлечения гиперссылок
        * Создайте параметры, которые используются для извлечения гиперссылок
        * Вызов метода [GetHyperlinks](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getHyperlinks()) извлекает все гиперссылки из всего документа.
        * Итерация по гиперссылкам и печать URL-адреса гиперссылки
     
      gisthash: "4aefff1fcc6733c0fc12b736d7e36711"
      gistfile: "hyperlinks_extraction_from_document_page_area.java"

    - title_left: "Системные Требования"
      content_left: |
        GroupDocs.Parser для Java поддерживается на всех основных платформах и операционных системах. Он может создавать документы в Microsoft Word, Excel, PowerPoint, Outlook, OpenOffice и более 50 других форматах. Для получения полного руководства по системным требованиям, пожалуйста, посетите системные требования перед выполнением приведенного ниже кода. Убедитесь, что в вашей системе установлены следующие предварительные требования:
        * Операционные системы: Microsoft Windows, Linux, MacOS
        * Поддержка версий Java: J2SE 7.0 (1.7), J2SE 8.0 (1.8) или выше
        * Получите последнюю версию Java API GroupDocs.Assembly из GroupDocs [репозитория](https://repository.groupdocs.com/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs-parser)
        
      title_right: "Зачем использовать GroupDocs.Assembly"
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