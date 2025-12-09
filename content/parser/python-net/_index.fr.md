---
############################# Static ############################
layout: "landing"
date: 2025-12-09T21:34:38
draft: false

lang: fr
product: "Parser"
product_tag: "parser"
platform: "Python"
platform_tag: "python-net"

############################# Drop-down ############################
supported_platforms:
  items:
    # supported_platforms loop
    - title: ".NET"
      tag: "net"
    # supported_platforms loop
    - title: "Java"
      tag: "java"
    # supported_platforms loop
    - title: "Python"
      tag: "python-net"

############################# Head ############################
head_title: "GroupDocs.Parser for Python via .NET SDK d'analyseur de documents pour Python"
head_description: "SDK d'analyseur de documents haute performance pour Python. Extrayez le texte, les images, les métadonnées, les codes-barres, les tableaux et d'autres données à partir de PDF, Word, Excel, e‑mails et plus de 50 formats de documents."

############################# Header ############################
title: "SDK d'analyseur de documents pour Python"
description: "Ajoutez une analyse de documents rapide et précise à vos applications Python et extrayez le texte, les images, les métadonnées et les données structurées à partir de documents et d’images."
words:
  for: "pour"

actions:
  hidden: true # Hide version 0 is released
  main: "Télécharger PyPI"
  main_link: "https://pypi.org/project/groupdocs-parser-net/"
  alt: "Licence"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/python-net/"
  title: "Prêt à commencer ?"
  description: "Essayez les fonctionnalités de GroupDocs.Parser gratuitement ou demandez une licence"

release:
  enable: false
  title: "Version {0} publiée"
  notes: "Voir les nouveautés"
  downloads: "Téléchargements"

code:
  title: "Extraire du texte avec Python"
  more: "Plus d'exemples"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Python-via-.NET/"
  install: "pip install groupdocs-parser-net"
  content: |
    ```python {style=abap}  
    from groupdocs.parser import Parser

    # Charger le document
    with Parser("sample.pdf") as parser:
        # Extraire le texte du document
        text = parser.GetText()

        # Imprimer tout le texte extrait
        print(text)
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser en un coup d'œil"
  description: "SDK d'analyseur de documents pour effectuer une analyse de documents à haute précision dans les applications Python"
  features:
    # feature loop
    - title: "Extraire des données depuis les documents"
      content: "GroupDocs.Parser for Python via .NET API vous permet de récupérer le texte, les métadonnées et les images d'un large éventail de formats de fichiers tels que les documents Office, les e‑mails, les pièces jointes et les archives. Cet outil puissant vous aide à accéder et à traiter efficacement les informations précieuses contenues dans ces fichiers pour diverses applications comme l’analyse de données, l’indexation de moteurs de recherche ou les systèmes de gestion de contenu."

    # feature loop
    - title: "Analyser les documents"
      content: "Extrayez divers éléments tels que les hyperliens, les tableaux, les QR codes, les codes-barres et les données des formulaires PDF. Analysez également toute information souhaitée à partir de documents en utilisant des modèles personnalisés."

    # feature loop
    - title: "Personnaliser les résultats"
      content: "Python API vous permet de récupérer des données dans divers formats tels que brut, structuré, HTML ou Markdown. De plus, l'API propose une fonctionnalité de recherche pour localiser des mots ou des expressions spécifiques dans le texte des documents."

############################# Platforms ############################
platforms:
  enable: true
  title: "Indépendance de plateforme"
  description: "GroupDocs.Parser for Python via .NET prend en charge les systèmes d'exploitation, frameworks et gestionnaires de paquets suivants"
  items:
    # platform loop
    - title: "Amazon"
      image: "amazon"
    # platform loop
    - title: "Docker"
      image: "docker"
    # platform loop
    - title: "Azure"
      image: "azure"
    # platform loop
    - title: "VS Code"
      image: "vs_code"
    # platform loop
    - title: "ReSharper"
      image: "resharper"
    # platform loop
    - title: "macOS"
      image: "finder"
    # platform loop
    - title: "Linux"
      image: "linux"
    # platform loop
    - title: "NuGet"
      image: "nuget"

############################# File formats ############################
formats:
  enable: true
  title: "Formats de fichiers pris en charge"
  description: |
    GroupDocs.Parser for Python via .NET prend en charge les opérations avec les [formats de fichiers](https://docs.groupdocs.com/parser/python-net/supported-document-formats/) suivants.
  groups:
    # group loop
    - color: "green"
      content: |
        ### Formats Microsoft Office
        * **Word:** DOCX, DOC, DOCM, DOT, DOTX, DOTM, RTF
        * **Excel:** XLSX, XLS, XLSM, XLSB, XLTM, XLT, XLTM, XLTX, XLAM, SXC, SpreadsheetML
        * **PowerPoint:** PPT, PPTX, PPS, PPSX, PPSM, POT, POTM, POTX, PPTM
    # group loop
    - color: "blue"
      content: |
        ### Images et autres formats
        * **Portable:** PDF 
        * **Images:** JPG, BMP, PNG, TIFF, GIF
        * **Autres formats Office:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### Autres formats
        * **Web:** HTML, MHTML 
        * **Archives:** ZIP, TAR, 7Z 
        * **e-books:** CHM, EPUB, FB2, MOBI 

############################# Features ############################
features:
  enable: true
  title: "Fonctions GroupDocs.Parser for Python via .NET"
  description: "Extrayez des données des PDF, des documents Office, des images et d'autres formats rapidement et précisément avec notre SDK d'analyseur de documents Python"

  items:
    # feature loop
    - icon: "text"
      title: "Extraire du texte"
      content: "Extrayez des informations textuelles de divers formats de fichiers tels que les documents Office, les fichiers PDF et les images pour une lisibilité et une analyse aisées."

    # feature loop
    - icon: "image"
      title: "Extraire des images"
      content: "Récupérez le contenu visuel de diverses sources comme les documents Office, les fichiers PDF pour un accès et une utilisation pratiques."

    # feature loop
    - icon: "qr"
      title: "Scanner les QR codes"
      content: "Détectez et décodez les QR codes présents dans les documents Office, les fichiers PDF ou le contenu visuel pour une récupération d'information efficace."

    # feature loop
    - icon: "email"
      title: "Extraire des données des pièces jointes d'e‑mail et des archives"
      content: "Collectez des informations précieuses à partir des messages e‑mail, des pièces jointes et des sources de données compressées pour une analyse et une exploitation efficaces."

    # feature loop
    - icon: "table"
      title: "Extraire des tableaux"
      content: "Identifiez et extrayez les données tabulaires des documents PDF pour une analyse et une utilisation organisées."

    # feature loop
    - icon: "hyperlink"
      title: "Extraire les hyperliens"
      content: "Localisez et extrayez les hyperliens et adresses e‑mail dans les documents Office ou les fichiers PDF pour un accès efficace."

    # feature loop
    - icon: "pdf"
      title: "Analyser les formulaires PDF"
      content: "Les formulaires PDF sont des documents numériques contenant des champs remplissables pour l'interaction utilisateur, permettant de saisir des informations électroniquement. L'API Python peut être utilisée pour extraire les données de ces formulaires afin d'optimiser le traitement."

    # feature loop
    - icon: "template"
      title: "Analyser les données par modèles"
      content: "Créez des modèles personnalisés et utilisez‑les avec l'API Python pour analyser des informations spécifiques à partir de fichiers PDF, simplifiant ainsi les processus d'extraction de données."

    # feature loop
    - icon: "search"
      title: "Rechercher du texte dans des documents"
      content: "Localisez rapidement des mots ou des motifs spécifiques dans les documents."


############################# Code samples ############################
code_samples:
  enable: true
  title: "Exemples de code"
  description: "Au‑delà de l'extraction de texte de base, voici les cas d'utilisation les plus courants pour une extraction rapide de texte, d'images et de métadonnées."
  items:
    # code sample loop
    - title: "Rechercher du texte dans un document"
      content: |
        Cet exemple montre comment rechercher une phrase précise dans un document PDF et afficher où elle a été trouvée.
        {{< landing/code title="Recherche de texte dans un document en Python">}}
        ```python {style=abap}
        from groupdocs.parser import Parser

        # Charger le document
        with Parser("sample.pdf") as parser:
            # Afficher l'index de page et le rectangle où la phrase a été trouvée
            for area in parser.Search("Total Amount"):
                # Afficher l'index de page et le rectangle où la phrase a été trouvée
                print(f"Page {area.PageIndex}, Rectangle: {area.Rectangle}")
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Extraire des images d'un document"
      content: |
        Cet exemple montre comment extraire des images d'un document PDF et les enregistrer dans un fichier.
        {{< landing/code title="Extraction d'images d'un document en Python">}}
        ```python {style=abap}    
        from groupdocs.parser import Parser

        # Charger le document
        with Parser("sample.docx") as parser:
            # Extraire les images du document
            images = parser.GetImages()

            # Enregistrer les images dans un fichier
            index = 1
            for image in images:
                image.Save(f"image_{index}.png")
                index += 1
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Extraire les métadonnées d'un document"
      content: |
        Cet exemple montre comment extraire les métadonnées d'un document PDF et les afficher.
        {{< landing/code title="Extraction de métadonnées d'un document en Python">}}
        ```python {style=abap}    
        from groupdocs.parser import Parser

        # Charger le document
        with Parser("sample.pdf") as parser:
            # Extraire les métadonnées du document
            metadata = parser.GetMetadata()

            # Afficher les métadonnées
            for item in metadata:
                print(f"{item.Name}: {item.Value}")
        ```
        {{< /landing/code >}}
---
