---
############################# Static ############################
layout: "auto-gen-gist"
draft: false
path: "fr/parser/net/extract/rtf/"
otherformats: DOC DOT DOCX DOCM DOTX DOTM TXT ODT OTT RTF XHTML MHTML MD XML EPUB FB2 CHM XLS XLT XLSX XLSM XLSB XLTX XLTM ODS CSV OTS XLA XLAM PPT PPTX  PPS POT PPSX PPTM POTX PPSM ODP OTP PST OST EML EMLX MSG ONE 

############################# Head ############################
head_title: "API .NET pour analyser et extraire des hyperliens à partir de documents, de pages ou d'une zone de page"
head_description: "GroupDocs.Parser .NET API permet aux programmeurs de logiciels d'extraire des hyperliens à partir de documents, de pages ou de pages de PDF, DOCX, XLSX, CSV, PPTX, EML, MSG, EPUB et bien d'autres."

############################# Header ############################
title: "Extraire des liens hypertexte à partir de documents, de pages ou d'une zone de page spécifique via l'API C#/VB.NET"
description: "L'API GroupDocs.Parser .NET permet aux développeurs de logiciels d'analyser et d'extraire des hyperliens à partir de documents, de pages ou de pages Zone de PDF, DOC, DOCX, PPT, PPTX, EML, MSG, XLS, XLSX, CSV, ODT, RTF, EPUB et bien d'autres documents."

######################### Download Button #######################
button:
    enable: true

############################# About ############################
about:
    enable: true
    title: "Comment analyser et extraire des liens hypertexte à partir de documents ou de pages via .NET ?"
    content: |
       Un lien hypertexte est un morceau de texte ou une image ou une icône qui pointe vers un document entier ou vers une partie particulière d'un document. L'utilisation d'hyperliens permet aux utilisateurs de naviguer vers une page Web ou un document. Il est souvent nécessaire d'extraire des hyperliens d'un document et de l'utiliser pour accéder à un document externe ou à une page Web. GroupDocs.Parser .NET API est une fascinante API d'extraction de texte de document qui fournit des fonctionnalités complètes pour la mise en œuvre de solutions d'extraction de texte et de métadonnées. Il prend en charge l'extraction de texte et d'hyperliens à partir des formats PDF, e-mails, livres électroniques, Microsoft Office : Word (DOC, DOCX), PowerPoint (PPT, PPTX), Excel (XLS, XLSX), formats LibreOffice et bien d'autres. Il prend en charge plusieurs fonctionnalités avancées pour l'analyse de documents, l'extraction de texte brut et structuré, la recherche de texte par mots-clés, l'extraction de métadonnées ou d'images, de conteneurs ainsi que de pièces jointes et bien d'autres.

############################# content ############################
steps:
    enable: true
    block:
    - title_left: "Extrayez les liens hypertexte des documents RTF via .NET"
      content_left: |
       GroupDocs.Parser .NET fournit une prise en charge complète pour extraire des liens hypertexte à partir de documents RTF. L'exemple de code C# .NET suivant montre comment extraire des liens hypertexte dans un document RTF. 

      title_right: "Comment extraire des hyperliens"
      content_right: |
        * Créer une instance de [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser)
        * Vérifier le document pour la prise en charge de l'extraction de lien hypertexte
        * Extraire les hyperliens du document
        * Appelez la méthode [GetHyperlinks](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/gethyperlinks) pour extraire tous les liens hypertexte de l'ensemble du document.
        * Itérer sur les hyperliens et imprimer l'URL de l'hyperlien

      gisthash: "35be3a09e0135c65be790c42c5c86d37"
      gistfile: "Extract_hyperlinks_form_documents.cs"

    - title_left: "Extraire les liens hypertexte de la page RTF Documents"
      content_left: |
       GroupDocs.Parser .NET permet aux développeurs de logiciels d'extraire des liens hypertexte à partir de documents RTF avec quelques lignes de code. Le code C# .NET ci-dessous montre l'extraction de liens hypertexte dans un document RTF. 

      title_right: "Extraire les hyperliens via .NET"
      content_right: |
        * Créer une instance de [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser)
        * Vérifier le document pour la prise en charge de l'extraction de lien hypertexte
        * Obtenez des informations sur le document en appelant [GetDocumentInfo](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/getdocumentinfo) 
        * Itérer sur les pages et imprimer un numéro de page
        * Extraire les hyperliens du document
        * Appelez la méthode [GetHyperlinks](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/gethyperlinks) pour extraire tous les liens hypertexte de l'ensemble du document.
        * Itérer sur les hyperliens et imprimer l'URL de l'hyperlien
     
      gisthash: "e71f8e39ba36ebf97034dfbf6fceeec1"
      gistfile: "hyperlinks_extraction_form_documents_page.cs"
      
    - title_left: "Extraire les liens hypertexte de la zone de page RTF Documents"
      content_left: |
       L'API GroupDocs.Parser .NET prend entièrement en charge l'extraction de liens hypertexte à partir de documents RTF en toute simplicité. L'exemple de code .NET suivant montre comment extraire des liens hypertexte d'une zone de page de document RTF.

      title_right: "Comment extraire des hyperliens à l'aide de .NET"
      content_right: |
        * Créer une instance de [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser) 
        * Vérifier le document pour la prise en charge de l'extraction de lien hypertexte
        * Créer les options qui sont utilisées pour l'extraction de lien hypertexte
        * Appelez la méthode [GetHyperlinks](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/gethyperlinks) pour extraire tous les liens hypertexte de l'ensemble du document.
        * Itérer sur les hyperliens et imprimer l'URL de l'hyperlien
     
      gisthash: "eefbede6f391ea44ddb6901edb353950"
      gistfile: "hyperlinks_extraction_from__documents_page_area.cs"

    - title_left: "Configuration requise"
      content_left: |
        Les API GroupDocs.Assembly .NET sont prises en charge sur toutes les principales plateformes et systèmes d'exploitation. Pour un guide complet de la configuration système requise, veuillez visiter [configuration système](hhttps://docs.groupdocs.com/parser/net/system-requirements/) Avant d'exécuter le code ci-dessous, assurez-vous que les conditions préalables suivantes sont installées sur votre système:
        * Systèmes d'exploitation : Microsoft Windows, Linux, MacOS
        * Environnement de développement : Visual Studio, Xamarin, MonoDevelop etc.
        * Frameworks : .NET Framework, .NET Standard, .NET Core, Mono
        * Obtenez la dernière version des API GroupDocs.Assembly .NET à partir de [NuGet](https://www.nuget.org/packages/GroupDocs.parser/)
        
      title_right: "Pourquoi utiliser GroupDocs.Assembly"
      content_right: |
        * Prise en charge de l'extraction de texte brut à partir de tous les documents pris en charge
        * Analyse de documents via des modèles définis par l'utilisateur.
        * Prise en charge complète de l'extraction de texte structuré
        * Recherche de texte par mot-clé ainsi que par expression régulière
        * Extrayez du texte formaté, des métadonnées, des images, des conteneurs et des pièces jointes.
        * Extraire la table des matières pour certains formats de document pris en charge.
        * Analyser les données de formulaire à partir de documents PDF.
        * Extraire les hyperliens du document

demos:
    enable: true


more_formats:
    enable: true


back_to_top:
    enable: true
---