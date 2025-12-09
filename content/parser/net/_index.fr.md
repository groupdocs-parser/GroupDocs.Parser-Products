---
############################# Static ############################
layout: "landing"
date: 2025-12-09T14:10:41
draft: false

lang: fr
product: "Parser"
product_tag: "parser"
platform: "Net"
platform_tag: "net"

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
head_title: "GroupDocs.Parser for .NET SDK d'analyse de documents pour .NET"
head_description: "SDK d'analyse de documents haute performance pour .NET. Extrayez le texte, les images, les métadonnées, les codes-barres, les tableaux et d'autres données à partir de PDF, Word, Excel, e‑mails et plus de 50 formats de documents."

############################# Header ############################
title: "SDK d'analyse de documents pour .NET"
description: "Ajoutez une analyse de documents rapide et précise à vos applications .NET et extrayez le texte, les images, les métadonnées et les données structurées à partir de documents et d'images."
words:
  for: "pour"

actions:
  main: "Nuget Télécharger"
  main_link: "https://www.nuget.org/packages/GroupDocs.Parser"
  alt: "Licence"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/net/"
  title: "Prêt à commencer ?"
  description: "Essayez les fonctionnalités de GroupDocs.Parser gratuitement ou demandez une licence"

release:
  title: "Version {0} publiée"
  notes: "Voir les nouveautés"
  downloads: "Téléchargements"

code:
  title: "Analysez rapidement le contenu d'un document avec le SDK"
  more: "Plus d'exemples"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
  install: "dotnet add package GroupDocs.Parser"
  content: |
    ```csharp {style=abap}   
    // Transmettez le fichier source à l'instance Parser
    using (var parser = new Parser("source.pdf"))
    {
        // Transmettez le texte du document à TextReader
        using (var textReader = parser.GetText())
        {
            // Traitez le texte du document
            Console.WriteLine(textReader?.ReadToEnd());
        }
    }  
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser en un coup d'œil"
  description: "SDK d'analyse de documents pour réaliser une analyse de documents haute précision dans les applications .NET"
  features:
    # feature loop
    - title: "Extraire des données à partir de documents"
      content: "GroupDocs.Parser for .NET API vous permet de récupérer le texte, les métadonnées et les images d'un large éventail de formats de fichiers tels que les documents Office, les e‑mails, les pièces jointes et les archives. Cet outil puissant vous aide à accéder et à traiter efficacement les informations précieuses contenues dans ces fichiers pour diverses applications comme l'analyse de données, l'indexation de moteurs de recherche ou les systèmes de gestion de contenu."

    # feature loop
    - title: "Analyser des documents"
      content: "Extrayez divers éléments tels que les hyperliens, les tableaux, les QR codes, les codes-barres et les données des formulaires PDF. Analysez également toute information souhaitée à partir de documents à l'aide de modèles personnalisés."

    # feature loop
    - title: "Personnaliser les résultats"
      content: "L'API .NET vous permet de récupérer des données dans divers formats tels que brut, structuré, HTML ou Markdown. De plus, l'API offre une fonctionnalité de recherche pour localiser des mots ou des phrases spécifiques dans le texte des documents."

############################# Platforms ############################
platforms:
  enable: true
  title: "Indépendance de plateforme"
  description: "GroupDocs.Parser for .NET prend en charge les systèmes d’exploitation, les frameworks et les gestionnaires de packages suivants"
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
    GroupDocs.Parser for .NET prend en charge les opérations avec les [formats de fichiers](https://docs.groupdocs.com/parser/net/supported-document-formats/) suivants.
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
  title: "GroupDocs.Parser for .NET fonctionnalités"
  description: "Extrayez des données des PDF, des documents Office, des images et d'autres formats rapidement et avec précision grâce à notre SDK d'analyse de documents .NET"

  items:
    # feature loop
    - icon: "text"
      title: "Extraire du texte"
      content: "Extrayez les informations textuelles de divers formats de fichiers tels que les documents Office, les fichiers PDF et les images pour une lecture et une analyse aisées."

    # feature loop
    - icon: "image"
      title: "Extraire des images"
      content: "Récupérez le contenu visuel de diverses sources comme les documents Office ou les fichiers PDF pour un accès et une utilisation pratiques."

    # feature loop
    - icon: "qr"
      title: "Scanner les QR Codes"
      content: "Détectez et décodez les QR codes présents dans les documents Office, les fichiers PDF ou le contenu visuel pour une récupération d'informations efficace."

    # feature loop
    - icon: "email"
      title: "Extraire des données des pièces jointes d'e‑mail et des archives"
      content: "Recueillez des informations précieuses à partir des messages électroniques, des pièces jointes et des sources de données compressées pour une analyse et une utilisation efficaces."

    # feature loop
    - icon: "table"
      title: "Extraire les tableaux"
      content: "Identifiez et extrayez les données tabulaires des documents PDF pour une analyse et une utilisation organisées."

    # feature loop
    - icon: "hyperlink"
      title: "Extraire les hyperliens"
      content: "Localisez et extrayez les hyperliens et les adresses e‑mail dans les documents Office ou les fichiers PDF pour un accès efficace."

    # feature loop
    - icon: "pdf"
      title: "Analyser les formulaires PDF"
      content: "Les formulaires PDF sont des documents numériques contenant des champs remplissables pour l’interaction utilisateur, permettant de saisir des informations électroniquement. L’API .NET peut être utilisée pour extraire les données de ces formulaires afin de les traiter efficacement."

    # feature loop
    - icon: "template"
      title: "Analyser les données à l’aide de modèles"
      content: "Créez des modèles personnalisés et utilisez‑les avec l’API .NET pour analyser des informations spécifiques à partir de fichiers PDF, simplifiant ainsi les processus d’extraction de données."

    # feature loop
    - icon: "search"
      title: "Rechercher du texte dans les documents"
      content: "Localisez rapidement des mots ou des motifs spécifiques dans les documents."


############################# Code samples ############################
code_samples:
  enable: true
  title: "Exemples de code"
  description: "Quelques cas d’utilisation typiques des opérations GroupDocs.Parser for .NET"
  items:
    # code sample loop
    - title: "Extraire des images de documents PDF"
      content: |
        GroupDocs.Parser for .NET facilite l’extraction d’images par les développeurs C# à partir des [documents](https://docs.groupdocs.com/parser/net/extract-images-from-documents/) :
        {{< landing/code title="Extraire des images de documents PDF en C#">}}
        ```csharp {style=abap}
        // Créez une instance de la classe Parser
        using (var parser = new Parser("source.pptx"))
        {
            // Extrayez les images
            var images = parser.GetImages();

            // Vérifiez si quelque chose a été extrait
            if (images == null)
            {
                return;
            }
            // Itérez sur les images
            foreach (PageImageArea image in images)
            {
                // Affichez l'index de page, le rectangle et le type d'image
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Type: {2}", 
                    image.Page.Index, image.Rectangle, image.FileType));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Extraire les codes-barres à partir d’images"
      content: |
        Utilisez notre API .NET pour extraire les [codes‑barres](https://docs.groupdocs.com/parser/net/extract-barcodes-from-document/) à partir d’images :
        {{< landing/code title="Extraire les codes-barres d'images en C#">}}
        ```csharp {style=abap}   
        // Chargez l'image source dans Parser
        using (var parser = new Parser("source.jpg"))
        {
            // Vérifiez si le fichier prend en charge l'extraction de codes-barres
            if (parser.Features.Barcodes)
            {
                // Extrayez les codes-barres du fichier
                var barcodes = parser.GetBarcodes();

                // Itérez sur les codes-barres
                foreach (var barcode in barcodes)
                {
                    // Affichez l'index de page
                    Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                    // Affichez la valeur du code-barres
                    Console.WriteLine("Value: " + barcode.Value);
                }
            }
        }
        ```
        {{< /landing/code >}}

---
