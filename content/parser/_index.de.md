---
############################# Static ############################
layout: "family"
date:  2025-12-09T14:52:35
draft: false

product: "Parser"
product_tag: "parser"

lang: de

############################# Head ############################
head_title: "Document Parser SDKs für PDF, Word & Excel | GroupDocs"
head_description: "Document Parser SDK zum Extrahieren von Text, Bildern, Metadaten, Barcodes und Tabellen aus PDF-, Word-, Excel-Dateien, E-Mails und über 50 weiteren Dokumentformaten für .NET-, Java- und Python-Anwendungen."

############################# Header ############################
title: "Document Parser SDK"
description:  |
  Entwicklerfreundliches Document Parser SDK zum Extrahieren von Text, Bildern, Barcodes, Metadaten und Tabellen aus über 50 Dokument- und Bildformaten.

  Integrieren Sie die leistungsstarke Dokumentenverarbeitung in Ihre .NET-, Java- und Python-Anwendungen mit minimalem Programmieraufwand.

  Verwenden Sie flexible Vorlagen und erweiterte APIs, um Parsing‑Regeln anzupassen und saubere, strukturierte Datenausgaben bereitzustellen.

############################# Supported Platforms ###############################
supported_platforms:
  enable: true
  head_title: "Wählen Sie Ihre Plattform"
  title: "Plattformunabhängigkeit"
  description: "GroupDocs.Parser-Bibliothek unterstützt die folgenden Betriebssysteme und Frameworks:"
  details_link_title: "Mehr erfahren"

  items:
    # items loop
    - title: ".NET"
      description: GroupDocs.Parser for .NET 
      color: "blue"
      tag: "net"
      link: "/parser/net/"
      features_link: "https://docs.groupdocs.com/parser/net/system-requirements/"
      features:
          # features loop
          - rows: "3"
            content: |
                    .NET Framework 4.6.2 or higher <br> .NET Core 2.0 or higher <br> .NET 6.0 or higher
      
          # features loop
          - rows: "1"
            content: |
                    Windows <br> Linux <br> Mac OS
      
          # features loop
          - rows: "4"
            content: |
                    Microsoft Visual Studio <br> JetBrains Rider <br> Microsoft Visual Code
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats
      

    # items loop
    - title: "Java"
      description: GroupDocs.Parser for Java
      color: "red"
      tag: "java"
      link: "/parser/java/"
      features_link: "https://docs.groupdocs.com/parser/java/system-requirements/"
      features:
          # features loop
          - rows: "3"
            content: |
                    Java 8 or higher <br> Kotlin
      
          # features loop
          - rows: "1"
            content: |
                    Windows <br> Linux <br> Mac OS
      
          # features loop
          - rows: "4"
            content: |
                    IntelliJ IDEA <br> Eclipse <br> NetBeans
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats


    # items loop
    - title: "Python"
      description: GroupDocs.Parser for Python
      color: "yellow"
      tag: "python-net"
      link: "/parser/python-net/"
      features_link: "https://docs.groupdocs.com/parser/python-net/system-requirements/"
      features:
          # features loop
          - rows: "3"
            content: |
                    Python 3.5+
      
          # features loop
          - rows: "1"
            content: |
                    Windows <br> Linux <br> macOS
      
          # features loop
          - rows: "4"
            content: |
                    PyCharm, VS Code, Jupyter Notebook
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats                    

############################# Features ###############################
features:
  enable: true
  title: "GroupDocs.Parser auf einen Blick"
  description: "Leistungsstarkes Document Parser SDK zum Extrahieren strukturierter und unstrukturierter Daten aus PDFs, Office-Dokumenten, Bildern, E-Mails und Archiven."

  items:
    # items loop
    - icon: "text"
      title: "Text extrahieren"
      content: "Extrahieren Sie Textinformationen aus verschiedenen Dateiformaten"

    # items loop
    - icon: "image"
      title: "Bilder extrahieren"
      content: "Abrufen visueller Inhalte aus verschiedenen Quellen"

    # items loop
    - icon: "template"
      title: "Daten mit Vorlagen parsen"
      content: "Erstellen Sie benutzerdefinierte Vorlagen und verwenden Sie diese, um spezifische Informationen zu parsen"

    # items loop
    - icon: "pdf"
      title: "PDF-Formulare parsen"
      content: "PDF-Formulare sind digitale Dokumente mit ausfüllbaren Feldern für die Benutzerinteraktion"

############################# Code Samples ###############################
code_samples:
  enable: true
  title: "GroupDocs.Parser Codebeispiele"
  description: "Einige Anwendungsfälle typischer GroupDocs.Parser-Operationen in C#, Java und Python"

  items:
    # items loop
    - title: "Text aus PDF-Dokumenten extrahieren"
      content: "GroupDocs.Parser API erleichtert das Extrahieren von Text aus Dokumenten durch wenige Schritte."
      samples:
          # samples loop
          - language: "C#"
            color: "blue"
            content: |
              ```csharp {style=abap}  
                // Erstellen Sie eine Instanz der Klasse Parser und übergeben Sie die gewünschte Datei.
                using (var parser = new Parser("source.pdf"))
                {
                    // Text extrahieren
                    using (var textReader = parser.GetText())
                    {
                        // Den extrahierten Text verarbeiten
                        Console.WriteLine(textReader?.ReadToEnd());
                    }
                }     
              ```
          # samples loop
          - language: "Java"
            color: "red"
            content: |
              ```java {style=abap}
                // Erstellen Sie eine Instanz der Klasse Parser und übergeben Sie die gewünschte Datei.
                try (Parser parser = new Parser("source.pdf"))
                {
                    // Text extrahieren
                    try (TextReader reader = parser.getText())
                    {
                        // Den extrahierten Text verarbeiten
                        System.out.println(reader == null 
                                ? "" 
                                : reader.readToEnd());
                    }
                }  
              ```
          # samples loop
          - language: "Python"
            color: "green"
            content: |
              ```python {style=abap}
                from groupdocs.parser import Parser

                # Erstellen Sie eine Instanz der Klasse Parser und übergeben Sie die gewünschte Datei.
                with Parser("source.pdf") as parser:
                    # Text extrahieren
                    text = parser.get_text()

                    # Den extrahierten Text verarbeiten
                    print(text)
              ```
############################# Supported Formats ###############################
formats:
  enable: true
  title: "Über 50 unterstützte Dokument- und Bildformate"
  description: "GroupDocs.Parser Document Parser SDK ermöglicht Parsing‑Operationen über Office-Dokumente, PDFs, Bilder, E-Mails, Archive und mehr."

############################# Metrics ###############################
metrics:
  enable: true
  title: "GroupDocs.Parser Erfolge"
  description: "Entdecken Sie die wichtigsten Kennzahlen der Erfolge unserer Bibliothek"

  items:
    # items loop
    - number: "50+"
      title: "Unterstützte Formate"
      content: "GroupDocs.Parser unterstützt Operationen mit mehr als 50 gängigen Dateiformaten."

    # items loop
    - number: "1600k"
      title: "NuGet-Downloads"
      content: "GroupDocs.Parser für .NET NuGet-Paket wurde mehr als 1.600.000 Mal heruntergeladen."

    # items loop
    - number: "18k"
      title: "Maven-Downloads"
      content: "GroupDocs.Parser hat 18.000 Downloads bei Maven. Leistungsstarke Java-Parsing-Funktionen."

    # items loop
    - number: "140+"
      title: "Zufriedene Kunden"
      content: "Sowohl berühmte Unternehmen als auch einzelne Entwickler bevorzugen GroupDocs-Produkte, um innovative Lösungen zu entwickeln."


############################# Customers ###############################
customers:
  enable: true
  title: "Unsere zufriedenen Kunden"
  description: "GroupDocs-Bibliotheken werden von weltweit renommierten und angesehenen Marken eingesetzt."

  items:
    # items loop
    - title: "BenQ Corporation"
      logo: "benq"
      
    # items loop
    - title: "Nasdaq Stock Market"
      logo: "nasdaq"
      
    # items loop
    - title: "AT&T Inc."
      logo: "att"
      
    # items loop
    - title: "Customer logo AstraZeneca"
      logo: "astrazeneca"
      
    # items loop
    - title: "Central Bank of Argentina"
      logo: "argentinacentralbank"
      
    # items loop
    - title: "Roche Holding AG"
      logo: "roche"
      
    # items loop
    - title: "Capita"
      logo: "capita"
      
    # items loop
    - title: "Axa S.A."
      logo: "axa"
      
    # items loop
    - title: "Instructure Inc."
      logo: "instructure"
      
    # items loop
    - title: "Wipro"
      logo: "wipro"


############################# Actions ###############################
actions:
  enable: true
  title: "Bereit, loszulegen?"
  description: "Testen Sie die GroupDocs.Parser-Funktionen kostenlos auf Ihrer Plattform"

  items:
    # items loop
    - title: ".NET"
      color: "blue"
      link: "/parser/net/"

    # items loop
    - title: "Java"
      color: "red"
      link: "/parser/java/"

############################# FAQ ###############################
faq:
  enable: true
  title: "Häufig gestellte Fragen"
  description: "Antworten auf die am häufigsten gestellten Fragen."

  items:
    # items loop
    - question: "Benötigt die GroupDocs.Parser-Bibliothek zusätzliche Drittanbieter-Software, um Dokumente zu verarbeiten?"
      answer: "GroupDocs.Parser erfordert keine Installation externer Software wie Adobe Acrobat, Microsoft Office oder andere."

    # items loop
    - question: "Kann ich die GroupDocs.Parser-Bibliothek vor dem Kauf testen?"
      answer: "Ja, Sie können GroupDocs.Parser ohne Lizenzkauf testen. Wird die Bibliothek ohne Lizenz installiert, arbeitet sie im Testmodus. In diesem Modus werden dem resultierenden Dokument Testkennzeichnungen hinzugefügt und es wird auf die ersten 3 Seiten gekürzt. Wenn Sie GroupDocs.Parser ohne die Einschränkungen der Testversion testen möchten, können Sie auch eine 30‑tägige temporäre Lizenz anfordern. Weitere Details finden Sie unter [weitere Details](https://purchase.groupdocs.com/temporary-license/)."

    # items loop
    - question: "Welche Lizenzen gibt es?"
      answer: "Wir bieten verschiedene Lizenztypen, die den Bedürfnissen einzelner Entwickler oder Unternehmen entsprechen. Lizenztypen hängen von der Anzahl der Entwickler, der Anzahl der Entwickler‑Standorte und davon ab, ob Sie unser SDK/API an Ihre Endkunden weitergeben müssen. Alternativ können Sie nutzungsbasierte (Metered) Lizenzen basierend auf dem monatlichen Produktverbrauch wählen. Erfahren Sie mehr [hier](https://purchase.groupdocs.com/pricing/parser/net/)."

############################# Cloud Links ###############################
cloud_links:
  enable: true
  title: "GroupDocs.Parser Low‑Code‑Dokumenten‑Parser‑APIs"
  description: "Integrieren Sie Dokumenten‑Parsing‑Funktionen in jede Anwendung mittels unserer cloud‑basierten REST‑API und SDKs."
  
  items:
    # items loop
    - title: "GroupDocs.Parser Cloud for cURL"
      content: "cURL-Befehle für die REST‑basierte Dokumenten‑Parser‑Cloud‑API zum Parsen von Dokumenten über ein breites Spektrum unterstützter, beliebter Dateiformate."
      icon: "groupdocs_parser-for-curl"
      link: "https://products.groupdocs.cloud/parser/curl"

    # items loop
    - title: "GroupDocs.Parser Cloud for .NET"
      content: "Extrahieren Sie Bilder, Text, Dokumenteninformationen oder parsen Sie beliebige Dokumente anhand benutzerdefinierter Vorlagen in Ihren Microsoft .NET‑Anwendungen."
      icon: "groupdocs_parser-for-net"
      link: "https://products.groupdocs.cloud/parser/net"

    # items loop
    - title: "GroupDocs.Parser Cloud for Java"
      content: "Cloud‑SDK für Java‑Entwickler zum Parsen von Dokumenten sowie zum Extrahieren von Dokumenteninformationen und Daten in Java‑basierten Anwendungen."
      icon: "groupdocs_parser-for-java"
      link: "https://products.groupdocs.cloud/parser/java"

############################# App links ###############################
app_links:
  enable: true
  title: "GroupDocs.Parser Dokumenten‑Parser No‑Code‑Apps"
  description: "Webbasierte Dokumenten‑Parser‑Apps, mit denen Sie Daten aus über 50 gängigen Dateiformaten direkt im Browser extrahieren können."

  items:
    # items loop
    - title: "GroupDocs.Parser Total"
      content: "Kostenlose Online‑App zum Parsen von Word-, Excel‑, PowerPoint‑, PDF‑ und über 50 weiteren Dokumenttypen."
      icon: "groupdocs_parser-app"
      link: "https://products.groupdocs.app/parser/total"

    # items loop
    - title: "GroupDocs.Parser DOCX"
      content: "Parsen Sie Word‑Dokumente direkt in Ihrem Webbrowser, um Bilder, Text oder Metadaten zu extrahieren."
      icon: "groupdocs_words-app"
      link: "https://products.groupdocs.app/parser/docx"

    # items loop
    - title: "GroupDocs.Parser PDF"
      content: "Kostenlose PDF‑Parsing‑App, die auf jeder Plattform oder jedem Gerät ohne Einschränkungen arbeitet."
      icon: "groupdocs_pdf-app"
      link: "https://products.groupdocs.app/parser/pdf"


      


---