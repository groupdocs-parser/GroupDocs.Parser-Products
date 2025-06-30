


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:17
draft: false
lang: it
format: Xlsx
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Leggi codici a barre dai file XLSX nelle app Java"
head_description: "Con GroupDocs.Parser, estrai dati dei codici a barre dai documenti XLSX utilizzando Java senza strumenti esterni."

############################# Header ############################
title: "Leggi codici a barre da XLSX utilizzando Java" 
description: "Estrai contenuti di codici a barre da file PDF, Word, Excel e immagini utilizzando GroupDocs.Parser nelle tue applicazioni Java."
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Scarica la versione di prova gratuita"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "Panoramica dell'API GroupDocs.Parser for Java"
    link: "/parser/java/"
    link_title: "Scopri di più"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) offre una soluzione completa per il parsing dei documenti in Java. Consente agli sviluppatori di estrarre codici a barre, testo, immagini e informazioni strutturate da diversi formati di file come PDF, Word, Excel, PowerPoint e altri, senza la necessità di librerie di terze parti.

############################# Steps ############################
steps:
    enable: true
    title: "Come leggere codici a barre da Xlsx in Java"
    content: |
      Con [GroupDocs.Parser](/parser/java/), gli sviluppatori di Java possono estrarre codici a barre dai documenti XLSX in pochi passaggi:
      
      1. Carica il documento XLSX utilizzando Parser.
      2. Verifica che il documento supporti l'estrazione dei codici a barre.
      3. Usa l'API per recuperare i dati dei codici a barre.
      4. Scorri i risultati dei codici a barre e applicali secondo necessità.
   
    code:
      platform: "net"
      copy_title: "Copia"
      install:
        command: |
          <dependencies>
            <dependency>
              <groupId>com.groupdocs</groupId>
              <artifactId>groupdocs-parser</artifactId>
              <version>{0}</version>
            </dependency>
          </dependencies>

          <repositories>
            <repository>
              <id>repository.groupdocs.com</id>
              <name>GroupDocs Repository</name>
              <url>https://repository.groupdocs.com/repo/</url>
            </repository>
          </repositories>
        copy_tip: "clicca per copiare"
        copy_done: "copiato"
      links:
        #  loop
        - title: "Altri esempi"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java/"
        #  loop
        - title: "Documentazione"
          link: "https://docs.groupdocs.com/parser/java/"
          
      content: |
        ```java {style=abap}
        // Apri un documento contenente codici a barre utilizzando Parser
        try (Parser parser = new Parser("input.xlsx"))
        {
            // Controlla il supporto per i codici a barre per il file
            if (!parser.getFeatures().isBarcodes())
            {
                System.out.println("Gestisci tipi di file non supportati");
                return;
            }

            // Estrai e utilizza i dati dei codici a barre
            Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();
            for(PageBarcodeArea barcode : barcodes)
            {
                System.out.println("Page: " + barcode.getPage().getIndex());
                System.out.println("Value: " + barcode.getValue());
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "Ulteriori capacità di parsing"
  description: "GroupDocs.Parser va oltre l'estrazione dei codici a barre: consente anche di estrarre testo semplice, immagini ed elementi strutturati per supportare flussi di lavoro basati sui dati."
  image: "/img/parser/features_extract-barcode.webp" # 500x500 px
  image_description: "Funzionalità di estrazione codici a barre e dati"
  features:
    # feature loop
    - title: "Ampio supporto per formati di codici a barre"
      content: "Rileva formati di codici a barre standard tra cui QR Code, Code 39, Data Matrix, EAN, Aztec e altri."

    # feature loop
    - title: "Leggi codici a barre da più fonti"
      content: "Estrai informazioni sui codici a barre da documenti Office, PDF e file immagine come PNG, JPG e BMP."

    # feature loop
    - title: "Impostazione personalizzata della lettura dei codici a barre"
      content: "Affina l'estrazione dei codici a barre con opzioni per mirare a regioni specifiche e file multi-pagina."
      
  code_samples:
    # code sample loop
    - title: "Esempio: estrai codici a barre da PDF con opzioni"
      content: |
        Questo esempio dimostra l'estrazione di codici a barre da un documento PDF utilizzando impostazioni personalizzate.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Inizializza il parser con un documento PDF
        try (Parser parser = new Parser("input.pdf"))
        {
            // Assicurati che il documento supporti la lettura dei codici a barre
            if (!parser.getFeatures().isBarcodes())
            {
                return;
            }

            // Applica filtri con le opzioni dei codici a barre
            BarcodeOptions options = new BarcodeOptions(QualityMode.Low, QualityMode.Low, "QR");

            // Estrai i codici a barre utilizzando il parser
            Iterable<PageBarcodeArea> barcodes = parser.getBarcodes(options);

            // Gestisci ciascun risultato del codice a barre
            for (PageBarcodeArea barcode : barcodes)
            {
                System.out.println("Page: " + String.valueOf(barcode.getPage().getIndex()));
                System.out.println("Value: " + barcode.getValue());
            }
        }
        ```
        {{< /landing/code >}}


############################# Actions ############################

actions:
  enable: true
  title: "Pronto per iniziare?"
  description: "Prova le funzionalità di GroupDocs.Parser gratuitamente o richiedi una licenza"
  items:
    #  loop
    - title: "Download di Maven"
      link: "https://releases.groupdocs.com/parser/java/"
      color: "red"
        #  loop
    - title: "Licenze"
      link: "https://purchase.groupdocs.com/pricing/parser/java/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "Formati di file supportati per la lettura dei codici a barre"
    exclude: "XLSX"
    description: "GroupDocs.Parser può leggere codici a barre da molti tipi di documenti e immagini. Di seguito sono riportati alcuni dei formati comunemente supportati."
    items: 
        # format loop 1
        - name: "Analizza PDF"
          format: "PDF"
          link: "/parser/java/extract-barcode/pdf/"
          description: "(Formato Documento Portatile)"
          
        # format loop 2
        - name: "Analizza DOCX"
          format: "DOCX"
          link: "/parser/java/extract-barcode/docx/"
          description: "(Documento Word Office 2007+)"
          
        # format loop 3
        - name: "Analizza PPTX"
          format: "PPTX"
          link: "/parser/java/extract-barcode/pptx/"
          description: "(Formato di presentazione Open XML)"
          
        # format loop 4
        - name: "Analizza XLSX"
          format: "XLSX"
          link: "/parser/java/extract-barcode/xlsx/"
          description: "(Cartella di lavoro Open XML)"
          
        # format loop 5
        - name: "Analizza ODT"
          format: "ODT"
          link: "/parser/java/extract-barcode/odt/"
          description: "(Documento di testo OpenDocument)"
          
        # format loop 6
        - name: "Analizza ODS"
          format: "ODS"
          link: "/parser/java/extract-barcode/ods/"
          description: "(Foglio di calcolo OpenDocument)"
          
        # format loop 7
        - name: "Analizza ODP"
          format: "ODP"
          link: "/parser/java/extract-barcode/odp/"
          description: "(Presentazione OpenDocument)"
          
        # format loop 8
        - name: "Analizza EPUB"
          format: "EPUB"
          link: "/parser/java/extract-barcode/epub/"
          description: "(File eBook Open)"
          
        # format loop 9
        - name: "Analizza FB2"
          format: "FB2"
          link: "/parser/java/extract-barcode/fb2/"
          description: "(eBook FictionBook)"
         
          

---