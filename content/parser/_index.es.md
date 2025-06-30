---
############################# Static ############################
layout: "family"
date:  2025-06-30T10:26:00
draft: false

product: "Parser"
product_tag: "parser"

lang: es

############################# Head ############################
head_title: "Aplicaciones de análisis de documentos .NET, Java y APIs en la nube"
head_description: "Obtenga una solución integral para el análisis de documentos para aplicaciones .NET, Java y basadas en la nube. Extraiga datos de formatos de documentos en línea utilizando una sencilla función de arrastrar y soltar."

############################# Header ############################
title: "Solución de análisis de documentos"
description:  |
  API robusta para la extracción de datos de varios formatos de archivo.

  Analice documentos con un mínimo esfuerzo de codificación.

  Personalice los resultados del análisis.

############################# Supported Platforms ###############################
supported_platforms:
  enable: true
  head_title: "Elige tu plataforma"
  title: "Independencia de la plataforma"
  description: "La biblioteca GroupDocs.Parser es compatible con los siguientes sistemas operativos y marcos de trabajo:"
  details_link_title: "Aprende más"

  items:
    # items loop
    - title: ".NET"
      description: GroupDocs.Parser .NET 
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
      description: GroupDocs.Parser Java
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

############################# Features ###############################
features:
  enable: true
  title: "GroupDocs.Parser en un vistazo"
  description: "API para el análisis de datos en PDF, Word, Excel y más"

  items:
    # items loop
    - icon: "text"
      title: "Extraer texto"
      content: "Extraiga información textual de varios formatos de archivo."

    # items loop
    - icon: "image"
      title: "Extraer imágenes"
      content: "Recupere contenido visual de diversas fuentes."

    # items loop
    - icon: "template"
      title: "Analizar datos por plantillas"
      content: "Cree plantillas personalizadas y utilícelas para analizar información específica."

    # items loop
    - icon: "pdf"
      title: "Analizar formularios PDF"
      content: "Los formularios PDF son documentos digitales que presentan campos rellenables para la interacción del usuario."

############################# Code Samples ###############################
code_samples:
  enable: true
  title: "Ejemplos de código de GroupDocs.Parser"
  description: "Algunos casos de uso de operaciones típicas de GroupDocs.Parser en C# y Java"

  items:
    # items loop
    - title: "Cómo extraer texto de documentos PDF"
      content: "La API GroupDocs.Parser permite extraer texto de documentos implementando unos pocos pasos."
      samples:
          # samples loop
          - language: "C#"
            color: "blue"
            content: |
                    <code class="language-csharp" data-lang="csharp">

                        // Cree una instancia de la clase Parser pasando el archivo deseado.
                        using (var parser = new Parser("source.pdf"))
                        {
                            // Extraiga un texto.
                            using (var textReader = parser.GetText())
                            {
                                // Procese el texto extraído.
                                Console.WriteLine(textReader?.ReadToEnd());
                            }
                        }     
                        
                    </code>

          # samples loop
          - language: "Java"
            color: "red"
            content: |
                    <code class="language-java" data-lang="java">

                        // Cree una instancia de la clase Parser pasando el archivo deseado.
                        try (Parser parser = new Parser("source.pdf"))
                        {
                            // Extraiga un texto.
                            try (TextReader reader = parser.getText())
                            {
                                // Procese el texto extraído.
                                System.out.println(reader == null 
                                        ? "" 
                                        : reader.readToEnd());
                            }
                        }  

                    </code>


############################# Supported Formats ###############################
formats:
  enable: true
  title: "Más de 50 formatos de archivo compatibles"
  description: "GroupDocs.Parser permite operaciones de análisis dentro de diversas familias de formatos."

############################# Metrics ###############################
metrics:
  enable: true
  title: "Logros de GroupDocs.Parser"
  description: "Descubre las métricas clave de los logros de nuestra biblioteca."

  items:
    # items loop
    - number: "50+"
      title: "Formatos compatibles"
      content: "GroupDocs.Parser admite operaciones con más de 50 formatos de archivo populares."

    # items loop
    - number: "1600k"
      title: "Descargas de NuGet"
      content: "El paquete NuGet de GroupDocs.Parser para .NET ha sido descargado más de 1,600,000 veces."

    # items loop
    - number: "18k"
      title: "Descargas de Maven"
      content: "GroupDocs.Parser tiene 18,000 descargas en Maven. Potentes características de análisis para Java."

    # items loop
    - number: "140+"
      title: "Clientes satisfechos"
      content: "Empresas reconocidas y desarrolladores individuales prefieren los productos de GroupDocs para construir soluciones innovadoras."


############################# Customers ###############################
customers:
  enable: true
  title: "Nuestros clientes satisfechos"
  description: "Las bibliotecas de GroupDocs son utilizadas por marcas mundialmente reconocidas y distinguidas."

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
  description: "Pruebe las funciones de GroupDocs.Parser de forma gratuita en su plataforma."

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
  description: "Respuestas a las preguntas más comunes."

  items:
    # items loop
    - question: "¿La biblioteca GroupDocs.Parser necesita algún otro software de terceros para manipular documentos?"
      answer: "GroupDocs.Parser no requiere la instalación de ningún software externo como Adobe Acrobat, Microsoft Office o cualquier otro."

    # items loop
    - question: "¿Puedo probar la biblioteca GroupDocs.Parser antes de comprarla?"
      answer: "Sí, puede probar GroupDocs.Parser sin comprar una licencia. Una vez instalada sin licencia, la biblioteca funciona en modo de prueba. En este modo, se agregan insignias de prueba al documento resultante y se recorta a las primeras 3 páginas. Si desea probar GroupDocs.Parser sin las limitaciones de la versión de prueba, también puede solicitar una licencia temporal de 30 días. Para más detalles, [vea](https://purchase.groupdocs.com/temporary-license/)."

    # items loop
    - question: "¿Qué tipos de licencias tienen?"
      answer: "Ofrecemos varios tipos de licencias para satisfacer las necesidades de desarrolladores o empresas particulares. Los tipos de licencia dependen del número de desarrolladores, la cantidad de ubicaciones de desarrolladores y si necesita entregar nuestro SDK/API a sus clientes finales. Alternativamente, puede elegir licencias basadas en el uso mensual del producto. Aprenda más [aquí](https://purchase.groupdocs.com/pricing/parser/net/)."

############################# Cloud Links ###############################
cloud_links:
  enable: true
  title: "APIs de GroupDocs.Parser de bajo código"
  description: "Incorpore capacidades de análisis de documentos en cualquier aplicación utilizando nuestra API REST basada en la nube."
  
  items:
    # items loop
    - title: "GroupDocs.Parser Cloud for cURL"
      content: "Comandos cURL para la API de análisis de documentos en la nube para analizar documentos en una amplia variedad de formatos de archivo populares."
      icon: "groupdocs_parser-for-curl"
      link: "https://products.groupdocs.cloud/parser/curl"

    # items loop
    - title: "GroupDocs.Parser Cloud for .NET"
      content: "Extraiga imágenes, texto, información del documento o incluso analice cualquier documento mediante la plantilla definida por el usuario en sus aplicaciones de Microsoft .NET."
      icon: "groupdocs_parser-for-net"
      link: "https://products.groupdocs.cloud/parser/net"

    # items loop
    - title: "GroupDocs.Parser Cloud for Java"
      content: "SDK en la nube para desarrolladores de Java para analizar documentos, extraer información del documento y datos dentro de aplicaciones basadas en Java."
      icon: "groupdocs_parser-for-java"
      link: "https://products.groupdocs.cloud/parser/java"

############################# App links ###############################
app_links:
  enable: true
  title: "Aplicaciones sin código GroupDocs.Parser"
  description: "Aplicación basada en web que le permite realizar análisis a través de más de 50 formatos de archivo populares directamente en su navegador."

  items:
    # items loop
    - title: "GroupDocs.Parser Total"
      content: "Aplicación en línea gratuita para analizar tipos de documentos como Word, Excel, PowerPoint, PDF y más de 50 otros."
      icon: "groupdocs_parser-app"
      link: "https://products.groupdocs.app/parser/total"

    # items loop
    - title: "GroupDocs.Parser DOCX"
      content: "Analice documentos de Word directamente desde su navegador web para extraer imágenes, texto o metadatos."
      icon: "groupdocs_words-app"
      link: "https://products.groupdocs.app/parser/docx"

    # items loop
    - title: "GroupDocs.Parser PDF"
      content: "Aplicación de análisis de PDF gratuita que funciona en cualquier plataforma o dispositivo sin limitaciones."
      icon: "groupdocs_pdf-app"
      link: "https://products.groupdocs.app/parser/pdf"


      


---