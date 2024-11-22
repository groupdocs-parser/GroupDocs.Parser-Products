---
############################# Static ############################
layout: "family"
date:  2024-02-13T17:01:03
draft: false

product: "Parser"
product_tag: "parser"

lang: es

############################# Head ############################
head_title: ".NET, Java, API en la nube y aplicaciones de análisis de documentos en línea"
head_description: "Obtenga una solución de análisis de documentos todo en uno para .NET, Java y aplicaciones basadas en la nube. Extraiga datos de formatos de documentos en línea usando la función simple de arrastrar y soltar"

############################# Header ############################
title: "Solución de análisis de documentos"
description: |
  API robusta para extracción de datos de varios formatos de archivo.

  Analice documentos con un mínimo esfuerzo de codificación.

  Personalice los resultados del análisis.

############################# Supported Platforms ###############################
supported_platforms:
  enable: true
  head_title: "Elige tu plataforma"
  title: "Independencia de plataforma"
  description: "La biblioteca GroupDocs.Parser admite los siguientes sistemas operativos y marcos:"
  details_link_title: "Aprende más"

  items:
    # items loop
    - title: ".NET"
      description: GroupDocs.Parser para .NET 
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
      description: GroupDocs.Parser para Java
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
  title: "GroupDocs.Parser de un vistazo"
  description: "API para análisis de datos en PDF, Word, Excel y más."

  items:
    # items loop
    - icon: "text"
      title: "Extraer texto"
      content: "Extraiga información textual de varios formatos de archivo."

    # items loop
    - icon: "image"
      title: "Extraer imágenes"
      content: "Recuperar contenido visual de diversas fuentes."

    # items loop
    - icon: "template"
      title: "Analizar datos por plantillas"
      content: "Cree plantillas personalizadas y utilícelas para analizar información específica."

    # items loop
    - icon: "pdf"
      title: "Analizar PDF formularios"
      content: "PDF Los formularios son documentos digitales que incluyen campos que se pueden completar para la interacción del usuario."

############################# Code Samples ###############################
code_samples:
  enable: true
  title: "GroupDocs.Parser ejemplos de código"
  description: "Algunos casos de uso de operaciones GroupDocs.Parser típicas en C# y Java."

  items:
    # items loop
    - title: "Cómo extraer texto de PDF documentos"
      content: "La API GroupDocs.Parser facilita a los desarrolladores de C# la extracción de texto de documentos mediante la implementación de unos sencillos pasos."
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
  title: "Más de 50 formatos de archivo compatibles"
  description: "GroupDocs.Parser permite operaciones del analizador dentro de varias familias de formatos."

############################# Metrics ###############################
metrics:
  enable: false
  title: "Métricas detalladas y conocimientos estadísticos"
  description: "Explore un análisis exhaustivo de nuestras cifras clave, que ofrece métricas integrales y conocimientos estadísticos sobre nuestros logros, influencia y expansión."

  items:
    # items loop
    - number: "50+"
      title: "Formatos soportados"
      content: "La API admite más de 50 de los formatos de archivos y documentos más utilizados."

    # items loop
    - number: "700k"
      title: "NuGet descargas"
      content: "GroupDocs.Parser for .NET ha recibido más de 800 000 descargas a través del administrador de paquetes NuGet."

    # items loop
    - number: "15k"
      title: "Descargas de Maven"
      content: "GroupDocs.Parser for Java ha acumulado más de 15.000 descargas desde nuestro repositorio Maven."


############################# Customers ###############################
customers:
  enable: true
  title: "Nuestros clientes felices"
  description: "GroupDocs bibliotecas son empleadas por marcas distinguidas y reconocidas a nivel mundial en todo el mundo."

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
  title: "¿Listo para comenzar?"
  description: "Pruebe GroupDocs.Parser funciones gratis en su plataforma"

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
  title: "Preguntas frecuentes"
  description: "Respuestas a las preguntas más frecuentes."

  items:
    # items loop
    - question: "¿La biblioteca GroupDocs.Parser necesita algún otro software de terceros para manipular documentos?"
      answer: "GroupDocs.Parser no requiere la instalación de ningún software externo como Adobe Acrobat, Microsoft Office o cualquier otro."

    # items loop
    - question: "¿Puedo probar la biblioteca GroupDocs.Parser antes de comprarla?"
      answer: "Sí, puedes probar GroupDocs.Parser sin comprar una licencia. Una vez instalada sin licencia, la biblioteca funciona en modo de prueba. En este modo, se agregan insignias de prueba al documento resultante y se recorta a las primeras 3 páginas. Si desea probar GroupDocs.Parser sin las limitaciones de la versión de prueba, también puede solicitar una licencia temporal de 30 días. Para más detalles, ver [purchase.groupdocs.com/temporary-license/](https://purchase.groupdocs.com/temporary-license/)"

    # items loop
    - question: "¿Qué licencias tienes?"
      answer: "Ofrecemos varios tipos de licencias para satisfacer las necesidades de desarrolladores o empresas particulares. Los tipos de licencia dependen de la cantidad de desarrolladores, la cantidad de ubicaciones de sitios de desarrolladores y si necesita entregar nuestro SDK/API a sus clientes finales. Alternativamente, puede elegir licencias medidas según el uso mensual del producto. Obtenga más información en [purchase.groupdocs.com/policies/](https://purchase.groupdocs.com/policies/)"

############################# Cloud Links ###############################
cloud_links:
  enable: true
  title: "GroupDocs.Parser API de código reducido"
  description: "Incorpore capacidades de análisis de documentos en cualquier aplicación utilizando nuestra API REST basada en la nube."
  
  items:
    # items loop
    - title: "GroupDocs.Parser Cloud for cURL"
      content: "Comandos cURL para RESTla API de nube del analizador de documentos completo para analizar documentos en una amplia gama de formatos de archivos populares admitidos."
      icon: "groupdocs_parser-for-curl"
      link: "https://products.groupdocs.cloud/parser/curl"

    # items loop
    - title: "GroupDocs.Parser Cloud for .NET"
      content: "Extraiga imágenes, texto, información de documentos o incluso analice cualquier documento mediante una plantilla definida por el usuario en sus aplicaciones de Microsoft .NET."
      icon: "groupdocs_parser-for-net"
      link: "https://products.groupdocs.cloud/parser/net"

    # items loop
    - title: "GroupDocs.Parser Cloud for Java"
      content: "SDK de nube para desarrolladores de Java para analizar documentos y extraer información y datos de documentos dentro de aplicaciones basadas en Java."
      icon: "groupdocs_parser-for-java"
      link: "https://products.groupdocs.cloud/parser/java"

############################# App links ###############################
app_links:
  enable: true
  title: "GroupDocs.Parser aplicaciones sin código"
  description: "Aplicación basada en web que le permite realizar análisis en más de 50 formatos de archivos populares directamente en su navegador."

  items:
    # items loop
    - title: "GroupDocs.Parser Total"
      content: "Aplicación en línea gratuita para analizar Word, Excel, PowerPoint, PDF y más de 30 tipos de documentos."
      icon: "groupdocs_parser-app"
      link: "https://products.groupdocs.app/parser/total"

    # items loop
    - title: "GroupDocs.Parser DOCX"
      content: "Analice Word documentos directamente desde su navegador web para extraer imágenes, texto o metadatos."
      icon: "groupdocs_words-app"
      link: "https://products.groupdocs.app/parser/docx"

    # items loop
    - title: "GroupDocs.Parser PDF"
      content: "Aplicación de análisis PDF gratuita que funciona en cualquier plataforma o dispositivo sin limitaciones."
      icon: "groupdocs_pdf-app"
      link: "https://products.groupdocs.app/parser/pdf"     


---