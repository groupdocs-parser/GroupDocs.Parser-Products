---
############################# Static ############################
layout: "landing"
date: 2024-02-13T17:01:03
draft: false
#operation: 
#parsertype: 
#fileformat: 
#productName: Java
lang: "de"
#productCode: java
#otherformats: 
#breadcrumb: Put  parser on  for Java
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: ".NET, Java, Cloud-APIs und Online-Dokumentparser-Apps"
head_description: "Holen Sie sich eine All-in-One-Lösung zum Parsen von Dokumenten für .NET, Java und cloudbasierte Anwendungen. Extrahieren Sie Daten aus Dokumentformaten online mit der einfachen Drag-and-Drop-Funktion"

############################# Header ############################
title: "Dokumente analysieren<br>über Java API"
description: "Extrahieren Sie Daten aus Dokumenten und Bildern auf jeder Plattform mit unseren flexiblen APIs und App-basierten Lösungen für Programmierer und Endbenutzer."
words:
  for: "für"

actions:
  main: "Kostenloser Maven-Download"
  main_link: "https://releases.groupdocs.com/java/repo/com/groupdocs/groupdocs-parser/"
  alt: "Lizenzierung"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/java"
  title: "Bereit anzufangen?"
  description: "Testen Sie die Funktionen von GroupDocs.Parser kostenlos oder fordern Sie eine Lizenz an"

release:
  title: "Version {0} veröffentlicht"
  notes: "Schau was neu ist"
  downloads: "Downloads"

code:
  title: "Text aus PDF-Dateien in Java extrahieren"
  more: "Mehr Beispiele"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java"
  install: |
    <dependency>
      <groupId>com.groupdocs</groupId>
      <artifactId>groupdocs-parser</artifactId>
      <version>{0}</version>
    </dependency>
  content: |
    ```java {style=abap}  
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
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser Übersicht"
  description: "API zum Durchführen der Dokumentenanalyse in Java-Anwendungen"
  features:
    # feature loop
    - title: "Extrahieren Sie Daten aus Dokumenten"
      content: "Mit der Java-API können Sie Text, Metadaten und Bilder aus einer Vielzahl von Dateiformaten wie Office-Dokumenten, E-Mails, Anhängen und Archiven abrufen. Dieses leistungsstarke Tool hilft Ihnen, effizient auf die in diesen Dateien enthaltenen wertvollen Informationen zuzugreifen und diese für verschiedene Anwendungen wie Datenanalyse, Suchmaschinenindizierung oder Content-Management-Systeme zu verarbeiten."

    # feature loop
    - title: "Dokumente analysieren"
      content: "Extrahieren Sie verschiedene Elemente wie Hyperlinks, Tabellen, QR-Codes, Barcodes und Daten aus PDF-Formularen. Analysieren Sie außerdem alle gewünschten Informationen aus Dokumenten mithilfe benutzerdefinierter Vorlagen."

    # feature loop
    - title: "Anpassen der Ergebnisse"
      content: "Mit der Java API können Sie Daten in verschiedenen Formaten abrufen, z. B. roh, strukturiert, HTML oder Markdown. Darüber hinaus bietet die API eine Suchfunktion zum Auffinden bestimmter Wörter oder Phrasen im Text von Dokumenten."

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
        ### Microsoft Office Formate
        * **Word:**  DOCX, DOC, DOCM, DOT, DOTX, DOTM, RTF
        * **Excel:** XLSX, XLS, XLSM, XLSB, XLTM, XLT, XLTM, XLTX, XLAM, SXC, SpreadsheetML
        * **PowerPoint:** PPT, PPTX, PPS, PPSX, PPSM, POT, POTM, POTX, PPTM
    # group loop
    - color: "blue"
      content: |
        ### Bilder und andere Formate
        * **Portable:** PDF
        * **Bilder:** JPG, BMP, PNG, TIFF, GIF, DICOM, WEBP
        * **Andere Büroformate:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### Andere Formate
        * **Netz:** HTML, MHTML
        * **Archiv:** ZIP, TAR, 7Z
        * **E-Books:** CHM, EPUB, FB2, MOBI

############################# Features ############################
features:
  enable: true
  title: "GroupDocs.Parser Funktionen"
  description: "Extrahieren Sie Daten aus PDFs, Office-Dokumenten und Bildern schnell und genau."

  items:
    # feature loop
    - icon: "text"
      title: "Text extrahieren"
      content: "Extrahieren Sie Textinformationen aus verschiedenen Dateiformaten wie Office-Dokumenten, PDF-Dateien und Bildern für eine einfache Lesbarkeit und Analyse."

    # feature loop
    - icon: "image"
      title: "Bilder extrahieren"
      content: "Rufen Sie visuelle Inhalte aus verschiedenen Quellen wie Office-Dokumenten und PDF Dateien ab, um bequem darauf zuzugreifen und sie zu verwenden."

    # feature loop
    - icon: "qr"
      title: "QR-Codes scannen"
      content: "Erkennen und dekodieren Sie QR-Codes in Bürodokumenten, PDF Dateien oder visuellen Inhalten für einen effizienten Informationsabruf."

    # feature loop
    - icon: "email"
      title: "Extrahieren Sie Daten aus E-Mail-Anhängen und Archiven"
      content: "Sammeln Sie wertvolle Informationen aus E-Mail-Nachrichten, Dateianhängen und komprimierten Datenquellen für eine effektive Analyse und Nutzung."

    # feature loop
    - icon: "table"
      title: "Tabellen extrahieren"
      content: "Identifizieren und extrahieren Sie tabellarische Daten aus PDF Dokumenten zur organisierten Analyse und Verwendung."

    # feature loop
    - icon: "hyperlink"
      title: "Extrahieren Sie Hyperlinks"
      content: "Suchen und extrahieren Sie Hyperlinks und E-Mail-Adressen in Office-Dokumenten oder PDF-Dateien für einen effizienten Zugriff."

    # feature loop
    - icon: "pdf"
      title: "Analysieren Sie PDF-Formulare"
      content: "PDF Formulare sind digitale Dokumente mit ausfüllbaren Feldern für die Benutzerinteraktion, die es ihnen ermöglichen, Informationen elektronisch einzugeben. Mithilfe der Java-API können Daten aus diesen Formularen für eine effiziente Verarbeitung extrahiert werden."

    # feature loop
    - icon: "template"
      title: "Analysieren Sie Daten nach Vorlagen"
      content: "Erstellen Sie benutzerdefinierte Vorlagen und nutzen Sie diese mit der Java-API, um bestimmte Informationen aus PDF-Dateien zu analysieren und so Datenextraktionsprozesse zu vereinfachen."

    # feature loop
    - icon: "search"
      title: "Suchen Sie einen Text in Dokumenten"
      content: "Finden Sie schnell bestimmte Wörter oder Muster in Dokumenten."

############################# Code samples ############################
code_samples:
  enable: true
  title: "Codebeispiel"
  description: "Einige Anwendungsfälle typischer GroupDocs.Parser for Java-Vorgänge"
  items:
    # code sample loop
    - title: "Extrahieren Sie Bilder aus PDF-Dokumenten"
      content: |
        Die Java-API erleichtert Java-Entwicklern das Extrahieren von Bildern aus Dokumenten durch die Implementierung einiger einfacher Schritte.
        {{< landing/code title="Extrahieren Sie Bilder aus PDF Dokumenten in Java">}}
        ```java {style=abap}
        // Create an instance of Parser class
        try (Parser parser = new Parser(fileName)) {
            // Extract images
            Iterable<PageImageArea> images = parser.getImages();
            // Check if images extraction is supported
            if (images != null) {
                int imageIndex = 0;
                // Iterate over images
                for (PageImageArea image : images) {
                    // Save the image to the file
                    image.save(String.format("%s%s", imageIndex, image.getFileType().getExtension()));
                }
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Barcodes aus Bildern extrahieren"
      content: |
        Die Java-API erleichtert Java-Entwicklern das Extrahieren von Barcodes aus Dokumenten durch die Implementierung einiger einfacher Schritte.
        {{< landing/code title="Barcodes aus Bildern extrahieren">}}
        ```java {style=abap}   
        // Create an instance of Parser class
        try (Parser parser = new Parser(fileName)) {
            // // Check if the file supports barcode extracting
            if (!parser.getFeatures().isBarcodes()) {
                // Extract barcodes from the file.
                Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();
                // Iterate over barcodes
                for (PageBarcodeArea barcode : barcodes) {
                    // Print the page index
                    System.out.println("Page: " + barcode.getPage().getIndex());
                    // Print the barcode value
                    System.out.println("Value: " + barcode.getValue());
                }
            }
        }
        ```
        {{< /landing/code >}}

---
