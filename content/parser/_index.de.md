---
############################# Static ############################
layout: "family"
date:  2024-02-13T17:01:03
draft: false

product: "Parser"
product_tag: "parser"

lang: de

############################# Head ############################
head_title: ".NET, Java, Cloud-APIs und Online-Dokumentparser-Apps"
head_description: "Holen Sie sich eine All-in-One-Lösung zum Parsen von Dokumenten für .NET, Java und cloudbasierte Anwendungen. Extrahieren Sie Daten aus Dokumentformaten online mit der einfachen Drag-and-Drop-Funktion"

############################# Header ############################
title: "Lösung zum Parsen von Dokumenten"
description: |
  Robuste API zur Datenextraktion aus verschiedenen Dateiformaten.

  Analysieren Sie Dokumente mit minimalem Programmieraufwand.

  Parsing-Ergebnisse anpassen.

############################# Supported Platforms ###############################
supported_platforms:
  enable: true
  head_title: "Wählen Sie Ihre Plattform"
  title: "Plattformunabhängigkeit"
  description: "Die GroupDocs.Parser-Bibliothek unterstützt die folgenden Betriebssysteme und Frameworks:"
  details_link_title: "Erfahren Sie mehr"

  items:
    # items loop
    - title: ".NET"
      description: GroupDocs.Parser für .NET 
      color: "blue"
      tag: "net"
      link: "/parser/net/"
      features_link: "https://docs.groupdocs.com/parser/net/system-requirements/"
      features:
          # features loop
          - rows: "4"
            content: |
                    .NET Framework 4.6.2 or higher
                    .NET Core 2.0 or higher
                    .NET 6.0 or higher
      
          # features loop
          - rows: "1"
            content: |
                    Windows, Linux, Mac OS
      
          # features loop
          - rows: "3"
            content: |
                    Microsoft Visual Studio
                    JetBrains Rider
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats
      

    # items loop
    - title: "Java"
      description: GroupDocs.Parser für Java
      color: "red"
      tag: "java"
      link: "/parser/java/"
      features_link: "https://docs.groupdocs.com/parser/java/system-requirements/"
      features:
          # features loop
          - rows: "4"
            content: |
                    Java 8 or higher
                    Kotlin
      
          # features loop
          - rows: "1"
            content: |
                    Windows, Linux, Mac OS
      
          # features loop
          - rows: "3"
            content: |
                    IntelliJ IDEA
                    Eclipse
                    NetBeans
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats

############################# Features ###############################
features:
  enable: true
  title: "GroupDocs.Parser auf einen Blick"
  description: "API zum Parsen von Daten über PDF, Word, Excel und mehr."

  items:
    # items loop
    - icon: "text"
      title: "Text extrahieren"
      content: "Extrahieren Sie Textinformationen aus verschiedenen Dateiformaten."

    # items loop
    - icon: "image"
      title: "Bilder extrahieren"
      content: "Rufen Sie visuelle Inhalte aus verschiedenen Quellen ab."

    # items loop
    - icon: "template"
      title: "Analysieren Sie Daten nach Vorlagen"
      content: "Erstellen Sie benutzerdefinierte Vorlagen und nutzen Sie diese zum Analysieren spezifischer Informationen."

    # items loop
    - icon: "pdf"
      title: "Analysieren Sie PDF-Formulare"
      content: "PDF Formulare sind digitale Dokumente mit ausfüllbaren Feldern für die Benutzerinteraktion."

############################# Code Samples ###############################
code_samples:
  enable: true
  title: "GroupDocs.Parser Codebeispiele"
  description: "Einige Anwendungsfälle typischer GroupDocs.Parser-Operationen in C# und Java."

  items:
    # items loop
    - title: "So extrahieren Sie Text aus PDF-Dokumenten"
      content: "Die GroupDocs.Parser-API erleichtert C#-Entwicklern das Extrahieren von Text aus Dokumenten durch die Implementierung einiger einfacher Schritte."
      samples:
          # samples loop
          - language: "C#"
            color: "blue"
            content: |
              <pre>
              // Create an instance of Parser class
              using (var parser = new Parser(fileName))
              {
                  // Extract a text into the reader
                  using (var textReader = parser.GetText())
                  {
                      // Print a text from the document
                      Console.WriteLine(textReader?.ReadToEnd());
                  }
              }
              </pre>
          # samples loop
          - language: "Java"
            color: "red"
            content: |
              <pre>
              // Create an instance of Parser class
              try (Parser parser = new Parser(fileName)) {
                  // Extract a text into the reader
                  try (TextReader reader = parser.getText()) {
                      // Print a text from the document
                      System.out.println(reader == null 
                              ? "" 
                              : reader.readToEnd());
                  }
              }
              <pre>

############################# Supported Formats ###############################
formats:
  enable: true
  title: "Über 50 Dateiformate werden unterstützt"
  description: "GroupDocs.Parser ermöglicht Parser-Operationen innerhalb verschiedener Formatfamilien."

############################# Metrics ###############################
metrics:
  enable: false
  title: "Detaillierte Kennzahlen und statistische Erkenntnisse"
  description: "Entdecken Sie eine gründliche Analyse unserer Schlüsselzahlen, die umfassende Kennzahlen und statistische Einblicke in unsere Erfolge, unseren Einfluss und unsere Expansion bietet."

  items:
    # items loop
    - number: "50+"
      title: "Unterstützte Formate"
      content: "Die API unterstützt mehr als 50 der am häufigsten verwendeten Datei- und Dokumentformate."

    # items loop
    - number: "700k"
      title: "NuGet Downloads"
      content: "GroupDocs.Parser for .NET hat über den Paketmanager NuGet über 800.000 Downloads erhalten."

    # items loop
    - number: "15k"
      title: "Maven-Downloads"
      content: "GroupDocs.Parser for Java hat über 15.000 Downloads aus unserem Maven-Repository gesammelt."


############################# Customers ###############################
customers:
  enable: true
  title: "Unsere zufriedenen Kunden"
  description: "GroupDocs Bibliotheken werden von weltweit bekannten und angesehenen Marken auf der ganzen Welt eingesetzt."

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
  title: "Bereit anzufangen?"
  description: "Testen Sie die Funktionen von GroupDocs.Parser kostenlos auf Ihrer Plattform"

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
    - question: "Benötigt die GroupDocs.Parser-Bibliothek weitere Software von Drittanbietern, um Dokumente zu bearbeiten?"
      answer: "Für GroupDocs.Parser ist keine Installation externer Software wie Adobe Acrobat, Microsoft Office oder andere erforderlich."

    # items loop
    - question: "Kann ich die GroupDocs.Parser-Bibliothek testen, bevor ich sie kaufe?"
      answer: "Ja, Sie können GroupDocs.Parser ausprobieren, ohne eine Lizenz zu kaufen. Nach der Installation ohne Lizenz funktioniert die Bibliothek im Testmodus. In diesem Modus werden dem resultierenden Dokument Testabzeichen hinzugefügt und es wird auf die ersten drei Seiten zugeschnitten. Wenn Sie GroupDocs.Parser ohne die Einschränkungen der Testversion testen möchten, können Sie auch eine 30-tägige temporäre Lizenz anfordern. Weitere Einzelheiten finden Sie unter [purchase.groupdocs.com/temporary-license/](https://purchase.groupdocs.com/temporary-license/)"

    # items loop
    - question: "Welche Lizenzen haben Sie?"
      answer: "Wir bieten verschiedene Lizenztypen an, um den Anforderungen bestimmter Entwickler oder Unternehmen gerecht zu werden. Die Lizenztypen hängen von der Anzahl der Entwickler, der Anzahl der Standorte der Entwicklerstandorte und davon ab, ob Sie Ihren Endkunden unser SDK/API bereitstellen müssen. Alternativ können Sie getaktete Lizenzen basierend auf der monatlichen Nutzung des Produkts wählen. Erfahren Sie mehr unter [purchase.groupdocs.com/policies/](https://purchase.groupdocs.com/policies/)"

############################# Cloud Links ###############################
cloud_links:
  enable: true
  title: "GroupDocs.Parser Low-Code-APIs"
  description: "Integrieren Sie Dokumentparser-Funktionen mithilfe unserer cloudbasierten REST-API in jede Anwendung."
  
  items:
    # items loop
    - title: "GroupDocs.Parser Cloud for cURL"
      content: "cURL-Befehle für die RESTvollständige Dokumentenparser-Cloud-API zum Parsen von Dokumenten in einer Vielzahl unterstützter gängiger Dateiformate."
      icon: "groupdocs_parser-for-curl"
      link: "https://products.groupdocs.cloud/parser/curl"

    # items loop
    - title: "GroupDocs.Parser Cloud for .NET"
      content: "Extrahieren Sie Bilder, Text, Dokumentinformationen oder analysieren Sie jedes Dokument anhand einer benutzerdefinierten Vorlage in Ihren Microsoft .NET-Anwendungen."
      icon: "groupdocs_parser-for-net"
      link: "https://products.groupdocs.cloud/parser/net"

    # items loop
    - title: "GroupDocs.Parser Cloud for Java"
      content: "Cloud SDK für Java-Entwickler zum Analysieren von Dokumenten, Extrahieren von Dokumentinformationen und Daten in Java-basierten Anwendungen."
      icon: "groupdocs_parser-for-java"
      link: "https://products.groupdocs.cloud/parser/java"

############################# App links ###############################
app_links:
  enable: true
  title: "GroupDocs.Parser NoCode-Apps"
  description: "Webbasierte Anwendung, mit der Sie die Analyse von mehr als 50 gängigen Dateiformaten direkt in Ihrem Browser durchführen können."

  items:
    # items loop
    - title: "GroupDocs.Parser Total"
      content: "Kostenlose Online-App zum Parsen von Word, Excel, PowerPoint, PDF und über 30 weiteren Dokumenttypen."
      icon: "groupdocs_parser-app"
      link: "https://products.groupdocs.app/parser/total"

    # items loop
    - title: "GroupDocs.Parser DOCX"
      content: "Analysieren Sie Word Dokumente direkt in Ihrem Webbrowser, um Bilder, Text oder Metadaten zu extrahieren."
      icon: "groupdocs_words-app"
      link: "https://products.groupdocs.app/parser/docx"

    # items loop
    - title: "GroupDocs.Parser PDF"
      content: "Kostenlose PDF-Parsing-App, die auf jeder Plattform und jedem Gerät ohne Einschränkungen funktioniert."
      icon: "groupdocs_pdf-app"
      link: "https://products.groupdocs.app/parser/pdf"     


---