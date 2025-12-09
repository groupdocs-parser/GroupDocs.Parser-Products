---
############################# Static ############################
layout: "family"
date:  2025-12-09T14:52:35
draft: false

product: "Parser"
product_tag: "parser"

lang: es

############################# Head ############################
head_title: "SDKs de análisis de documentos para PDF, Word y Excel | GroupDocs"
head_description: "SDK de análisis de documentos para extraer texto, imágenes, metadatos, códigos de barras y tablas de PDF, Word, Excel, correos electrónicos y más de 50 formatos de documento para aplicaciones .NET, Java y Python."

############################# Header ############################
title: "SDK de análisis de documentos"
description:  |
  SDK de análisis de documentos fácil para desarrolladores que extrae texto, imágenes, códigos de barras, metadatos y tablas de más de 50 formatos de documentos e imágenes.

  Integra el análisis de documentos de alto rendimiento en tus aplicaciones .NET, Java y Python con un esfuerzo de codificación mínimo.

  Utiliza plantillas flexibles y APIs avanzadas para personalizar las reglas de análisis y ofrecer salidas de datos limpias y estructuradas.

############################# Supported Platforms ###############################
supported_platforms:
  enable: true
  head_title: "Elige tu plataforma"
  title: "Independencia de plataforma"
  description: "La biblioteca GroupDocs.Parser es compatible con los siguientes sistemas operativos y frameworks:"
  details_link_title: "Más información"

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
  title: "GroupDocs.Parser en un vistazo"
  description: "Potente SDK de análisis de documentos para extraer datos estructurados y no estructurados de PDFs, documentos de Office, imágenes, correos electrónicos y archivos."

  items:
    # items loop
    - icon: "text"
      title: "Extraer texto"
      content: "Extraer información textual de varios formatos de archivo"

    # items loop
    - icon: "image"
      title: "Extraer imágenes"
      content: "Recuperar contenido visual de diversas fuentes"

    # items loop
    - icon: "template"
      title: "Analizar datos con plantillas"
      content: "Crear plantillas personalizadas y utilizarlas para analizar información específica"

    # items loop
    - icon: "pdf"
      title: "Analizar formularios PDF"
      content: "Los formularios PDF son documentos digitales con campos rellenables para la interacción del usuario"

############################# Code Samples ###############################
code_samples:
  enable: true
  title: "GroupDocs.Parser ejemplos de código"
  description: "Algunos casos de uso típicos de operaciones de GroupDocs.Parser en C#, Java y Python"

  items:
    # items loop
    - title: "Cómo extraer texto de documentos PDF"
      content: "La API de GroupDocs.Parser facilita la extracción de texto de documentos mediante unos pocos pasos."
      samples:
          # samples loop
          - language: "C#"
            color: "blue"
            content: |
              ```csharp {style=abap}  
                // Cree una instancia de la clase Parser pasando el archivo deseado
                using (var parser = new Parser("source.pdf"))
                {
                    // Extraiga texto
                    using (var textReader = parser.GetText())
                    {
                        // Procese el texto extraído
                        Console.WriteLine(textReader?.ReadToEnd());
                    }
                }     
              ```
          # samples loop
          - language: "Java"
            color: "red"
            content: |
              ```java {style=abap}
                // Cree una instancia de la clase Parser pasando el archivo deseado
                try (Parser parser = new Parser("source.pdf"))
                {
                    // Extraiga texto
                    try (TextReader reader = parser.getText())
                    {
                        // Procese el texto extraído
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

                # Cree una instancia de la clase Parser pasando el archivo deseado
                with Parser("source.pdf") as parser:
                    # Extraiga texto
                    text = parser.get_text()

                    # Procese el texto extraído
                    print(text)
              ```
############################# Supported Formats ###############################
formats:
  enable: true
  title: "Más de 50 formatos de documentos e imágenes compatibles"
  description: "GroupDocs.Parser Document Parser SDK permite operaciones de análisis en documentos de Office, PDFs, imágenes, correos electrónicos, archivos y más."

############################# Metrics ###############################
metrics:
  enable: true
  title: "Logros de GroupDocs.Parser"
  description: "Descubra los indicadores clave de los logros de nuestra biblioteca"

  items:
    # items loop
    - number: "50+"
      title: "Formatos admitidos"
      content: "GroupDocs.Parser admite operaciones con más de 50 formatos de archivo populares."

    # items loop
    - number: "1600k"
      title: "Descargas de NuGet"
      content: "El paquete NuGet de GroupDocs.Parser para .NET se ha descargado más de 1,600,000 veces."

    # items loop
    - number: "18k"
      title: "Descargas de Maven"
      content: "GroupDocs.Parser tiene 18,000 descargas en Maven. Potentes funciones de análisis para Java."

    # items loop
    - number: "140+"
      title: "Clientes satisfechos"
      content: "Tanto empresas famosas como desarrolladores individuales prefieren los productos de GroupDocs para crear soluciones innovadoras."


############################# Customers ###############################
customers:
  enable: true
  title: "Nuestros clientes satisfechos"
  description: "Las bibliotecas de GroupDocs son utilizadas por marcas reconocidas y distinguidas a nivel mundial."

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
  description: "Respuestas a las preguntas más habituales."

  items:
    # items loop
    - question: "¿La biblioteca GroupDocs.Parser necesita algún otro software de terceros para manipular documentos?"
      answer: "GroupDocs.Parser no requiere instalar ningún software externo, como Adobe Acrobat, Microsoft Office u otro."

    # items loop
    - question: "¿Puedo probar la biblioteca GroupDocs.Parser antes de comprarla?"
      answer: "Sí, puede probar GroupDocs.Parser sin comprar una licencia. Cuando se instala sin licencia, la biblioteca funciona en modo de prueba. En este modo, se añaden insignias de prueba al documento resultante y se recorta a las primeras 3 páginas. Si desea probar GroupDocs.Parser sin las limitaciones de la versión de prueba, también puede solicitar una licencia temporal de 30 días. Para más detalles, [ver](https://purchase.groupdocs.com/temporary-license/)."

    # items loop
    - question: "¿Qué licencias ofrecen?"
      answer: "Ofrecemos varios tipos de licencias para adaptarse a las necesidades de desarrolladores o empresas específicas. Los tipos de licencia dependen del número de desarrolladores, del número de ubicaciones del sitio de desarrollo y de si necesita distribuir nuestro SDK/API a sus clientes finales. Alternativamente, puede elegir licencias por consumo basadas en el uso mensual del producto. Obtenga más información [aquí](https://purchase.groupdocs.com/pricing/parser/net/)."

############################# Cloud Links ###############################
cloud_links:
  enable: true
  title: "GroupDocs.Parser APIs de análisis de documentos de bajo código"
  description: "Incorpore capacidades de análisis de documentos en cualquier aplicación utilizando nuestra API REST y SDKs basados en la nube."
  
  items:
    # items loop
    - title: "GroupDocs.Parser Cloud for cURL"
      content: "Comandos cURL para la API Cloud de análisis de documentos RESTful que permiten analizar documentos en una amplia gama de formatos de archivo populares soportados."
      icon: "groupdocs_parser-for-curl"
      link: "https://products.groupdocs.cloud/parser/curl"

    # items loop
    - title: "GroupDocs.Parser Cloud for .NET"
      content: "Extraiga imágenes, texto, información del documento o incluso analice cualquier documento mediante una plantilla definida por el usuario en sus aplicaciones Microsoft .NET."
      icon: "groupdocs_parser-for-net"
      link: "https://products.groupdocs.cloud/parser/net"

    # items loop
    - title: "GroupDocs.Parser Cloud for Java"
      content: "SDK en la nube para desarrolladores Java que permite analizar documentos, extraer información del documento y datos dentro de aplicaciones basadas en Java."
      icon: "groupdocs_parser-for-java"
      link: "https://products.groupdocs.cloud/parser/java"

############################# App links ###############################
app_links:
  enable: true
  title: "Aplicaciones sin código GroupDocs.Parser Document Parser"
  description: "Aplicaciones web de análisis de documentos que le permiten extraer datos de más de 50 formatos de archivo populares directamente en su navegador."

  items:
    # items loop
    - title: "GroupDocs.Parser Total"
      content: "Aplicación online gratuita para analizar Word, Excel, PowerPoint, PDF y más de 50 tipos de documentos."
      icon: "groupdocs_parser-app"
      link: "https://products.groupdocs.app/parser/total"

    # items loop
    - title: "GroupDocs.Parser DOCX"
      content: "Analice documentos Word directamente desde su navegador web para extraer imágenes, texto o metadatos."
      icon: "groupdocs_words-app"
      link: "https://products.groupdocs.app/parser/docx"

    # items loop
    - title: "GroupDocs.Parser PDF"
      content: "Aplicación gratuita de análisis de PDF que funciona en cualquier plataforma o dispositivo sin limitaciones."
      icon: "groupdocs_pdf-app"
      link: "https://products.groupdocs.app/parser/pdf"


      


---