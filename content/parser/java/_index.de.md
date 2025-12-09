---
############################# Static ############################
layout: "landing"
date: 2025-12-09T14:10:41
draft: false

lang: de
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Drop-down ############################
supported_platforms:
  items:
    # supported_platforms loop
    - title: ".NET"
      tag: "net"
    # supported_platforms loop
    - title: "Java"
      tag: "java"
    # supported_platforms loop
    - title: "Python"
      tag: "python-net"

############################# Head ############################
head_title: "GroupDocs.Parser for Java Document Parser SDK für Java"
head_description: "Leistungsstarkes Document Parser SDK für Java. Extrahieren Sie Text, Bilder, Metadaten, Barcodes, Tabellen und weitere Daten aus PDF, Word, Excel, E-Mails und über 50 Dokumentformaten."

############################# Header ############################
title: "Document Parser SDK für Java"
description: "Fügen Sie Ihren Java‑Apps eine schnelle, präzise Dokumenten‑Parsing‑Funktion hinzu und extrahieren Sie Text, Bilder, Metadaten sowie strukturierte Daten aus Dokumenten und Bildern."
words:
  for: "für"

actions:
  main: "Maven Download"
  main_link: "https://releases.groupdocs.com/java/repo/com/groupdocs/groupdocs-parser/"
  alt: "Lizenzierung"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/java/"
  title: "Bereit, loszulegen?"
  description: "Testen Sie die GroupDocs.Parser-Funktionen kostenlos oder fordern Sie eine Lizenz an"

release:
  title: "Version {0} veröffentlicht"
  notes: "Erfahren Sie, was neu ist"
  downloads: "Downloads"

code:
  title: "Dokumentinhalt schnell mit dem SDK parsen"
  more: "Weitere Beispiele"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java/"
  install: |
    <dependency>
      <groupId>com.groupdocs</groupId>
      <artifactId>groupdocs-parser</artifactId>
      <version>{0}</version>
    </dependency>
  content: |
    ```java {style=abap}  
    // Übergeben Sie die Quelldatei an die Parser‑Instanz
    try (Parser parser = new Parser("source.pdf"))
    {
        // Übergeben Sie den Dokumententext an TextReader
        try (TextReader reader = parser.getText())
        {
            // Verarbeiten Sie den Dokumententext
            System.out.println(reader == null 
                ? "" 
                : reader.readToEnd());
        }
    }
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser auf einen Blick"
  description: "Document Parser SDK für die Durchführung hochgenauer Dokumenten‑Parsing‑Vorgänge in Java‑Anwendungen"
  features:
    # feature loop
    - title: "Daten aus Dokumenten extrahieren"
      content: "GroupDocs.Parser for Java API ermöglicht das Abrufen von Text, Metadaten und Bildern aus einer Vielzahl von Dateiformaten wie Office-Dokumenten, E-Mails, Anhängen und Archiven. Dieses leistungsstarke Werkzeug unterstützt Sie dabei, wertvolle Informationen in diesen Dateien effizient zu erhalten und zu verarbeiten, z. B. für Datenanalysen, die Indexierung durch Suchmaschinen oder Content‑Management‑Systeme."

    # feature loop
    - title: "Dokumente parsen"
      content: "Extrahieren Sie verschiedene Elemente wie Hyperlinks, Tabellen, QR‑Codes, Barcodes und Daten aus PDF‑Formularen. Außerdem können Sie beliebige Informationen aus Dokumenten mithilfe benutzerdefinierter Vorlagen parsen."

    # feature loop
    - title: "Ergebnisse anpassen"
      content: "Java API ermöglicht das Abrufen von Daten in verschiedenen Formaten wie Roh, strukturiert, HTML oder Markdown. Außerdem bietet die API eine Suchfunktion zum Finden bestimmter Wörter oder Phrasen im Text von Dokumenten."

############################# Platforms ############################
platforms:
  enable: true
  title: "Plattformunabhängigkeit"
  description: "GroupDocs.Parser for Java unterstützt die folgenden Betriebssysteme, Frameworks und Paketmanager"
  items:
    # platform loop
    - title: "Amazon"
      image: "amazon"
    # platform loop
    - title: "Docker"
      image: "docker"
    # platform loop
    - title: "Azure"
      image: "azure"
    # platform loop
    - title: "Eclipse"
      image: "eclipse"
    # platform loop
    - title: "IntelliJ"
      image: "intellij"
    # platform loop
    - title: "Windows"
      image: "windows"
    # platform loop
    - title: "Linux"
      image: "linux"
    # platform loop
    - title: "Maven"
      image: "maven"

############################# File formats ############################
formats:
  enable: true
  title: "Unterstützte Dateiformate"
  description: |
    GroupDocs.Parser for Java unterstützt Vorgänge mit den folgenden [Dateiformaten](https://docs.groupdocs.com/parser/java/supported-document-formats/).
  groups:
    # group loop
    - color: "green"
      content: |
        ### Microsoft‑Office‑Formate
        * **Word:** DOCX, DOC, DOCM, DOT, DOTX, DOTM, RTF
        * **Excel:** XLSX, XLS, XLSM, XLSB, XLTM, XLT, XLTM, XLTX, XLAM, SXC, SpreadsheetML
        * **PowerPoint:** PPT, PPTX, PPS, PPSX, PPSM, POT, POTM, POTX, PPTM
    # group loop
    - color: "blue"
      content: |
        ### Bilder & andere Formate
        * **Tragbar:** PDF 
        * **Bilder:** JPG, BMP, PNG, TIFF, GIF
        * **Andere Office-Formate:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### Weitere Formate
        * **Web:** HTML, MHTML 
        * **Archive:** ZIP, TAR, 7Z 
        * **eBooks:** CHM, EPUB, FB2, MOBI 
        
        

############################# Features ############################
features:
  enable: true
  title: "GroupDocs.Parser for Java Funktionen"
  description: "Extrahieren Sie Daten aus PDFs, Office‑Dokumenten, Bildern und anderen Formaten schnell und genau mit unserem Java Document Parser SDK."

  items:
    # feature loop
    - icon: "text"
      title: "Text extrahieren"
      content: "Extrahieren Sie Textinformationen aus verschiedenen Dateiformaten wie Office‑Dokumenten, PDF‑Dateien und Bildern für einfache Lesbarkeit und Analyse."

    # feature loop
    - icon: "image"
      title: "Bilder extrahieren"
      content: "Rufen Sie visuelle Inhalte aus verschiedenen Quellen wie Office‑Dokumenten und PDF‑Dateien ab für bequemen Zugriff und Nutzung."

    # feature loop
    - icon: "qr"
      title: "QR‑Codes scannen"
      content: "Erkennen und dekodieren Sie QR‑Codes, die in Office‑Dokumenten, PDF‑Dateien oder visuellen Inhalten enthalten sind, für effiziente Informationsbeschaffung."

    # feature loop
    - icon: "email"
      title: "Daten aus E‑Mail‑Anhängen und Archiven extrahieren"
      content: "Sammeln Sie wertvolle Informationen aus E-Mails, Dateianhängen und komprimierten Datenquellen für eine effektive Analyse und Nutzung."

    # feature loop
    - icon: "table"
      title: "Tabellen extrahieren"
      content: "Identifizieren und extrahieren Sie tabellarische Daten aus PDF-Dokumenten für eine strukturierte Analyse und Verwendung."

    # feature loop
    - icon: "hyperlink"
      title: "Hyperlinks extrahieren"
      content: "Ermitteln und extrahieren Sie Hyperlinks und E-Mail-Adressen in Office-Dokumenten oder PDF-Dateien für einen effizienten Zugriff."

    # feature loop
    - icon: "pdf"
      title: "PDF-Formulare parsen"
      content: "PDF-Formulare sind digitale Dokumente mit ausfüllbaren Feldern für die Benutzerinteraktion, die die elektronische Eingabe von Informationen ermöglichen. Die .NET API kann verwendet werden, um Daten aus diesen Formularen für eine effiziente Verarbeitung zu extrahieren."

    # feature loop
    - icon: "template"
      title: "Daten mithilfe von Vorlagen parsen"
      content: "Erstellen Sie benutzerdefinierte Vorlagen und verwenden Sie diese mit der .NET API, um spezifische Informationen aus PDF-Dateien zu parsen und so den Datenextraktionsprozess zu vereinfachen."

    # feature loop
    - icon: "search"
      title: "Text in Dokumenten suchen"
      content: "Suchen Sie schnell bestimmte Wörter oder Muster in Dokumenten."


############################# Code samples ############################
code_samples:
  enable: true
  title: "Codebeispiele"
  description: "Einige Anwendungsfälle typischer GroupDocs.Parser for Java‑Operationen"
  items:
    # code sample loop
    - title: "Bilder aus PDF‑Dokumenten extrahieren"
      content: |
        GroupDocs.Parser for Java erleichtert Java‑Entwicklern das Extrahieren von Bildern aus [Dokumenten](https://docs.groupdocs.com/parser/java/extract-images-from-documents/):
        {{< landing/code title="Bilder aus PDF-Dokumenten in Java extrahieren">}}
        ```java {style=abap}
        // Erstellen Sie eine Instanz der Klasse Parser
        try (Parser parser = new Parser("source.pdf"))
        {
            // Bilder extrahieren
            Iterable<PageImageArea> images = parser.getImages();

            // Prüfen, ob etwas extrahiert wurde
            if (images == null) {
                return;
            }

            // Durchlaufen Sie die Bilder
            for (PageImageArea image : images) {
                // Seitenindex, Rechteck und Bildtyp ausgeben
                System.out.println(String.format("Page: %d, R: %s, Type: %s", 
                    image.getPage().getIndex(), image.getRectangle(), image.getFileType()));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Barcodes aus Bildern extrahieren"
      content: |
        Verwenden Sie unsere Java‑API, um [Barcodes](https://docs.groupdocs.com/parser/java/extract-barcodes-from-document/) aus Bildern zu extrahieren:
        {{< landing/code title="Barcodes aus Bildern in Java extrahieren">}}
        ```java {style=abap}   
        // Quellbild in Parser laden
        try (Parser parser = new Parser("source.jpg")){

            // Prüfen, ob die Datei die Barcode-Extraktion unterstützt
            if (!parser.getFeatures().isBarcodes()) {

                // Barcodes aus der Datei extrahieren
                Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();

                // Barcodes durchlaufen
                for (PageBarcodeArea barcode : barcodes) {
                    // Seitenindex ausgeben
                    System.out.println("Page: " + barcode.getPage().getIndex());
                    // Barcode-Wert ausgeben
                    System.out.println("Value: " + barcode.getValue());
                }
            }
        }
        ```
        {{< /landing/code >}}

---
