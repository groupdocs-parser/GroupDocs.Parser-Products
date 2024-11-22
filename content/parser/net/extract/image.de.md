---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:10
draft: false
otherformats: doc docm docx dot dotm dotx epub html mht mhtml odp ods odt one otp ott pdf

############################# Head ############################
head_title: "Extrahieren Sie Bilder aus Excel, Word, PDF und anderen Dokumenten oder Seiten über .NET"
head_description: "Mit der GroupDocs.Parser .NET API können Softwareprogrammierer Bilder aus verschiedenen Dokumenten wie MS Excel, Word, PowerPoint, PDF und mehr in ihren .NET Apps extrahieren."

############################# Header ############################
title: "Extrahieren Sie Bilder aus PDF, DOCX, PPTX, MSG, XLSX Dokumenten und Seiten über die C#.NET API"
description: "Mit der API GroupDocs.Parser .NET können Programmierer Bilder aus PDF, DOC, DOCX, PPT, PPTX, EML, MSG, XLS, XLSX und CSV extrahieren , ODT, RTF und EPUB Dokumente oder Dokumentseiten."
bg_image: "https://cms.admin.containerize.com/templates/aspose/App_Themes/V3/images/bg/header1.png"
bg_overlay: false
button:
    enable: true
    icon: "fas fa-arrow-down"
    label: "Download kostenlose Testversion"
    link: "https://downloads.groupdocs.com/parser/net"

############################# SubMenu ############################
submenu:
    enable: true

    left:
        img_alt: "GroupDocs.Parser for .NET"
        image: "https://cms.admin.containerize.com/templates/groupdocs/images/product-logos/90x90-noborder/groupdocs-parser-net.png"
        product: "GroupDocs.Parser"
        platform: ".NET"

    middle:
        button:

            # button loop
            - link: "https://apireference.groupdocs.com/parser/net"
              text: "API-Referenz"

            # button loop
            - link: "https://github.com/groupdocs-parser"
              text: "Codebeispiele"

            # button loop
            - link: "https://products.groupdocs.app/parser/family"
              text: "Live-Demos"

            # button loop
            - link: "https://purchase.groupdocs.com/pricing/parser/net"
              text: "Preisgestaltung"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/net"
        link_buy: "https://purchase.groupdocs.com"

############################# About ############################
about:
    enable: true
    title: "Wie extrahiere ich Bilder aus Dokumenten über .NET?"
    content: |
        Bilder können verwendet werden, um Informationen auf eine Weise zu vermitteln, die möglicherweise nicht mit Worten ausgedrückt werden kann. Bilder helfen uns dabei, die Aufmerksamkeit des Benutzers zu erregen und schwierige Konzepte mühelos zu erklären. Manchmal fanden wir beim Lesen von Dokumenten, Zeitschriften oder bei Präsentationen faszinierende Bilder und wollten sie herunterladen. GroupDocs.Parser for .NET ist eine leistungsstarke API, die Benutzern hilft, nützliche Anwendungen zum Extrahieren von Bildern aus verschiedenen Dokumenttypen und zum Speichern dieser in PNG, JPEG, WebP, GIF, BMP und anderen Formaten zu entwickeln. Die API unterstützt die Text- und Bildextraktion aus einigen der am häufigsten verwendeten Dateiformate, z. B. PDF, E-Mails, E-Books, Microsoft Office-Formate: Word (DOC, DOCX), { 284} (PPT, PPTX), Excel (XLS, XLSX), LibreOffice-Formate und viele mehr. Die API unterstützt außerdem vollständig das Parsen von Dokumenten, das Extrahieren von reinem und strukturiertem Text, die Textsuche nach Schlüsselwörtern, das Extrahieren von Metadaten oder Bildern, Containern sowie Anhängen und vieles mehr.
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: "Extrahieren Sie Bilder aus Dokumenten in .NET"
    content_left: |
        [GroupDocs.Parser for .NET](/de/parser/net/) erleichtert C# Entwicklern das Extrahieren von Bildern aus Dokumenten durch die Implementierung einiger einfacher Schritte.
        
        * Instanziieren Sie das [Parser](https://reference.groupdocs.com/net/parser/groupdocs.parser/parser)-Objekt für das ursprüngliche Dokument.
        * Rufen Sie die Methode [GetImages](https://reference.groupdocs.com/net/parser/groupdocs.parser/parser/methods/getimages) auf und rufen Sie eine Sammlung von Bildobjekten ab.
        * Überprüfen Sie, ob der Reader nicht *null* ist (die Extraktion von Bildern wird für das Dokument unterstützt);
        * Durchlaufen Sie die Sammlung und ermitteln Sie Größen, Bildtypen und Bildinhalte.

    title_right: "Erfahren Sie mehr über die Bildextraktion"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/net/extract-images-from-document/">So extrahieren Sie Bilder aus einem Dokument</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-images-from-document-page/">So extrahieren Sie Bilder von einer Dokumentseite</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-images-from-document-page-area/">So extrahieren Sie Bilder aus dem Seitenbereich eines Dokuments</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-images-to-files/">So extrahieren Sie Bilder in Dateien</a>

    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="So extrahieren Sie Bilder aus Dokumenten mithilfe des Beispielcodes C#">}}

        ```csharp    
        // Extrahieren Sie Bilder aus Dokumenten mithilfe der GroupDocs.Parser-API
        // Erstellen Sie eine Instanz der Parser-Klasse
        using (Parser parser = new Parser(filePath)) {
            // Bilder extrahieren
            IEnumerable<PageImageArea> images = parser.GetImages();
            // Überprüfen Sie, ob die Bildextraktion unterstützt wird
            if (images == null) {
                Console.WriteLine("Das Extrahieren von Bildern wird nicht unterstützt");
                return;
            }
            // Über Bilder iterieren
            foreach (PageImageArea image in images) {
                // Drucken Sie einen Seitenindex, ein Rechteck und einen Bildtyp:
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Type: {2}", image.Page.Index, image.Rectangle, image.FileType));
            }
        }
        ```
     {{< /parser/code-parser >}}

############################# More ############################
more:
    enable: true
    title_left: "System Anforderungen"
    content_left: |
        GroupDocs.Parser for .NET APIs werden auf allen wichtigen Plattformen und Betriebssystemen unterstützt. Bevor Sie den folgenden Code ausführen, stellen Sie bitte sicher, dass die folgenden Voraussetzungen auf Ihrem System installiert sind.
        
        * Betriebssysteme: Microsoft Windows, Linux, MacOS
        * Entwicklungsumgebungen: Microsoft Visual Studio, Xamarin, MonoDevelop
        * Rahmenwerke
        * Laden Sie die neueste Version von GroupDocs.Parser for .NET von [Nuget](https://www.nuget.org/packages/groupdocs.parser) herunter.

    title_right: "Warum GroupDocs.Parser for .NET verwenden?"
    content_right: |
        * Unterstützung für die Extraktion von Klartext aus allen unterstützten Dokumenten    
        * Parsen von Dokumenten über benutzerdefinierte Vorlagen    
        * Vollständige Unterstützung der strukturierten Textextraktion    
        * Textsuche über Schlüsselwörter sowie reguläre Ausdrücke    
        * Extrahieren Sie formatierten Text, Metadaten, Bilder, Container und Anhänge    
        * Extrahieren Sie das Inhaltsverzeichnis für einige unterstützte Dokumentformate    
        * Analysieren Sie Formulardaten aus PDF-Dokumenten    
        * Extrahieren Sie Hyperlinks aus dem Dokument   

############################# Demos ############################
demos:
    enable: true
    title: "Live-Demos – Bilder aus Dokumenten online extrahieren"
    content: |
       Extrahieren Sie jetzt Bilder aus Dokumenten, indem Sie die Website [GroupDocs.Parser Live Demos](https://products.groupdocs.app/parser/images/) besuchen.
       Die Live-Demo bietet folgende Vorteile.
        
############################# About Formats ############################
about_formats:
    enable: true

############################# More Formats ############################
more_formats:
    enable: true
    title: "Extrahieren Sie Bilder aus anderen Dokumentformaten"
    content: |
        .NET API zum Parsen und Extrahieren von Bildern für Dateiformate und Bilder. Extrahieren Sie Daten für einige der gängigen Dateiformate, wie unten aufgeführt.

############################# Back to top ###############################
back_to_top:
    enable: true
---