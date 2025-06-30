


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:24
draft: false
lang: it
format: Docx
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Estrai collegamenti ipertestuali da file DOCX in app Java"
head_description: "Utilizza GroupDocs.Parser per trovare ed estrarre collegamenti URL da documenti DOCX nei progetti Java—senza necessità di software aggiuntivo."

############################# Header ############################
title: "Estrai collegamenti ipertestuali da DOCX con Java" 
description: "Estrai collegamenti web e collegamenti ipertestuali da file PDF, documenti Word, fogli Excel e altri documenti utilizzando GroupDocs.Parser nel tuo ambiente Java."
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Scarica la Versione di Prova Gratuita"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "Informazioni sull'API GroupDocs.Parser for Java"
    link: "/parser/java/"
    link_title: "Scopri di più"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) è un'API robusta per l'estrazione di contenuti progettata per sviluppatori Java. Offre strumenti per estrarre collegamenti ipertestuali, dati strutturati, immagini e testo da formati popolari come DOCX, XLSX, PDF, HTML e altro—il tutto senza la necessità di plugin esterni.

############################# Steps ############################
steps:
    enable: true
    title: "Come estrarre collegamenti ipertestuali da Docx in Java"
    content: |
      [GroupDocs.Parser](/parser/java/) semplifica l'estrazione di collegamenti ipertestuali da file DOCX nelle applicazioni Java con questi passaggi fondamentali:
      
      1. Apri il file DOCX utilizzando un'istanza di Parser.
      2. Assicurati che l'estrazione dei collegamenti ipertestuali sia disponibile per il formato del file.
      3. Estrai tutti i collegamenti ipertestuali utilizzando il metodo appropriato.
      4. Scorri i risultati e processa ogni collegamento come necessario.
   
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
        // Carica il file che può contenere collegamenti ipertestuali utilizzando Parser
        try (Parser parser = new Parser("input.docx")) {

            // Controlla se il formato del documento supporta l'analisi dei collegamenti ipertestuali
            if (!parser.getFeatures().isHyperlinks()) {
                System.out.println("L'estrazione dei collegamenti ipertestuali non è disponibile per il file");
                return;
            }

            // Estrai e utilizza i dati dei collegamenti ipertestuali dal documento
            Iterable<PageHyperlinkArea> hyperlinks = parser.getHyperlinks();

            for (PageHyperlinkArea h : hyperlinks) {
                System.out.println(h.getText());
                System.out.println(h.getUrl());
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "Strumenti completi per l'analisi dei documenti"
  description: "Oltre ad estrarre collegamenti ipertestuali, GroupDocs.Parser ti consente di raccogliere altri contenuti utili come testo semplice, media incorporati e dati strutturati per utilizzi in flussi di lavoro automatizzati."
  image: "/img/parser/features_extract-hyperlink.webp" # 500x500 px
  image_description: "Estrazione di collegamenti ipertestuali e analisi dei documenti"
  features:
    # feature loop
    - title: "Rilevamento preciso dei collegamenti"
      content: "Cattura tutti i tipi di collegamenti ipertestuali da diversi layout di documenti, inclusi testi cliccabili e URL nascosti."

    # feature loop
    - title: "Funziona con documenti e contenuti web"
      content: "Estrai collegamenti da file PDF, DOCX, XLSX, HTML e file immagine che contengono collegamenti ipertestuali incorporati."

    # feature loop
    - title: "Comportamento di estrazione personalizzato"
      content: "Affina il modo in cui vengono estratti i collegamenti ipertestuali utilizzando opzioni come intervalli di pagina, tipi di collegamenti o filtri di contenuto."
      
  code_samples:
    # code sample loop
    - title: "Esempio: estrazione di collegamenti ipertestuali da un PDF con opzioni personalizzate"
      content: |
        Questo esempio dimostra come estrarre tutti i collegamenti da un file PDF utilizzando impostazioni di estrazione dei collegamenti.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Apri il PDF utilizzando la classe Parser
        try (Parser parser = new Parser("input.docx"))
        {
            // Verifica che il supporto dei collegamenti ipertestuali sia abilitato per questo documento
            if (!parser.getFeatures().isHyperlinks()) {
                return;
            }

            // Applica opzioni per filtrare i collegamenti
            PageAreaOptions options = new PageAreaOptions(new Rectangle(new Point(380, 90), new Size(150, 50)));

            // Usa il parser per ottenere i dati dei collegamenti ipertestuali
            Iterable<PageHyperlinkArea> hyperlinks = parser.getHyperlinks(options);

            // Itera tra i collegamenti e gestiscili di conseguenza
            for (PageHyperlinkArea h : hyperlinks) {
                System.out.println(h.getText());
                System.out.println(h.getUrl());
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
    title: "Formati di documento che supportano l'estrazione di collegamenti ipertestuali"
    exclude: "DOCX"
    description: "Con GroupDocs.Parser, puoi estrarre collegamenti ipertestuali da molti formati file comunemente utilizzati. Di seguito è riportato un elenco di formati tipicamente supportati."
    items: 
        # format loop 1
        - name: "Analizza PDF"
          format: "PDF"
          link: "/parser/java/extract-hyperlink/pdf/"
          description: "(Formato Documento Portatile)"
          
        # format loop 2
        - name: "Analizza DOCX"
          format: "DOCX"
          link: "/parser/java/extract-hyperlink/docx/"
          description: "(Documento Word Office 2007+)"
          
        # format loop 3
        - name: "Analizza PPTX"
          format: "PPTX"
          link: "/parser/java/extract-hyperlink/pptx/"
          description: "(Formato di presentazione Open XML)"
          
        # format loop 4
        - name: "Analizza XLSX"
          format: "XLSX"
          link: "/parser/java/extract-hyperlink/xlsx/"
          description: "(Cartella di lavoro Open XML)"
          
        # format loop 5
        - name: "Analizza TXT"
          format: "TXT"
          link: "/parser/java/extract-hyperlink/txt/"
          description: "(File di testo)"
          
        # format loop 6
        - name: "Analizza RTF"
          format: "RTF"
          link: "/parser/java/extract-hyperlink/rtf/"
          description: "(Formato di Testo Ricco)"
          
        # format loop 7
        - name: "Analizza XML"
          format: "XML"
          link: "/parser/java/extract-hyperlink/xml/"
          description: "(Linguaggio di Markup Estensibile)"
          
        # format loop 8
        - name: "Analizza EPUB"
          format: "EPUB"
          link: "/parser/java/extract-hyperlink/epub/"
          description: "(File eBook Open)"
         
          

---