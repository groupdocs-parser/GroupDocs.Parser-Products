---
############################# Static ############################
layout: "auto-gen-gist"
draft: false
path: "fr/parser/java/extract/image/ots/"
otherformats: DOC DOT DOCX DOCM DOTX DOTM TXT ODT OTT RTF PDF XHTML MHTML MD XML EPUB FB2 CHM XLS XLT XLSX XLSM XLSB XLTX XLTM ODS CSV XLAM PPT PPTX  PPS POT PPSX PPTM POTX PPSM ODP OTP PST OST EML EMLX MSG ONE 

############################# Head ############################
head_title: "Comment extraire des images d'Excel, Word, PDF et autres documents via Java ?"
head_description: "L'API Java GroupDocs.Parser permet aux développeurs de logiciels d'analyser et d'extraire des images à partir de documents PDF, DOC, DOCX, PPT, PPTX, XLS, XLSX, de la zone de page et des e-mails dans les applications Java."

############################# Header ############################
title: "API Java pour analyser et extraire des images à partir de pages Excel, Word, PowerPoint, PDF et autres documents"
description: "L'API Java GroupDocs.Parser permet aux programmeurs d'extraire des images de documents PDF, DOC, DOCX, PPT, PPTX, EML, MSG, XLS, XLSX, CSV, ODT, RTF et EPUB ou de pages de documents dans des applications Java."

######################### Download Button #######################
button:
    enable: true

############################# About ############################
about:
    enable: true
    title: "Apprenez à extraire des images de documents ou d'une page spécifique via l'API Java ?"
    content: |
       Une image vaut mille mots et ne peut être ignorée dans le monde visuel d'aujourd'hui tout en créant un contenu attrayant. Les images peuvent être une excellente source de communication d'informations et attirer l'attention de l'utilisateur. Il est souvent nécessaire d'obtenir des images à partir de documents, de revues ou de présentations et de les utiliser ailleurs. GroupDocs.Parser pour Java est une API puissante qui aide les développeurs de logiciels et les programmeurs à créer une solution pour analyser et extraire des images ou d'autres informations à partir de nombreux types de documents. Il prend également en charge l'enregistrement d'images aux formats PNG, JPEG, WebP, GIF, BMP et autres. L'API a inclus la prise en charge de certains formats de documents populaires, tels que PDF, les formats Microsoft Office : Word (DOC, DOCX), PowerPoint (PPT, PPTX), Excel (XLS, XLSX), les formats LibreOffice, les e-mails, les livres électroniques et bien d'autres. . Il a également inclus la prise en charge de certaines fonctionnalités avancées liées à l'analyse de documents, à l'extraction de texte brut et structuré, à la recherche de texte par mots-clés, à l'extraction de métadonnées ou d'images, de conteneurs ainsi que de pièces jointes et bien d'autres.

############################# content ############################
steps:
    enable: true
    block:
    - title_left: "Comment extraire des images de documents OTS"
      content_left: |
       GroupDocs.Parser Java a inclus une fonctionnalité pour extraire des images à partir de documents OTS. L'exemple de code Java suivant montre comment extraire facilement des images du document OTS. 

      title_right: "Obtenir des images à partir de documents via Java"
      content_right: |
        * Créez une instance de [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser)
        * Vérifiez si le document prend en charge l'extraction d'images
        * Appelez la méthode [getImages()](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getImages()) pour extraire toutes les images de l'ensemble du document.
        * Extraire toutes les images du document
        * Itérer sur les images et imprimer le type d'image

      gisthash: "b13e690d2593f92081abd99948363e06"
      gistfile: "extract_images_form_documents.java"

    - title_left: "Extraction d'images à partir de la page des documents OTS"
      content_left: |
       L'API Java GroupDocs.Parser permet aux développeurs de logiciels d'extraire des images des documents OTS avec quelques lignes de code. Le code Java ci-dessous montre l'extraction d'images d'un document OTS. 

      title_right: "Comment extraire des images de fichiers via Java"
      content_right: |
        * Créez une instance de [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser)
        * Vérifiez si le document prend en charge l'extraction d'images
        * Obtenez des informations sur le document en appelant la méthode [getDocumentInfo](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getDocumentInfo()).
        * Vérifier le document pour l'existence des pages
        * Itérer sur les pages et imprimer un numéro de page
        * Appelez la méthode [getImages()](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getImages()) pour extraire toutes les images de l'ensemble du document.
        * Itérer sur les images et imprimer le type d'image
     
      gisthash: "68450336a57c5d8df06b4ef1ea69b29f"
      gistfile: "extract_images_form_documents_page.java"
      
    - title_left: "Comment extraire des images de la zone de page des documents OTS"
      content_left: |
       L'API Java GroupDocs.Parser a fourni un support complet pour l'extraction de la facilité de page du document OTS. Le code Java suivant montre comment les programmeurs peuvent extraire des images d'une zone de page de document OTS dans leurs propres applications Java.

      title_right: "Extraire des images à l'aide de Java ?"
      content_right: |
        * Créez une instance de [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser)
        * Créer les options qui sont utilisées pour l'extraction d'images
        * Vérifiez le document pour le support d'extraction d'images
        * Appelez la méthode [getImages()](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getImages()) pour extraire les images du coin supérieur gauche d'une page.
        * Itérer sur les images et imprimer l'URL des images
     
      gisthash: "40143a56569ae88e7e7c972ccca041b5"
      gistfile: "extract_images_form_documents_page_area.java"

    - title_left: "Comment extraire des images dans un fichier via l'API Java"
      content_left: |
       L'API Java GroupDocs.Parser permet d'extraire des images du document OTS et d'enregistrer le contenu de l'image dans un fichier. Le code Java suivant montre comment les programmeurs peuvent extraire des images du fichier de leur choix dans leurs propres applications Java.

      title_right: "Extraire des images d'un document vers un fichier"
      content_right: |
        * Créez une instance de [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser)
        * Vérifiez le document pour le support d'extraction d'images
        * Appelez la méthode [getImages()](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getImages()) pour extraire les images du coin supérieur gauche d'une page.
        * Créez les options pour enregistrer l'image dans le format de fichier pris en charge
        * Itérer sur les images et imprimer l'URL des images
     
      gisthash: "6faeafc93e4412265b7439209828950b"
      gistfile: "images_saving_to_files.java"

    - title_left: "Configuration requise"
      content_left: |
        GroupDocs.Parser pour Java est pris en charge sur toutes les principales plates-formes et systèmes d'exploitation. Il peut générer des documents dans Microsoft Word, Excel, PowerPoint, Outlook, OpenOffice et plus de 50 autres formats. Pour un guide complet de la configuration système requise, veuillez visiter la configuration système requise avant d'exécuter le code ci-dessous, veuillez vous assurer que les prérequis suivants sont installés sur votre système:
        * Systèmes d'exploitation : Microsoft Windows, Linux, MacOS
        * Prise en charge des versions Java : J2SE 7.0 (1.7), J2SE 8.0 (1.8) ou supérieur
        * Obtenez la dernière version des API Java GroupDocs.Assembly à partir de GroupDocs [Repository](https://repository.groupdocs.com/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs-parser)
        
      title_right: "Pourquoi utiliser GroupDocs.Parser"
      content_right: |
        * Extraire un texte brut de n'importe lequel des documents pris en charge.
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