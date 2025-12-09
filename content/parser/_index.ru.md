---
############################# Static ############################
layout: "family"
date:  2025-12-09T14:52:35
draft: false

product: "Parser"
product_tag: "parser"

lang: ru

############################# Head ############################
head_title: "SDK для парсинга документов PDF, Word и Excel | GroupDocs"
head_description: "SDK для парсинга документов, позволяющий извлекать текст, изображения, метаданные, штрихкоды и таблицы из PDF, Word, Excel, электронных писем и более чем 50 других форматов документов для приложений на .NET, Java и Python."

############################# Header ############################
title: "SDK парсинга документов"
description:  |
  Удобный для разработчиков SDK парсинга документов для извлечения текста, изображений, штрихкодов, метаданных и таблиц из более чем 50 форматов документов и изображений.

  Интегрируйте высокопроизводительный парсинг документов в свои приложения на .NET, Java и Python с минимальными усилиями по написанию кода.

  Используйте гибкие шаблоны и расширенные API для настройки правил парсинга и получения чистых, структурированных данных.

############################# Supported Platforms ###############################
supported_platforms:
  enable: true
  head_title: "Выберите платформу"
  title: "Независимость от платформы"
  description: "Библиотека GroupDocs.Parser поддерживает следующие операционные системы и фреймворки:"
  details_link_title: "Узнать больше"

  items:
    # items loop
    - title: ".NET"
      description: GroupDocs.Parser for .NET 
      color: "blue"
      tag: "net"
      link: "/parser/net/"
      features_link: "https://docs.groupdocs.com/parser/net/system-requirements/"
      features:
          # features loop
          - rows: "3"
            content: |
                    .NET Framework 4.6.2 or higher <br> .NET Core 2.0 or higher <br> .NET 6.0 or higher
      
          # features loop
          - rows: "1"
            content: |
                    Windows <br> Linux <br> Mac OS
      
          # features loop
          - rows: "4"
            content: |
                    Microsoft Visual Studio <br> JetBrains Rider <br> Microsoft Visual Code
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats
      

    # items loop
    - title: "Java"
      description: GroupDocs.Parser for Java
      color: "red"
      tag: "java"
      link: "/parser/java/"
      features_link: "https://docs.groupdocs.com/parser/java/system-requirements/"
      features:
          # features loop
          - rows: "3"
            content: |
                    Java 8 or higher <br> Kotlin
      
          # features loop
          - rows: "1"
            content: |
                    Windows <br> Linux <br> Mac OS
      
          # features loop
          - rows: "4"
            content: |
                    IntelliJ IDEA <br> Eclipse <br> NetBeans
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats


    # items loop
    - title: "Python"
      description: GroupDocs.Parser for Python
      color: "yellow"
      tag: "python-net"
      link: "/parser/python-net/"
      features_link: "https://docs.groupdocs.com/parser/python-net/system-requirements/"
      features:
          # features loop
          - rows: "3"
            content: |
                    Python 3.5+
      
          # features loop
          - rows: "1"
            content: |
                    Windows <br> Linux <br> macOS
      
          # features loop
          - rows: "4"
            content: |
                    PyCharm, VS Code, Jupyter Notebook
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats                    

############################# Features ###############################
features:
  enable: true
  title: "GroupDocs.Parser в двух словах"
  description: "Мощный SDK парсинга документов для извлечения структурированных и неструктурированных данных из PDF, офисных документов, изображений, электронных писем и архивов."

  items:
    # items loop
    - icon: "text"
      title: "Извлечение текста"
      content: "Извлечение текстовой информации из различных форматов файлов"

    # items loop
    - icon: "image"
      title: "Извлечение изображений"
      content: "Получение визуального контента из различных источников"

    # items loop
    - icon: "template"
      title: "Парсинг данных по шаблонам"
      content: "Создавайте пользовательские шаблоны и используйте их для парсинга конкретной информации"

    # items loop
    - icon: "pdf"
      title: "Парсинг PDF‑форм"
      content: "PDF‑формы — это цифровые документы с заполняемыми полями для взаимодействия пользователя"

############################# Code Samples ###############################
code_samples:
  enable: true
  title: "GroupDocs.Parser примеры кода"
  description: "Некоторые примеры типовых операций GroupDocs.Parser на C#, Java и Python"

  items:
    # items loop
    - title: "Как извлечь текст из PDF‑документов"
      content: "GroupDocs.Parser API упрощает извлечение текста из документов, выполнив несколько шагов."
      samples:
          # samples loop
          - language: "C#"
            color: "blue"
            content: |
              ```csharp {style=abap}  
                // Создайте экземпляр класса Parser, передав нужный файл
                using (var parser = new Parser("source.pdf"))
                {
                    // Извлеките текст
                    using (var textReader = parser.GetText())
                    {
                        // Обработайте извлечённый текст
                        Console.WriteLine(textReader?.ReadToEnd());
                    }
                }     
              ```
          # samples loop
          - language: "Java"
            color: "red"
            content: |
              ```java {style=abap}
                // Создайте экземпляр класса Parser, передав нужный файл
                try (Parser parser = new Parser("source.pdf"))
                {
                    // Извлеките текст
                    try (TextReader reader = parser.getText())
                    {
                        // Обработайте извлечённый текст
                        System.out.println(reader == null 
                                ? "" 
                                : reader.readToEnd());
                    }
                }  
              ```
          # samples loop
          - language: "Python"
            color: "green"
            content: |
              ```python {style=abap}
                from groupdocs.parser import Parser

                # Создайте экземпляр класса Parser, передав нужный файл
                with Parser("source.pdf") as parser:
                    # Извлеките текст
                    text = parser.get_text()

                    # Обработайте извлечённый текст
                    print(text)
              ```
############################# Supported Formats ###############################
formats:
  enable: true
  title: "Поддерживается более 50 форматов документов и изображений"
  description: "SDK парсинга документов GroupDocs.Parser позволяет выполнять операции парсинга для офисных документов, PDF, изображений, электронных писем, архивов и многого другого."

############################# Metrics ###############################
metrics:
  enable: true
  title: "Достижения GroupDocs.Parser"
  description: "Узнайте ключевые показатели достижений нашей библиотеки"

  items:
    # items loop
    - number: "50+"
      title: "Поддерживаемые форматы"
      content: "GroupDocs.Parser поддерживает работу более чем с 50 популярными форматами файлов."

    # items loop
    - number: "1600k"
      title: "Скачивания NuGet"
      content: "Пакет GroupDocs.Parser для .NET в NuGet был загружен более 1 600 000 раз."

    # items loop
    - number: "18k"
      title: "Скачивания Maven"
      content: "GroupDocs.Parser имеет 18 000 загрузок в Maven. Мощные функции парсинга для Java."

    # items loop
    - number: "140+"
      title: "Довольные клиенты"
      content: "Известные компании и отдельные разработчики предпочитают продукты GroupDocs для создания инновационных решений."


############################# Customers ###############################
customers:
  enable: true
  title: "Наши довольные клиенты"
  description: "GroupDocs библиотеки используют всемирно известные и выдающиеся бренды по всему миру."

  items:
    # items loop
    - title: "BenQ Corporation"
      logo: "benq"
      
    # items loop
    - title: "Nasdaq Stock Market"
      logo: "nasdaq"
      
    # items loop
    - title: "AT&T Inc."
      logo: "att"
      
    # items loop
    - title: "Customer logo AstraZeneca"
      logo: "astrazeneca"
      
    # items loop
    - title: "Central Bank of Argentina"
      logo: "argentinacentralbank"
      
    # items loop
    - title: "Roche Holding AG"
      logo: "roche"
      
    # items loop
    - title: "Capita"
      logo: "capita"
      
    # items loop
    - title: "Axa S.A."
      logo: "axa"
      
    # items loop
    - title: "Instructure Inc."
      logo: "instructure"
      
    # items loop
    - title: "Wipro"
      logo: "wipro"


############################# Actions ###############################
actions:
  enable: true
  title: "Готовы начать?"
  description: "Попробуйте функции GroupDocs.Parser бесплатно на вашей платформе"

  items:
    # items loop
    - title: ".NET"
      color: "blue"
      link: "/parser/net/"

    # items loop
    - title: "Java"
      color: "red"
      link: "/parser/java/"

############################# FAQ ###############################
faq:
  enable: true
  title: "Часто задаваемые вопросы"
  description: "Ответы на самые часто задаваемые вопросы."

  items:
    # items loop
    - question: "Требует ли библиотека GroupDocs.Parser какого-либо стороннего программного обеспечения для работы с документами?"
      answer: "GroupDocs.Parser не требует установки какого-либо внешнего программного обеспечения, такого как Adobe Acrobat, Microsoft Office или другое."

    # items loop
    - question: "Могу ли я попробовать библиотеку GroupDocs.Parser перед её покупкой?"
      answer: "Да, вы можете попробовать GroupDocs.Parser без покупки лицензии. При установке без лицензии библиотека работает в режиме пробной версии. В этом режиме к полученному документу добавляются ярлыки trial, и он ограничивается первыми 3 страницами. Если вы хотите протестировать GroupDocs.Parser без ограничений пробной версии, вы также можете запросить 30‑дневную временную лицензию. Подробнее см. [см.](https://purchase.groupdocs.com/temporary-license/)."

    # items loop
    - question: "Какие лицензии вы предлагаете?"
      answer: "Мы предлагаем несколько типов лицензий, соответствующих потребностям конкретных разработчиков или компаний. Типы лицензий зависят от количества разработчиков, количества площадок разработчиков и того, нужно ли предоставлять наш SDK/API конечным клиентам. Кроме того, вы можете выбрать лицензии с оплатой за использование (Metered), основанные на месячном потреблении продукта. Подробнее [здесь](https://purchase.groupdocs.com/pricing/parser/net/)."

############################# Cloud Links ###############################
cloud_links:
  enable: true
  title: "GroupDocs.Parser API парсера документов low‑code"
  description: "Интегрируйте возможности парсинга документов в любое приложение с помощью нашего облачного REST API и SDK."
  
  items:
    # items loop
    - title: "GroupDocs.Parser Cloud for cURL"
      content: "cURL‑команды для RESTful Cloud API парсера документов, позволяющие парсить документы из широкого спектра поддерживаемых популярных файловых форматов."
      icon: "groupdocs_parser-for-curl"
      link: "https://products.groupdocs.cloud/parser/curl"

    # items loop
    - title: "GroupDocs.Parser Cloud for .NET"
      content: "Извлекайте изображения, текст, сведения о документе или даже парсите любой документ по пользовательскому шаблону в ваших приложениях Microsoft .NET."
      icon: "groupdocs_parser-for-net"
      link: "https://products.groupdocs.cloud/parser/net"

    # items loop
    - title: "GroupDocs.Parser Cloud for Java"
      content: "Облачный SDK для разработчиков Java, позволяющий парсить документы, извлекать информацию о документе и данные в Java‑приложениях."
      icon: "groupdocs_parser-for-java"
      link: "https://products.groupdocs.cloud/parser/java"

############################# App links ###############################
app_links:
  enable: true
  title: "GroupDocs.Parser Приложения парсера документов без кода"
  description: "Веб‑приложения парсера документов, позволяющие извлекать данные из более чем 50 популярных файловых форматов прямо в браузере."

  items:
    # items loop
    - title: "GroupDocs.Parser Total"
      content: "Бесплатное онлайн‑приложение для парсинга Word, Excel, PowerPoint, PDF и более 50 других типов документов."
      icon: "groupdocs_parser-app"
      link: "https://products.groupdocs.app/parser/total"

    # items loop
    - title: "GroupDocs.Parser DOCX"
      content: "Парсите документы Word напрямую из веб‑браузера, чтобы извлекать изображения, текст или метаданные."
      icon: "groupdocs_words-app"
      link: "https://products.groupdocs.app/parser/docx"

    # items loop
    - title: "GroupDocs.Parser PDF"
      content: "Бесплатное приложение для парсинга PDF, работающее на любой платформе или устройстве без ограничений."
      icon: "groupdocs_pdf-app"
      link: "https://products.groupdocs.app/parser/pdf"


      


---