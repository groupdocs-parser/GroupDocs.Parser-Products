


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:16
draft: false
lang: de
format: Pdf
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Barcode aus PDF-Dateien in Java-Apps lesen"
head_description: "GroupDocs.Parser ermöglicht es, Barcode-Daten aus PDF-Dokumenten mit Java ohne externe Tools zu extrahieren."

############################# Header ############################
title: "Barcode aus PDF mit Java lesen" 
description: "Extrahieren Sie Barcode-Inhalte aus PDF-, Word-, Excel- und Bilddateien mit GroupDocs.Parser in Ihren Java-Anwendungen."
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
    title: "Übersicht über die GroupDocs.Parser for Java-API"
    link: "/parser/java/"
    link_title: "Mehr erfahren"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) bietet eine umfassende Lösung für die Dokumentenbearbeitung in Java. Entwickler können Barcodes, Texte, Bilder und strukturierte Informationen aus verschiedenen Dateiformaten wie PDF, Word, Excel, PowerPoint und anderen extrahieren – ohne Drittanbieterbibliotheken nutzen zu müssen.

############################# Steps ############################
steps:
    enable: true
    title: "So lesen Sie Barcodes aus Pdf in Java"
    content: |
      Mit [GroupDocs.Parser](/parser/java/) können Java-Entwickler Barcodes aus PDF-Dokumenten in wenigen Schritten extrahieren:
      
      1. Parser verwenden, um das PDF-Dokument zu laden.
      2. Überprüfen Sie, ob das Dokument die Barcode-Extraktion unterstützt.
      3. Verwenden Sie die API, um die Barcode-Daten abzurufen.
      4. Durchlaufen Sie die Barcode-Ergebnisse und wenden Sie sie nach Bedarf an.
   
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
        // Öffnen Sie ein Dokument mit Barcodes mit Parser
        try (Parser parser = new Parser("input.pdf"))
        {
            // Überprüfen Sie die Barcode-Unterstützung für die Datei
            if (!parser.getFeatures().isBarcodes())
            {
                System.out.println("Verarbeiten Sie nicht unterstützte Dateitypen");
                return;
            }

            // Extrahieren und verwenden Sie die Barcode-Daten
            Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();
            for(PageBarcodeArea barcode : barcodes)
            {
                System.out.println("Page: " + barcode.getPage().getIndex());
                System.out.println("Value: " + barcode.getValue());
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "Weitere Parsing-Funktionen"
  description: "GroupDocs.Parser geht über die Barcode-Extraktion hinaus – es ermöglicht auch das Extrahieren von reinem Text, Bildern und strukturierten Elementen zur Unterstützung datengestützter Arbeitsabläufe."
  image: "/img/parser/features_extract-barcode.webp" # 500x500 px
  image_description: "Barcode- und Datenausgabe-Funktionen"
  features:
    # feature loop
    - title: "Breite Unterstützung von Barcode-Formaten"
      content: "Erkennen Sie standardisierte Barcode-Formate wie QR-Code, Code 39, Data Matrix, EAN, Aztec und andere."

    # feature loop
    - title: "Barcodes aus mehreren Quellen lesen"
      content: "Extrahieren Sie Barcode-Informationen aus Office-Dokumenten, PDFs und Bilddateien wie PNG, JPG und BMP."

    # feature loop
    - title: "Benutzerdefinierte Barcode-Leseeinrichtung"
      content: "Feinabstimmung der Barcode-Extraktion mit Optionen zur gezielten Bearbeitung spezifischer Bereiche und mehrseitiger Dateien."
      
  code_samples:
    # code sample loop
    - title: "Beispiel: Barcodes aus PDF mit Optionen extrahieren"
      content: |
        Dieses Beispiel zeigt die Barcode-Extraktion aus einem PDF-Dokument mit benutzerdefinierten Einstellungen.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Parser mit PDF-Dokument initialisieren
        try (Parser parser = new Parser("input.pdf"))
        {
            // Sicherstellen, dass das Dokument das Barcode-Lesen unterstützt
            if (!parser.getFeatures().isBarcodes())
            {
                return;
            }

            // Filterung mit Barcode-Optionen anwenden
            BarcodeOptions options = new BarcodeOptions(QualityMode.Low, QualityMode.Low, "QR");

            // Barcodes mit dem Parser extrahieren
            Iterable<PageBarcodeArea> barcodes = parser.getBarcodes(options);

            // Jedes Barcode-Ergebnis verarbeiten
            for (PageBarcodeArea barcode : barcodes)
            {
                System.out.println("Page: " + String.valueOf(barcode.getPage().getIndex()));
                System.out.println("Value: " + barcode.getValue());
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
    title: "Unterstützte Dateien für das Barcode-Lesen"
    exclude: "PDF"
    description: "GroupDocs.Parser kann Barcodes aus vielen Dokumenten- und Bildformaten lesen. Im Folgenden sind einige der häufig unterstützten Formate aufgeführt."
    items: 
        # format loop 1
        - name: "PDF parsen"
          format: "PDF"
          link: "/parser/java/extract-barcode/pdf/"
          description: "(Portable Document Format)"
          
        # format loop 2
        - name: "DOCX parsen"
          format: "DOCX"
          link: "/parser/java/extract-barcode/docx/"
          description: "(Office 2007+ Word-Dokument)"
          
        # format loop 3
        - name: "PPTX parsen"
          format: "PPTX"
          link: "/parser/java/extract-barcode/pptx/"
          description: "(Open XML-Präsentationsformat)"
          
        # format loop 4
        - name: "XLSX parsen"
          format: "XLSX"
          link: "/parser/java/extract-barcode/xlsx/"
          description: "(Open XML-Arbeitsmappe)"
          
        # format loop 5
        - name: "ODT parsen"
          format: "ODT"
          link: "/parser/java/extract-barcode/odt/"
          description: "(OpenDocument-Textdokument)"
          
        # format loop 6
        - name: "ODS parsen"
          format: "ODS"
          link: "/parser/java/extract-barcode/ods/"
          description: "(OpenDocument-Tabellenkalkulation)"
          
        # format loop 7
        - name: "ODP parsen"
          format: "ODP"
          link: "/parser/java/extract-barcode/odp/"
          description: "(OpenDocument-Präsentation)"
          
        # format loop 8
        - name: "EPUB parsen"
          format: "EPUB"
          link: "/parser/java/extract-barcode/epub/"
          description: "(Open eBook-Datei)"
          
        # format loop 9
        - name: "FB2 parsen"
          format: "FB2"
          link: "/parser/java/extract-barcode/fb2/"
          description: "(FictionBook eBook)"
         
          

---