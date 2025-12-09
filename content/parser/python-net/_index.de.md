---
############################# Static ############################
layout: "landing"
date: 2025-12-09T21:34:38
draft: false

lang: de
product: "Parser"
product_tag: "parser"
platform: "Python"
platform_tag: "python-net"

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
head_title: "GroupDocs.Parser for Python via .NET Document Parser SDK für Python"
head_description: "Leistungsstarkes Document Parser SDK für Python. Extrahieren Sie Text, Bilder, Metadaten, Barcodes, Tabellen und andere Daten aus PDF, Word, Excel, E‑Mails und mehr als 50 Dokumentformaten."

############################# Header ############################
title: "Document Parser SDK für Python"
description: "Fügen Sie Ihren Python‑Apps eine schnelle, genaue Dokumenten‑Parsing‑Funktion hinzu und extrahieren Sie Text, Bilder, Metadaten sowie strukturierte Daten aus Dokumenten und Bildern."
words:
  for: "für"

actions:
  hidden: true # Hide version 0 is released
  main: "PyPI Download"
  main_link: "https://pypi.org/project/groupdocs-parser-net/"
  alt: "Lizenzierung"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/python-net/"
  title: "Bereit, loszulegen?"
  description: "Testen Sie die GroupDocs.Parser-Funktionen kostenlos oder fordern Sie eine Lizenz an"

release:
  enable: false
  title: "Version {0} veröffentlicht"
  notes: "Erfahren Sie, was neu ist"
  downloads: "Downloads"

code:
  title: "Text mit Python extrahieren"
  more: "Weitere Beispiele"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Python-via-.NET/"
  install: "pip install groupdocs-parser-net"
  content: |
    ```python {style=abap}  
    from groupdocs.parser import Parser

    # Dokument laden
    with Parser("sample.pdf") as parser:
        # Text aus dem Dokument extrahieren
        text = parser.GetText()

        # Den gesamten extrahierten Text ausgeben
        print(text)
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser auf einen Blick"
  description: "Document Parser SDK für hochpräzises Dokumenten‑Parsing in Python‑Anwendungen"
  features:
    # feature loop
    - title: "Daten aus Dokumenten extrahieren"
      content: "GroupDocs.Parser for Python via .NET API ermöglicht es Ihnen, Text, Metadaten und Bilder aus einer Vielzahl von Dateiformaten wie Office‑Dokumenten, E‑Mails, Anhängen und Archiven abzurufen. Dieses leistungsstarke Tool hilft Ihnen, effizient auf die wertvollen Informationen in diesen Dateien zuzugreifen und sie für verschiedene Anwendungen wie Datenanalyse, Suchmaschinen‑Indexierung oder Content‑Management‑Systeme zu verarbeiten."

    # feature loop
    - title: "Dokumente parsen"
      content: "Extrahieren Sie verschiedene Elemente wie Hyperlinks, Tabellen, QR‑Codes, Barcodes und Daten aus PDF‑Formularen. Außerdem können Sie gewünschte Informationen aus Dokumenten mithilfe benutzerdefinierter Vorlagen parsen."

    # feature loop
    - title: "Ergebnisse anpassen"
      content: "Python API ermöglicht es Ihnen, Daten in verschiedenen Formaten wie Roh‑, strukturiert, HTML oder Markdown abzurufen. Zusätzlich bietet die API eine Suchfunktion zum Auffinden bestimmter Wörter oder Phrasen im Text von Dokumenten."

############################# Platforms ############################
platforms:
  enable: true
  title: "Plattformunabhängigkeit"
  description: "GroupDocs.Parser for Python via .NET unterstützt die folgenden Betriebssysteme, Frameworks und Paketmanager"
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
    GroupDocs.Parser for Python via .NET unterstützt Vorgänge mit den folgenden [Dateiformaten](https://docs.groupdocs.com/parser/python-net/supported-document-formats/).
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
  title: "GroupDocs.Parser for Python via .NET Funktionen"
  description: "Extrahieren Sie Daten aus PDFs, Office‑Dokumenten, Bildern und anderen Formaten schnell und genau mit unserem Python Document Parser SDK"

  items:
    # feature loop
    - icon: "text"
      title: "Text extrahieren"
      content: "Extrahieren Sie textuelle Informationen aus verschiedenen Dateiformaten wie Office‑Dokumenten, PDF‑Dateien und Bildern für eine einfache Lesbarkeit und Analyse."

    # feature loop
    - icon: "image"
      title: "Bilder extrahieren"
      content: "Rufen Sie visuelle Inhalte aus verschiedenen Quellen wie Office‑Dokumenten und PDF‑Dateien ab, um sie bequem zu nutzen."

    # feature loop
    - icon: "qr"
      title: "QR‑Codes scannen"
      content: "Erkennen und dekodieren Sie QR‑Codes, die in Office‑Dokumenten, PDF‑Dateien oder visuellen Inhalten enthalten sind, für eine effiziente Informationsbeschaffung."

    # feature loop
    - icon: "email"
      title: "Daten aus E‑Mail‑Anhängen und Archiven extrahieren"
      content: "Sammeln Sie wertvolle Informationen aus E‑Mail‑Nachrichten, Dateianhängen und komprimierten Datenquellen für eine effektive Analyse und Nutzung."

    # feature loop
    - icon: "table"
      title: "Tabellen extrahieren"
      content: "Identifizieren und extrahieren Sie tabellarische Daten aus PDF‑Dokumenten für eine strukturierte Analyse und Nutzung."

    # feature loop
    - icon: "hyperlink"
      title: "Hyperlinks extrahieren"
      content: "Hyperlinks und E‑Mail‑Adressen in Office‑Dokumenten oder PDF‑Dateien finden und extrahieren, um einen effizienten Zugriff zu ermöglichen."

    # feature loop
    - icon: "pdf"
      title: "PDF‑Formulare parsen"
      content: "PDF‑Formulare sind digitale Dokumente mit ausfüllbaren Feldern für die Benutzerinteraktion, die eine elektronische Eingabe von Informationen ermöglichen. Die Python‑API kann verwendet werden, um Daten aus diesen Formularen zu extrahieren und effizient zu verarbeiten."

    # feature loop
    - icon: "template"
      title: "Daten mit Vorlagen parsen"
      content: "Erstellen Sie benutzerdefinierte Vorlagen und nutzen Sie sie mit der Python‑API, um spezifische Informationen aus PDF‑Dateien zu parsen und den Datenextraktionsprozess zu vereinfachen."

    # feature loop
    - icon: "search"
      title: "Text in Dokumenten suchen"
      content: "Suchen Sie schnell nach bestimmten Wörtern oder Mustern in Dokumenten."


############################# Code samples ############################
code_samples:
  enable: true
  title: "Codebeispiele"
  description: "Über die grundlegende Textextraktion hinaus finden Sie hier die häufigsten Anwendungsfälle für schnelle Text‑, Bild‑ und Metadaten‑Extraktion."
  items:
    # code sample loop
    - title: "Text in einem Dokument suchen"
      content: |
        Dieses Beispiel zeigt, wie man nach einer bestimmten Phrase in einem PDF‑Dokument sucht und ausgibt, wo sie gefunden wurde.
        {{< landing/code title="Text in einem Dokument in Python suchen">}}
        ```python {style=abap}
        from groupdocs.parser import Parser

        # Dokument laden
        with Parser("sample.pdf") as parser:
            # Seitenindex und Rechteck ausgeben, in dem die Phrase gefunden wurde
            for area in parser.Search("Total Amount"):
                # Seitenindex und Rechteck ausgeben, in dem die Phrase gefunden wurde
                print(f"Page {area.PageIndex}, Rectangle: {area.Rectangle}")
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Bilder aus einem Dokument extrahieren"
      content: |
        Dieses Beispiel zeigt, wie man Bilder aus einem PDF‑Dokument extrahiert und in einer Datei speichert.
        {{< landing/code title="Bilder aus einem Dokument in Python extrahieren">}}
        ```python {style=abap}    
        from groupdocs.parser import Parser

        # Dokument laden
        with Parser("sample.docx") as parser:
            # Bilder aus dem Dokument extrahieren
            images = parser.GetImages()

            # Bilder in einer Datei speichern
            index = 1
            for image in images:
                image.Save(f"image_{index}.png")
                index += 1
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Metadaten aus einem Dokument extrahieren"
      content: |
        Dieses Beispiel zeigt, wie man Metadaten aus einem PDF‑Dokument extrahiert und ausgibt.
        {{< landing/code title="Metadaten aus einem Dokument in Python extrahieren">}}
        ```python {style=abap}    
        from groupdocs.parser import Parser

        # Dokument laden
        with Parser("sample.pdf") as parser:
            # Metadaten aus dem Dokument extrahieren
            metadata = parser.GetMetadata()

            # Metadaten ausgeben
            for item in metadata:
                print(f"{item.Name}: {item.Value}")
        ```
        {{< /landing/code >}}
---
