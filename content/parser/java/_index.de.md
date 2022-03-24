---
############################# Static ############################
layout: "product"
date: 2021-04-27T09:31:06+03:00
draft: false

product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Java-API zum Analysieren von Text, Bildern und Metadaten aus PDF, Word, Excel, HTML"
head_description: "Java-Dokument-Parser-API zum Extrahieren von Text, Bildern, Metadaten und Kodierungen aus Datenbanken, Word, Excel, Präsentationen, PDF-, E-Mail-, EPUB- und ZIP-Dateien."

############################# Header ############################
title: "Java-Parser-API zum Extrahieren von Daten"
description: "Java-API zum Analysieren und Extrahieren von Bildern und Text mit Metadaten aus Dokumenten, Präsentationen, Archiven und E-Mails."
button:
    enable: true

############################# SubMenu ############################
submenu:
    enable: true
    
    left:
        img_alt: "GroupDocs.Parser for Java"
        image: "/border/groupdocs-parser-java.svg"
        product: "GroupDocs.Parser"
        platform: "Java"

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
            - link: "https://purchase.groupdocs.com/pricing/parser/java"
              text: "Preisgestaltung"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/java/"
        link_buy: "https://purchase.groupdocs.com"

############################# Überblick ############################
overview:
    enable: true
    content: |
      GroupDocs.Parser für Java ist eine Text-, Bild- und Metadaten-Extraktions-API, die mehr als 50 gängige Dokumenttypen unterstützt, um die Erstellung von Geschäftsanwendungen mit Funktionen zum Analysieren von rohem, strukturiertem und formatiertem Text zu unterstützen. Es unterstützt auch das Parsen von Dokumenten mit vordefinierten Vorlagen und ermöglicht das schnelle und genaue Extrahieren komplexer Daten aus Rechnungen und anderen typischen Dokumenten. Mit GroupDocs.Parser für Java können Sie Text und Metadaten aus passwortgeschützten Dateien aller gängigen Formate extrahieren, darunter Textverarbeitungsdokumente, Excel-Tabellen, PowerPoint-Präsentationen, OneNote, PDF-Dateien und ZIP-Archive.
    tabs:
      enable: true     
      
      ## TAB ONE ##
      tab_one:
        description: |
          Nachfolgend finden Sie eine Übersicht über GroupDocs.Parser für Java:

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
          GroupDocs.Parser for Java unterstützt folgende [Dokumentdateiformate](https://docs.groupdocs.com/parser/java/supported-document-formats/):

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
                * **BOM**: UTF32 LE, UTF32 BE, UTF16 LE, UTF16 BE, UTF8 und UTF7
                * **Inhalt**: UTF32 LE, UTF32 BE, UTF16 LE, UTF16 BE, UTF8 und ANSI

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
          GroupDocs.Parser for Java unterstützt das Folgen Betriebssysteme:
        
        left:
          enable: true
          table:
            # table loop
            - icon: "fab fa-windows"
              title: "Betriebssysteme"
              content: |
                * Microsoft Windows Desktop
                * Microsoft Windows Server
                * Linux
                * MacOS

            # table loop
            - icon: "fas fa-code"
              title: "Unterstützte Frameworks"
              content: |
                * Java 7 (1.7) und höher

        right:
          enable: true
          table:
            # table loop
            - icon: "fas fa-cogs"
              title: "Entwicklungsumgebungen"
              content: |
                * NetBeans
                * IntelliJ IDEA
                * Eclipse
            # table loop
            - icon: "fas fa-tools"
              title: "Build-Automatisierungstool"
              content: |
                * Maven

############################# Merkmale ############################
features:
    enable: true
    title: "GroupDocs.Parser for Java Merkmale"

    feature:
      # feature loop
      - icon: "fas fa-copy"
        content: "Zählen Sie das Wortvorkommen für einzelne oder mehrere Dokumente statistisch"

      # feature loop
      - icon: "fas fa-eye"
        content: "Extrahieren Sie Text und Metadaten aus Excel-Tabellen und PowerPoint-Präsentationsvorlagen"

      # feature loop
      - icon: "fas fa-bolt"
        content: "Text aus einer Datei oder einem Stream abrufen, ohne Document Reader zu installieren"
      
      # feature loop
      - icon: "fas fa-file-powerpoint"
        content: "Pull Out Formatted Text from a Document Using Fast or Standard Textextraktion Mode"

      # feature loop
      - icon: "fas fa-code"
        content: "Erkennen Sie den Medientyp passwortgeschützter XML-Dokumente und extrahieren Sie Text daraus"

      # feature loop
      - icon: "fas fa-cloud"
        content: "Holen Sie formatierten Text aus PowerPoint-Präsentationen, E-Mails und Anhängen programmgesteuert"

      # feature loop
      - icon: "fas fa-remove-format"
        content: "Vertreiben Sie Text aus einzelnen oder mehreren Seiten eines OneNote-Dokuments"

      # feature loop
      - icon: "fas fa-comment-slash"
        content: "Ziehen Sie Rohtext aus einer einfachen PDF-Datei oder einem PDF-Portfolio-Dokument heraus"

      # feature loop
      - icon: "fas fa-location-arrow"
        content: "Extrahieren Sie Daten aus PDF-, MS Word-, Excel- und Präsentationsdokumenten"

      # feature loop
      - icon: "fas fa-border-all"
        content: "Extrahieren Sie rohen oder formatierten Text aus Zellen, Zeilen und Spalten aus einer Excel-Tabelle"

      # feature loop
      - icon: "fas fa-wrench"
        content: "Sammeln Sie rohen oder HTML-formatierten Text aus Word-Dokumenten und extrahieren Sie markierten Text aus Dokumenten"

      # feature loop
      - icon: "fas fa-columns"
        content: "Holen Sie sich Daten aus den PDF-Formularen und erhalten Sie eine formatierte Tabelle aus einem PDF- oder Word-Dokument"

      # feature loop
      - icon: "fas fa-file-word"
        content: "Ziehen Sie einzelne Sätze oder ganzen Text aus EPUB-, CHM-, Markdown- und FB2-Dateien heraus"

      # feature loop
      - icon: "fas fa-envelope"
        content: "Excerpt Table of Contents from Datenbanks, PDF, EPUB, CHM & Word Processing Documents"

      # feature loop
      - icon: "fas fa-print"
        content: "Textbereich aus Dokumenten zur Analyse abrufen und Text mit intakter Inhaltsstruktur herausziehen"

      # feature loop
      - icon: "fas fa-file-archive"
        content: "Abrufen von Metadaten aus unterstützten Dokumentformaten"

      # feature loop
      - icon: "fas fa-lock"
        content: "Alle oder ausgewählte Bilder aus unterstützten Formaten herausziehen und extrahierte Bilder drehen"

      # feature loop
      - icon: "fas fa-file-code"
        content: "Extract Text from Files within Zip Archives & OST Containers – Medientyp erkennens for Zip Container Items"
      
      # feature loop
      - icon: "fas fa-fill-drip"
        content: "Abrufen von Daten aus E-Mail-Container (Exchange-Webserver, POP3, IMAP)"

      # feature loop
      - icon: "fas fa-heading"
        content: "Finden Sie einfachen Text, ganze Wörter und reguläre Ausdrücke in Dokumenten"

      # feature loop
      - icon: "fas fa-project-diagram"
        content: "Dokumentvorlage vorbereiten, Daten aus Dokument extrahieren und Datenfelder und Tabellen analysieren"

      # feature loop
      - icon: "fas fa-cube"
        content: "Hervorgehobene Ausdrücke in Dokumenten suchen und extrahieren"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Ziehen Sie Text mit dem Nur-Text-Formatierer (einfach und ASCII) oder benutzerdefinierter Formatierung mit Kanten, Winkeln und Schnittpunkten heraus"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Abrufen und formatieren Sie Text (Schriftarten, Hyperlinks, Überschriften, Listen und Tabellen) mit dem Markdown-Formatierer"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Holen Sie sich Text mit HTML-Formatierer und wenden Sie den Formatierer auf Absatz, Hyperlink, Schriftart, Überschriften, Listen und Tabellen an"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Tabellenlayout verschieben und Tabellen in einem rechteckigen Bereich anhand von Spaltentrennzeichen erkennen"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Extrahieren Sie Text aus Formen, WordArt-Objekten und Textfeldern in Microsoft Office-Dateiformaten"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Extract Text from Email Servers and Datenbanks via JDBC"

    more_feature:
      # more_feature_loop
      - title: "Holen Sie sich Text mit Nur-Text- oder HTML-Formatierern"
        content: |
          Mit GroupDocs.Parser für Java können Sie verschiedene Formatierer auf Text und HTML anwenden. Sie können Text mit Plain Text Formatter sowohl für Einfach als auch für ASCII abrufen. Sie können auch Text mit HTML-Formatierer abrufen und Formatierungen auf Absätze, Hyperlinks, Schriftarten, Überschriften, Listen und Tabellen anwenden.

############################# Support ############################
support:
    enable: true

############################# Solutions ############################
solutions:
    enable: true
    title: "GroupDocs.Parser bietet APIs zum Anzeigen von Dokumenten für andere beliebte Entwicklungsumgebungen"

    solution:
        # solution loop
        - img_alt: "GroupDocs.Parser for .NET"
          image: "/border/groupdocs-parser-net.svg"
          product: "GroupDocs.Parser"
          platform: ".NET"
          link: "/parser/net/"

############################# Back to top ###############################
back_to_top:
  enable: true
---