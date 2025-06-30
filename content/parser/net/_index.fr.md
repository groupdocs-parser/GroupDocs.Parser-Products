---
############################# Static ############################
layout: "landing"
date: 2025-06-30T10:26:00
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

############################# Head ############################
head_title: "Applications d'analyse de documents GroupDocs.Parser for .NET"
head_description: "Obtenez une solution d'analyse de documents tout-en-un pour les applications .NET. Extrayez des données à partir de formats de documents en ligne à l'aide d'une fonctionnalité simple de glisser-déposer."

############################# Header ############################
title: "Analysez des documents via l'API .NET"
description: "Extrayez des données à partir de documents et d'images sur n'importe quelle plateforme à l'aide de nos APIs flexibles et de solutions basées sur des applications pour les programmeurs et les utilisateurs finaux."
words:
  for: "pour"

actions:
  main: "Télécharger Nuget"
  main_link: "https://www.nuget.org/packages/GroupDocs.Parser"
  alt: "Licences"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/net/"
  title: "Prêt à commencer ?"
  description: "Essayez les fonctionnalités de GroupDocs.Parser gratuitement ou demandez une licence"

release:
  title: "Version {0} publiée"
  notes: "Voir les nouveautés"
  downloads: "Téléchargements"

code:
  title: "Analysez rapidement le contenu des documents"
  more: "Plus d'exemples"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
  install: "dotnet add package GroupDocs.Parser"
  content: |
    ```csharp {style=abap}   
    // Passez le fichier source à l'instance Parser
    using (var parser = new Parser("source.pdf"))
    {
        // Passez le texte du document à TextReader
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
  description: "API pour effectuer l'analyse de documents dans les applications .NET"
  features:
    # feature loop
    - title: "Extraire des données à partir de documents"
      content: "L'API GroupDocs.Parser for .NET vous permet de récupérer du texte, des métadonnées et des images à partir d'une large gamme de formats de fichiers tels que les documents Office, les e-mails, les pièces jointes et les archives. Cet outil puissant vous aide à accéder efficacement et à traiter les informations précieuses contenues dans ces fichiers pour diverses applications comme l'analyse de données, l'indexation par les moteurs de recherche ou les systèmes de gestion de contenu."

    # feature loop
    - title: "Analyser des documents"
      content: "Extraire divers éléments tels que des hyperliens, des tableaux, des QR codes, des codes-barres et des données à partir de formulaires PDF. Analysez également toute information souhaitée à partir des documents en utilisant des modèles personnalisés."

    # feature loop
    - title: "Personnalisation des résultats"
      content: "L'API .NET vous permet de récupérer des données dans divers formats tels que brut, structuré, HTML ou Markdown. De plus, l'API offre une fonctionnalité de recherche pour localiser des mots ou des phrases spécifiques dans le texte des documents."

############################# Platforms ############################
platforms:
  enable: true
  title: "Indépendance de la plateforme"
  description: "GroupDocs.Parser for .NET prend en charge les systèmes d'exploitation, les frameworks et les gestionnaires de paquets suivants"
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
        * **Autres formats de bureau:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### Autres formats
        * **Web:** HTML, MHTML 
        * **Archives:** ZIP, TAR, 7Z 
        * **e-Books:** CHM, EPUB, FB2, MOBI 
        
        

############################# Features ############################
features:
  enable: true
  title: "Fonctionnalités de GroupDocs.Parser for .NET"
  description: "Extraire des données des PDFs, des documents Office et des images rapidement et précisément"

  items:
    # feature loop
    - icon: "text"
      title: "Extraire du texte"
      content: "Extraire des informations textuelles à partir de divers formats de fichiers tels que les documents de bureau, les fichiers PDF et les images pour une lisibilité et une analyse conviviales."

    # feature loop
    - icon: "image"
      title: "Extraire des images"
      content: "Récupérer du contenu visuel à partir de sources diverses comme les documents de bureau et les fichiers PDF pour un accès et une utilisation pratiques."

    # feature loop
    - icon: "qr"
      title: "Scanner des QR Codes"
      content: "Détecter et décoder les QR codes présents dans les documents de bureau, les fichiers PDF ou le contenu visuel pour une récupération efficace des informations."

    # feature loop
    - icon: "email"
      title: "Extraire des données à partir des pièces jointes d'emails et des archives"
      content: "Rassembler des informations précieuses à partir des messages électroniques, des pièces jointes et des sources de données compressées pour une analyse et une utilisation efficaces."

    # feature loop
    - icon: "table"
      title: "Extraire des tableaux"
      content: "Identifier et extraire des données tabulaires à partir de documents PDF pour une analyse et une utilisation organisées."

    # feature loop
    - icon: "hyperlink"
      title: "Extraire des hyperliens"
      content: "Localiser et extraire des hyperliens et des adresses électroniques dans les documents de bureau ou les fichiers PDF pour un accès efficace."

    # feature loop
    - icon: "pdf"
      title: "Analyser des formulaires PDF"
      content: "Les formulaires PDF sont des documents numériques comportant des champs remplissables permettant aux utilisateurs d'entrer des informations électroniquement. L'API .NET peut être utilisée pour extraire des données de ces formulaires pour un traitement efficace."

    # feature loop
    - icon: "template"
      title: "Analyser des données par modèles"
      content: "Créez des modèles personnalisés et utilisez-les avec l'API .NET pour analyser des informations spécifiques à partir de fichiers PDF, simplifiant ainsi les processus d'extraction de données."

    # feature loop
    - icon: "search"
      title: "Rechercher du texte dans des documents"
      content: "Localiser rapidement des mots ou des motifs spécifiques dans des documents."


############################# Code samples ############################
code_samples:
  enable: true
  title: "Exemples de code"
  description: "Quelques cas d'utilisation des opérations typiques GroupDocs.Parser for .NET"
  items:
    # code sample loop
    - title: "Extraire des images à partir de documents PDF"
      content: |
        GroupDocs.Parser for .NET permet aux développeurs C# d'extraire des images à partir de [documents](https://docs.groupdocs.com/parser/net/extract-images-from-documents/) :
        {{< landing/code title="Extraire des images à partir de documents PDF en C#">}}
        ```csharp {style=abap}
        // Créez une instance de la classe Parser
        using (var parser = new Parser("source.pptx"))
        {
            // Extraire des images
            var images = parser.GetImages();

            // Vérifiez si quelque chose a été extrait
            if (images == null)
            {
                return;
            }
            // Parcourez les images
            foreach (PageImageArea image in images)
            {
                // Imprimez l'index de la page, le rectangle et le type d'image
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Type: {2}", 
                    image.Page.Index, image.Rectangle, image.FileType));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Extraire des codes-barres à partir d'images"
      content: |
        Utilisez notre API .NET pour extraire des [codes-barres](https://docs.groupdocs.com/parser/net/extract-barcodes-from-document/) à partir d'images :
        {{< landing/code title="Extraire des codes-barres à partir d'images en C#">}}
        ```csharp {style=abap}   
        // Chargez l'image source dans Parser
        using (var parser = new Parser("source.jpg"))
        {
            // Vérifiez si le fichier prend en charge l'extraction de codes-barres
            if (parser.Features.Barcodes)
            {
                // Extraire des codes-barres du fichier
                var barcodes = parser.GetBarcodes();

                // Parcourez les codes-barres
                foreach (var barcode in barcodes)
                {
                    // Imprimez l'index de la page
                    Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                    // Imprimez la valeur du code-barres
                    Console.WriteLine("Value: " + barcode.Value);
                }
            }
        }
        ```
        {{< /landing/code >}}

---
