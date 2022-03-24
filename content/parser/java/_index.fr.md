---
############################# Static ############################
layout: "product"
date: 2021-04-27T09:31:06+03:00
draft: false

product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "API Java pour analyser du texte, des images et des métadonnées à partir de PDF Word Excel HTML"
head_description: "API d'analyse de documents Java pour extraire du texte, des images, des métadonnées et de l'encodage à partir de bases de données, Word, Excel, présentations, fichiers PDF, e-mail, EPUB et ZIP."

############################# Header ############################
title: "API Java Analyseur pour extraire des données"
description: "API Java pour analyser et extraire des images et du texte avec des métadonnées à partir de documents, présentations, archives et e-mails."
button:
    enable: true

############################# SubMenu ############################
submenu:
    enable: true
    
    left:
        img_alt: "GroupDocs.Parser for Java"
        image: "/border/groupdocs-parser-java.svg"
        product: "GroupDocs.Parser"
        platform: "Java"

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
            - link: "https://purchase.groupdocs.com/pricing/parser/java"
              text: "Pricing"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/java/"
        link_buy: "https://purchase.groupdocs.com"

############################# Aperçu ############################
overview:
    enable: true
    content: |
      GroupDocs.Parser pour Java est une API d'extraction de texte, d'image et de métadonnées, prenant en charge plus de 50 types de documents populaires pour aider à créer des applications métier avec des fonctionnalités d'analyse de texte brut, structuré et formaté. Il prend également en charge l'analyse de documents à l'aide de modèles prédéfinis et permet d'extraire des données complexes de factures et d'autres documents typiques avec rapidité et précision. GroupDocs.Parser pour Java vous permet d'extraire du texte et des métadonnées à partir de fichiers protégés par mot de passe de tous les formats populaires, y compris les documents de traitement de texte, les feuilles de calcul Excel, les présentations PowerPoint, OneNote, les fichiers PDF et les archives ZIP.
    tabs:
      enable: true     
      
      ## TAB ONE ##
      tab_one:
        description: |
          Voici un aperçu de GroupDocs.Parser pour Java :

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
          GroupDocs.Parser pour Java prend en charge les [formats de fichier de document](https://docs.groupdocs.com/parser/java/supported-document-formats/) :

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
          GroupDocs.Parser for Java prend en charge la suite Systèmes d'exploitation:
        
        left:
          enable: true
          table:
            # table loop
            - icon: "fab fa-windows"
              title: "Systèmes d'exploitation"
              content: |
                * Bureau Microsoft Windows
                * Serveur Microsoft Windows
                * Linux
                * Mac OS

            # table loop
            - icon: "fas fa-code"
              title: "Cadres pris en charge"
              content: |
                * Java 7 (1.7) et supérieur

        right:
          enable: true
          table:
            # table loop
            - icon: "fas fa-cogs"
              title: "Environnements de développement"
              content: |
                * NetBeans
                * IDÉE IntelliJ
                * Éclipse
            # table loop
            - icon: "fas fa-tools"
              title: "Outil d'automatisation de construction"
              content: |
                * Maven

############################# Caractéristiques ############################
features:
    enable: true
    title: "GroupDocs.Parser for Java Caractéristiques"

    feature:
      # feature loop
      - icon: "fas fa-copy"
        content: "Compter statistiquement l'occurrence des mots pour un ou plusieurs documents"

      # feature loop
      - icon: "fas fa-eye"
        content: "Extraire du texte et des métadonnées à partir de feuilles de calcul Excel et de modèles de présentation PowerPoint"

      # feature loop
      - icon: "fas fa-bolt"
        content: "Récupérer du texte à partir d'un fichier ou d'un flux, sans installer le lecteur de documents"
      
      # feature loop
      - icon: "fas fa-file-powerpoint"
        content: "Pull Out Formatted Text from a Document Using Fast or Standard Extraction de texte Mode"

      # feature loop
      - icon: "fas fa-code"
        content: "Détecter le type de média des documents XML protégés par mot de passe et en extraire le texte"

      # feature loop
      - icon: "fas fa-cloud"
        content: "Récupérer du texte formaté à partir d'une présentation PowerPoint, d'e-mails et de pièces jointes par programme"

      # feature loop
      - icon: "fas fa-remove-format"
        content: "Chasser le texte d'une ou plusieurs pages d'un document OneNote"

      # feature loop
      - icon: "fas fa-comment-slash"
        content: "Extrayez le texte brut d'un fichier PDF simple ou d'un document de portefeuille PDF"

      # feature loop
      - icon: "fas fa-location-arrow"
        content: "Extraire des données à partir de documents PDF, MS Word, Excel et de présentation"

      # feature loop
      - icon: "fas fa-border-all"
        content: "Extraire du texte brut ou formaté à partir de cellules, de lignes et de colonnes à partir d'une feuille de calcul Excel"

      # feature loop
      - icon: "fas fa-wrench"
        content: "Recueillir du texte brut ou au format HTML à partir d'un document Word et extraire du texte en surbrillance à partir de documents"

      # feature loop
      - icon: "fas fa-columns"
        content: "Obtenir des données à partir des formulaires PDF et obtenir un tableau formaté à partir d'un document PDF ou Word"

      # feature loop
      - icon: "fas fa-file-word"
        content: "Extraction d'une seule phrase ou d'un texte entier à partir de fichiers EPUB, CHM, Markdown et FB2"

      # feature loop
      - icon: "fas fa-envelope"
        content: "Extrait de la table des matières des bases de données, PDF, EPUB, CHM et documents de traitement de texte"

      # feature loop
      - icon: "fas fa-print"
        content: "Récupérer la zone de texte des documents pour analyse et extraire le texte avec sa structure de contenu intacte"

      # feature loop
      - icon: "fas fa-file-archive"
        content: "Obtenir des métadonnées à partir de formats de documents pris en charge"

      # feature loop
      - icon: "fas fa-lock"
        content: "Dessinez toutes les images ou les images sélectionnées à partir des formats pris en charge et faites pivoter les images extraites"

      # feature loop
      - icon: "fas fa-file-code"
        content: "Extraire le texte des fichiers dans les archives Zip et les conteneurs OST - Détecter les types de médias pour les éléments de conteneur Zip"
      
      # feature loop
      - icon: "fas fa-fill-drip"
        content: "Récupérer les données du conteneur de messagerie (serveur Web Exchange, POP3, IMAP)"

      # feature loop
      - icon: "fas fa-file-excel"
        content: "Extrayez du texte des conteneurs de base de données de manière rapide, fiable et efficace"

      # feature loop
      - icon: "fas fa-heading"
        content: "Trouver du texte simple, un mot entier et une expression régulière dans les documents"

      # feature loop
      - icon: "fas fa-project-diagram"
        content: "Préparer le modèle de document, extraire les données du document et analyser les champs et les tableaux de données"

      # feature loop
      - icon: "fas fa-cube"
        content: "Rechercher et extraire les expressions en surbrillance dans les documents"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Extrayez du texte avec le formateur de texte brut (simple et ASCII) ou un formatage personnalisé avec des bords, des angles et des intersections"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Récupérer et formater du texte (police, hyperliens, en-têtes, listes et tableaux) avec Markdown Formatter"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Obtenez du texte avec le formateur HTML et appliquez le formateur au paragraphe, au lien hypertexte, à la police, aux en-têtes, aux listes et aux tableaux"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Déplacer la disposition du tableau et détecter les tableaux dans une zone rectangulaire par des séparateurs de colonnes"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Extraire du texte à partir de formes, d'objets WordArt et de zones de texte dans les formats de fichier Microsoft Office"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Extraire des images dans des fichiers - Enregistrer aux formats JPG, PNG, GIF, BMP, PNG ou WEBP"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Extraire le texte des serveurs de messagerie et des bases de données via JDBC"

    more_feature :
      # more_feature_loop
      - title: "Obtenir du texte avec du texte brut ou des formateurs HTML"
        content: |
          Avec GroupDocs.Parser pour Java, vous pouvez appliquer divers formateurs au texte et au HTML. Vous pouvez extraire du texte avec Plain Text Formatter pour Simple et ASCII. Vous pouvez également obtenir du texte avec HTML Formatter et appliquer une mise en forme au paragraphe, au lien hypertexte, à la police, aux en-têtes, aux listes et aux tableaux.

############################# Support ############################
support:
    enable: true

############################# Solutions ############################
solutions:
    enable: true
    title: "GroupDocs.Parser propose des API de visualisation de documents pour d'autres environnements de développement populaires"

    solution:
        # solution loop
        - img_alt: "GroupDocs.Parser for .NET"
          image: "/border/groupdocs-parser-net.svg"
          product: "GroupDocs.Parser"
          platform: ".NET"
          link: "/parser/net/"

############################# Back to top ###############################
back_to_top:
  enable: true
---