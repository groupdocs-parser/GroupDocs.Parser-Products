---
############################# Static ############################
layout: "landing"
date: 2025-12-09T14:10:41
draft: false

lang: de
product: "Parser"
product_tag: "parser"
platform: "Net"
platform_tag: "net"

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
head_title: "GroupDocs.Parser for .NET Document Parser SDK für .NET"
head_description: "Leistungsstarkes Document Parser SDK für .NET. Extrahiert Text, Bilder, Metadaten, Barcodes, Tabellen und andere Daten aus PDF, Word, Excel, E‑Mails und über 50 Dokumentformaten."

############################# Header ############################
title: "Document Parser SDK für .NET"
description: "Fügen Sie Ihren .NET‑Apps eine schnelle und präzise Dokumentenparsing hinzu und extrahieren Sie Text, Bilder, Metadaten und strukturierte Daten aus Dokumenten und Bildern."
words:
  for: "für"

actions:
  main: "Nuget Download"
  main_link: "https://www.nuget.org/packages/GroupDocs.Parser"
  alt: "Lizenzierung"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/net/"
  title: "Bereit, loszulegen?"
  description: "Testen Sie die GroupDocs.Parser-Funktionen kostenlos oder fordern Sie eine Lizenz an"

release:
  title: "Version {0} veröffentlicht"
  notes: "Erfahren Sie, was neu ist"
  downloads: "Downloads"

code:
  title: "Dokumentinhalt schnell mit dem SDK parsen"
  more: "Weitere Beispiele"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
  install: "dotnet add package GroupDocs.Parser"
  content: |
    ```csharp {style=abap}   
    // Übergeben Sie die Quelldatei an die Parser‑Instanz
    using (var parser = new Parser("source.pdf"))
    {
        // Übergeben Sie den Dokumententext an TextReader
        using (var textReader = parser.GetText())
        {
            // Dokumententext verarbeiten
            Console.WriteLine(textReader?.ReadToEnd());
        }
    }  
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser auf einen Blick"
  description: "Document Parser SDK für hochpräzises Dokumentenparsing in .NET‑Anwendungen"
  features:
    # feature loop
    - title: "Daten aus Dokumenten extrahieren"
      content: "GroupDocs.Parser for .NET API ermöglicht das Abrufen von Text, Metadaten und Bildern aus einer Vielzahl von Dateiformaten wie Office-Dokumenten, E‑Mails, Anhängen und Archiven. Dieses leistungsstarke Werkzeug hilft Ihnen, effizient auf wertvolle Informationen in diesen Dateien zuzugreifen und sie zu verarbeiten, z. B. für Datenanalyse, Suchmaschinen‑Indexierung oder Content‑Management‑Systeme."

    # feature loop
    - title: "Dokumente parsen"
      content: "Extrahieren Sie verschiedene Elemente wie Hyperlinks, Tabellen, QR‑Codes, Barcodes und Daten aus PDF‑Formularen. Außerdem können Sie beliebige Informationen aus Dokumenten mithilfe benutzerdefinierter Vorlagen parsen."

    # feature loop
    - title: "Ergebnisse anpassen"
      content: ".NET API ermöglicht das Abrufen von Daten in verschiedenen Formaten wie Rohdaten, strukturiert, HTML oder Markdown. Zusätzlich bietet die API eine Suchfunktion, um bestimmte Wörter oder Phrasen im Text von Dokumenten zu finden."

############################# Platforms ############################
platforms:
  enable: true
  title: "Plattformunabhängigkeit"
  description: "GroupDocs.Parser for .NET unterstützt die folgenden Betriebssysteme, Frameworks und Paketmanager"
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
    - title: "VS Code"
      image: "vs_code"
    # platform loop
    - title: "ReSharper"
      image: "resharper"
    # platform loop
    - title: "macOS"
      image: "finder"
    # platform loop
    - title: "Linux"
      image: "linux"
    # platform loop
    - title: "NuGet"
      image: "nuget"

############################# File formats ############################
formats:
  enable: true
  title: "Unterstützte Dateiformate"
  description: |
    GroupDocs.Parser for .NET unterstützt Vorgänge mit den folgenden [Dateiformaten](https://docs.groupdocs.com/parser/net/supported-document-formats/).
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
  title: "GroupDocs.Parser for .NET Funktionen"
  description: "Extrahieren Sie Daten aus PDFs, Office‑Dokumenten, Bildern und anderen Formaten schnell und präzise mit unserem .NET Document Parser SDK"

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
  description: "Einige Anwendungsfälle typischer GroupDocs.Parser for .NET-Operationen"
  items:
    # code sample loop
    - title: "Bilder aus PDF-Dokumenten extrahieren"
      content: |
        GroupDocs.Parser for .NET erleichtert C# Entwicklern das Extrahieren von Bildern aus [Dokumenten](https://docs.groupdocs.com/parser/net/extract-images-from-documents/):
        {{< landing/code title="Bilder aus PDF-Dokumenten in C# extrahieren">}}
        ```csharp {style=abap}
        // Erstellen Sie eine Instanz der Klasse Parser
        using (var parser = new Parser("source.pptx"))
        {
            // Bilder extrahieren
            var images = parser.GetImages();

            // Prüfen, ob etwas extrahiert wurde
            if (images == null)
            {
                return;
            }
            // Durchlaufen Sie die Bilder
            foreach (PageImageArea image in images)
            {
                // Seitenindex, Rechteck und Bildtyp ausgeben
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Type: {2}", 
                    image.Page.Index, image.Rectangle, image.FileType));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Barcodes aus Bildern extrahieren"
      content: |
        Verwenden Sie unsere .NET‑API, um [Barcodes](https://docs.groupdocs.com/parser/net/extract-barcodes-from-document/) aus Bildern zu extrahieren:
        {{< landing/code title="Barcodes aus Bildern in C# extrahieren">}}
        ```csharp {style=abap}   
        // Quellbild in Parser laden
        using (var parser = new Parser("source.jpg"))
        {
            // Prüfen, ob die Datei die Barcode-Extraktion unterstützt
            if (parser.Features.Barcodes)
            {
                // Barcodes aus der Datei extrahieren
                var barcodes = parser.GetBarcodes();

                // Barcodes durchlaufen
                foreach (var barcode in barcodes)
                {
                    // Seitenindex ausgeben
                    Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                    // Barcode-Wert ausgeben
                    Console.WriteLine("Value: " + barcode.Value);
                }
            }
        }
        ```
        {{< /landing/code >}}

---
