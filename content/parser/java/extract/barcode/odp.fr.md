---
############################# Static ############################
layout: "auto-gen-gist"
draft: false
path: "fr/parser/java/extract/barcode/odp/"
otherformats: DOC DOT DOCX DOCM DOTX DOTM TXT ODT OTT RTF PDF XHTML MHTML MD XML EPUB FB2 CHM XLS XLT XLSX XLSM XLSB XLTX XLTM ODS CSV OTS XLA XLAM PPT PPTX  PPS POT PPSX PPTM POTX PPSM OTP PST OST EML EMLX MSG ONE 

############################# Head ############################
head_title: "Extraire les codes-barres d'Excel, Word, PDF et autres documents via l'API Java "
head_description: "L'API Java GroupDocs.Parser permet aux développeurs de logiciels d'extraire des codes-barres à partir de PDF, MS Excel, Word, PowerPoint, Outlook, OneNote et d'autres documents dans les applications Java."

############################# Header ############################
title: "Comment extraire des codes-barres de PDF, DOCX, PPTX, EML, MSG, XLSX et EPUB via l'API Java"
description: "L'API Java GroupDocs.Parser permet aux développeurs de logiciels d'extraire des codes-barres de PDF, Word (DOC, DOCX), Excel (XLS, XLSX), PowerPoint (PPT, PPTX), Outlook (EML, MSG) et de nombreux autres documents."

######################### Download Button #######################
button:
    enable: true

############################# About ############################
about:
    enable: true
    title: "Apprenez à extraire des codes-barres d'Excel, Word, PDF et autres documents via Java ?"
    content: |
       L'image des codes à barres se compose d'une série de lignes noires parallèles et d'espaces blancs de largeurs variables qui peuvent être utilisés pour coder des informations dans un motif visuel. Il a été introduit dans les années 1970 et fait maintenant partie intégrante des entreprises commerciales. GroupDocs.Parser for Java est une API puissante qui permet aux programmeurs de logiciels de créer des applications pour analyser différents types de documents et en extraire du texte, des images et des codes-barres. Il a inclus la prise en charge de certains des types de documents les plus courants tels que PDF, e-mails, livres électroniques, formats Microsoft Office : Word (DOC, DOCX), PowerPoint (PPT, PPTX), Excel (XLS, XLSX), e-mails (EML, MSG ) et bien d'autres. L'API Java inclut la prise en charge de plusieurs fonctionnalités importantes liées à l'analyse de documents et à l'extraction de données, telles que l'extraction de texte brut, l'extraction de texte structuré, l'extraction de texte au format Markdown, l'extraction de texte d'une page ou d'une zone de page spécifique, l'extraction de code-barres d'un document, l'extraction de métadonnées ou photos et bien d'autres. 

############################# content ############################
steps:
    enable: true
    block:
    - title_left: "Comment extraire les codes-barres de ODP Documents via Java"
      content_left: |
       L'API Java GroupDocs.Parser permet aux programmeurs d'extraire facilement les codes-barres des documents ODP. L'exemple de code Java suivant montre comment extraire des images de codes-barres dans un document ODP avec un minimum d'effort et de coût. 

      title_right: "Extraire les codes-barres de Docs via Java"
      content_right: |
        * Créez une instance de [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser)
        * vérifier si l'extraction des codes-barres est prise en charge
        * Appelez la méthode [GetBarcodes](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getBarcodes()) pour extraire tous les codes-barres de l'ensemble du document.
        * Itérer sur les codes-barres dans le document
        * Imprimez tous les codes à barres et sa valeur

      gisthash: "bb2393a5db93e1795d41d908ad23e158"
      gistfile: "barcode_extraction_form_documents.java"

    - title_left: "Obtenez des codes-barres à partir de la page de ODP Document via Java"
      content_left: |
       GroupDocs.Parser Java permet aux développeurs de logiciels d'analyser et d'obtenir facilement des codes-barres à partir d'une page de documents ODP. Le code Java suivant montre comment l'extraction de code-barres peut être réalisée à partir d'une page de document spécifique dans un document ODP. 

      title_right: "Comment obtenir un code-barres à partir d'une page de fichier"
      content_right: |
        * Créez une instance de [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser)
        * Vérifiez le document pour le support d'extraction de codes à barres
        * Appelez la méthode [GetBarcodes](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getBarcodes(int)) pour extraire tous les codes-barres de la 2ème page du document.
        * Itérer sur les pages pour les codes à barres
        * Imprimer le numéro de page et la valeur des codes-barres
     
      gisthash: "ff09980eef6df60d5a3272b91b5607cf"
      gistfile: "barcodes_extraction_form_documents_page.java"
      
    - title_left: "Comment extraire les codes-barres de la zone de page ODP Documents"
      content_left: |
       L'API Java GroupDocs.Parser prend entièrement en charge l'extraction de codes-barres à partir de documents ODP en toute simplicité. L'exemple de code Java suivant montre comment effectuer une extraction de codes-barres à partir d'une zone de page de document ODP.

      title_right: "Extraire le code-barres d'une zone de page de fichier via Java"
      content_right: |
        * Créez une instance de [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser)
        * personnaliser la création d'options pouvant être utilisées pour l'extraction de codes-barres
        * Vérifiez le document pour le support d'extraction de codes à barres
        * Appelez la méthode [GetBarcodes](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getBarcodes(int)) pour extraire tous les codes-barres de la 2ème page du document.
        * Itérer sur les codes-barres dans le document
        * Imprimer le numéro de page et la valeur des codes-barres
     
      gisthash: "1737589e775a06a6300245cea525dac0"
      gistfile: "barcodes_extraction_from_documents_page_area.java"

    - title_left: "System Anforderungen"
      content_left: |
        GroupDocs.Parser für Java wird auf allen wichtigen Plattformen und Betriebssystemen unterstützt. Es kann Dokumente in Microsoft Word, Excel, PowerPoint, Outlook, OpenOffice und über 50 anderen Formaten erstellen. Um einen vollständigen Leitfaden zu den Systemanforderungen zu erhalten, besuchen Sie bitte die Systemanforderungen, bevor Sie den folgenden Code ausführen. Stellen Sie bitte sicher, dass die folgenden Voraussetzungen auf Ihrem System installiert sind:
        * Betriebssysteme: Microsoft Windows, Linux, MacOS
        * Unterstützung für Java-Versionen: J2SE 7.0 (1.7), J2SE 8.0 (1.8) oder höher
        * Holen Sie sich die neueste Version der GroupDocs.Parser-Java-APIs von GroupDocs [Repository](https://repository.groupdocs.com/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs-parser)
        
      title_right: "Warum GroupDocs.Parser verwenden"
      content_right: |
        * Extrahieren Sie einen einfachen Text aus einem der unterstützten Dokumente.
        * Unterstützung zum Extrahieren von Inhaltsverzeichnissen
        * Extrahieren Sie formatierten Text, Metadaten, Bilder, Container und Anhänge.
        * Dokumente parsen über benutzerdefinierte Vorlagen.
        * Suchen Sie Text mit Schlüsselwörtern oder regulären Ausdrücken.
        * Unterstützung für die Extraktion von strukturiertem Text
        * Inhaltsverzeichnis für einige unterstützte Dokumentformate extrahieren.
        * Analysieren Sie Formulardaten aus PDF-Dokumenten.

demos:
    enable: true
        

more_formats:
    enable: true


back_to_top:
    enable: true
---