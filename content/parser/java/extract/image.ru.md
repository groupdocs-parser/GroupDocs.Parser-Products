---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:10
draft: false
otherformats: doc docm docx dot dotm dotx epub html mht mhtml odp ods odt one otp ott pdf

############################# Head ############################
head_title: "Как извлечь изображения из Excel, Word, PDF и других документов с помощью Java?"
head_description: "GroupDocs.Parser for Java позволяет разработчикам программного обеспечения анализировать и извлекать изображения из документов PDF, DOC, DOCX, PPT, PPTX, XLS, XLSX, области страницы и электронных писем внутри приложений Java."

############################# Header ############################
title: "Java API для анализа и извлечения изображений из Excel, Word, PowerPoint, PDF и других страниц документов"
description: "GroupDocs.Parser for Java API позволяет программистам извлекать изображения из документов PDF, DOC, DOCX, PPT, PPTX, EML, MSG, XLS, XLSX, CSV, ODT, RTF и EPUB или страниц документа внутри приложений Java."
bg_image: "https://cms.admin.containerize.com/templates/aspose/App_Themes/V3/images/bg/header1.png"
bg_overlay: false
button:
    enable: true
    icon: "fas fa-arrow-down"
    label: "Скачать бесплатную пробную версию"
    link: "https://downloads.groupdocs.com/parser/java"

############################# SubMenu ############################
submenu:
    enable: true

    left:
        img_alt: "GroupDocs.Parser for Java"
        image: "https://cms.admin.containerize.com/templates/groupdocs/images/product-logos/90x90-noborder/groupdocs-parser-java.png"
        product: "GroupDocs.Parser"
        platform: "Java"

    middle:
        button:

            # button loop
            - link: "https://apireference.groupdocs.com/parser/java"
              text: "Справочник по API"

            # button loop
            - link: "https://github.com/groupdocs-parser"
              text: "Примеры кода"

            # button loop
            - link: "https://products.groupdocs.app/parser/family"
              text: "Живые демонстрации"

            # button loop
            - link: "https://purchase.groupdocs.com/pricing/parser/java"
              text: "Цены"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/java"
        link_buy: "https://purchase.groupdocs.com"

############################# About ############################
about:
    enable: true
    title: "Узнайте, как извлекать изображения из документа или его определенной страницы с помощью Java API?"
    content: |
        Изображение стоит тысячи слов, и его нельзя игнорировать в современном визуальном мире при создании привлекательного контента. Изображения могут быть отличным источником информации, а также привлекать внимание пользователя. Часто требуется получить изображения из документов, журналов или презентаций и использовать их в другом месте. GroupDocs.Parser for Java — это мощный API, который помогает разработчикам программного обеспечения и программистам создавать решения для анализа и извлечения изображений или другой информации из многочисленных типов документов. Он также поддерживает сохранение изображений в форматах PNG, JPEG, WebP, GIF, BMP и других. API включает поддержку некоторых популярных форматов документов, таких как PDF, форматы Microsoft Office: Word (DOC, DOCX), PowerPoint (PPT, PPTX), Excel (XLS, XLSX), форматы LibreOffice, электронные письма, электронные книги и многие другие. . Он также включает поддержку некоторых расширенных функций, связанных с анализом документов, извлечением простого и структурированного текста, поиском текста по ключевым словам, извлечением метаданных или изображений, контейнеров, а также вложений и многим другим.
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: "Извлечение изображений из документов в Java"
    content_left: |
        [GroupDocs.Parser for Java](/ru/parser/java/) позволяет разработчикам Java легко извлекать изображения из документов, выполняя несколько простых шагов.
        
        * Создать объект [Parser](https://reference.groupdocs.com/java/parser/com.groupdocs.parser/Parser) для исходного документа;
        * Вызвать метод [getImages](https://reference.groupdocs.com/parser/java/com.groupdocs.parser/parser/#getImages--) и получить коллекцию объектов изображения;
        * Проверить, не является ли ридер *null* (для документа поддерживается извлечение изображений);
        * Переберите коллекцию и получите размеры, типы изображений и содержимое изображений.

    title_right: "Узнать больше про извлечение изображений"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/java/extract-images-from-document/">Как извлечь изображения из документа в Java</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-images-from-document-page/">Как извлечь изображения из страницы документа в Java</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-images-from-document-page-area/">Как извлечь изображения из области страницы документа в Java</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-images-to-files/">Как извлечь изображения из документа в файлы в Java</a>

    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="Как извлечь изображения из документов, используя пример кода Java">}}

        ```java    
        // Извлечение изображений из документов с помощью API GroupDocs.Parser
        // Создайте экземпляр класса Parser
        try (Parser parser = new Parser(Constants.SampleImagesPdf)) {
            // Извлечь изображения
            Iterable<PageImageArea> images = parser.getImages();
            // Проверьте, поддерживается ли извлечение изображений
            if (images == null) {
                System.out.println("Извлечение изображений не поддерживается");
                return;
            }
            // Перебирать изображения
            for (PageImageArea image : images) {
                // Распечатайте индекс страницы, прямоугольник и тип изображения:
                System.out.println(String.format("Page: %d, R: %s, Type: %s", image.getPage().getIndex(), image.getRectangle(), image.getFileType()));
            }
        }
        ```
     {{< /parser/code-parser >}}

############################# More ############################
more:
    enable: true
    title_left: "Системные Требования"
    content_left: |
        GroupDocs.Parser for Java API поддерживаются на всех основных платформах и операционных системах. Перед выполнением приведенного ниже кода убедитесь, что в вашей системе установлены следующие предварительные компоненты.
        
        * Операционные системы: Microsoft Windows, Linux, MacOS
        * Среды разработки: NetBeans, Intellij IDEA, Eclipse, etc.
        * Фреймворки
        * Загрузите последнюю версию GroupDocs.Parser for Java из [Maven](https://repository.groupdocs.com/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs-parser)

    title_right: "Зачем использовать GroupDocs.Parser for Java"
    content_right: |
        * Поддержка извлечения простого текста из любых поддерживаемых документов    
        * Парсинг документов по пользовательским шаблонам    
        * Полная поддержка извлечения структурированного текста    
        * Текстовый поиск по ключевому слову и регулярному выражению    
        * Извлечение форматированного текста, метаданных, изображений, контейнеров и вложений    
        * Извлечение оглавления для некоторых поддерживаемых форматов документов    
        * Парсинг данных форм из PDF-документов    
        * Извлечение гиперссылок из документа   

############################# Demos ############################
demos:
    enable: true
    title: "Живые демонстрации - извлечение изображений из документов онлайн"
    content: |
       Извлекайте изображения из документов прямо сейчас, посетив веб-сайт [GroupDocs.Parser Live Demos](https://products.groupdocs.app/parser/images/).
       Живая демонстрация имеет следующие преимущества.
        
############################# About Formats ############################
about_formats:
    enable: true

############################# More Formats ############################
more_formats:
    enable: true
    title: "Извлечение изображений из других форматов документов"
    content: |
        Java API анализа документов и извлечения изображений для форматов файлов и изображений. Извлеките данные для некоторых популярных форматов файлов, как указано ниже.

############################# Back to top ###############################
back_to_top:
    enable: true
---