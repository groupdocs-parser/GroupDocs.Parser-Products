


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:19
draft: false
lang: fr
format: Pptx
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "Extraire des codes-barres des fichiers PPTX dans les applications C#"
head_description: "Utilisez GroupDocs.Parser pour détecter et extraire les données des codes-barres à partir des fichiers PPTX dans C# sans logiciel supplémentaire."

############################# Header ############################
title: "Extraire des codes-barres à partir de PPTX en utilisant C#" 
description: "Détectez et extrayez les informations des codes-barres à partir de fichiers PDF, Word, Excel et d'images en utilisant GroupDocs.Parser dans vos applications .NET."
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Téléchargez l'essai gratuit"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "À propos de l'API GroupDocs.Parser for .NET"
    link: "/parser/net/"
    link_title: "En savoir plus"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/) est une API puissante de parsing de documents pour les développeurs .NET. Elle permet l'extraction de texte, d'images, de contenu structuré et de codes-barres à partir de divers formats de fichiers, y compris PDF, Word, Excel, PowerPoint, et plus encore — le tout sans avoir recours aux outils externes.

############################# Steps ############################
steps:
    enable: true
    title: "Étapes pour extraire des codes-barres à partir de Pptx dans C#"
    content: |
      [GroupDocs.Parser](/parser/net/) vous permet d'extraire des données de codes-barres à partir des fichiers PPTX dans les applications .NET en suivant ces étapes simples :
      
      1. Chargez le fichier PPTX en utilisant une instance de Parser.
      2. Vérifiez que le document prend en charge l'extraction de codes-barres.
      3. Récupérez la liste des codes-barres du document.
      4. Parcourez les résultats et utilisez les valeurs des codes-barres extraits.
   
    code:
      platform: "net"
      copy_title: "Copier"
      install:
        command: |
        command: "dotnet add package GroupDocs.Parser"
        copy_tip: "Cliquez pour copier"
        copy_done: "copié"
      links:
        #  loop
        - title: "Plus d'exemples"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
        #  loop
        - title: "Documentation"
          link: "https://docs.groupdocs.com/parser/net/"
          
      content: |
        ```csharp {style=abap}
        // Chargez le document contenant des codes-barres en utilisant la classe Parser
        using (Parser parser = new Parser("input.pptx")) {

            // Vérifiez que le fichier prend en charge l'extraction de codes-barres
            if (!parser.Features.Barcodes) {
                Console.WriteLine("L'extraction de codes-barres n'est pas prise en charge");
                return;
            }

            // Récupérez et traitez les codes-barres extraits
            IEnumerable<PageBarcodeArea> barcodes = parser.GetBarcodes();

            foreach (PageBarcodeArea barcode in barcodes) {
                Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                Console.WriteLine("Value: " + barcode.Value);
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "Fonctionnalités avancées de parsing de documents"
  description: "Au-delà de l'extraction des codes-barres, GroupDocs.Parser vous permet d'extraire du texte brut, des images et des données structurées pour supporter des flux de travail d'automatisation et de traitement de données avancés."
  image: "/img/parser/features_extract-barcode.webp" # 500x500 px
  image_description: "Reconnaissance de codes-barres et parsing de documents"
  features:
    # feature loop
    - title: "Prise en charge de plusieurs formats de codes-barres"
      content: "Reconnaissez les types de codes-barres courants tels que QR Code, Code 128, Data Matrix, EAN, Aztec, et plus."

    # feature loop
    - title: "Extraire des codes-barres des documents et des images"
      content: "Lisez des codes-barres à partir de documents PDF, Word, Excel et de formats d'image tels que JPEG, PNG, et BMP."

    # feature loop
    - title: "Paramètres d'extraction personnalisables"
      content: "Configurez les options de détection, telles que les régions de numérisation et le traitement de documents multi-pages."
      
  code_samples:
    # code sample loop
    - title: "Comment extraire des codes-barres d'un PDF en utilisant des options de codes-barres"
      content: |
        Cet exemple montre comment extraire des codes-barres à partir d'un fichier PDF en utilisant des options spécifiques d'extraction de codes-barres.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Chargez le fichier PDF avec la classe Parser
        using (Parser parser = new Parser("input.pdf"))
        {
            // Confirmez que l'extraction de codes-barres est prise en charge
            if (!parser.Features.Barcodes)
            {
                return;
            }

            // Utilisez des options de codes-barres pour filtrer les résultats
            BarcodeOptions options = new BarcodeOptions(QualityMode.Low, QualityMode.Low, "QR");

            // Récupérez les données de codes-barres du document
            IEnumerable<PageBarcodeArea> barcodes = parser.GetBarcodes(options);

            // Traitez la liste des codes-barres extraits
            foreach (PageBarcodeArea barcode in barcodes)
            {
                Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                Console.WriteLine("Value: " + barcode.Value);
            }
        }
        ```
        {{< /landing/code >}}


############################# Actions ############################

actions:
  enable: true
  title: "Prêt à commencer ?"
  description: "Essayez les fonctionnalités de GroupDocs.Parser gratuitement ou demandez une licence"
  items:
    #  loop
    - title: "Téléchargement Nuget"
      link: "https://releases.groupdocs.com/parser/net/"
      color: "red"
        #  loop
    - title: "Licences"
      link: "https://purchase.groupdocs.com/pricing/parser/net/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "Formats pris en charge pour l'extraction des codes-barres"
    exclude: "PPTX"
    description: "GroupDocs.Parser prend en charge la détection des codes-barres dans une large gamme de formats de documents et d'images. Consultez ci-dessous les types de fichiers couramment pris en charge."
    items: 
        # format loop 1
        - name: "Analyse PDF"
          format: "PDF"
          link: "/parser/net/extract-barcode/pdf/"
          description: "(Format de document portable)"
          
        # format loop 2
        - name: "Analyse DOCX"
          format: "DOCX"
          link: "/parser/net/extract-barcode/docx/"
          description: "(Document Word 2007+)"
          
        # format loop 3
        - name: "Analyse PPTX"
          format: "PPTX"
          link: "/parser/net/extract-barcode/pptx/"
          description: "(Format de présentation Open XML)"
          
        # format loop 4
        - name: "Analyse XLSX"
          format: "XLSX"
          link: "/parser/net/extract-barcode/xlsx/"
          description: "(Classeur Open XML)"
          
        # format loop 5
        - name: "Analyse ODT"
          format: "ODT"
          link: "/parser/net/extract-barcode/odt/"
          description: "(Document texte OpenDocument)"
          
        # format loop 6
        - name: "Analyse ODS"
          format: "ODS"
          link: "/parser/net/extract-barcode/ods/"
          description: "(Tableur OpenDocument)"
          
        # format loop 7
        - name: "Analyse ODP"
          format: "ODP"
          link: "/parser/net/extract-barcode/odp/"
          description: "(Présentation OpenDocument)"
          
        # format loop 8
        - name: "Analyse EPUB"
          format: "EPUB"
          link: "/parser/net/extract-barcode/epub/"
          description: "(Fichier eBook Open)"
          
        # format loop 9
        - name: "Analyse FB2"
          format: "FB2"
          link: "/parser/net/extract-barcode/fb2/"
          description: "(eBook FictionBook)"
         
          

---