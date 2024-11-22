---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:10
draft: false
otherformats: doc docm docx dot dotm dotx epub html mht mhtml odp ods odt one otp ott pdf

############################# Head ############################
head_title: "Извлечение изображений из Excel, Word, PDF и других документов или страниц через C#"
head_description: "GroupDocs.Parser for .NET API позволяет программистам извлекать изображения из различных документов, таких как MS Excel, Word, PowerPoint, PDF и других, в свои приложения .NET."

############################# Header ############################
title: "Извлечение изображений из документов и страниц PDF, DOCX, PPTX, MSG, XLSX через C# .NET API"
description: "GroupDocs.Parser for .NET API позволяет программистам извлекать изображения из документов PDF, DOC, DOCX, PPT, PPTX, EML, MSG, XLS, XLSX, CSV, ODT, RTF и EPUB или страниц документа."
bg_image: "https://cms.admin.containerize.com/templates/aspose/App_Themes/V3/images/bg/header1.png"
bg_overlay: false
button:
    enable: true
    icon: "fas fa-arrow-down"
    label: "Скачать бесплатную пробную версию"
    link: "https://downloads.groupdocs.com/parser/net"

############################# SubMenu ############################
submenu:
    enable: true

    left:
        img_alt: "GroupDocs.Parser for .NET"
        image: "https://cms.admin.containerize.com/templates/groupdocs/images/product-logos/90x90-noborder/groupdocs-parser-net.png"
        product: "GroupDocs.Parser"
        platform: ".NET"

    middle:
        button:

            # button loop
            - link: "https://apireference.groupdocs.com/parser/net"
              text: "Справочник по API"

            # button loop
            - link: "https://github.com/groupdocs-parser"
              text: "Примеры кода"

            # button loop
            - link: "https://products.groupdocs.app/parser/family"
              text: "Живые демонстрации"

            # button loop
            - link: "https://purchase.groupdocs.com/pricing/parser/net"
              text: "Цены"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/net"
        link_buy: "https://purchase.groupdocs.com"

############################# About ############################
about:
    enable: true
    title: "Как извлечь изображения из документа, страницы или области страницы через .NET?"
    content: |
        Изображения могут использоваться для передачи информации таким образом, который не может быть выражен словами. Изображения помогают нам привлечь внимание пользователя и с легкостью объясняют сложные концепции. Иногда, читая документы, журналы или извлекая пользу из презентаций, мы часто находили интересные изображения и хотели их скачать. GroupDocs.Parser for .NET — это мощный API, который помогает пользователям разрабатывать полезные приложения для извлечения изображений из различных типов документов и сохранения их в форматах PNG, JPEG, WebP, GIF, BMP и других. API поддерживает извлечение текста и изображений из некоторых наиболее часто используемых форматов файлов, таких как PDF, электронные письма, электронные книги, форматы Microsoft Office: Word (DOC, DOCX), PowerPoint (PPT, PPTX), Excel (XLS). , XLSX), форматы LibreOffice и многие другие. API также полностью поддерживает синтаксический анализ документов, извлечение простого и структурированного текста, поиск текста по ключевым словам, извлечение метаданных или изображений, контейнеров, а также вложений и многое другое.
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: "Извлечение изображений из документов в .NET"
    content_left: |
        [GroupDocs.Parser for .NET](/ru/parser/net/) позволяет разработчикам C# легко извлекать изображения из документов, выполняя несколько простых шагов.
        
        * Создать объект [Parser](https://reference.groupdocs.com/net/parser/groupdocs.parser/parser) для исходного документа;
        * Вызвать метод [GetImages](https://reference.groupdocs.com/net/parser/groupdocs.parser/parser/methods/getimages) и получить коллекцию объектов изображения;
        * Проверить, не является ли ридер *null* (для документа поддерживается извлечение изображений);
        * Переберите коллекцию и получите размеры, типы изображений и содержимое изображений.

    title_right: "Узнать больше про извлечение изображений"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/net/extract-images-from-document/">Как извлечь изображения из документа в C#</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-images-from-document-page/">Как извлечь изображения из страницы документа в C#</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-images-from-document-page-area/">Как извлечь изображения из области страницы документа в C#</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-images-to-files/">Как извлечь изображения из документа в файлы в C#</a>

    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="Как извлечь изображения из документов, используя пример кода C#">}}

        ```csharp    
        // Извлечение изображений из документов с помощью API GroupDocs.Parser
        // Создайте экземпляр класса Parser
        using (Parser parser = new Parser(filePath)) {
            // Извлечь изображения
            IEnumerable<PageImageArea> images = parser.GetImages();
            // Проверьте, поддерживается ли извлечение изображений
            if (images == null) {
                Console.WriteLine("Извлечение изображений не поддерживается");
                return;
            }
            // Перебирать изображения
            foreach (PageImageArea image in images) {
                // Распечатайте индекс страницы, прямоугольник и тип изображения:
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Type: {2}", image.Page.Index, image.Rectangle, image.FileType));
            }
        }
        ```
     {{< /parser/code-parser >}}

############################# More ############################
more:
    enable: true
    title_left: "Системные Требования"
    content_left: |
        GroupDocs.Parser for .NET API поддерживаются на всех основных платформах и операционных системах. Перед выполнением приведенного ниже кода убедитесь, что в вашей системе установлены следующие предварительные компоненты.
        
        * Операционные системы: Microsoft Windows, Linux, MacOS
        * Среды разработки: Microsoft Visual Studio, Xamarin, MonoDevelop
        * Фреймворки
        * Загрузите последнюю версию GroupDocs.Parser for .NET из [Nuget](https://www.nuget.org/packages/groupdocs.parser)

    title_right: "Зачем использовать GroupDocs.Parser for .NET"
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
        .NET API анализа документов и извлечения изображений для форматов файлов и изображений. Извлеките данные для некоторых популярных форматов файлов, как указано ниже.

############################# Back to top ###############################
back_to_top:
    enable: true
---