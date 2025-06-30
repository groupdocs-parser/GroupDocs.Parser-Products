


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:26
draft: false
lang: es
format: Pptx
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "Extraer hipervínculos de archivos PPTX en aplicaciones C#"
head_description: "Utiliza GroupDocs.Parser para detectar y extraer hipervínculos de archivos PPTX en C# sin herramientas o software adicionales."

############################# Header ############################
title: "Extraer hipervínculos de PPTX utilizando C#" 
description: "Detecta y extrae URLs e hipervínculos de PDF, Word, Excel y otros tipos de documentos utilizando GroupDocs.Parser en tus aplicaciones .NET."
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Descargar Prueba Gratuita"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "Acerca de la API GroupDocs.Parser for .NET"
    link: "/parser/net/"
    link_title: "Aprender más"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/) es una API versátil de análisis de documentos para desarrolladores de .NET. Permite extraer hipervínculos, texto, imágenes y contenido estructurado de diversos formatos de archivo como PDF, Word, Excel, HTML y más, sin depender de software externo.

############################# Steps ############################
steps:
    enable: true
    title: "Pasos para extraer hipervínculos de Pptx en C#"
    content: |
      [GroupDocs.Parser](/parser/net/) permite a los desarrolladores de .NET extraer hipervínculos de archivos PPTX siguiendo estos simples pasos:
      
      1. Carga el archivo PPTX utilizando una instancia de Parser.
      2. Verifica si el documento soporta la extracción de hipervínculos.
      3. Recupera la lista de hipervínculos del documento.
      4. Recorre los resultados y trabaja con las URLs extraídas.
   
    code:
      platform: "net"
      copy_title: "Copiar"
      install:
        command: |
        command: "dotnet add package GroupDocs.Parser"
        copy_tip: "haga clic para copiar"
        copy_done: "copiado"
      links:
        #  loop
        - title: "Más ejemplos"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
        #  loop
        - title: "Documentación"
          link: "https://docs.groupdocs.com/parser/net/"
          
      content: |
        ```csharp {style=abap}
        // Carga el documento que contiene hipervínculos utilizando la clase Parser
        using (Parser parser = new Parser("input.pptx")) {

            // Verifica que el archivo soporte extracción de hipervínculos
            if (!parser.Features.Hyperlinks)
            {
                Console.WriteLine("La extracción de hipervínculos no está disponible para el archivo");
                return;
            }

            // Recupera y procesa los hipervínculos extraídos
            IEnumerable<PageHyperlinkArea> hyperlinks = parser.GetHyperlinks();

            foreach (PageHyperlinkArea h in hyperlinks)
            {
                Console.WriteLine(h.Text);
                Console.WriteLine(h.Url);
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "Capacidades avanzadas de análisis de documentos"
  description: "Además de la extracción de hipervínculos, GroupDocs.Parser te permite extraer texto, metadatos, imágenes y datos estructurados, apoyando flujos de trabajo de procesamiento de datos potentes."
  image: "/img/parser/features_extract-hyperlink.webp" # 500x500 px
  image_description: "Detección de hipervínculos y análisis de documentos"
  features:
    # feature loop
    - title: "Detección de hipervínculos de documentos"
      content: "Extrae rápidamente URLs y anotaciones de enlace de documentos como PDFs, archivos de Word, hojas de cálculo y más."

    # feature loop
    - title: "Soporte para enlaces web y embebidos"
      content: "Detecta y extrae tanto URLs web estándar como enlaces embebidos en múltiples formatos."

    # feature loop
    - title: "Opciones de análisis flexibles"
      content: "Personaliza las configuraciones de extracción para escanear secciones o páginas específicas para mejorar el rendimiento y la precisión."
      
  code_samples:
    # code sample loop
    - title: "Cómo extraer hipervínculos de un PDF utilizando opciones de enlace"
      content: |
        Este ejemplo de código muestra cómo extraer todos los hipervínculos de un archivo PDF utilizando opciones personalizadas.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Inicializa el Parser con el documento PDF
        using (Parser parser = new Parser("input.docx"))
        {
            // Verifica si se soporta la extracción de hipervínculos
            if (!parser.Features.Hyperlinks)
            {
                return;
            }

            // Establece opciones de extracción de enlaces para restringir resultados
            PageAreaOptions options = new PageAreaOptions(new Rectangle(new Point(380, 90), new Size(150, 50)));

            // Extrae datos de hipervínculos del documento
            IEnumerable<PageHyperlinkArea> hyperlinks = parser.GetHyperlinks(options);

            // Gestiona la lista de enlaces extraídos
            foreach (PageHyperlinkArea h in hyperlinks)
            {
                Console.WriteLine(h.Text);
                Console.WriteLine(h.Url);
            }
        }
        ```
        {{< /landing/code >}}


############################# Actions ############################

actions:
  enable: true
  title: "¿Listo para comenzar?"
  description: "Pruebe las características de GroupDocs.Parser gratis o solicite una licencia"
  items:
    #  loop
    - title: "Descarga de Nuget"
      link: "https://releases.groupdocs.com/parser/net/"
      color: "red"
        #  loop
    - title: "Licenciamiento"
      link: "https://purchase.groupdocs.com/pricing/parser/net/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "Formatos compatibles para extracción de hipervínculos"
    exclude: "PPTX"
    description: "GroupDocs.Parser puede extraer hipervínculos de una amplia variedad de tipos de documentos. Consulta a continuación los formatos comúnmente compatibles."
    items: 
        # format loop 1
        - name: "Analizar PDF"
          format: "PDF"
          link: "/parser/net/extract-hyperlink/pdf/"
          description: "(Formato de documento portátil)"
          
        # format loop 2
        - name: "Analizar DOCX"
          format: "DOCX"
          link: "/parser/net/extract-hyperlink/docx/"
          description: "(Documento Word 2007+)"
          
        # format loop 3
        - name: "Analizar PPTX"
          format: "PPTX"
          link: "/parser/net/extract-hyperlink/pptx/"
          description: "(Formato de presentación Open XML)"
          
        # format loop 4
        - name: "Analizar XLSX"
          format: "XLSX"
          link: "/parser/net/extract-hyperlink/xlsx/"
          description: "(Libro de trabajo Open XML)"
          
        # format loop 5
        - name: "Analizar TXT"
          format: "TXT"
          link: "/parser/net/extract-hyperlink/txt/"
          description: "(Archivo de texto)"
          
        # format loop 6
        - name: "Analizar RTF"
          format: "RTF"
          link: "/parser/net/extract-hyperlink/rtf/"
          description: "(Formato de texto enriquecido)"
          
        # format loop 7
        - name: "Analizar XML"
          format: "XML"
          link: "/parser/net/extract-hyperlink/xml/"
          description: "(Lenguaje de marcado extensible)"
          
        # format loop 8
        - name: "Analizar EPUB"
          format: "EPUB"
          link: "/parser/net/extract-hyperlink/epub/"
          description: "(Archivo de eBook abierto)"
         
          

---