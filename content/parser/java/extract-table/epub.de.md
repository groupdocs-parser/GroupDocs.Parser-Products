


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:38
draft: false
lang: de
format: Epub
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Tabellen aus EPUB-Dokumenten in Java-Anwendungen abrufen"
head_description: "Extrahieren Sie strukturierte tabellarische Daten aus EPUB-Dateien in Java-Anwendungen mit GroupDocs.Parser – keine externen Tools erforderlich."

############################# Header ############################
title: "Tabellendaten aus EPUB mit Java abrufen" 
description: "Erkennen und extrahieren Sie nahtlos Tabellen aus Formaten wie PDF, DOCX und XLSX mit GroupDocs.Parser in Ihren Java-Workflows."
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
    title: "Einführung in die GroupDocs.Parser for Java-API"
    link: "/parser/java/"
    link_title: "Mehr erfahren"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) ist eine funktionsreiche API zur Inhaltsextraktion für Java-Plattformen. Sie ermöglicht Entwicklern, Tabellen, Texte, Grafiken, Links und strukturierte Daten aus PDFs, Word-Dokumenten, Excel-Tabellen, PowerPoint-Präsentationen und mehr präzise zu parsen – ohne dass Drittanbieter-Plugins erforderlich sind.

############################# Steps ############################
steps:
    enable: true
    title: "So extrahieren Sie Tabellen aus Epub in Java"
    content: |
      Um Tabellen aus EPUB-Dokumenten mit [GroupDocs.Parser](/parser/java/) zu parsen, folgen Sie diesen Schritten in Ihrer Java-Umgebung:
      
      1. Erstellen Sie eine Parser-Instanz und laden Sie die Ziel-EPUB-Datei.
      2. Überprüfen Sie, ob die Datei die strukturierte Tabellenerfassung unterstützt.
      3. Verwenden Sie die API, um Tabellenelemente aus dem Dokument abzurufen.
      4. Nutzen Sie die extrahierten Daten in Analysen, Berichterstattung oder Automatisierungssystemen.
   
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
        // Laden Sie das Eingabedokument mit Parser, das Tabellenelemente enthält.
        try (Parser parser = new Parser("input.epub"))
        {
            // Überprüfen Sie, ob der Dokumenttyp die Tabellenkennung zulässt.
            if (!parser.getFeatures().isTables()) {
                System.out.println("Fügen Sie Logik für Dateien hinzu, die keine Tabellen unterstützen.");
                return;
            }

            // Definieren Sie Regeln zur Interpretation der Tabellenstruktur.
            TemplateTableLayout layout = new TemplateTableLayout(
                    java.util.Arrays.asList(new Double[]{50.0, 95.0, 275.0, 415.0, 485.0, 545.0}),
                    java.util.Arrays.asList(new Double[]{325.0, 340.0, 365.0, 395.0}));

            // Legen Sie Parameter zum Extrahieren von Tabellen fest.
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            //  Führen Sie die Tabellenerfassung auf dem geladenen Dokument aus.
            Iterable<PageTableArea> tables = parser.getTables(options);

            //  Verarbeiten Sie jede aus dem Ergebnis extrahierte Tabelle.
            for (PageTableArea t : tables) 
            {
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "Erweiterte Inhaltsextraktionswerkzeuge"
  description: "Neben der Lesung von Tabellen unterstützt GroupDocs.Parser die Erfassung von Plain Text, visuellen Elementen, eingebetteten Metadaten und strukturierten Objekten zur Optimierung von Dokumentenverarbeitungsaufgaben."
  image: "/img/parser/features_extract-table.webp" # 500x500 px
  image_description: "Strukturierte Inhalte und tabellarische Daten extrahieren"
  features:
    # feature loop
    - title: "Präzise Tabellenerfassung über Formate hinweg"
      content: "Unterstützung der Tabellenerfassung aus Standarddokumenttypen wie PDF, Word, Excel und HTML mit hoher Genauigkeit."

    # feature loop
    - title: "Lesen tabellarischer Strukturen aus unterschiedlichen Quellen"
      content: "Rufen Sie Tabellendaten aus Tabellenkalkulationen, Dokumenten und Berichten ab und bewahren Sie die Struktur und Ausrichtung."

    # feature loop
    - title: "Anpassbare Einstellungen zur Tabellenerfassung"
      content: "Kontrollieren Sie die Layouterkennung, verwalten Sie Kopf- und Fußzeilen und optimieren Sie die Extraktion mit flexiblen Konfigurationsoptionen."
      
  code_samples:
    # code sample loop
    - title: "Beispiel: Tabellen aus einem Excel-Dokument extrahieren"
      content: |
        Dieses Beispiel zeigt, wie Sie Tabelleninhalte in einer Excel (XLSX)-Datei mit GroupDocs.Parser extrahieren und durchlaufen.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Initialisieren Sie Parser mit der Excel-Datei.
        try (Parser parser = new Parser("input.pdf"))
        {
            // Beenden Sie, wenn die Tabellenerfassung für dieses Dokument nicht unterstützt wird.
            if (!parser.getFeatures().isTables())
            {
                return;
            }

            // Anwenden von Regeln zur Bestimmung des Tabellenlayouts.
            TemplateTableLayout layout = new TemplateTableLayout(
                    java.util.Arrays.asList(new Double[]{50.0, 95.0, 275.0, 415.0, 485.0, 545.0}),
                    java.util.Arrays.asList(new Double[]{325.0, 340.0, 365.0, 395.0}));

            // Einstellungen für die Tabellenerfassung konfigurieren.
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            // Den Extraktionsprozess aufrufen.
            Iterable<PageTableArea> tables = parser.getTables(options);

            // Über alle geparsten Tabellenstrukturen iterieren.
            for (PageTableArea t : tables)
            {
                // Über jede Zeile innerhalb der Tabelle iterieren.
                for (int row = 0; row < t.getRowCount(); row++)
                {
                    // Jede Zelle in der aktuellen Zeile verarbeiten.
                    for (int column = 0; column < t.getColumnCount(); column++) 
                    {
                        // Auf den Inhalt der aktuellen Zelle zugreifen und ihn lesen.
                        PageTableAreaCell cell = t.getCell(row, column);
                        if (cell != null)
                        {
                            // Den Textwert jeder Tabellenzelle ausgeben.
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
    title: "Unterstützte Dokumenttypen für die Tabellenerfassung"
    exclude: "EPUB"
    description: "GroupDocs.Parser bietet zuverlässige Tabellenerkennung über mehrere Dateitypen hinweg. Hier ist eine Liste der am häufigsten unterstützten Dokumentenformate zur Extraktion von Tabellen."
    items: 
        # format loop 1
        - name: "PDF parsen"
          format: "PDF"
          link: "/parser/java/extract-table/pdf/"
          description: "(Portable Document Format)"
          
        # format loop 2
        - name: "DOCX parsen"
          format: "DOCX"
          link: "/parser/java/extract-table/docx/"
          description: "(Office 2007+ Word-Dokument)"
          
        # format loop 3
        - name: "PPTX parsen"
          format: "PPTX"
          link: "/parser/java/extract-table/pptx/"
          description: "(Open XML-Präsentationsformat)"
          
        # format loop 4
        - name: "XLSX parsen"
          format: "XLSX"
          link: "/parser/java/extract-table/xlsx/"
          description: "(Open XML-Arbeitsmappe)"
          
        # format loop 5
        - name: "TXT parsen"
          format: "TXT"
          link: "/parser/java/extract-table/txt/"
          description: "(Textdatei)"
          
        # format loop 6
        - name: "RTF parsen"
          format: "RTF"
          link: "/parser/java/extract-table/rtf/"
          description: "(Rich Text Format)"
          
        # format loop 7
        - name: "XML parsen"
          format: "XML"
          link: "/parser/java/extract-table/xml/"
          description: "(eXtensible Markup Language)"
          
        # format loop 8
        - name: "EPUB parsen"
          format: "EPUB"
          link: "/parser/java/extract-table/epub/"
          description: "(Open eBook-Datei)"
         
          

---