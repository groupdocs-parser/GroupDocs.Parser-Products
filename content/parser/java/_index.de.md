---
############################# Static ############################
layout: "landing"
date: 2025-06-30T10:26:00
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

############################# Head ############################
head_title: "GroupDocs.Parser for Java Dokumentenparser-Apps"
head_description: "Erhalten Sie eine All-in-One-Lösung zum Dokumentenparsen für Java-Anwendungen. Daten aus Dokumentformaten online mit einer einfachen Drag-and-Drop-Funktion extrahieren."

############################# Header ############################
title: "Dokumente über Java API parsen"
description: "Extrahieren Sie Daten aus Dokumenten und Bildern auf jeder Plattform mit unseren flexiblen APIs und anwendungsbasierten Lösungen für Programmierer und Endbenutzer."
words:
  for: "für"

actions:
  main: "Maven herunterladen"
  main_link: "https://releases.groupdocs.com/java/repo/com/groupdocs/groupdocs-parser/"
  alt: "Lizenzierung"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/java/"
  title: "Bereit zu starten?"
  description: "Testen Sie die Funktionen von GroupDocs.Parser kostenlos oder fordern Sie eine Lizenz an"

release:
  title: "Version {0} veröffentlicht"
  notes: "Siehe, was neu ist"
  downloads: "Downloads"

code:
  title: "Dokumenteninhalt schnell abrufen"
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
    // Übergeben Sie die Quelldatei an die Parser-Instanz
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
  description: "API zum Durchführen von Dokumentenverarbeitung in Java-Anwendungen"
  features:
    # feature loop
    - title: "Daten aus Dokumenten extrahieren"
      content: "GroupDocs.Parser for Java API ermöglicht es Ihnen, Text, Metadaten und Bilder aus einer Vielzahl von Dateiformaten wie Office-Dokumenten, E-Mails, Anhängen und Archiven zu extrahieren. Dieses leistungsstarke Tool hilft Ihnen, wertvolle Informationen effizient zuzugreifen und zu verarbeiten, die in diesen Dateien für verschiedene Anwendungen wie Datenanalyse, Suchmaschinenindizierung oder Content-Management-Systeme enthalten sind."

    # feature loop
    - title: "Dokumente parsen"
      content: "Extrahieren Sie verschiedene Elemente wie Hyperlinks, Tabellen, QR-Codes, Barcodes und Daten aus PDF-Formularen. Auch beliebige Informationen aus Dokumenten mithilfe benutzerdefinierter Vorlagen parsen."

    # feature loop
    - title: "Ergebnisse anpassen"
      content: "Java API ermöglicht es Ihnen, Daten in verschiedenen Formaten wie Rohdaten, strukturiert, HTML oder Markdown zu ermitteln. Darüber hinaus bietet die API eine Suchfunktion zum Auffinden spezifischer Wörter oder Phrasen im Text der Dokumente."

############################# Platforms ############################
platforms:
  enable: true
  title: "Plattformunabhängigkeit"
  description: "GroupDocs.Parser for Java unterstützt die folgenden Betriebssysteme, Frameworks und Paketmanager."
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
    GroupDocs.Parser for Java unterstützt Operationen mit den folgenden [Dateiformaten](https://docs.groupdocs.com/parser/java/supported-document-formats/).
  groups:
    # group loop
    - color: "green"
      content: |
        ### Microsoft Office-Formate
        * **Word:** DOCX, DOC, DOCM, DOT, DOTX, DOTM, RTF
        * **Excel:** XLSX, XLS, XLSM, XLSB, XLTM, XLT, XLTM, XLTX, XLAM, SXC, SpreadsheetML
        * **PowerPoint:** PPT, PPTX, PPS, PPSX, PPSM, POT, POTM, POTX, PPTM
    # group loop
    - color: "blue"
      content: |
        ### Bilder & andere Formate
        * **Portabel:** PDF 
        * **Bilder:** JPG, BMP, PNG, TIFF, GIF
        * **Andere Büroformate:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### Weitere Formate
        * **Web:** HTML, MHTML 
        * **Archive:** ZIP, TAR, 7Z 
        * **e-Books:** CHM, EPUB, FB2, MOBI 
        
        

############################# Features ############################
features:
  enable: true
  title: "GroupDocs.Parser for Java Funktionen"
  description: "Daten aus PDFs, Office-Dokumenten und Bildern schnell und präzise extrahieren"

  items:
    # feature loop
    - icon: "text"
      title: "Text extrahieren"
      content: "Textuelle Informationen aus verschiedenen Dateiformaten wie Office-Dokumenten, PDF-Dateien und Bildern extrahieren, um eine einfache Lesbarkeit und Analyse zu gewährleisten."

    # feature loop
    - icon: "image"
      title: "Bilder extrahieren"
      content: "Visuelle Inhalte aus unterschiedlichen Quellen wie Office-Dokumenten und PDF-Dateien abrufen, um einen bequemen Zugriff zu erhalten."

    # feature loop
    - icon: "qr"
      title: "QR-Codes scannen"
      content: "Erkennen und Dekodieren von QR-Codes, die in Office-Dokumenten, PDF-Dateien oder visuellen Inhalten vorhanden sind, um Informationen effizient abzurufen."

    # feature loop
    - icon: "email"
      title: "Daten aus E-Mail-Anhängen und Archiven extrahieren"
      content: "Wertvolle Informationen aus E-Mail-Nachrichten, Dateianhängen und komprimierten Datenquellen zusammenstellen, um eine effektive Analyse und Nutzung zu gewährleisten."

    # feature loop
    - icon: "table"
      title: "Tabellen extrahieren"
      content: "Identifizieren und extrahieren Sie tabellarische Daten aus PDF-Dokumenten für eine organisierte Analyse und Nutzung."

    # feature loop
    - icon: "hyperlink"
      title: "Hyperlinks extrahieren"
      content: "Lokalisieren und extrahieren Sie Hyperlinks und E-Mail-Adressen in Office-Dokumenten oder PDF-Dateien für einen effizienten Zugriff."

    # feature loop
    - icon: "pdf"
      title: "PDF-Formulare parsen"
      content: "PDF-Formulare sind digitale Dokumente mit ausfüllbaren Feldern zur Benutzerinteraktion, die es ihnen ermöglichen, Informationen elektronisch einzugeben. .NET-API kann verwendet werden, um Daten aus diesen Formularen für eine effiziente Verarbeitung zu extrahieren."

    # feature loop
    - icon: "template"
      title: "Daten durch Vorlagen parsen"
      content: "Erstellen Sie benutzerdefinierte Vorlagen und verwenden Sie diese mit der .NET-API, um spezifische Informationen aus PDF-Dateien zu extrahieren und die Datenextraktionsprozesse zu vereinfachen."

    # feature loop
    - icon: "search"
      title: "Text in Dokumenten suchen"
      content: "Schnell spezifische Wörter oder Muster innerhalb von Dokumenten finden."


############################# Code samples ############################
code_samples:
  enable: true
  title: "Codebeispiele"
  description: "Einige Anwendungsfälle typischer GroupDocs.Parser for Java-Operationen"
  items:
    # code sample loop
    - title: "Bilder aus PDF-Dokumenten extrahieren"
      content: |
        GroupDocs.Parser for Java erleichtert es Java-Entwicklern, Bilder aus [Dokumenten](https://docs.groupdocs.com/parser/java/extract-images-from-documents/) zu extrahieren:
        {{< landing/code title="Bilder aus PDF-Dokumenten in Java extrahieren">}}
        ```java {style=abap}
        // Erstellen Sie eine Instanz der Parser-Klasse
        try (Parser parser = new Parser("source.pdf"))
        {
            // Bilder extrahieren
            Iterable<PageImageArea> images = parser.getImages();

            // Überprüfen, ob etwas extrahiert wurde
            if (images == null) {
                return;
            }

            // Über Bilder iterieren
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
        Verwenden Sie unsere Java-API, um [Barcodes](https://docs.groupdocs.com/parser/java/extract-barcodes-from-document/) aus Bildern zu extrahieren:
        {{< landing/code title="Barcode aus Bildern in Java extrahieren">}}
        ```java {style=abap}   
        // Laden Sie das Quellbild in Parser
        try (Parser parser = new Parser("source.jpg")){

            // Überprüfen, ob die Datei die Barcode-Extraktion unterstützt
            if (!parser.getFeatures().isBarcodes()) {

                // Barcodes aus der Datei extrahieren
                Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();

                // Über Barcodes iterieren
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
