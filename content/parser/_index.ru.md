---
############################# Static ############################
layout: "family"
date:  2024-02-13T17:01:03
draft: false

product: "Parser"
product_tag: "parser"

lang: ru

############################# Head ############################
head_title: ".NET, Java, облачные API и приложения для онлайн-анализа документов"
head_description: "Получите комплексное решение для анализа документов для .NET, Java и облачных приложений. Извлекайте данные из форматов документов онлайн с помощью простой функции перетаскивания."

############################# Header ############################
title: "Решение для анализа документов"
description: |
  Надежный API для извлечения данных из различных форматов файлов.

  Анализируйте документы с минимальными усилиями по кодированию.

  Настройте результаты анализа.

############################# Supported Platforms ###############################
supported_platforms:
  enable: true
  head_title: "Выберите свою платформу"
  title: "Поддерживаемые платформы"
  description: "Библиотека GroupDocs.Parser поддерживает следующие операционные системы и платформы:"
  details_link_title: "Узнать больше"

  items:
    # items loop
    - title: ".NET"
      description: GroupDocs.Parser для .NET 
      color: "blue"
      tag: "net"
      link: "/parser/net/"
      features_link: "https://docs.groupdocs.com/parser/net/system-requirements/"
      features:
          # features loop
          - rows: "4"
            content: |
                    .NET Framework 4.6.2 or higher
                    .NET Core 2.0 or higher
                    .NET 6.0 or higher
      
          # features loop
          - rows: "1"
            content: |
                    Windows, Linux, Mac OS
      
          # features loop
          - rows: "3"
            content: |
                    Microsoft Visual Studio
                    JetBrains Rider
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats
      

    # items loop
    - title: "Java"
      description: GroupDocs.Parser для Java
      color: "red"
      tag: "java"
      link: "/parser/java/"
      features_link: "https://docs.groupdocs.com/parser/java/system-requirements/"
      features:
          # features loop
          - rows: "4"
            content: |
                    Java 8 or higher
                    Kotlin
      
          # features loop
          - rows: "1"
            content: |
                    Windows, Linux, Mac OS
      
          # features loop
          - rows: "3"
            content: |
                    IntelliJ IDEA
                    Eclipse
                    NetBeans
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats

############################# Features ###############################
features:
  enable: true
  title: "Набор функций GroupDocs.Parser"
  description: "API для анализа данных по PDF, Word, Excel и другим."

  items:
    # items loop
    - icon: "text"
      title: "Извлечь текст"
      content: "Извлекайте текстовую информацию из файлов различных форматов."

    # items loop
    - icon: "image"
      title: "Извлечение изображений"
      content: "Извлекайте визуальный контент из различных источников."

    # items loop
    - icon: "template"
      title: "Парсить данные по шаблонам"
      content: "Создавайте собственные шаблоны и используйте их для анализа конкретной информации."

    # items loop
    - icon: "pdf"
      title: "Анализ форм PDF"
      content: "PDF Формы представляют собой цифровые документы с заполняемыми полями для взаимодействия с пользователем."

############################# Code Samples ###############################
code_samples:
  enable: true
  title: "Примеры кода GroupDocs.Parser"
  description: "Некоторые варианты использования типичных операций GroupDocs.Parser в C# и Java."

  items:
    # items loop
    - title: "Как извлечь текст из документов PDF"
      content: "GroupDocs.Parser API позволяет разработчикам C# легко извлекать текст из документов, выполнив несколько простых шагов."
      samples:
          # samples loop
          - language: "C#"
            color: "blue"
            content: |
              <pre>
              // Create an instance of Parser class
              using (var parser = new Parser(fileName))
              {
                  // Extract a text into the reader
                  using (var textReader = parser.GetText())
                  {
                      // Print a text from the document
                      Console.WriteLine(textReader?.ReadToEnd());
                  }
              }
              </pre>
          # samples loop
          - language: "Java"
            color: "red"
            content: |
              <pre>
              // Create an instance of Parser class
              try (Parser parser = new Parser(fileName)) {
                  // Extract a text into the reader
                  try (TextReader reader = parser.getText()) {
                      // Print a text from the document
                      System.out.println(reader == null 
                              ? "" 
                              : reader.readToEnd());
                  }
              }
              <pre>

############################# Supported Formats ###############################
formats:
  enable: true
  title: "Поддерживается более 50 форматов файлов"
  description: "GroupDocs.Parser позволяет выполнять операции синтаксического анализа в различных семействах форматов."

############################# Metrics ###############################
metrics:
  enable: false
  title: "Подробные показатели и статистические данные"
  description: "Изучите тщательный анализ наших ключевых показателей, предлагающий комплексные показатели и статистическую информацию о наших достижениях, влиянии и расширении."

  items:
    # items loop
    - number: "50+"
      title: "Поддерживаемые форматы"
      content: "API поддерживает более 50 наиболее широко используемых форматов файлов и документов."

    # items loop
    - number: "700k"
      title: "NuGet загрузок"
      content: "GroupDocs.Parser for .NET получил более 800 тысяч загрузок через менеджер пакетов NuGet."

    # items loop
    - number: "15k"
      title: "Загрузки Maven"
      content: "GroupDocs.Parser for Java накопил более 15 тысяч загрузок из нашего репозитория Maven."


############################# Customers ###############################
customers:
  enable: true
  title: "Наши счастливые клиенты"
  description: "Библиотеки GroupDocs используются всемирно известными и выдающимися брендами по всему миру."

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
  description: "Попробуйте функции GroupDocs.Parser бесплатно на своей платформе."

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
  description: "Ответы на наиболее часто задаваемые вопросы."

  items:
    # items loop
    - question: "Требуется ли библиотеке GroupDocs.Parser какое-либо другое стороннее программное обеспечение для управления документами?"
      answer: "GroupDocs.Parser не требует установки какого-либо внешнего программного обеспечения, например Adobe Acrobat, Microsoft Office или любого другого."

    # items loop
    - question: "Могу ли я опробовать библиотеку GroupDocs.Parser перед ее покупкой?"
      answer: "Да, вы можете попробовать GroupDocs.Parser без покупки лицензии. После установки без лицензии библиотека работает в пробном режиме. В этом режиме к полученному документу добавляются пробные значки, и он обрезается до первых трех страниц. Если вы хотите протестировать GroupDocs.Parser без ограничений пробной версии, вы также можете запросить 30-дневную временную лицензию. Более подробную информацию см. [purchase.groupdocs.com/temporary-license/](https://purchase.groupdocs.com/temporary-license/)"

    # items loop
    - question: "Какие лицензии у вас есть?"
      answer: "Мы предлагаем несколько типов лицензий, соответствующих потребностям конкретных разработчиков или компаний. Типы лицензий зависят от количества разработчиков, количества расположений сайтов разработчиков и от того, нужно ли вам доставлять наш SDK/API конечным клиентам. Альтернативно вы можете выбрать лимитные лицензии, основанные на ежемесячном использовании продукта. Узнайте больше на [purchase.groupdocs.com/policies/](https://purchase.groupdocs.com/policies/)"

############################# Cloud Links ###############################
cloud_links:
  enable: true
  title: "GroupDocs.Parser API с минимальным кодом"
  description: "Включите возможности синтаксического анализа документов в любое приложение с помощью нашего облачного API REST."
  
  items:
    # items loop
    - title: "GroupDocs.Parser Cloud for cURL"
      content: "Команды cURL для RESTfull анализатора документов Cloud API для анализа документов в широком спектре поддерживаемых популярных форматов файлов."
      icon: "groupdocs_parser-for-curl"
      link: "https://products.groupdocs.cloud/parser/curl"

    # items loop
    - title: "GroupDocs.Parser Cloud for .NET"
      content: "Извлекайте изображения, текст, информацию о документе или даже анализируйте любой документ по пользовательскому шаблону в приложениях Microsoft .NET."
      icon: "groupdocs_parser-for-net"
      link: "https://products.groupdocs.cloud/parser/net"

    # items loop
    - title: "GroupDocs.Parser Cloud for Java"
      content: "Cloud SDK для разработчиков Java для анализа документов, извлечения информации о документах и ​​данных в приложениях на основе Java."
      icon: "groupdocs_parser-for-java"
      link: "https://products.groupdocs.cloud/parser/java"

############################# App links ###############################
app_links:
  enable: true
  title: "GroupDocs.Parser NoCode-приложения"
  description: "Веб-приложение, позволяющее выполнять анализ файлов более чем 50 популярных форматов прямо в браузере."

  items:
    # items loop
    - title: "GroupDocs.Parser Total"
      content: "Бесплатное онлайн-приложение для анализа Word, Excel, PowerPoint, PDF и более 30 типов документов."
      icon: "groupdocs_parser-app"
      link: "https://products.groupdocs.app/parser/total"

    # items loop
    - title: "GroupDocs.Parser DOCX"
      content: "Анализируйте документы Word непосредственно в веб-браузере для извлечения изображений, текста или метаданных."
      icon: "groupdocs_words-app"
      link: "https://products.groupdocs.app/parser/docx"

    # items loop
    - title: "GroupDocs.Parser PDF"
      content: "Бесплатное приложение для анализа PDF, которое работает на любой платформе или устройстве без каких-либо ограничений."
      icon: "groupdocs_pdf-app"
      link: "https://products.groupdocs.app/parser/pdf"     


---