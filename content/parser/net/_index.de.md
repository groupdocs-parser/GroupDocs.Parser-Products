---
############################# Static ############################
layout: "product"
date: 2021-04-27T09:31:06+03:00
draft: false

product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: ".NET-Parsing-API, extrahieren Sie Metadaten von Textbildern aus PDF Word Excel"
head_description: "C# .NET-Dokumentparsing-API zum Extrahieren von Text, Bildern, Metadaten und Codierung aus Datenbanken, PDF-, Word-, Excel-, Präsentations-, Web-, E-Mail-, EPUB- und ZIP-Dateiformaten."

############################# Header ############################
title: ".NET-API zum Extrahieren von Dokumentdaten"
description: "Bilder, rohen oder formatierten Text und Metadaten aus Dokumenten, Tabellenkalkulationen, Präsentationen, E-Mails und Archiven aus .NET-Apps extrahieren."
button:
    enable: true

############################# SubMenu ############################
submenu:
    enable: true
    
    left:
        img_alt: "GroupDocs.Parser for .NET"
        image: "/border/groupdocs-parser-net.svg"
        product: "GroupDocs.Parser"
        platform: ".NET"

    middle:
        button:
            # button loop
            - link: "#overview"
              text: "Überblick"

            # button loop
            - link: "#features"
              text: "Merkmale"

            # button loop
            - link: "#support"
              text: "Support"

            # button loop
            - link: "https://products.groupdocs.app/parser"
              text: "Live Demo"

            # button loop
            - link: "https://purchase.groupdocs.com/pricing/parser/net"
              text: "Preisgestaltung"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/net/"
        link_buy: "https://purchase.groupdocs.com"

############################# Überblick ############################
overview:
    enable: true
    content: |
      GroupDocs.Parser für .NET ist eine Text-, Metadaten- und Bildextraktions-API für Geschäftsanwendungen, die mit C#, ASP.NET und anderen .NET-Technologien entwickelt wurden. Es unterstützt die Extraktion von rohem, formatiertem und strukturiertem Text sowie Metadaten aus den Dateien unterstützter Formate. Durch GroupDocs.Parser für .NET können Ihre Anwendungen auch passwortgeschützte Dokumente für gängige Formate wie Textverarbeitungsdokumente, Excel-Tabellen, PowerPoint-Präsentationen, OneNote, PDF-Dateien und ZIP-Archive parsen.
    tabs:
      enable: true
      
      ## TAB ONE ##
      tab_one:
        description: |
          Nachfolgend finden Sie eine Übersicht über GroupDocs.Parser für .NET:
      
        left:
          enable: true
          icon: "fas fa-tools"
          title: "Merkmale"
          content: |
            * Bilder extrahieren
            * Rohtext extrahieren
            * Formatierten Text extrahieren
            * Strukturierten Text extrahieren
            * Metadaten extrahieren
            * Auszug aus Dateien in ZIP-Datei
            * Durch Suchen extrahieren
            * Mit Textformatierern extrahieren
            * Kodierungsstandard erkennen
            * Medientyp erkennen
        
        right:
          enable: true
          icon: "fab fa-html5"
          title: "Die API"
          content: |
            * Ruft Eingabedatei ab
            * Ruft rohen oder formatierten Text ab
            * Ruft Metadaten ab
      
      ## TAB TWO ##
      tab_two:
        description: |
          GroupDocs.Parser für .NET unterstützt die folgenden [Dokumentdateiformate](https://docs.groupdocs.com/parser/net/supported-document-formats/):

        left:
          enable: true
          table:
            # table loop
            - title: "Textextraktion"
              content: |
                * **Text**: DOC, DOCX, DOT, DOTM, DOTX, DOCM, RTF, ODT, OTT, TXT, MD, WordprocessingML (XML)
                * **Spreadsheets**: XLS, XLSX, CSV, XLSM, XLSB, ODS, SpreadsheetML (XML), XLT, XLTX, XLTM, OTS, XLA,, XLAM, TSV
                * **Präsentationen**: PPT, PPTX, PPTM, PPS, PPSX, PPSM, POT, POTX, POTM, ODP, OTP
                * **OneNote**: EINS
                * **E-Mail**: MSG, EML, EMLX, PST, OST, MS EXCHANGE SERVER, POP, IMAP
                * **Elektronische Veröffentlichung**: EPUB, FB2
                * **Portables Dokument**: PDF, PDF-Portfolio, verschlüsseltes PDF
                * **DOM-basiert**: XML, HTML, XHTML, MHTML
                * **Komprimierung & Verpackung**: ZIP, CHM
                * **Datenbank**: ADO.NET

            # table loop
            - title: "Kodierungserkennung"
              content: |
                * **BOM**: UTF32 LE, UTF32 BE, UTF16 LE, UTF16 BE, UTF8, and UTF7
                * **Inhalt**: UTF32 LE, UTF32 BE, UTF16 LE, UTF16 BE, UTF8, and ANSI

        right:
          enable: true
          table:
            # table loop
            - title: "Metadatenextraktion"
              content: |
                * **Text**: DOC, DOCX, DOT, DOTX, DOTM, OTT, ODT
                * **Tabellenkalkulationen**: XLS, XLSX, XLT, XLTX, XLTM, XLA, XLAM, OTS, ODS
                * **Präsentationen**: PPT, PPTX, POT, POTX, POTM, PPSM, PPTM, OTP, ODP
                * **E-Mail**: MSG, EML, EMLX
                * **Elektronische Veröffentlichung**: EPUB, FB2
                * **Andere**: PDF

            # table loop
            - title: "Text & Metadatenextraktion"
              content: |
                * **Vorlage**: DOTX, POTX
                * **Makrofähige Vorlage**: DOTM, POTM, PPSM, PPTM
                * **OpenDocument-Vorlage**: OTT

            # table loop
            - title: "Bildextraktion"
              content: |
                * **Text**: DOC, DOCX, DOCM, RTF, DOT, DOTM, DOTX, ODT
                * **Tabellen**: XLS, XLSX, XLSM, XLSB, ODS, XLT, XLTM, XLTX
                * **Präsentationen**: PPT, PPTX, PPTM, ODP, POT, POTM, POTX, PPS, PPSX, PPSM
                * **Portables Dokument**: PDF, POT, POTM, POTX
                * **Ebook**: CHM, EPUB, FB2
                * **Auszeichnung**: HTML

      ## TAB THREE ##
      tab_three:
        description: |
          GroupDocs.Parser for .NET unterstützt das Folgen Betriebssysteme, Frameworks & Paket-Managers:
        
        left:
          enable: true
          table:
            # table loop
            - icon: "fab fa-windows"
              title: "Betriebssysteme"
              content: |
                * Windows Desktop
                * Windows Server
                * Windows Azure
                * Linux

            # table loop
            - icon: "fas fa-code"
              title: "Unterstützte Frameworks"
              content: |
                * .NET Framework 2.0 oder höher
                * Mono Framework 1.2 oder höher
                * .NET-Standard 2.0
                * .NET Core 2.0

        right:
          enable: true
          table:
            # table loop
            - icon: "fas fa-box"
              title: "Paket-Manager"
              content: |
                * NuGet

            # table loop
            - icon: "fas fa-tools"
              title: "Entwicklungsumgebungen"
              content: |
                * Microsoft Visual Studio
                * Xamarin.Android
                * Xamarin.IOS
                * Xamarin.Mac
                * MonoDevelop

############################# Merkmale ############################
features:
    enable: true
    title: "GroupDocs.Parser for .NET Merkmale"

    feature:
      # feature loop
      - icon: "fas fa-copy"
        content: "Zählen Sie das Vorkommen von Wörtern in einzelnen oder mehreren Dateien statistisch"

      # feature loop
      - icon: "fas fa-eye"
        content: "Extrahieren Sie Text und Metadaten aus Excel-Arbeitsblättern und Präsentationsvorlagen"

      # feature loop
      - icon: "fas fa-bolt"
        content: "Extrahieren Sie Textinhalte aus einer Datei oder einem Stream, ohne Document Reader zu installieren"
      
      # feature loop
      - icon: "fas fa-file-powerpoint"
        content: "Get Formatted Text from a Document using Fast or Standard Textextraktion Mode"

      # feature loop
      - icon: "fas fa-code"
        content: "Erkennen Sie den Medientyp von passwortgeschützten XML-Dokumenten und ziehen Sie Text daraus"

      # feature loop
      - icon: "fas fa-cloud"
        content: "Erhalten Sie programmgesteuert formatierten Text aus E-Mails und Anhängen"

      # feature loop
      - icon: "fas fa-remove-format"
        content: "Zeichnen Sie Text aus einzelnen oder mehreren Seiten eines OneNote-Dokuments heraus"

      # feature loop
      - icon: "fas fa-comment-slash"
        content: "Extrahieren Sie Daten aus PDF-, MS Word-, Excel- und Präsentationsdokumenten"

      # feature loop
      - icon: "fas fa-location-arrow"
        content: "Extrahieren Sie Daten aus den PDF-Formularen und entnehmen Sie Text aus einer einfachen PDF-Datei oder einem PDF-Portfolio-Dokument"

      # feature loop
      - icon: "fas fa-border-all"
        content: "Holen Sie sich formatierten Text aus einer PowerPoint-Präsentation oder vertreiben Sie Text aus einer bestimmten Folie"

      # feature loop
      - icon: "fas fa-wrench"
        content: "Sammeln Sie rohen oder formatierten Text aus Zellen, Zeilen und Spalten aus einer Excel-Tabelle"

      # feature loop
      - icon: "fas fa-columns"
        content: "Extrahieren Sie rohen oder HTML-formatierten Text aus einem Word-Dokument"

      # feature loop
      - icon: "fas fa-file-word"
        content: "HTML-Formatierer unterstützt die Formatierung von Absatz, Hyperlink, Schriftart, Überschriften, Listen und Tabellen"

      # feature loop
      - icon: "fas fa-envelope"
        content: "Ziehen Sie einzelne Sätze oder ganzen Text aus EPUB-, CHM-, Markdown- und FB2-Dateien heraus"

      # feature loop
      - icon: "fas fa-print"
        content: "Auszug aus dem Inhaltsverzeichnis von Datenbanken, PDF, EPUB, CHM & Textverarbeitungsdokumenten"

      # feature loop
      - icon: "fas fa-file-archive"
        content: "Ziehen Sie Text mit intakter Inhaltsstruktur heraus und extrahieren Sie hervorgehobenen Text aus Dokumenten"

      # feature loop
      - icon: "fas fa-lock"
        content: "Erhalten Sie Textbereich aus Dokumenten für die Analyse und zeichnen Sie Metadaten aus unterstützten Dokumentformaten"

      # feature loop
      - icon: "fas fa-file-code"
        content: "Erhalten Sie alle oder ausgewählte Bilder aus unterstützten Formaten und drehen Sie extrahierte Bilder"
      
      # feature loop
      - icon: "fas fa-fill-drip"
        content: "Entnehmen Sie Text aus Dateien in Zip-Archiven und OST-Containern und erkennen Sie Dateitypen von ZIP-Container-Elementen"

      # feature loop
      - icon: "fas fa-file-excel"
        content: "Abrufen von Daten aus E-Mail-Container (Exchange-Webserver, POP3, IMAP)"

      # feature loop
      - icon: "fas fa-heading"
        content: "Suchen Sie in Dokumenten nach einfachem Text, ganzen Wörtern und regulären Ausdrücken"

      # feature loop
      - icon: "fas fa-project-diagram"
        content: "Dokumentvorlage vorbereiten, Daten aus Dokument extrahieren und Datenfelder und Tabellen analysieren"

      # feature loop
      - icon: "fas fa-cube"
        content: "Suchen und extrahieren Sie hervorgehobene Ausdrücke in Dokumenten"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Holen Sie sich Text mit Plain Text Formatter (Einfach & ASCII) oder mit Markdown Formatter"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Markdown Formatter unterstützt die Formatierung von Schriftarten, Hyperlinks, Überschriften, Listen und Tabellen"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Führen Sie eine benutzerdefinierte Formatierung mit Kanten, Winkeln und Schnittpunkten durch, um einfachen Text zu formatieren"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Tabellenlayout verschieben und Tabellen in einem rechteckigen Bereich anhand von Spaltentrennzeichen erkennen"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Extrahieren Sie Text aus Formen, WordArt-Objekten und Textfeldern in Microsoft Office-Dateiformaten"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Bilder in Dateien extrahieren – Speichern im JPG-, PNG-, GIF-, BMP-, PNG- oder WEBP-Format"

    more_feature:
      # more_feature_loop
      - title: "Extrahieren von Text aus einem Dokument"
        content: |
          Die Verwendung von GroupDocs.Parser for .NET API zum Extrahieren von Text aus einem Dokument ist einfach und mit nur wenigen Codezeilen möglich:

          ```cs
          // Erstellen Sie eine Instanz der Parser-Klasse
          using(Parser parser = new Parser("sample.docx"))
          {
            // Text in den Reader extrahieren
            using(TextReader reader = parser.GetText())
            {
              // Text aus dem Dokument drucken
              // Wenn die Textextraktion nicht unterstützt wird, ist reader null
              Console.WriteLine(reader == null ? "Text extraction isn't supported." : reader.ReadToEnd());
            }
          }
          ```

############################# Support ############################
support:
    enable: true

############################# Solutions ############################
solutions:
    enable: true
    title: "GroupDocs.Parser bietet APIs zum Anzeigen von Dokumenten für andere beliebte Entwicklungsumgebungen"

    solution:
        # solution loop
        - img_alt: "GroupDocs.Parser for Java"
          image: "/border/groupdocs-parser-java.svg"
          product: "GroupDocs.Parser"
          platform: "Java"
          link: "/parser/java/"

############################# Back to top ###############################
back_to_top:
  enable: true
---