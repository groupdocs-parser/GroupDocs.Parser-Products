


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:26
draft: false
lang: de
format: Rtf
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "Hyperlinks aus RTF-Dateien in C#-Apps extrahieren"
head_description: "GroupDocs.Parser verwenden, um Hyperlinks aus RTF-Dateien in C# ohne zusätzliche Werkzeuge oder Software zu erkennen und zu extrahieren."

############################# Header ############################
title: "Hyperlinks aus RTF mit C# extrahieren" 
description: "URLs und Hyperlinks aus PDF-, Word-, Excel- und anderen Dokumenttypen mithilfe von GroupDocs.Parser in Ihren .NET-Anwendungen erkennen und extrahieren."
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Kostenlose Testversion herunterladen"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "Über die GroupDocs.Parser for .NET API"
    link: "/parser/net/"
    link_title: "Mehr erfahren"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/) ist eine vielseitige API zum Parsen von Dokumenten für .NET-Entwickler. Sie unterstützt die Extraktion von Hyperlinks, Texten, Bildern und strukturierten Inhalten aus verschiedenen Dateiformaten wie PDF, Word, Excel, HTML und mehr — ohne auf externe Software angewiesen zu sein.

############################# Steps ############################
steps:
    enable: true
    title: "Schritte zum Extrahieren von Hyperlinks aus Rtf in C#"
    content: |
      [GroupDocs.Parser](/parser/net/) ermöglicht es .NET-Entwicklern, Hyperlinks aus RTF-Dateien durch Befolgung dieser einfachen Schritte zu extrahieren:
      
      1. RTF-Datei mit einer Parser-Instanz laden.
      2. Überprüfen Sie, ob das Dokument die Extraktion von Hyperlinks unterstützt.
      3. Die Liste der Hyperlinks aus dem Dokument abrufen.
      4. Durch die Ergebnisse iterieren und mit den extrahierten URLs arbeiten.
   
    code:
      platform: "net"
      copy_title: "Kopieren"
      install:
        command: |
        command: "dotnet add package GroupDocs.Parser"
        copy_tip: "Klicken zum Kopieren"
        copy_done: "Kopiert"
      links:
        #  loop
        - title: "Weitere Beispiele"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
        #  loop
        - title: "Dokumentation"
          link: "https://docs.groupdocs.com/parser/net/"
          
      content: |
        ```csharp {style=abap}
        // Laden Sie das Dokument mit Hyperlinks unter Verwendung der Parser-Klasse
        using (Parser parser = new Parser("input.rtf")) {

            // Überprüfen Sie, ob die Datei die Extraktion von Hyperlinks unterstützt
            if (!parser.Features.Hyperlinks)
            {
                Console.WriteLine("Die Hyperlink-Extraktion ist für die Datei nicht verfügbar");
                return;
            }

            // Extrahierte Hyperlinks abrufen und verarbeiten
            IEnumerable<PageHyperlinkArea> hyperlinks = parser.GetHyperlinks();

            foreach (PageHyperlinkArea h in hyperlinks)
            {
                Console.WriteLine(h.Text);
                Console.WriteLine(h.Url);
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "Erweiterte Dokumentenverarbeitungsfunktionen"
  description: "Neben der Extraktion von Hyperlinks ermöglicht GroupDocs.Parser die Extraktion von Texten, Metadaten, Bildern und strukturierten Daten – und unterstützt leistungsstarke Datenverarbeitungs-Workflows."
  image: "/img/parser/features_extract-hyperlink.webp" # 500x500 px
  image_description: "Erkennung von Hyperlinks und Dokumentenverarbeitung"
  features:
    # feature loop
    - title: "Erkennung von Hyperlinks aus Dokumenten"
      content: "URLs und Linkannotationen schnell aus Dokumenten wie PDFs, Word-Dateien, Tabellenkalkulationen und mehr extrahieren."

    # feature loop
    - title: "Unterstützung für Web- und eingebettete Links"
      content: "Standard-Web-URLs und eingebettete Dokumentenlinks über mehrere Formate hinweg erkennen und extrahieren."

    # feature loop
    - title: "Flexible Parsing-Optionen"
      content: "Extraktionseinstellungen anpassen, um bestimmte Abschnitte oder Seiten zu scannen und so Leistung und Genauigkeit zu verbessern."
      
  code_samples:
    # code sample loop
    - title: "Wie man Hyperlinks aus einer PDF mit Linkoptionen extrahiert"
      content: |
        Dieses Codebeispiel zeigt, wie man alle Hyperlinks aus einer PDF-Datei unter Verwendung benutzerdefinierter Optionen extrahiert.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Initialisieren Sie die Parser mit dem PDF-Dokument
        using (Parser parser = new Parser("input.docx"))
        {
            // Überprüfen Sie, ob die Hyperlink-Extraktion unterstützt wird
            if (!parser.Features.Hyperlinks)
            {
                return;
            }

            // Link-Extraktionsoptionen festlegen, um Ergebnisse einzugrenzen
            PageAreaOptions options = new PageAreaOptions(new Rectangle(new Point(380, 90), new Size(150, 50)));

            // Hyperlinkdaten aus dem Dokument extrahieren
            IEnumerable<PageHyperlinkArea> hyperlinks = parser.GetHyperlinks(options);

            // Die Liste der extrahierten Links verarbeiten
            foreach (PageHyperlinkArea h in hyperlinks)
            {
                Console.WriteLine(h.Text);
                Console.WriteLine(h.Url);
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
    - title: "Nuget herunterladen"
      link: "https://releases.groupdocs.com/parser/net/"
      color: "red"
        #  loop
    - title: "Lizenzierung"
      link: "https://purchase.groupdocs.com/pricing/parser/net/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "Unterstützte Formate für die Hyperlink-Extraktion"
    exclude: "RTF"
    description: "GroupDocs.Parser kann Hyperlinks aus einer Vielzahl von Dokumenttypen extrahieren. Unten sehen Sie die häufig unterstützten Formate."
    items: 
        # format loop 1
        - name: "PDF parsen"
          format: "PDF"
          link: "/parser/net/extract-hyperlink/pdf/"
          description: "(Portable Document Format)"
          
        # format loop 2
        - name: "DOCX parsen"
          format: "DOCX"
          link: "/parser/net/extract-hyperlink/docx/"
          description: "(Office 2007+ Word-Dokument)"
          
        # format loop 3
        - name: "PPTX parsen"
          format: "PPTX"
          link: "/parser/net/extract-hyperlink/pptx/"
          description: "(Open XML-Präsentationsformat)"
          
        # format loop 4
        - name: "XLSX parsen"
          format: "XLSX"
          link: "/parser/net/extract-hyperlink/xlsx/"
          description: "(Open XML-Arbeitsmappe)"
          
        # format loop 5
        - name: "TXT parsen"
          format: "TXT"
          link: "/parser/net/extract-hyperlink/txt/"
          description: "(Textdatei)"
          
        # format loop 6
        - name: "RTF parsen"
          format: "RTF"
          link: "/parser/net/extract-hyperlink/rtf/"
          description: "(Rich Text Format)"
          
        # format loop 7
        - name: "XML parsen"
          format: "XML"
          link: "/parser/net/extract-hyperlink/xml/"
          description: "(eXtensible Markup Language)"
          
        # format loop 8
        - name: "EPUB parsen"
          format: "EPUB"
          link: "/parser/net/extract-hyperlink/epub/"
          description: "(Open eBook-Datei)"
         
          

---