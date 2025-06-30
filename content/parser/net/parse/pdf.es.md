


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:53
draft: false
lang: es
format: Pdf
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "Analizar datos de archivos PDF en aplicaciones C#"
head_description: "Utiliza GroupDocs.Parser para extraer texto, imágenes, tablas y otros datos de archivos PDF en C# sin depender de herramientas de terceros."

############################# Header ############################
title: "Analiza documentos PDF con C#" 
description: "Extrae de manera eficiente texto, metadatos, tablas e imágenes de archivos PDF, Word, Excel e imagen utilizando GroupDocs.Parser en tus proyectos de .NET."
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Descargar prueba gratuita"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "Acerca de la API GroupDocs.Parser for .NET"
    link: "/parser/net/"
    link_title: "Aprender más"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/) es una API de análisis de documentos rica en características, diseñada para desarrolladores de .NET. Soporta la extracción de texto plano y estructurado, metadatos, imágenes, tablas y códigos de barras de formatos populares como PDF, DOCX, XLSX, PPTX, y más, sin dependencias de software adicionales.

############################# Steps ############################
steps:
    enable: true
    title: "Pasos para extraer datos de Pdf en C#"
    content: |
      Sigue estos pasos para analizar contenido de documentos PDF en tus aplicaciones .NET utilizando [GroupDocs.Parser](/parser/net/):
      
      1. Carga el documento PDF utilizando una instancia de Parser.
      2. Extrae el contenido deseado, como texto, tablas o metadatos.
      3. Verifica que los datos extraídos sean válidos.
      4. Utiliza la salida analizada en tus procesos, automatización o sistemas de negocio.
   
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
        // Carga tu documento en Parser
        using (Parser parser = new Parser("input.pdf")) {

            // Extrae todo el contenido de texto del archivo
            using (TextReader reader = parser.GetText()) 
            {
                // Si el texto no está disponible, el resultado será nulo
                // Utiliza el texto extraído en tu aplicación
                Console.WriteLine(reader == null ? 
                    "La extracción de texto no es compatible con este formato" : reader.ReadToEnd());
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "Capacidades completas de análisis de documentos"
  description: "GroupDocs.Parser permite más que solo lectura de texto — soporta extracción de códigos de barras, análisis de imágenes, acceso a metadatos y procesamiento de datos estructurados para automatización avanzada y análisis de datos."
  image: "/img/parser/features_parse.webp" # 500x500 px
  image_description: "Extracción de contenido y capacidades de análisis de documentos"
  features:
    # feature loop
    - title: "Soporte para diversos tipos de contenido de archivos"
      content: "Extrae datos incluyendo texto, imágenes, tablas y campos de formatos de documentos como PDF, Word, Excel, HTML y más."

    # feature loop
    - title: "Trabaja con archivos escaneados y digitales"
      content: "Analiza datos tanto de documentos escaneados como de archivos digitales nativos, con soporte para OCR y extracción consciente del diseño."

    # feature loop
    - title: "Parámetros de extracción configurables"
      content: "Ajusta la lógica de análisis con opciones flexibles como selección de rango de páginas, orientación de regiones y plantillas de detección de campos."
      
  code_samples:
    # code sample loop
    - title: "Cómo analizar PDF utilizando plantillas"
      content: |
        Este ejemplo muestra cómo extraer datos estructurados de un PDF utilizando una plantilla de análisis predefinida con GroupDocs.Parser.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Carga el archivo PDF con la clase Parser
        using (Parser parser = new Parser("input.pdf"))
        {
            // Analiza el documento según la plantilla
            DocumentData data = parser.ParseByTemplate(GetTemplate());

            // Verifica si la extracción de formulario es compatible
            if (data == null)
            {
                return;
            }

            // Procesa los campos obtenidos
            for (int i = 0; i < data.Count; i++)
            {
                Console.Write(data[i].Name + ": ");
                PageTextArea area = data[i].PageArea as PageTextArea;
                Console.WriteLine(area == null ? "Not a template field" : area.Text);
            }
        }

        private static Template GetTemplate()
        {
            // Crea parámetros de detector para la tabla 'Detalles'
            TemplateTableParameters detailsTableParameters = 
                new TemplateTableParameters(new Rectangle(new Point(35, 320), new Size(530, 55)), null);

            TemplateItem[] templateItems = new TemplateItem[]
            {
                new TemplateTable(detailsTableParameters, "details", null)
            };

            Template template = new Template(templateItems);
            return template;
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
    title: "Formatos compatibles para la extracción de datos"
    exclude: "PDF"
    description: "GroupDocs.Parser permite el análisis de un amplio conjunto de formatos de documentos e imágenes. Explora los tipos de archivos soportados comúnmente utilizados en flujos de trabajo de extracción de datos."
    items: 
        # format loop 1
        - name: "Analizar PDF"
          format: "PDF"
          link: "/parser/net/parse/pdf/"
          description: "(Formato de documento portátil)"
          
        # format loop 2
        - name: "Analizar DOCX"
          format: "DOCX"
          link: "/parser/net/parse/docx/"
          description: "(Documento Word 2007+)"
          
        # format loop 3
        - name: "Analizar PPTX"
          format: "PPTX"
          link: "/parser/net/parse/pptx/"
          description: "(Formato de presentación Open XML)"
          
        # format loop 4
        - name: "Analizar XLSX"
          format: "XLSX"
          link: "/parser/net/parse/xlsx/"
          description: "(Libro de trabajo Open XML)"
          
        # format loop 5
        - name: "Analizar TXT"
          format: "TXT"
          link: "/parser/net/parse/txt/"
          description: "(Archivo de texto)"
          
        # format loop 6
        - name: "Analizar RTF"
          format: "RTF"
          link: "/parser/net/parse/rtf/"
          description: "(Formato de texto enriquecido)"
          
        # format loop 7
        - name: "Analizar XML"
          format: "XML"
          link: "/parser/net/parse/xml/"
          description: "(Lenguaje de marcado extensible)"
          
        # format loop 8
        - name: "Analizar EPUB"
          format: "EPUB"
          link: "/parser/net/parse/epub/"
          description: "(Archivo de eBook abierto)"
         
          

---