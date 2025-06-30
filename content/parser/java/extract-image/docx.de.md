


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:30
draft: false
lang: de
format: Docx
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Bilder aus DOCX-Dateien in Java-Anwendungen extrahieren"
head_description: "GroupDocs.Parser ermöglicht Ihnen das Extrahieren von Bildern aus DOCX-Dateien in Java ohne zusätzliche Tools."

############################# Header ############################
title: "Bilder aus DOCX mithilfe von Java extrahieren" 
description: "Extrahieren Sie eingebettete Bilder aus Dateien wie PDF, Word, Excel und mehr mit GroupDocs.Parser in Ihrer Java-Entwicklungsumgebung."
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Kostenlose Testversion herunterladen"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "Was ist GroupDocs.Parser for Java?"
    link: "/parser/java/"
    link_title: "Mehr erfahren"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) ist eine funktionsreiche Parsing-API, die speziell für Entwickler von Java entwickelt wurde. Sie ermöglicht das Extrahieren von Bildern, Text, Links und strukturierten Elementen aus verschiedenen Dateiformaten, einschließlich DOCX, XLSX, PDF, PNG, JPG und vielen anderen – ganz ohne externe Bibliotheken oder Anwendungen.

############################# Steps ############################
steps:
    enable: true
    title: "So extrahieren Sie Bilder aus Docx in Java"
    content: |
      Befolgen Sie diese Schritte, um Bilder aus DOCX-Dokumenten mit [GroupDocs.Parser](/parser/java/) in Ihrer Java-Anwendung zu extrahieren:
      
      1. Erstellen Sie eine Instanz von Parser und laden Sie die DOCX-Datei.
      2. Extrahieren Sie die Bilddaten aus dem geladenen Dokument.
      3. Verwenden oder exportieren Sie die extrahierten Bilder nach Bedarf.
   
    code:
      platform: "net"
      copy_title: "Kopieren"
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
        copy_tip: "Klicken zum Kopieren"
        copy_done: "Kopiert"
      links:
        #  loop
        - title: "Weitere Beispiele"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java/"
        #  loop
        - title: "Dokumentation"
          link: "https://docs.groupdocs.com/parser/java/"
          
      content: |
        ```java {style=abap}
        // Parser initialisieren und das Dokument mit Bildern laden unter Verwendung von Parser
        try (Parser parser = new Parser("input.docx"))
        {
            // Alle im Dokument eingebetteten Bildelemente sammeln
            Iterable<PageImageArea> images = parser.getImages();

            // Verarbeitung überspringen, wenn das Dokument keine Bilder enthält
            if (images == null) {
                return;
            }

            // Jedes Bild nach Bedarf behandeln
            for (PageImageArea image : images) {
                System.out.println(String.format("Page: %d, R: %s, Type: %s", image.getPage().getIndex(), 
                    image.getRectangle(), image.getFileType()));
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "Weitere Dokumentenbearbeitungsfähigkeiten"
  description: "Zusätzlich zur Bildextraktion ermöglicht GroupDocs.Parser das Extrahieren von Rohdaten wie Text, Links, Metadaten und strukturierten Daten für die Verarbeitung und Analyse."
  image: "/img/parser/features_extract-image.webp" # 500x500 px
  image_description: "Bilder und Inhalte aus Dokumenten extrahieren"
  features:
    # feature loop
    - title: "Funktioniert mit einer Vielzahl von Formaten"
      content: "Extrahieren Sie Bilder aus verschiedenen Dokumenttypen, einschließlich PDF, DOCX, PPTX, XLSX und Bildformaten wie PNG, JPEG und GIF."

    # feature loop
    - title: "Bildklarheit und -auflösung beibehalten"
      content: "Alle extrahierten Bilder behalten ihre ursprüngliche Auflösung und Dateityp, um konstante Qualität und Nutzbarkeit sicherzustellen."

    # feature loop
    - title: "Flexible Konfigurationsoptionen"
      content: "Passen Sie den Bildextraktionsprozess an, indem Sie Bilder nach Typ, Größe, Seitenindex oder Dateiformat filtern."
      
  code_samples:
    # code sample loop
    - title: "Bilder aus PDF-Dateien extrahieren und speichern"
      content: |
        Dieses Beispiel zeigt, wie Sie Bilder aus einem PDF-Dokument extrahieren und sie einzeln auf Ihrem Gerät speichern.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Verwenden Sie Parser, um die PDF-Datei zu öffnen
        try (Parser parser = new Parser("input.pdf"))
        {
            // Holen Sie die Bilder aus dem Dokumentinhalt
            Iterable<PageImageArea> images = parser.getImages();

            // Legen Sie Ausgabeparameter wie Format (z. B. JPEG oder PNG) fest
            ImageOptions options = new ImageOptions(ImageFormat.Png);

            // Speichern Sie die extrahierten Bilder in einem lokalen Verzeichnis
            int imageNumber = 0;
            for (PageImageArea image : images)
            {
                image.save(Constants.getOutputFilePath(String.format("%d.png", imageNumber)), options);
                imageNumber++;
            }
        }
        ```
        {{< /landing/code >}}


############################# Actions ############################

actions:
  enable: true
  title: "Bereit, loszulegen?"
  description: "Testen Sie die Funktionen von GroupDocs.Parser kostenlos oder fordern Sie eine Lizenz an"
  items:
    #  loop
    - title: "Maven herunterladen"
      link: "https://releases.groupdocs.com/parser/java/"
      color: "red"
        #  loop
    - title: "Lizenzierung"
      link: "https://purchase.groupdocs.com/pricing/parser/java/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "Unterstützte Dateitypen für die Bildextraktion"
    exclude: "DOCX"
    description: "GroupDocs.Parser unterstützt die Bildextraktion aus einer Vielzahl von Dokumenten und Bildern. Entdecken Sie die gängig unterstützten Formate unten."
    items: 
        # format loop 1
        - name: "PDF parsen"
          format: "PDF"
          link: "/parser/java/extract-image/pdf/"
          description: "(Portable Document Format)"
          
        # format loop 2
        - name: "DOCX parsen"
          format: "DOCX"
          link: "/parser/java/extract-image/docx/"
          description: "(Office 2007+ Word-Dokument)"
          
        # format loop 3
        - name: "PPTX parsen"
          format: "PPTX"
          link: "/parser/java/extract-image/pptx/"
          description: "(Open XML-Präsentationsformat)"
          
        # format loop 4
        - name: "XLSX parsen"
          format: "XLSX"
          link: "/parser/java/extract-image/xlsx/"
          description: "(Open XML-Arbeitsmappe)"
          
        # format loop 5
        - name: "ODT parsen"
          format: "ODT"
          link: "/parser/java/extract-image/odt/"
          description: "(OpenDocument-Textdokument)"
          
        # format loop 6
        - name: "ODS parsen"
          format: "ODS"
          link: "/parser/java/extract-image/ods/"
          description: "(OpenDocument-Tabellenkalkulation)"
          
        # format loop 7
        - name: "ODP parsen"
          format: "ODP"
          link: "/parser/java/extract-image/odp/"
          description: "(OpenDocument-Präsentation)"
          
        # format loop 8
        - name: "EPUB parsen"
          format: "EPUB"
          link: "/parser/java/extract-image/epub/"
          description: "(Open eBook-Datei)"
          
        # format loop 9
        - name: "FB2 parsen"
          format: "FB2"
          link: "/parser/java/extract-image/fb2/"
          description: "(FictionBook eBook)"
         
          

---