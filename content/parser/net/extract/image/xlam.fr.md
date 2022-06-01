---
############################# Static ############################
layout: "auto-gen-gist"
draft: false
path: "fr/parser/net/extract/image/xlam/"
otherformats: DOC DOT DOCX DOCM DOTX DOTM TXT ODT OTT RTF PDF XHTML MHTML MD XML EPUB FB2 CHM XLS XLT XLSX XLSM XLSB XLTX XLTM ODS CSV OTS XLA PPT PPTX  PPS POT PPSX PPTM POTX PPSM ODP OTP PST OST EML EMLX MSG ONE 

############################# Head ############################
head_title: "Extraire des images d'Excel, Word, PDF et autres documents ou pages via .NET"
head_description: "L'API GroupDocs.Parser .NET permet aux programmeurs de logiciels d'extraire des images de différents documents tels que MS Excel, Word, PowerPoint, PDF et plus encore dans leurs applications .NET."

############################# Header ############################
title: "Extraire des images de documents et pages PDF, DOCX, PPTX, MSG, XLSX via l'API C#.NET"
description: "L'API GroupDocs.Parser .NET permet aux programmeurs d'extraire des images de documents PDF, DOC, DOCX, PPT, PPTX, EML, MSG, XLS, XLSX, CSV, ODT, RTF et EPUB ou de pages de documents."

######################### Download Button #######################
button:
    enable: true

############################# About ############################
about:
    enable: true
    title: "Comment extraire des images de documents ou d'une zone de page via .NET?"
    content: |
       Les images peuvent être utilisées pour fournir des informations d'une manière telle qu'elles ne peuvent pas être exprimées par des mots. Les images nous aident à attirer l'attention de l'utilisateur et expliquent facilement les concepts difficiles. Parfois, en lisant des documents, des revues ou en profitant de présentations, nous avons souvent trouvé des images fascinantes et avons voulu les télécharger. GroupDocs.Parser pour .NET est une API puissante qui aide les utilisateurs à développer des applications utiles pour extraire des images de différents types de documents et les enregistrer aux formats PNG, JPEG, WebP, GIF, BMP et autres. L'API a inclus des supports pour le texte ainsi que l'extraction d'images à partir de certains des formats de fichiers les plus couramment utilisés, tels que PDF, e-mails, ebooks, formats Microsoft Office : Word (DOC, DOCX), PowerPoint (PPT, PPTX), Excel (XLS , XLSX), les formats LibreOffice et bien d'autres. L'API prend également entièrement en charge l'analyse de documents, l'extraction de texte brut et structuré, la recherche de texte par mots-clés, l'extraction de métadonnées ou d'images, de conteneurs ainsi que de pièces jointes et bien d'autres. 

############################# content ############################
steps:
    enable: true
    block:
    - title_left: "Extraire des images de documents XLAM  via C#"
      content_left: |
       L'API GroupDocs.Parser .NET permet aux développeurs de logiciels d'extraire des images des documents XLAM . L'exemple de code C# .NET suivant montre comment extraire des images dans un document XLAM . 

      title_right: "Comment extraire des images via .NET"
      content_right: |
        * Créez une instance de [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser)
        * vérifier si l'extraction d'images est prise en charge
        * Itérer sur les images du document
        * Appelez la méthode [getImages](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/getimages) pour extraire toutes les images de l'ensemble du document.
        * Imprimer toutes les images

      gisthash: "6bc9e8fea228c9e1b99425b338bb0f00"
      gistfile: "images_extraction_form_documents.cs"

    - title_left: "Extraction d'images de la page du document XLAM  via C#"
      content_left: |
       GroupDocs.Parser .NET permet aux développeurs de logiciels d'extraire des images de la page des documents XLAM . Le code C# .NET ci-dessous montre comment l'extraction d'images peut être réalisée dans un document XLAM . 

      title_right: "Extraire l'image du fichier via .NET"
      content_right: |
        * Créez une instance de [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser)  
        * Vérifier le document pour la prise en charge de l'extraction d'images
        * Obtenez des informations sur le document en appelant [GetDocumentInfo](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/getdocumentinfo)
        * Vérifier le document pour les pages existantes
        * Itérer sur les pages et imprimer un numéro de page
        * Appelez la méthode [getImages(Int32)](https://apireference.groupdocs.com/parser/net/groupdocs.parser.parser/getimages/methods/2) pour extraire toutes les images de l'ensemble du document.
        * Itérer sur les images et imprimer les images
     
      gisthash: "2000d476c202a688677f57a2fbd7ceab"
      gistfile: "images_extraction_form_documents_page.cs"
      
    - title_left: "Comment extraire une image de la zone de page des documents XLAM "
      content_left: |
       L'API GroupDocs.Parser .NET prend entièrement en charge l'extraction d'images à partir de documents XLAM  à l'aide de quelques lignes de code .NET. L'exemple de code .NET suivant montre comment effectuer une extraction d'images à partir d'une zone de page de document XLAM .

      title_right: "Extraire des images d'une zone de page de fichier via .NET"
      content_right: |
        * Créez une instance de [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser)   
        * personnaliser la création d'options pouvant être utilisées pour l'extraction d'images
        * Vérifiez le document pour le support d'extraction d'images
        * Extrayez les images du coin supérieur gauche d'une page en appelant la méthode [getImages(options)](https://apireference.groupdocs.com/parser/net/groupdocs.parser.parser/getimages/methods/3) à l'aide de la personnalisation Options.
        * Itérer sur les images et imprimer les images
     
      gisthash: "ea6c6b8fa613384f1e7f637dabcb7bca"
      gistfile: "extract_images_form_documents_page_area.cs"

    - title_left: "Comment extraire et enregistrer une image dans un fichier via C# .NET"
      content_left: |
       L'API GroupDocs.Parser .NET permet aux développeurs de logiciels d'extraire des images d'un document et de les enregistrer dans un fichier avec seulement quelques lignes de code .NET. L'exemple suivant montre comment effectuer l'extraction d'images à partir d'un document XLAM  et enregistrer le contenu de l'image dans le fichier. 

      title_right: "Enregistrer des images dans un fichier via .NET"
      content_right: |
        * Créez une instance de [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser)
        * Extraire des images du document
        * Appelez la méthode [getImages](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/getimages) pour extraire toutes les images de l'ensemble du document.
        * Vérifiez le document pour le support d'extraction d'images
        * Extrayez les images du coin supérieur gauche d'une page en appelant la méthode [getImages(options)](https://apireference.groupdocs.com/parser/net/groupdocs.parser.parser/getimages/methods/3) à l'aide de la personnalisation Options.
        * option Création pour enregistrer les images au format PNG
        * Parcourez les images et enregistrez l'image dans le fichier PNG
     
      gisthash: "bc242d5ff4050564fa275858ffa7d34f"
      gistfile: "images_saving_to_files.cs"

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