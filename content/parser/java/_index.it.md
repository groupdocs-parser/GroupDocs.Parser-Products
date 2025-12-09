---
############################# Static ############################
layout: "landing"
date: 2025-12-09T14:10:41
draft: false

lang: it
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

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
head_title: "GroupDocs.Parser for Java Document Parser SDK per Java"
head_description: "SDK per il parsing di documenti ad alte prestazioni per Java. Estrai testo, immagini, metadati, codici a barre, tabelle e altri dati da PDF, Word, Excel, email e oltre 50 formati di documento."

############################# Header ############################
title: "Document Parser SDK per Java"
description: "Aggiungi parsing di documenti rapido e preciso alle tue app Java ed estrai testo, immagini, metadati e dati strutturati da documenti e immagini."
words:
  for: "per"

actions:
  main: "Download Maven"
  main_link: "https://releases.groupdocs.com/java/repo/com/groupdocs/groupdocs-parser/"
  alt: "Licenza"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/java/"
  title: "Pronto per iniziare?"
  description: "Prova le funzionalità di GroupDocs.Parser gratuitamente o richiedi una licenza"

release:
  title: "Versione {0} rilasciata"
  notes: "Scopri le novità"
  downloads: "Download"

code:
  title: "Analizza rapidamente il contenuto dei documenti con l'SDK"
  more: "Altri esempi"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java/"
  install: |
    <dependency>
      <groupId>com.groupdocs</groupId>
      <artifactId>groupdocs-parser</artifactId>
      <version>{0}</version>
    </dependency>
  content: |
    ```java {style=abap}  
    // Passa il file sorgente all'istanza Parser
    try (Parser parser = new Parser("source.pdf"))
    {
        // Passa il testo del documento a TextReader
        try (TextReader reader = parser.getText())
        {
            // Elabora il testo del documento
            System.out.println(reader == null 
                ? "" 
                : reader.readToEnd());
        }
    }
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser in sintesi"
  description: "Document Parser SDK per eseguire parsing di documenti ad alta precisione nelle applicazioni Java"
  features:
    # feature loop
    - title: "Estrai dati dai documenti"
      content: "GroupDocs.Parser for Java API ti consente di recuperare testo, metadati e immagini da un'ampia gamma di formati di file, come documenti Office, email, allegati e archivi. Questo potente strumento ti aiuta ad accedere e a elaborare in modo efficiente le informazioni preziose contenute in questi file per varie applicazioni, come analisi dei dati, indicizzazione per motori di ricerca o sistemi di gestione dei contenuti."

    # feature loop
    - title: "Analizza documenti"
      content: "Estrai vari elementi come collegamenti ipertestuali, tabelle, codici QR, codici a barre e dati dai moduli PDF. Inoltre, analizza qualsiasi informazione desiderata dai documenti utilizzando template personalizzati."

    # feature loop
    - title: "Personalizzare i risultati"
      content: "Java API consente di recuperare i dati in diversi formati, come grezzo, strutturato, HTML o Markdown. Inoltre, l'API offre una funzionalità di ricerca per individuare parole o frasi specifiche all'interno del testo dei documenti."

############################# Platforms ############################
platforms:
  enable: true
  title: "Indipendenza dalla piattaforma"
  description: "GroupDocs.Parser for Java supporta i seguenti sistemi operativi, framework e gestori di pacchetti"
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
    - title: "Eclipse"
      image: "eclipse"
    # platform loop
    - title: "IntelliJ"
      image: "intellij"
    # platform loop
    - title: "Windows"
      image: "windows"
    # platform loop
    - title: "Linux"
      image: "linux"
    # platform loop
    - title: "Maven"
      image: "maven"

############################# File formats ############################
formats:
  enable: true
  title: "Formati di file supportati"
  description: |
    GroupDocs.Parser for Java supporta operazioni con i seguenti [formati di file](https://docs.groupdocs.com/parser/java/supported-document-formats/).
  groups:
    # group loop
    - color: "green"
      content: |
        ### Formati Microsoft Office
        * **Word:** DOCX, DOC, DOCM, DOT, DOTX, DOTM, RTF
        * **Excel:** XLSX, XLS, XLSM, XLSB, XLTM, XLT, XLTM, XLTX, XLAM, SXC, SpreadsheetML
        * **PowerPoint:** PPT, PPTX, PPS, PPSX, PPSM, POT, POTM, POTX, PPTM
    # group loop
    - color: "blue"
      content: |
        ### Immagini e altri formati
        * **Portatile:** PDF 
        * **Immagini:** JPG, BMP, PNG, TIFF, GIF
        * **Altri formati Office:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### Altri formati
        * **Web:** HTML, MHTML 
        * **Archivi:** ZIP, TAR, 7Z 
        * **e-Book:** CHM, EPUB, FB2, MOBI 
        
        

############################# Features ############################
features:
  enable: true
  title: "GroupDocs.Parser for Java caratteristiche"
  description: "Estrai dati da PDF, documenti Office, immagini e altri formati in modo rapido e preciso con il nostro SDK Java Document Parser"

  items:
    # feature loop
    - icon: "text"
      title: "Estrai testo"
      content: "Estrai informazioni testuali da vari formati di file, come documenti Office, PDF e immagini, per una facile leggibilità e analisi."

    # feature loop
    - icon: "image"
      title: "Estrai immagini"
      content: "Recupera contenuti visivi da diverse fonti, come documenti Office e file PDF, per un accesso e utilizzo pratici."

    # feature loop
    - icon: "qr"
      title: "Scansiona codici QR"
      content: "Rileva e decodifica i codici QR presenti in documenti Office, file PDF o contenuti visivi per un recupero efficiente delle informazioni."

    # feature loop
    - icon: "email"
      title: "Estrai dati da allegati email e archivi"
      content: "Raccogli informazioni preziose da messaggi email, allegati di file e sorgenti di dati compressi per un'analisi e un utilizzo efficaci."

    # feature loop
    - icon: "table"
      title: "Estrai tabelle"
      content: "Identifica ed estrai dati tabulari da documenti PDF per un'analisi e utilizzo organizzati."

    # feature loop
    - icon: "hyperlink"
      title: "Estrai collegamenti ipertestuali"
      content: "Individua ed estrae collegamenti ipertestuali e indirizzi email all'interno di documenti Office o file PDF per un accesso efficiente."

    # feature loop
    - icon: "pdf"
      title: "Analizza moduli PDF"
      content: "I moduli PDF sono documenti digitali con campi compilabili per l'interazione dell'utente, consentendo l'inserimento elettronico delle informazioni. L'API .NET può essere utilizzata per estrarre dati da questi moduli per un'elaborazione efficiente."

    # feature loop
    - icon: "template"
      title: "Analizza dati tramite template"
      content: "Crea template personalizzati e utilizzali con l'API .NET per analizzare informazioni specifiche da file PDF, semplificando i processi di estrazione dei dati."

    # feature loop
    - icon: "search"
      title: "Cerca testo nei documenti"
      content: "Individua rapidamente parole o pattern specifici all'interno dei documenti."


############################# Code samples ############################
code_samples:
  enable: true
  title: "Esempi di codice"
  description: "Alcuni casi d'uso tipici delle operazioni GroupDocs.Parser for Java"
  items:
    # code sample loop
    - title: "Estrai immagini da documenti PDF"
      content: |
        GroupDocs.Parser for Java semplifica per gli sviluppatori Java l'estrazione di immagini dai [documenti](https://docs.groupdocs.com/parser/java/extract-images-from-documents/):
        {{< landing/code title="Estrai immagini da documenti PDF in Java">}}
        ```java {style=abap}
        // Crea un'istanza della classe Parser
        try (Parser parser = new Parser("source.pdf"))
        {
            // Estrai immagini
            Iterable<PageImageArea> images = parser.getImages();

            // Verifica se è stato estratto qualcosa
            if (images == null) {
                return;
            }

            // Itera sulle immagini
            for (PageImageArea image : images) {
                // Stampa l'indice della pagina, il rettangolo e il tipo di immagine
                System.out.println(String.format("Page: %d, R: %s, Type: %s", 
                    image.getPage().getIndex(), image.getRectangle(), image.getFileType()));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Estrai codici a barre dalle immagini"
      content: |
        Utilizza la nostra API Java per estrarre [codici a barre](https://docs.groupdocs.com/parser/java/extract-barcodes-from-document/) dalle immagini:
        {{< landing/code title="Estrai codici a barre dalle immagini in Java">}}
        ```java {style=abap}   
        // Carica l'immagine sorgente in Parser
        try (Parser parser = new Parser("source.jpg")){

            // Verifica se il file supporta l'estrazione di codici a barre
            if (!parser.getFeatures().isBarcodes()) {

                // Estrai i codici a barre dal file
                Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();

                // Itera sui codici a barre
                for (PageBarcodeArea barcode : barcodes) {
                    // Stampa l'indice della pagina
                    System.out.println("Page: " + barcode.getPage().getIndex());
                    // Stampa il valore del codice a barre
                    System.out.println("Value: " + barcode.getValue());
                }
            }
        }
        ```
        {{< /landing/code >}}

---
