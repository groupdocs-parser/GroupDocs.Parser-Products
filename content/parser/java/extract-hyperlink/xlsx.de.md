


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:23
draft: false
lang: de
format: Xlsx
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Hyperlinks aus XLSX-Dateien in Java-Apps extrahieren"
head_description: "Verwenden Sie GroupDocs.Parser, um URL-Links aus XLSX-Dokumenten in Java-Projekten zu finden und zu extrahieren – keine zusätzliche Software erforderlich."

############################# Header ############################
title: "Hyperlinks aus XLSX mit Java extrahieren" 
description: "Ziehen Sie Webseiten-Links und Hyperlinks aus PDFs, Word-Dateien, Excel-Tabellen und anderen Dokumenten mit GroupDocs.Parser in Ihrer Java-Umgebung heraus."
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
    title: "Über die GroupDocs.Parser for Java API"
    link: "/parser/java/"
    link_title: "Mehr erfahren"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) ist eine leistungsstarke API zur Inhaltsextraktion, die für Java-Entwickler entwickelt wurde. Sie bietet Werkzeuge zum Extrahieren von Hyperlinks, strukturierten Daten, Bildern und Text aus gängigen Formaten wie DOCX, XLSX, PDF, HTML und mehr – ganz ohne externe Plugins.

############################# Steps ############################
steps:
    enable: true
    title: "Wie man Hyperlinks aus Xlsx in Java extrahiert"
    content: |
      [GroupDocs.Parser](/parser/java/) vereinfacht die Hyperlink-Extraktion aus XLSX-Dateien in Java-Anwendungen mit diesen grundlegenden Schritten:
      
      1. Öffnen Sie die XLSX-Datei mit einer Instanz von Parser.
      2. Stellen Sie sicher, dass die Hyperlink-Extraktion für das Dateiformat verfügbar ist.
      3. Extrahieren Sie alle Hyperlinks mit der entsprechenden Methode.
      4. Durchlaufen Sie die Ergebnisse und verarbeiten Sie jeden Link nach Bedarf.
   
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
        // Laden Sie die Datei, die möglicherweise Hyperlinks enthält, mit dem Parser
        try (Parser parser = new Parser("input.xlsx")) {

            // Überprüfen Sie, ob das Dokumentenformat die Hyperlink-Analyse unterstützt
            if (!parser.getFeatures().isHyperlinks()) {
                System.out.println("Die Hyperlink-Extraktion ist für die Datei nicht verfügbar");
                return;
            }

            // Extrahieren Sie die Hyperlink-Daten aus dem Dokument und verwenden Sie sie
            Iterable<PageHyperlinkArea> hyperlinks = parser.getHyperlinks();

            for (PageHyperlinkArea h : hyperlinks) {
                System.out.println(h.getText());
                System.out.println(h.getUrl());
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "Umfassende Dokumentenverarbeitungstools"
  description: "Neben der Extraktion von Hyperlinks ermöglicht GroupDocs.Parser die Sammlung weiterer nützlicher Inhalte wie Klartext, eingebettete Medien und strukturierte Daten für den Einsatz in automatisierten Workflows."
  image: "/img/parser/features_extract-hyperlink.webp" # 500x500 px
  image_description: "Hyperlink-Extraktion und Dokumentenanalyse"
  features:
    # feature loop
    - title: "Präzise Linkerkennung"
      content: "Erfassen Sie alle Arten von Hyperlinks aus verschiedenen Dokumentenlayouts, einschließlich klickbarem Text und versteckten URLs."

    # feature loop
    - title: "Funktioniert mit Dokumenten und Webinhalten"
      content: "Ziehen Sie Links aus PDF, DOCX, XLSX, HTML und Bilddateien, die eingebettete Hyperlinks enthalten."

    # feature loop
    - title: "Benutzerdefiniertes Extraktionsverhalten"
      content: "Verfeinern Sie, wie Hyperlinks extrahiert werden, mit Optionen wie Seitenbereichen, Linktypen oder Inhaltsfiltern."
      
  code_samples:
    # code sample loop
    - title: "Beispiel: Extrahieren von Hyperlinks aus einem PDF mit benutzerdefinierten Optionen"
      content: |
        Dieses Beispiel demonstriert, wie alle Links aus einer PDF-Datei mithilfe von Link-Extraktionseinstellungen extrahiert werden.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Öffnen Sie die PDF-Datei mit der Parser-Klasse
        try (Parser parser = new Parser("input.docx"))
        {
            // Überprüfen Sie, ob die Hyperlinkunterstützung für dieses Dokument aktiviert ist
            if (!parser.getFeatures().isHyperlinks()) {
                return;
            }

            // Wenden Sie Optionen an, um Links zu filtern
            PageAreaOptions options = new PageAreaOptions(new Rectangle(new Point(380, 90), new Size(150, 50)));

            // Verwenden Sie den Parser, um Hyperlink-Daten zu erhalten
            Iterable<PageHyperlinkArea> hyperlinks = parser.getHyperlinks(options);

            // Iterieren Sie über die Links und behandeln Sie sie entsprechend
            for (PageHyperlinkArea h : hyperlinks) {
                System.out.println(h.getText());
                System.out.println(h.getUrl());
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
    title: "Dokumentenformate, die die Hyperlink-Extraktion unterstützen"
    exclude: "XLSX"
    description: "Mit GroupDocs.Parser können Sie Hyperlinks aus vielen häufig verwendeten Dateiformaten extrahieren. Nachfolgend finden Sie eine Liste von Formaten, die in der Regel unterstützt werden."
    items: 
        # format loop 1
        - name: "PDF parsen"
          format: "PDF"
          link: "/parser/java/extract-hyperlink/pdf/"
          description: "(Portable Document Format)"
          
        # format loop 2
        - name: "DOCX parsen"
          format: "DOCX"
          link: "/parser/java/extract-hyperlink/docx/"
          description: "(Office 2007+ Word-Dokument)"
          
        # format loop 3
        - name: "PPTX parsen"
          format: "PPTX"
          link: "/parser/java/extract-hyperlink/pptx/"
          description: "(Open XML-Präsentationsformat)"
          
        # format loop 4
        - name: "XLSX parsen"
          format: "XLSX"
          link: "/parser/java/extract-hyperlink/xlsx/"
          description: "(Open XML-Arbeitsmappe)"
          
        # format loop 5
        - name: "TXT parsen"
          format: "TXT"
          link: "/parser/java/extract-hyperlink/txt/"
          description: "(Textdatei)"
          
        # format loop 6
        - name: "RTF parsen"
          format: "RTF"
          link: "/parser/java/extract-hyperlink/rtf/"
          description: "(Rich Text Format)"
          
        # format loop 7
        - name: "XML parsen"
          format: "XML"
          link: "/parser/java/extract-hyperlink/xml/"
          description: "(eXtensible Markup Language)"
          
        # format loop 8
        - name: "EPUB parsen"
          format: "EPUB"
          link: "/parser/java/extract-hyperlink/epub/"
          description: "(Open eBook-Datei)"
         
          

---