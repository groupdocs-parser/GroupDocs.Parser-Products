


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:30
draft: false
lang: it
format: Odp
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Estrai immagini da file ODP nelle applicazioni Java"
head_description: "Con GroupDocs.Parser, puoi estrarre immagini da file ODP in Java senza la necessità di strumenti di terze parti."

############################# Header ############################
title: "Estrai immagini da ODP utilizzando Java" 
description: "Recupera immagini incorporate da file come PDF, Word, Excel e molto altro utilizzando GroupDocs.Parser nel tuo ambiente di sviluppo Java."
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Scarica Prova Gratuita"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "Che cos'è GroupDocs.Parser for Java?"
    link: "/parser/java/"
    link_title: "Scopri di più"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) è un API di parsing ricca di funzionalità progettata per gli sviluppatori Java. Permette l'estrazione di immagini, testo, link e elementi strutturati da vari formati file, inclusi DOCX, XLSX, PDF, PNG, JPG e molti altri — tutto senza la necessità di librerie o applicazioni esterne.

############################# Steps ############################
steps:
    enable: true
    title: "Come estrarre immagini da Odp in Java"
    content: |
      Segui questi passaggi per estrarre immagini da documenti ODP utilizzando [GroupDocs.Parser](/parser/java/) nella tua applicazione Java:
      
      1. Crea un'istanza di Parser e carica il file ODP.
      2. Estrai i dati delle immagini dal documento caricato.
      3. Utilizza o esporta le immagini estratte come necessario.
   
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
        // Inizializza il parser e carica il documento con le immagini utilizzando Parser
        try (Parser parser = new Parser("input.odp"))
        {
            // Raccogli tutti gli elementi immagine incorporati nel documento
            Iterable<PageImageArea> images = parser.getImages();

            // Salta l'elaborazione se il documento non contiene immagini
            if (images == null) {
                return;
            }

            // Gestisci ogni immagine come necessario
            for (PageImageArea image : images) {
                System.out.println(String.format("Page: %d, R: %s, Type: %s", image.getPage().getIndex(), 
                    image.getRectangle(), image.getFileType()));
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "Altre capacità di parsing dei documenti"
  description: "Oltre all'estrazione delle immagini, GroupDocs.Parser consente di estrarre contenuti grezzi come testo, link, metadati e dati strutturati per elaborazione e analisi."
  image: "/img/parser/features_extract-image.webp" # 500x500 px
  image_description: "Estrai immagini e contenuti dai documenti"
  features:
    # feature loop
    - title: "Funziona con una varietà di formati"
      content: "Estrai immagini da diversi tipi di documenti, inclusi PDF, DOCX, PPTX, XLSX, e formati immagine come PNG, JPEG e GIF."

    # feature loop
    - title: "Mantiene chiarezza e risoluzione delle immagini"
      content: "Tutte le immagini estratte mantengono la loro risoluzione originale e il tipo di file per garantire qualità e usabilità costanti."

    # feature loop
    - title: "Opzioni di configurazione flessibili"
      content: "Personalizza il processo di estrazione delle immagini filtrando le immagini per tipo, dimensione, indice di pagina o formato di file."
      
  code_samples:
    # code sample loop
    - title: "Estrai e salva immagini da file PDF"
      content: |
        Questo esempio mostra come estrarre immagini da un documento PDF e salvarle singolarmente sul tuo dispositivo.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Usa Parser per aprire il file PDF
        try (Parser parser = new Parser("input.pdf"))
        {
            // Ottieni le immagini dal contenuto del documento
            Iterable<PageImageArea> images = parser.getImages();

            // Imposta parametri di output come formato (ad esempio, JPEG o PNG)
            ImageOptions options = new ImageOptions(ImageFormat.Png);

            // Salva le immagini estratte in una directory locale
            int imageNumber = 0;
            for (PageImageArea image : images)
            {
                image.save(Constants.getOutputFilePath(String.format("%d.png", imageNumber)), options);
                imageNumber++;
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
    title: "Tipi di file supportati per l'estrazione delle immagini"
    exclude: "ODP"
    description: "GroupDocs.Parser supporta l'estrazione delle immagini in una vasta gamma di documenti e immagini. Esplora i formati comunemente supportati qui sotto."
    items: 
        # format loop 1
        - name: "Analizza PDF"
          format: "PDF"
          link: "/parser/java/extract-image/pdf/"
          description: "(Formato Documento Portatile)"
          
        # format loop 2
        - name: "Analizza DOCX"
          format: "DOCX"
          link: "/parser/java/extract-image/docx/"
          description: "(Documento Word Office 2007+)"
          
        # format loop 3
        - name: "Analizza PPTX"
          format: "PPTX"
          link: "/parser/java/extract-image/pptx/"
          description: "(Formato di presentazione Open XML)"
          
        # format loop 4
        - name: "Analizza XLSX"
          format: "XLSX"
          link: "/parser/java/extract-image/xlsx/"
          description: "(Cartella di lavoro Open XML)"
          
        # format loop 5
        - name: "Analizza ODT"
          format: "ODT"
          link: "/parser/java/extract-image/odt/"
          description: "(Documento di testo OpenDocument)"
          
        # format loop 6
        - name: "Analizza ODS"
          format: "ODS"
          link: "/parser/java/extract-image/ods/"
          description: "(Foglio di calcolo OpenDocument)"
          
        # format loop 7
        - name: "Analizza ODP"
          format: "ODP"
          link: "/parser/java/extract-image/odp/"
          description: "(Presentazione OpenDocument)"
          
        # format loop 8
        - name: "Analizza EPUB"
          format: "EPUB"
          link: "/parser/java/extract-image/epub/"
          description: "(File eBook Open)"
          
        # format loop 9
        - name: "Analizza FB2"
          format: "FB2"
          link: "/parser/java/extract-image/fb2/"
          description: "(eBook FictionBook)"
         
          

---