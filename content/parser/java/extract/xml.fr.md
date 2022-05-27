---
############################# Static ############################
layout: "auto-gen-gist"
draft: false
path: "fr/parser/java/extract//"
otherformats: DOC DOT DOCX DOCM DOTX DOTM TXT ODT OTT RTF PDF XHTML MHTML MD XML FB2 CHM XLS XLT XLSX XLSM XLSB XLTX XLTM ODS CSV OTS XLA XLAM PPT PPTX  PPS POT PPSX PPTM POTX PPSM ODP OTP PST OST EML EMLX MSG ONE 

############################# Head ############################
head_title: "Extraction d'hyperliens à partir de documents, de pages ou de zones de page via l'API Java"
head_description: "L'API Java GroupDocs.Parser permet aux développeurs d'extraire des hyperliens à partir de documents, d'une page de document ou d'une zone de page spécifique d'Excel, PowerPoint, PDF, Outlook, etc."

############################# Header ############################
title: "API Java pour extraire des hyperliens à partir de documents, de pages ou d'une zone de page particulière"
description: "L'API Java GroupDocs.Parser facilite le travail des développeurs en leur permettant d'extraire des hyperliens à partir de documents, d'une page de document ou d'une zone de page spécifique de PDF, DOCX, PPTX, EML, MSG, XLS, XLSX, CSV, RTF, EPUB et bien d'autres."

######################### Download Button #######################
button:
    enable: true

############################# About ############################
about:
    enable: true
    title: "Comment effectuer une extraction d'hyperliens à partir de divers documents via Java ?"
    content: |
       Cette page Web explique comment analyser et extraire des hyperliens à partir de différents types de documents, de pages de documents ou d'une zone particulière d'une page en utilisant seulement quelques lignes de code Java. Le lien hypertexte peut être très utile pour naviguer entre les pages ou les sites Web et peut pointer vers un document entier ou vers une partie particulière d'un document, des graphiques, des sons, des adresses e-mail et plus encore. GroupDocs.Parser for Java est une API très puissante qui permet aux développeurs de logiciels d'analyser des documents et d'extraire du texte ainsi que des métadonnées de divers documents populaires dans leurs propres applications Java. Il a inclus plusieurs fonctionnalités avancées pour extraire du texte et des hyperliens à partir de divers types de documents tels que PDF, e-mails, livres électroniques, formats Microsoft Office : Word (DOC, DOCX), PowerPoint (PPT, PPTX), Excel (XLS, XLSX), formats LibreOffice et beaucoup plus.

############################# content ############################
steps:
    enable: true
    block:
    - title_left: "Comment extraire des liens hypertexte de  Documents"
      content_left: |
       GroupDocs.Parser Java a inclus une fonctionnalité pour extraire des liens hypertexte à partir de documents . L'exemple de code Java suivant montre comment les liens hypertexte peuvent être extraits du document . 

      title_right: "Extraire les hyperliens via Java"
      content_right: |
        * Créez une instance de [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser)
        * Vérifiez si le document prend en charge l'extraction de liens hypertexte
        * Extraire les hyperliens du document
        * Appelez la méthode [GetHyperlinks](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getHyperlinks()) pour extraire tous les hyperliens de l'ensemble du document.
        * Itérer sur les hyperliens et imprimer l'URL de l'hyperlien

      gisthash: "036de701f5f17a02dd2353ee547afd5b"
      gistfile: "extract_hyperlinks_form_documents.java"

    - title_left: "Comment extraire des liens hypertexte de la page  Documents"
      content_left: |
       GroupDocs.Parser .NET permet aux développeurs de logiciels d'extraire des liens hypertexte à partir de documents  avec quelques lignes de code. Le code C# .NET ci-dessous montre l'extraction de liens hypertexte dans un document . 

      title_right: "Extraire les hyperliens via Java"
      content_right: |
        * Créez une instance de [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser)
        * Vérifiez si le document prend en charge l'extraction de liens hypertexte
        * Get document info by calling [getDocumentInfo](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getDocumentInfo()) method.
        * Itérer sur les pages et imprimer un numéro de page
        * Extraire les hyperliens du document
        * Appelez la méthode [GetHyperlinks](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getHyperlinks()) pour extraire tous les hyperliens de l'ensemble du document.
        * Iterate over hyperlinks and Print the hyperlink URL
     
      gisthash: "bcca6319f2287edb7295443c1def46ee"
      gistfile: "extract_hyperlinks_form_documents_page.java"
      
    - title_left: "Extraire les liens hypertexte de la zone de page  Documents"
      content_left: |
       L'API Java GroupDocs.Parser a fourni une prise en charge complète pour extraire les liens hypertexte de la facilité de page du document . Le code Java suivant montre comment les programmeurs peuvent extraire des liens hypertexte d'une zone de page de document  dans leurs propres applications Java.

      title_right: "Comment extraire des hyperliens en utilisant Java ?"
      content_right: |
        * Créez une instance de [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser) 
        * Vérifiez si le document prend en charge l'extraction de liens hypertexte
        * Créer les options qui sont utilisées pour l'extraction de lien hypertexte
        * Appelez la méthode [GetHyperlinks](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getHyperlinks()) pour extraire tous les hyperliens de l'ensemble du document.
        * Itérer sur les hyperliens et imprimer l'URL de l'hyperlien
     
      gisthash: "4aefff1fcc6733c0fc12b736d7e36711"
      gistfile: "hyperlinks_extraction_from_document_page_area.java"

    - title_left: "Configuration requise"
      content_left: |
        GroupDocs.Parser pour Java est pris en charge sur toutes les principales plates-formes et systèmes d'exploitation. Il peut générer des documents dans Microsoft Word, Excel, PowerPoint, Outlook, OpenOffice et plus de 50 autres formats. Pour un guide complet de la configuration système requise, veuillez visiter la configuration système requise avant d'exécuter le code ci-dessous, assurez-vous que les prérequis suivants sont installés sur votre système :
         * Systèmes d'exploitation : Microsoft Windows, Linux, MacOS
         * Prise en charge des versions Java : J2SE 7.0 (1.7), J2SE 8.0 (1.8) ou supérieur
         * Obtenez la dernière version des API Java GroupDocs.Assembly à partir de GroupDocs [Repository](https://repository.groupdocs.com/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs-parser)
        
      title_right: "Pourquoi utiliser GroupDocs.Assembly"
      content_right: |
        * Extraire un texte brut de l'un des documents pris en charge.
        * Prise en charge de l'extraction de la table des matières
        * Extrayez du texte formaté, des métadonnées, des images, des conteneurs et des pièces jointes.
        * Analyse de documents via des modèles définis par l'utilisateur.
        * Recherche de texte à l'aide d'un mot-clé ou d'une expression régulière.
        * Prise en charge de l'extraction de texte structuré
        * Extraire la table des matières pour certains formats de document pris en charge.
        * Analyser les données de formulaire à partir de documents PDF.

demos:
    enable: true
        
more_formats:
    enable: true


back_to_top:
    enable: true
---