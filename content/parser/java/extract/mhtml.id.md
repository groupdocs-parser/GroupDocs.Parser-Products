---
layout: "auto-gen-gist"
draft: false
path: "de/parser/java/extract//"
otherformats: DOC DOT DOCX DOCM DOTX DOTM TXT ODT OTT RTF PDF XHTML MHTML XML EPUB FB2 CHM XLS XLT XLSX XLSM XLSB XLTX XLTM ODS CSV OTS XLA XLAM PPT PPTX  PPS POT PPSX PPTM POTX PPSM ODP OTP PST OST EML EMLX MSG ONE 

head_title: "Extrahieren von Hyperlinks aus Dokumenten, Seiten oder Seitenbereichen über die Java-API"
head_description: "GroupDocs.Parser Java API ermöglicht Entwicklern das Extrahieren von Hyperlinks aus Dokumenten, Dokumentseiten oder bestimmten Seitenbereichen von Excel, PowerPoint, PDF, Outlook und mehr."

title: "Java-API zum Extrahieren von Hyperlinks aus Dokumenten, Seiten oder bestimmten Seitenbereichen"
description: "GroupDocs.Parser Java API erleichtert Entwicklern die Arbeit, indem es ihnen ermöglicht, Hyperlinks aus Dokumenten, Dokumentseiten oder bestimmten Seitenbereichen von PDF, DOCX, PPTX, EML, MSG, XLS, XLSX, CSV, und zu extrahilen mehr, RTF, EP."

button:
    enable: true

about:
    enable: true
    title: "Wie führe ich eine Hyperlink-Extraktion aus verschiedenen Dokumenten über Java durch?"
    content: |
       Auf dieser Webseite wird erklärt, wie Sie Hyperlinks aus verschiedenen Dokumenttypen, Dokumentseiten oder einem bestimmten Bereich einer Seite mit nur wenigen Zeilen Java-Code parsen und extrahieren. Hyperlinks können sehr nützlich sein, um zwischen Seiten oder Websites zu navigieren, und können auf ein ganzes Dokument oder auf einen bestimmten Teil innerhalb eines Dokuments, Grafiken, Sounds, E-Mail-Adressen. GroupDocs.Parser für Java ist eine sehr leistungsfähige API, die es Softwareentwicklern ermöglicht, Dokumente zu parsen und Text sowie Metadaten aus verschiedenen populären Dokumenten in ihren eigenen Java-Anwendungen zu extrahieren. Es enthält mehrere erweiterte Funktionen zum Extrahieren von Text und Hyperlinks aus verschiedenen Dokumententypen wie PDF, E-Mails, E-Books, Microsoft Office-Formaten: Word (DOC, DOCX), PowerPoint (PPT, PPTX), Excel (XLS, XLSX) , LibreOffice-Formate und viele mehr.

steps:
    enable: true
    block:
    - title_left: "Jadi ekstrahieren Sie Hyperlinks aus -Dokumenten"
      content_left: |
       GroupDocs.Parser Java enthält Funktionen zum Extrahieren von Hyperlinks aus -Dokumenten. Das folgende Java-Codebeispiel zeigt, wie Hyperlinks aus dem -Dokument extrahiert werden können.

      title_right: "Extrahieren Sie Hyperlink über Java"
      content_right: |
        * Erstellen Sie eine Instanz von [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser)
        * berprüfen Sie, ob das Dokument die Hyperlink-Extraktion unterstützt
        * Hyperlinks aus dem Dokument extrahieren
        * Rufen Sie die Methode [GetHyperlinks](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getHyperlinks()) auf, um alle Hyperlinks aus dem gesamten Dokument zu extrahieren.
        * ber Hyperlink iterieren und die Hyperlink-URL drucken

      gisthash: "036de701f5f17a02dd2353ee547afd5b"
      gistfile: "extract_hyperlinks_form_documents.java"

    - title_left: "Jadi ekstrahieren Sie Hyperlinks von der -Dokumentenseite"
      content_left: |
       GroupDocs.Parser .NET dan Softwareentwicklern, dengan bantuan Codezeilen Hyperlinks aus -Dokumenten zu extrahieren. Der folgende C# .NET-Code zeigt die Ekstraksi von Hyperlinks innerhalb eines -Dokuments. 

      title_right: "Extrahieren Sie Hyperlink über Java"
      content_right: |
        * Erstellen Sie eine Instanz von [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser) 
        * berprüfen Sie, ob das Dokument die Hyperlink-Extraktion unterstützt
        * Rufen Sie Dokumentinformationen ab, indem Sie die Metode [getDocumentInfo](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getDocumentInfo()) aufrufen.
        * Iterieren Sie über Seiten und drucken Sie eine Seitenzahl
        * Hyperlinks aus dem Dokument extrahieren
        * Rufen Sie die Methode [GetHyperlinks](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getHyperlinks()) auf, um alle Hyperlinks aus dem gesamten Dokument zu extrahieren.
        * ber Hyperlink iterieren und die Hyperlink-URL drucken
     
      gisthash: "bcca6319f2287edb7295443c1def46ee"
      gistfile: "extract_hyperlinks_form_documents_page.java"
      
    - title_left: "Extrahieren Sie Hyperlinks aus dem Seitembereich für -Dokumente"
      content_left: |
       Die GroupDocs.Parser-Java-API bietet vollständige Unterstützung zum einfachen Extrahieren von Hyperlinks aus der Seite des -Dokuments. Der folgende Java-Code zeigt, wie Programmierer Hyperlinks aus einem -Dokumentseitenbereich in ihren eigenen Java-Anwendungen extrahieren können.

      title_right: "Dengan tambahan Hyperlinks mit Java?"
      content_right: |
        * Erstellen Sie eine Instanz von [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser) 
        * berprüfen Sie das Dokument auf Unterstützung für die Hyperlink-Extraktion
        * Erstellen Sie die Optionen, die für die Hyperlink-Extraktion verwendet werden
        * Rufen Sie die Methode [GetHyperlinks](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getHyperlinks()) auf, um alle Hyperlinks aus dem gesamten Dokument zu extrahieren.
        * ber Hyperlink iterieren und die Hyperlink-URL drucken
     
      gisthash: "4aefff1fcc6733c0fc12b736d7e36711"
      gistfile: "hyperlinks_extraction_from_document_page_area.java"

    - title_left: "Sistem Anforderungen"
      content_left: |
        GroupDocs.Parser für Java wird auf allen wichtigen Plattformen und Betriebssystemen unterstützt. Es kann Dokumente di Microsoft Word, Excel, PowerPoint, Outlook, OpenOffice dan über 50 anderen Format erstellen. Um einen vollständigen Leitfaden zu den Systemanforderungen zu erhalten, besuchen Sie bitte die Systemanforderungen, bevor Sie den folgenden Code ausführen. Stellen Sie bitte sicher, dass die folgenden Voraussetzungen auf Ihrem System installiert sind:
        * Sistem Betriebs: Microsoft Windows, Linux, MacOS
        * Unterstützung für Java-Versionen: J2SE 7.0 (1.7), J2SE 8.0 (1.8) atau lebih
        * Versi Holen Sie sich die neueste dari GroupDocs.Assembly-Java-APIs von GroupDocs [Repositori](https://repository.groupdocs.com/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs -pengurai)
        
      title_right: "Warum GroupDocs.Assembly verwenden"
      content_right: |
        * Extrahieren Sie einen einfachen Teks aus einem der unterstützten Dokumente.
        * Unterstützung zum Extrahieren von Inhaltsverzeichnissen
        * Extrahieren Sie formatierten Text, Metadaten, Bilder, Container und Anhänge.
        * Dokumente parsen über benutzerdefinierte Vorlagen.
        * Suchen Sie Text mit Schlüsselwörtern oder regulären Ausdrücken.
        * Unterstützung für die Ekstraksi von strukturiertem Text
        * Inhaltsverzeichnis für einige unterstützte Dokumentformat ekstrahieren.
        * Analysieren Sie Formulardaten aus PDF-Dokumenten.

demos:
    enable: true
        

more_formats:
    enable: true


back_to_top:
    enable: true
---
