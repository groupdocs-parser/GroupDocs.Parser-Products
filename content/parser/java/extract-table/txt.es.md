


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:38
draft: false
lang: es
format: Txt
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Recuperar tablas de documentos TXT en aplicaciones Java"
head_description: "Extraiga datos tabulares estructurados de archivos TXT en aplicaciones Java utilizando GroupDocs.Parser—sin necesidad de herramientas externas."

############################# Header ############################
title: "Recuperar datos de tablas de TXT usando Java" 
description: "Detecte y extraiga sin esfuerzo tablas de formatos como PDF, DOCX y XLSX con GroupDocs.Parser en sus flujos de trabajo Java."
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Descargar Prueba Gratuita"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "Introducción a la API de GroupDocs.Parser for Java"
    link: "/parser/java/"
    link_title: "Aprender más"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) es una API de extracción de contenido rica en funciones para plataformas Java. Permite a los desarrolladores analizar con precisión tablas, texto, gráficos, enlaces y datos estructurados de PDFs, documentos de Word, hojas de Excel, presentaciones de PowerPoint y más—sin requerir complementos de terceros.

############################# Steps ############################
steps:
    enable: true
    title: "Cómo recuperar tablas de Txt en Java"
    content: |
      Para analizar tablas de documentos TXT utilizando [GroupDocs.Parser](/parser/java/), siga estos pasos en su entorno Java:
      
      1. Cree una instancia de Parser y cargue el archivo objetivo TXT.
      2. Verifique que el archivo sea compatible con la extracción estructurada de tablas.
      3. Utilice la API para recuperar elementos de tabla del documento.
      4. Aproveche los datos extraídos en sistemas de análisis, informes o automatización.
   
    code:
      platform: "net"
      copy_title: "Copiar"
      install:
        command: |
          <dependencies>
            <dependency>
              <groupId>com.groupdocs</groupId>
              <artifactId>groupdocs-parser</artifactId>
              <version>{0}</version>
            </dependency>
          </dependencies>

          <repositories>
            <repository>
              <id>repository.groupdocs.com</id>
              <name>GroupDocs Repository</name>
              <url>https://repository.groupdocs.com/repo/</url>
            </repository>
          </repositories>
        copy_tip: "haga clic para copiar"
        copy_done: "copiado"
      links:
        #  loop
        - title: "Más ejemplos"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java/"
        #  loop
        - title: "Documentación"
          link: "https://docs.groupdocs.com/parser/java/"
          
      content: |
        ```java {style=abap}
        // Cargue el documento de entrada con Parser que incluye elementos de tabla
        try (Parser parser = new Parser("input.txt"))
        {
            // Verifique que el tipo de documento permita el reconocimiento de tablas
            if (!parser.getFeatures().isTables()) {
                System.out.println("Agregue lógica para archivos que no admiten tablas");
                return;
            }

            // Defina reglas para interpretar la estructura de la tabla
            TemplateTableLayout layout = new TemplateTableLayout(
                    java.util.Arrays.asList(new Double[]{50.0, 95.0, 275.0, 415.0, 485.0, 545.0}),
                    java.util.Arrays.asList(new Double[]{325.0, 340.0, 365.0, 395.0}));

            // Establezca parámetros para extraer tablas
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            //  Ejecute la extracción de tablas en el documento cargado
            Iterable<PageTableArea> tables = parser.getTables(options);

            //  Procese cada tabla extraída del resultado
            for (PageTableArea t : tables) 
            {
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "Herramientas avanzadas de extracción de contenido"
  description: "Más allá de leer tablas, GroupDocs.Parser admite la captura de texto plano, elementos visuales, metadatos incrustados y objetos estructurados para mejorar las tareas de procesamiento de documentos."
  image: "/img/parser/features_extract-table.webp" # 500x500 px
  image_description: "Extracción de contenido estructurado y datos tabulares"
  features:
    # feature loop
    - title: "Análisis preciso de tablas a través de formatos"
      content: "Soporte para la extracción de tablas de tipos de documentos estándar como PDF, Word, Excel y HTML con alta precisión."

    # feature loop
    - title: "Leer estructuras tabulares de diversas fuentes"
      content: "Recupere datos de tablas de hojas de cálculo, documentos e informes, preservando la estructura y alineación."

    # feature loop
    - title: "Configuraciones personalizables para la extracción de tablas"
      content: "Controle la detección de diseño, gestione encabezados y pies de página, y ajuste la extracción con opciones de configuración flexibles."
      
  code_samples:
    # code sample loop
    - title: "Ejemplo: extraer tablas de un documento de Excel"
      content: |
        Este ejemplo muestra cómo extraer y recorrer el contenido de tablas en un archivo de Excel (XLSX) utilizando GroupDocs.Parser.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Inicializar Parser con el archivo de Excel
        try (Parser parser = new Parser("input.pdf"))
        {
            // Salir si la extracción de tablas no es compatible con este documento
            if (!parser.getFeatures().isTables())
            {
                return;
            }

            // Aplicar reglas para localizar el diseño de la tabla
            TemplateTableLayout layout = new TemplateTableLayout(
                    java.util.Arrays.asList(new Double[]{50.0, 95.0, 275.0, 415.0, 485.0, 545.0}),
                    java.util.Arrays.asList(new Double[]{325.0, 340.0, 365.0, 395.0}));

            // Configurar ajustes para la extracción de tablas
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            // Invocar el proceso de extracción
            Iterable<PageTableArea> tables = parser.getTables(options);

            // Recorrer todas las estructuras de tabla analizadas
            for (PageTableArea t : tables)
            {
                // Iterar sobre cada fila dentro de la tabla
                for (int row = 0; row < t.getRowCount(); row++)
                {
                    // Procesar cada celda en la fila actual
                    for (int column = 0; column < t.getColumnCount(); column++) 
                    {
                        // Acceder y leer el contenido de la celda actual
                        PageTableAreaCell cell = t.getCell(row, column);
                        if (cell != null)
                        {
                            // Salida del valor textual de cada celda de la tabla
                            System.out.print(cell.getText());
                            System.out.print(" | ");
                        }
                    }
                }
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
    - title: "Descarga de Maven"
      link: "https://releases.groupdocs.com/parser/java/"
      color: "red"
        #  loop
    - title: "Licenciamiento"
      link: "https://purchase.groupdocs.com/pricing/parser/java/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "Tipos de documentos soportados para la extracción de tablas"
    exclude: "TXT"
    description: "GroupDocs.Parser proporciona detección confiable de tablas en múltiples tipos de archivos. Aquí hay una lista de los formatos de documentos más ampliamente soportados para la extracción de tablas."
    items: 
        # format loop 1
        - name: "Analizar PDF"
          format: "PDF"
          link: "/parser/java/extract-table/pdf/"
          description: "(Formato de documento portátil)"
          
        # format loop 2
        - name: "Analizar DOCX"
          format: "DOCX"
          link: "/parser/java/extract-table/docx/"
          description: "(Documento Word 2007+)"
          
        # format loop 3
        - name: "Analizar PPTX"
          format: "PPTX"
          link: "/parser/java/extract-table/pptx/"
          description: "(Formato de presentación Open XML)"
          
        # format loop 4
        - name: "Analizar XLSX"
          format: "XLSX"
          link: "/parser/java/extract-table/xlsx/"
          description: "(Libro de trabajo Open XML)"
          
        # format loop 5
        - name: "Analizar TXT"
          format: "TXT"
          link: "/parser/java/extract-table/txt/"
          description: "(Archivo de texto)"
          
        # format loop 6
        - name: "Analizar RTF"
          format: "RTF"
          link: "/parser/java/extract-table/rtf/"
          description: "(Formato de texto enriquecido)"
          
        # format loop 7
        - name: "Analizar XML"
          format: "XML"
          link: "/parser/java/extract-table/xml/"
          description: "(Lenguaje de marcado extensible)"
          
        # format loop 8
        - name: "Analizar EPUB"
          format: "EPUB"
          link: "/parser/java/extract-table/epub/"
          description: "(Archivo de eBook abierto)"
         
          

---