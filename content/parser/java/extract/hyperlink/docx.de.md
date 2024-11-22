---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:06
draft: false
otherformats: dot dotm dotx epub html mht mhtml odp ods odt one otp ott pdf pps ppsx
ext: docx

############################# Head ############################
head_title: "Extrahieren Sie Hyperlinks aus Dokumenten in Java"
head_description: "Mit der GroupDocs.Parser for Java-API können Entwickler Hyperlinks aus Dokumenten, Dokumentseiten oder bestimmten Seitenbereichen von Excel, PowerPoint, PDF, Outlook und mehr extrahieren."

############################# Header ############################
title: "Java API zum Extrahieren von Hyperlinks aus Dokumenten, Seiten oder bestimmten Seitenbereichen"
description: "Die API GroupDocs.Parser for Java erleichtert Entwicklern die Arbeit, indem sie ihnen das Extrahieren von Hyperlinks aus Dokumenten, der Dokumentseite oder einem bestimmten Seitenbereich von PDF, DOCX, PPTX, EML, MSG, XLS, {322 ermöglicht }, CSV, RTF, EPUB und viele mehr."
bg_image: "https://cms.admin.containerize.com/templates/aspose/App_Themes/V3/images/bg/header1.png"
bg_overlay: false
button:
    enable: true
    icon: "fas fa-arrow-down"
    label: "Download kostenlose Testversion"
    link: "https://downloads.groupdocs.com/parser/java"

############################# SubMenu ############################
submenu:
    enable: true

    left:
        img_alt: "GroupDocs.Parser for Java"
        image: "https://cms.admin.containerize.com/templates/groupdocs/images/product-logos/90x90-noborder/groupdocs-parser-java.png"
        product: "GroupDocs.Parser"
        platform: "Java"

    middle:
        button:

            # button loop
            - link: "https://apireference.groupdocs.com/parser/java"
              text: "API-Referenz"

            # button loop
            - link: "https://github.com/groupdocs-parser"
              text: "Codebeispiele"

            # button loop
            - link: "https://products.groupdocs.app/parser/family"
              text: "Live-Demos"

            # button loop
            - link: "https://purchase.groupdocs.com/pricing/parser/java"
              text: "Preisgestaltung"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/java"
        link_buy: "https://purchase.groupdocs.com"

############################# About ############################
about:
    enable: true
    title: "Wie kann ich Hyperlinks aus DOCX-Dokumenten über die Java-API analysieren und extrahieren?"
    content: |
        Ein Hyperlink ist ein Textstück, ein Bild oder ein Symbol, das auf ein gesamtes Dokument oder auf einen bestimmten Teil innerhalb eines Dokuments verweist. Durch die Verwendung von Hyperlinks können Benutzer zu einer Webseite oder einem Dokument navigieren. Oft ist es erforderlich, Hyperlinks aus einem Dokument zu extrahieren und diese für den Zugriff auf ein externes Dokument oder eine Webseite zu verwenden. GroupDocs.Parser for Java ist eine faszinierende API zur Extraktion von Dokumententexten, die vollständige Funktionalität für die Implementierung von Text- und Metadatenextraktionslösungen bietet. Es unterstützt die Extraktion von Text und Hyperlinks aus den Formaten PDF, E-Mails, E-Books und Microsoft Office: Word (DOC, DOCX), PowerPoint (PPT, PPTX), Excel ( XLS, XLSX), LibreOffice-Formate und viele mehr. Es unterstützt mehrere erweiterte Funktionen zum Parsen von Dokumenten, zum Extrahieren von einfachem und strukturiertem Text, zur Textsuche nach Schlüsselwörtern, zum Extrahieren von Metadaten oder Bildern, Containern sowie Anhängen und vielem mehr.
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: "Extrahieren Sie Hyperlinks von DOCX in Java"
    content_left: |
        [GroupDocs.Parser for Java](/de/parser/java/) erleichtert Java-Entwicklern das Extrahieren von Hyperlinks aus einer DOCX-Datei durch die Implementierung einiger einfacher Schritte.
        
        * Instanziieren Sie das [Parser](https://reference.groupdocs.com/java/parser/com.groupdocs.parser/Parser)-Objekt für das ursprüngliche Dokument.
        * Überprüfen Sie, ob das Dokument die Hyperlink-Extraktion unterstützt.
        * Rufen Sie die Methode [getHyperlinks](https://reference.groupdocs.com/parser/java/com.groupdocs.parser/parser/#getHyperlinks--) auf und rufen Sie die Sammlung von [PageHyperlinkArea](https://reference.groupdocs.com/parser/java/com.groupdocs.parser.data/PageHyperlinkArea) Objekte ab;
        * Durchlaufen Sie die Sammlung und erhalten Sie einen Hyperlinktext und eine URL.

    title_right: "Erfahren Sie mehr über die Extraktion von Hyperlinks"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/java/extract-hyperlinks-from-document/">So extrahieren Sie Hyperlinks aus einem Dokument</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-hyperlinks-from-document-page/">So extrahieren Sie Hyperlinks von einer Dokumentseite</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-hyperlinks-from-document-page-area/">So extrahieren Sie Hyperlinks aus dem Seitenbereich des Dokuments</a>
    
    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="So extrahieren Sie Hyperlinks aus der Datei DOCX mithilfe des Beispielcodes Java">}}

        ```java    
        // Extrahieren Sie Hyperlinks aus der Datei DOCX mit der API GroupDocs.Parser
        // Erstellen Sie eine Instanz der Parser-Klasse
        try (Parser parser = new Parser(Constants.HyperlinksPdf)) {
            // Überprüfen Sie, ob das Dokument die Hyperlink-Extraktion unterstützt
            if (!parser.getFeatures().isHyperlinks()) {
                System.out.println("Das Dokument unterstützt die Hyperlink-Extraktion nicht.");
                return;
            }
            // Extrahieren Sie Hyperlinks aus dem Dokument
            Iterable<PageHyperlinkArea> hyperlinks = parser.getHyperlinks();
            // Iterieren Sie über Hyperlinks
            for (PageHyperlinkArea h : hyperlinks) {
                // Drucken Sie den Hyperlinktext aus
                System.out.println(h.getText());
                // Drucken Sie die Hyperlink-URL aus
                System.out.println(h.getUrl());
                System.out.println();
            }
        }
        ```
     {{< /parser/code-parser >}}

############################# More ############################
more:
    enable: true
    title_left: "System Anforderungen"
    content_left: |
        GroupDocs.Parser for Java APIs werden auf allen wichtigen Plattformen und Betriebssystemen unterstützt. Bevor Sie den folgenden Code ausführen, stellen Sie bitte sicher, dass die folgenden Voraussetzungen auf Ihrem System installiert sind.
        
        * Betriebssysteme: Microsoft Windows, Linux, MacOS
        * Entwicklungsumgebungen: NetBeans, Intellij IDEA, Eclipse, etc.
        * Rahmenwerke
        * Laden Sie die neueste Version von GroupDocs.Parser for Java von [Maven](https://repository.groupdocs.com/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs-parser) herunter.

    title_right: "Warum GroupDocs.Parser for Java verwenden?"
    content_right: |
        * Unterstützung für die Extraktion von Klartext aus allen unterstützten Dokumenten    
        * Parsen von Dokumenten über benutzerdefinierte Vorlagen    
        * Vollständige Unterstützung der strukturierten Textextraktion    
        * Textsuche über Schlüsselwörter sowie reguläre Ausdrücke    
        * Extrahieren Sie formatierten Text, Metadaten, Bilder, Container und Anhänge    
        * Extrahieren Sie das Inhaltsverzeichnis für einige unterstützte Dokumentformate    
        * Analysieren Sie Formulardaten aus PDF-Dokumenten    
        * Extrahieren Sie Hyperlinks aus dem Dokument   
        
############################# About Formats ############################
about_formats:
    enable: true

############################# More Formats ############################
more_formats:
    enable: true
    title: "Extrahieren Sie Hyperlinks aus anderen Dokumentformaten"
    content: |
        Java API zum Parsen und Extrahieren von Hyperlinks für Dateiformate und Bilder. Extrahieren Sie Daten für einige der gängigen Dateiformate, wie unten aufgeführt.

############################# Back to top ###############################
back_to_top:
    enable: true
---