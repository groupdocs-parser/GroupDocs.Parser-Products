---
############################# Static ############################
layout: "product"
date: 2021-04-27T09:31:06+03:00
draft: false

product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "API d'analyse .NET, extraire les métadonnées des images de texte à partir de PDF Word Excel"
head_description: "API d'analyse de documents C# .NET pour extraire du texte, des images, des métadonnées et de l'encodage à partir de bases de données, PDF, Word, Excel, présentations, Web, e-mail, EPUB et formats de fichiers zip."

############################# Header ############################
title: ".NET API pour extraire les données de document"
description: "Extrayez des images, du texte brut ou formaté et des métadonnées de documents, feuilles de calcul, présentations, e-mails et archives à partir d'applications .NET."
button:
    enable: true

############################# SubMenu ############################
submenu:
    enable: true
    
    left:
        img_alt: "GroupDocs.Parser for .NET"
        image: "/border/groupdocs-parser-net.svg"
        product: "GroupDocs.Parser"
        platform: ".NET"

    middle:
        button:
            # button loop
            - link: "#overview"
              text: "Aperçu"

            # button loop
            - link: "#features"
              text: "Caractéristiques"

            # button loop
            - link: "#support"
              text: "Support"

            # button loop
            - link: "https://products.groupdocs.app/parser"
              text: "Live Demo"

            # button loop
            - link: "https://purchase.groupdocs.com/pricing/parser/net"
              text: "Pricing"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/net/"
        link_buy: "https://purchase.groupdocs.com"

############################# Aperçu ############################
overview:
    enable: true
    content: |
      GroupDocs.Parser pour .NET est une API d'extraction de texte, de métadonnées et d'images pour les applications métier développées à l'aide de C#, ASP.NET et d'autres technologies .NET. Il prend en charge l'extraction de texte brut, formaté et structuré ainsi que les métadonnées des fichiers de formats pris en charge. Grâce à GroupDocs.Parser pour .NET, vos applications peuvent également effectuer l'analyse de documents protégés par mot de passe pour les formats courants, tels que les documents de traitement de texte, les feuilles de calcul Excel, les présentations PowerPoint, OneNote, les fichiers PDF et les archives ZIP.
    tabs:
      enable: true
      
      ## TAB ONE ##
      tab_one:
        description: |
          Voici un aperçu de GroupDocs.Parser pour .NET :
      
        left:
          enable: true
          icon: "fas fa-tools"
          title: "Caractéristiques"
          content: |
            * Extraire des images
            * Extraire le texte brut
            * Extraire le texte formaté
            * Extraire le texte structuré
            * Extraire les métadonnées
            * Extraire des fichiers dans le fichier ZIP
            * Extraire en recherchant
            * Extraire avec des formateurs de texte
            * Détecter la norme d'encodage
            * Détecter le type de support
        
        right:
          enable: true
          icon: "fab fa-html5"
          title: "L'API"
          content: |
            * Obtient le fichier d'entrée
            * Récupère le texte brut ou formaté
            * Récupère les métadonnées
      
      ## TAB TWO ##
      tab_two:
        description: |
          GroupDocs.Parser pour .NET prend en charge les [formats de fichier de document] suivants (https://docs.groupdocs.com/parser/net/supported-document-formats/) :

        left:
          enable: true
          table:
            # table loop
            - title: "Extraction de texte"
              content: |
                * **Texte** : DOC, DOCX, DOT, DOTM, DOTX, DOCM, RTF, ODT, OTT, TXT, MD, WordprocessingML (XML)
                * **Feuilles de calcul** : XLS, XLSX, CSV, XLSM, XLSB, ODS, SpreadsheetML (XML), XLT, XLTX, XLTM, OTS, XLA, XLAM, TSV
                * **Présentations** : PPT, PPTX, PPTM, PPS, PPSX, PPSM, POT, POTX, POTM, ODP, OTP
                * **OneNote** : UNE
                * **E-mail** : MSG, EML, EMLX, PST, OST, MS EXCHANGE SERVER, POP, IMAP
                * **Édition électronique** : EPUB, FB2
                * **Document portable** : PDF, Portfolio PDF, PDF crypté
                * **Basé sur DOM** : XML, HTML, XHTML, MHTML
                * **Compression & Emballage** : ZIP, CHM
                * **Base de données** : ADO.NET

            # table loop
            - title: "Détection d'encodage"
              content: |
                * **BOM**: UTF32 LE, UTF32 BE, UTF16 LE, UTF16 BE, UTF8, and UTF7
                * **Content**: UTF32 LE, UTF32 BE, UTF16 LE, UTF16 BE, UTF8, and ANSI

        right:
          enable: true
          table:
            # table loop
            - title: "Extraction de métadonnées"
              content: |
                * **Texte** : DOC, DOCX, DOT, DOTX, DOTM, OTT, ODT
                * **Feuilles de calcul** : XLS, XLSX, XLT, XLTX, XLTM, XLA, XLAM, OTS, ODS
                * **Présentations** : PPT, PPTX, POT, POTX, POTM, PPSM, PPTM, OTP, ODP
                * **Courriel** : MSG, EML, EMLX
                * **Édition électronique** : EPUB, FB2
                * **Autre** : PDF

            # table loop
            - title: "Text & Extraction de métadonnées"
              content: |
                * **Modèle** : DOTX, POTX
                * **Modèle compatible avec les macros** : DOTM, POTM, PPSM, PPTM
                * **Modèle OpenDocument** : OTT

            # table loop
            - title: "Extraction d'images"
              content: |
                * **Texte** : DOC, DOCX, DOCM, RTF, DOT, DOTM, DOTX, ODT
                * **Feuilles de calcul** : XLS, XLSX, XLSM, XLSB, ODS, XLT, XLTM, XLTX
                * **Présentations** : PPT, PPTX, PPTM, ODP, POT, POTM, POTX, PPS, PPSX, PPSM
                * **Document portable** : PDF, POT, POTM, POTX
                * **Ebook** : CHM, EPUB, FB2
                * **Marquage** : HTML

      ## TAB THREE ##
      tab_three:
        description: |
          GroupDocs.Parser for .NET prend en charge la suite Systèmes d'exploitation, Frameworks & Directeur chargé d'emballages:
        
        left:
          enable: true
          table:
            # table loop
            - icon: "fab fa-windows"
              title: "Systèmes d'exploitation"
              content: |
                * Bureau Windows
                * Serveur Windows
                * windows Azure
                * Linux

            # table loop
            - icon: "fas fa-code"
              title: "Cadres pris en charge"
              content: |
                * .NET Framework 2.0 ou supérieur
                * Mono Framework 1.2 ou supérieur
                * Norme .NET 2.0
                * .NET Core 2.0

        right:
          enable: true
          table:
            # table loop
            - icon: "fas fa-box"
              title: "Directeur chargé d'emballage"
              content: |
                * NuGet

            # table loop
            - icon: "fas fa-tools"
              title: "Environnements de développement"
              content: |
                * Microsoft Visual Studio
                * Xamarin.Android
                * Xamarin.IOS
                * Xamarin.Mac
                * MonoDevelop

############################# Caractéristiques ############################
features:
    enable: true
    title: "GroupDocs.Parser for .NET Caractéristiques"

    feature:
      # feature loop
      - icon: "fas fa-copy"
        content: "Compter statistiquement l'occurrence de mots dans des fichiers uniques ou multiples"

      # feature loop
      - icon: "fas fa-eye"
        content: "Extraire du texte et des métadonnées à partir de feuilles de calcul Excel et de modèles de présentation"

      # feature loop
      - icon: "fas fa-bolt"
        content: "Extraire le contenu textuel d'un fichier ou d'un flux sans installer Document Reader"
      
      # feature loop
      - icon: "fas fa-file-powerpoint"
        content: "Get Formatted Text from a Document using Fast or Standard Extraction de texte Mode"

      # feature loop
      - icon: "fas fa-code"
        content: "Détecter le type de support des documents XML protégés par mot de passe et en extraire le texte"

      # feature loop
      - icon: "fas fa-cloud"
        content: "Obtenir par programme du texte formaté à partir d'e-mails et de pièces jointes"

      # feature loop
      - icon: "fas fa-remove-format"
        content: "Extraire du texte à partir d'une ou plusieurs pages d'un document OneNote"

      # feature loop
      - icon: "fas fa-comment-slash"
        content: "Extraire des données à partir de documents PDF, MS Word, Excel et de présentation"

      # feature loop
      - icon: "fas fa-location-arrow"
        content: "Extraire des données des formulaires PDF et extraire du texte d'un fichier PDF simple ou d'un document de portefeuille PDF"

      # feature loop
      - icon: "fas fa-border-all"
        content: "Obtenir du texte formaté à partir d'une présentation PowerPoint ou chasser du texte à partir d'une diapositive spécifique"

      # feature loop
      - icon: "fas fa-wrench"
        content: "Rassemblez du texte brut ou formaté à partir de cellules, de lignes et de colonnes à partir d'une feuille de calcul Excel"

      # feature loop
      - icon: "fas fa-columns"
        content: "Extraire du texte au format brut ou HTML à partir d'un document Word"

      # feature loop
      - icon: "fas fa-file-word"
        content: "Le formateur HTML prend en charge le formatage des paragraphes, des liens hypertexte, des polices, des en-têtes, des listes et des tableaux"

      # feature loop
      - icon: "fas fa-envelope"
        content: "Extraction d'une seule phrase ou d'un texte entier à partir de fichiers EPUB, CHM, Markdown et FB2"

      # feature loop
      - icon: "fas fa-print"
        content: "Extrait de la table des matières des bases de données, PDF, EPUB, CHM et documents de traitement de texte"

      # feature loop
      - icon: "fas fa-file-archive"
        content: "Extrayez le texte avec sa structure de contenu intacte et extrayez le texte en surbrillance des documents"

      # feature loop
      - icon: "fas fa-lock"
        content: "Obtenir une zone de texte à partir de documents pour analyse et extraire des métadonnées à partir de formats de document pris en charge"

      # feature loop
      - icon: "fas fa-file-code"
        content: "Obtenir toutes les images ou une sélection d'images à partir des formats pris en charge et faire pivoter les images extraites"
      
      # feature loop
      - icon: "fas fa-fill-drip"
        content: "Extraire le texte des fichiers dans les archives Zip et les conteneurs OST et détecter les types de fichiers des éléments de conteneur ZIP"

      # feature loop
      - icon: "fas fa-file-excel"
        content: "Obtenir des données à partir du conteneur de messagerie (serveur Web Exchange, POP3, IMAP)"

      # feature loop
      - icon: "fas fa-heading"
        content: "Rechercher du texte simple, des mots entiers et des expressions régulières dans les documents"

      # feature loop
      - icon: "fas fa-project-diagram"
        content: "Préparer le modèle de document, extraire les données du document et analyser les champs et les tableaux de données"

      # feature loop
      - icon: "fas fa-cube"
        content: "Rechercher et extraire des expressions en surbrillance dans des documents"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Obtenir du texte avec le formateur de texte brut (simple et ASCII) ou avec Markdown Formatter"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Markdown Formatter prend en charge le formatage de la police, des hyperliens, des en-têtes, des listes et des tableaux"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Effectuer un formatage personnalisé avec des bords, des angles et des intersections pour formater du texte brut"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Déplacer la disposition du tableau et détecter les tableaux dans une zone rectangulaire par des séparateurs de colonnes"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Extraire du texte à partir de formes, d'objets WordArt et de zones de texte dans les formats de fichier Microsoft Office"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Extraire des images dans des fichiers - Enregistrer aux formats JPG, PNG, GIF, BMP, PNG ou WEBP"

    more_feature :
      # more_feature_loop
      - title: "Extraire du texte d'un document"
        content: |
          L'utilisation de GroupDocs.Parser pour l'API .NET pour extraire du texte d'un document est simple et réalisée avec seulement quelques lignes de code :

          ```cs
          using(Parser parser = new Parser("sample.docx"))
          {
            // Extraire du texte dans le lecteur
            using(TextReader reader = parser.GetText())
            {
              // Imprimer le texte du document
              // Si l'extraction de texte n'est pas prise en charge, le lecteur est nul
              Console.WriteLine(reader == null ? "Text extraction isn't supported." : reader.ReadToEnd());
            }
          }
          ```

############################# Support ############################
support:
    enable: true

############################# Solutions ############################
solutions:
    enable: true
    title: "GroupDocs.Parser propose des API de visualisation de documents pour d'autres environnements de développement populaires"

    solution:
        # solution loop
        - img_alt: "GroupDocs.Parser for Java"
          image: "/border/groupdocs-parser-java.svg"
          product: "GroupDocs.Parser"
          platform: "Java"
          link: "/parser/java/"

############################# Back to top ###############################
back_to_top:
  enable: true
---