


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:38
draft: false
lang: it
format: Pdf
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Recupera tabelle da documenti PDF nelle app Java"
head_description: "Estrai dati tabulari strutturati da file PDF nelle applicazioni Java utilizzando GroupDocs.Parser—senza strumenti esterni."

############################# Header ############################
title: "Recupera dati tabulari da PDF utilizzando Java" 
description: "Rileva ed estrai senza sforzo tabelle da formati come PDF, DOCX e XLSX con GroupDocs.Parser nei tuoi flussi di lavoro Java."
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Scarica la Beta Gratuita"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "Introduzione all'API GroupDocs.Parser for Java"
    link: "/parser/java/"
    link_title: "Scopri di più"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) è un'API per l'estrazione dei contenuti ricca di funzionalità per piattaforme Java. Permette agli sviluppatori di analizzare con precisione tabelle, testo, grafica, collegamenti e dati strutturati da PDF, documenti Word, fogli Excel, presentazioni PowerPoint e altro—senza richiedere plugin di terze parti.

############################# Steps ############################
steps:
    enable: true
    title: "Come recuperare tabelle da Pdf in Java"
    content: |
      Per analizzare tabelle da documenti PDF utilizzando [GroupDocs.Parser](/parser/java/), segui questi passaggi nel tuo ambiente Java:
      
      1. Crea un'istanza di Parser e carica il file PDF di destinazione.
      2. Verifica che il file supporti l'estrazione strutturata delle tabelle.
      3. Utilizza l'API per recuperare gli elementi della tabella dal documento.
      4. Sfrutta i dati estratti in analisi, reportistica o sistemi di automazione.
   
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
        // Carica il documento di input con Parser che include elementi della tabella
        try (Parser parser = new Parser("input.pdf"))
        {
            // Verifica che il tipo di documento consenta il riconoscimento delle tabelle
            if (!parser.getFeatures().isTables()) {
                System.out.println("Aggiungi logica per file che non supportano le tabelle");
                return;
            }

            // Definisci regole per interpretare la struttura della tabella
            TemplateTableLayout layout = new TemplateTableLayout(
                    java.util.Arrays.asList(new Double[]{50.0, 95.0, 275.0, 415.0, 485.0, 545.0}),
                    java.util.Arrays.asList(new Double[]{325.0, 340.0, 365.0, 395.0}));

            // Imposta parametri per estrarre le tabelle
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            //  Esegui l'estrazione delle tabelle sul documento caricato
            Iterable<PageTableArea> tables = parser.getTables(options);

            //  Elabora ciascuna tabella estratta dal risultato
            for (PageTableArea t : tables) 
            {
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "Strumenti avanzati per l'estrazione dei contenuti"
  description: "Oltre a leggere le tabelle, GroupDocs.Parser supporta la cattura di testo semplice, elementi visivi, metadati incorporati e oggetti strutturati per migliorare le attività di elaborazione dei documenti."
  image: "/img/parser/features_extract-table.webp" # 500x500 px
  image_description: "Estrazione di contenuti strutturati e dati tabulari"
  features:
    # feature loop
    - title: "Parsing preciso delle tabelle attraverso formati"
      content: "Supporto per l'estrazione di tabelle da tipi di documento standard come PDF, Word, Excel e HTML con alta precisione."

    # feature loop
    - title: "Leggi strutture tabulari da fonti diverse"
      content: "Recupera dati tabulari da fogli di calcolo, documenti e report mantenendo la struttura e l'allineamento."

    # feature loop
    - title: "Impostazioni di estrazione delle tabelle personalizzabili"
      content: "Controlla il rilevamento del layout, gestisci intestazioni e piè di pagina e affina l'estrazione con opzioni di configurazione flessibili."
      
  code_samples:
    # code sample loop
    - title: "Esempio: estrai tabelle da un documento Excel"
      content: |
        Questo esempio mostra come estrarre e iterare attraverso il contenuto della tabella in un file Excel (XLSX) utilizzando GroupDocs.Parser.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Inizializza Parser con il file Excel
        try (Parser parser = new Parser("input.pdf"))
        {
            // Esci se l'estrazione della tabella non è supportata per questo documento
            if (!parser.getFeatures().isTables())
            {
                return;
            }

            // Applica regole per localizzare il layout della tabella
            TemplateTableLayout layout = new TemplateTableLayout(
                    java.util.Arrays.asList(new Double[]{50.0, 95.0, 275.0, 415.0, 485.0, 545.0}),
                    java.util.Arrays.asList(new Double[]{325.0, 340.0, 365.0, 395.0}));

            // Configura le impostazioni per l'estrazione delle tabelle
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            // Attiva il processo di estrazione
            Iterable<PageTableArea> tables = parser.getTables(options);

            // Itera su tutte le strutture tabellari analizzate
            for (PageTableArea t : tables)
            {
                // Itera su ogni riga all'interno della tabella
                for (int row = 0; row < t.getRowCount(); row++)
                {
                    // Elabora ogni cella nella riga corrente
                    for (int column = 0; column < t.getColumnCount(); column++) 
                    {
                        // Accedi e leggi il contenuto della cella corrente
                        PageTableAreaCell cell = t.getCell(row, column);
                        if (cell != null)
                        {
                            // Output il valore testuale di ciascuna cella della tabella
                            System.out.print(cell.getText());
                            System.out.print(" | ");
                        }
                    }
                }
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
    title: "Tipi di documento supportati per l'estrazione di tabelle"
    exclude: "PDF"
    description: "GroupDocs.Parser offre rilevamento affidabile delle tabelle su più tipi di file. Ecco un elenco dei formati di documento più ampiamente supportati per l'estrazione delle tabelle."
    items: 
        # format loop 1
        - name: "Analizza PDF"
          format: "PDF"
          link: "/parser/java/extract-table/pdf/"
          description: "(Formato Documento Portatile)"
          
        # format loop 2
        - name: "Analizza DOCX"
          format: "DOCX"
          link: "/parser/java/extract-table/docx/"
          description: "(Documento Word Office 2007+)"
          
        # format loop 3
        - name: "Analizza PPTX"
          format: "PPTX"
          link: "/parser/java/extract-table/pptx/"
          description: "(Formato di presentazione Open XML)"
          
        # format loop 4
        - name: "Analizza XLSX"
          format: "XLSX"
          link: "/parser/java/extract-table/xlsx/"
          description: "(Cartella di lavoro Open XML)"
          
        # format loop 5
        - name: "Analizza TXT"
          format: "TXT"
          link: "/parser/java/extract-table/txt/"
          description: "(File di testo)"
          
        # format loop 6
        - name: "Analizza RTF"
          format: "RTF"
          link: "/parser/java/extract-table/rtf/"
          description: "(Formato di Testo Ricco)"
          
        # format loop 7
        - name: "Analizza XML"
          format: "XML"
          link: "/parser/java/extract-table/xml/"
          description: "(Linguaggio di Markup Estensibile)"
          
        # format loop 8
        - name: "Analizza EPUB"
          format: "EPUB"
          link: "/parser/java/extract-table/epub/"
          description: "(File eBook Open)"
         
          

---