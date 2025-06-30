


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:38
draft: false
lang: id
format: Xml
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Ambil tabel dari dokumen XML dalam aplikasi Java"
head_description: "Ekstrak data tabular terstruktur dari file XML dalam aplikasi Java menggunakan GroupDocs.Parser—tanpa perlu alat eksternal."

############################# Header ############################
title: "Ambil data tabel dari XML menggunakan Java" 
description: "Dengan mulus mendeteksi dan mengekstraksi tabel dari format seperti PDF, DOCX, dan XLSX dengan GroupDocs.Parser dalam alur kerja Java Anda."
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Unduh Versi Percobaan Gratis"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "Pengantar API GroupDocs.Parser for Java"
    link: "/parser/java/"
    link_title: "Pelajari lebih lanjut"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) adalah API ekstraksi konten kaya fitur untuk platform Java. Ini memungkinkan pengembang untuk secara akurat mem-parsing tabel, teks, grafik, tautan, dan data terstruktur dari PDF, dokumen Word, lembar Excel, presentasi PowerPoint, dan lainnya—tanpa memerlukan plugin pihak ketiga.

############################# Steps ############################
steps:
    enable: true
    title: "Cara mengambil tabel dari Xml dalam Java"
    content: |
      Untuk mem-parsing tabel dari dokumen XML menggunakan [GroupDocs.Parser](/parser/java/), ikuti langkah-langkah berikut di lingkungan Java Anda:
      
      1. Buat instance Parser dan muat file XML yang ditargetkan.
      2. Verifikasi bahwa file mendukung ekstraksi tabel terstruktur.
      3. Gunakan API untuk mengambil elemen tabel dari dokumen.
      4. Manfaatkan data yang diekstrak dalam analitik, pelaporan, atau sistem otomatisasi.
   
    code:
      platform: "net"
      copy_title: "Salin"
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
        copy_tip: "klik untuk menyalin"
        copy_done: "disalin"
      links:
        #  loop
        - title: "Lebih banyak contoh"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java/"
        #  loop
        - title: "Dokumentasi"
          link: "https://docs.groupdocs.com/parser/java/"
          
      content: |
        ```java {style=abap}
        // Muat dokumen input dengan Parser yang mencakup elemen tabel
        try (Parser parser = new Parser("input.xml"))
        {
            // Verifikasi bahwa tipe dokumen mendukung pengenalan tabel
            if (!parser.getFeatures().isTables()) {
                System.out.println("Tambahkan logika untuk file yang tidak mendukung tabel");
                return;
            }

            // Tentukan aturan untuk memahami struktur tabel
            TemplateTableLayout layout = new TemplateTableLayout(
                    java.util.Arrays.asList(new Double[]{50.0, 95.0, 275.0, 415.0, 485.0, 545.0}),
                    java.util.Arrays.asList(new Double[]{325.0, 340.0, 365.0, 395.0}));

            // Atur parameter untuk mengekstrak tabel
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            //  Jalankan ekstraksi tabel pada dokumen yang dimuat
            Iterable<PageTableArea> tables = parser.getTables(options);

            //  Proses masing-masing tabel yang diekstrak dari hasil
            for (PageTableArea t : tables) 
            {
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "Alat ekstraksi konten tingkat lanjut"
  description: "Selain membaca tabel, GroupDocs.Parser mendukung pengambilan teks biasa, elemen visual, metadata tertanam, dan objek terstruktur untuk meningkatkan tugas pemrosesan dokumen."
  image: "/img/parser/features_extract-table.webp" # 500x500 px
  image_description: "Ekstraksi konten terstruktur dan data tabular"
  features:
    # feature loop
    - title: "Pemrosesan tabel yang tepat di berbagai format"
      content: "Dukungan untuk mengekstrak tabel dari jenis dokumen standar seperti PDF, Word, Excel, dan HTML dengan akurasi tinggi."

    # feature loop
    - title: "Baca struktur tabular dari berbagai sumber"
      content: "Ambil data tabel dari spreadsheet, dokumen, dan laporan sambil mempertahankan struktur dan penyelarasan."

    # feature loop
    - title: "Pengaturan ekstraksi tabel yang dapat disesuaikan"
      content: "Mengontrol deteksi tata letak, mengelola header dan footer, serta mengatur ekstraksi dengan opsi konfigurasi yang fleksibel."
      
  code_samples:
    # code sample loop
    - title: "Contoh: mengekstrak tabel dari dokumen Excel"
      content: |
        Contoh ini menunjukkan cara mengekstrak dan mengiterasi konten tabel dalam file Excel (XLSX) menggunakan GroupDocs.Parser.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Inisialisasi Parser dengan file Excel
        try (Parser parser = new Parser("input.pdf"))
        {
            // Keluar jika ekstraksi tabel tidak didukung untuk dokumen ini
            if (!parser.getFeatures().isTables())
            {
                return;
            }

            // Terapkan aturan untuk menemukan tata letak tabel
            TemplateTableLayout layout = new TemplateTableLayout(
                    java.util.Arrays.asList(new Double[]{50.0, 95.0, 275.0, 415.0, 485.0, 545.0}),
                    java.util.Arrays.asList(new Double[]{325.0, 340.0, 365.0, 395.0}));

            // Konfigurasi pengaturan untuk ekstraksi tabel
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            // Panggil proses ekstraksi
            Iterable<PageTableArea> tables = parser.getTables(options);

            // Iterasi melalui semua struktur tabel yang diparsing
            for (PageTableArea t : tables)
            {
                // Iterasi melalui setiap baris dalam tabel
                for (int row = 0; row < t.getRowCount(); row++)
                {
                    // Proses setiap sel dalam baris saat ini
                    for (int column = 0; column < t.getColumnCount(); column++) 
                    {
                        // Akses dan baca konten sel saat ini
                        PageTableAreaCell cell = t.getCell(row, column);
                        if (cell != null)
                        {
                            // Output nilai tekstual dari setiap sel tabel
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
  title: "Siap untuk memulai?"
  description: "Coba fitur GroupDocs.Parser secara gratis atau minta lisensi"
  items:
    #  loop
    - title: "Unduh Maven"
      link: "https://releases.groupdocs.com/parser/java/"
      color: "red"
        #  loop
    - title: "Lisensi"
      link: "https://purchase.groupdocs.com/pricing/parser/java/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "Tipe dokumen yang didukung untuk ekstraksi tabel"
    exclude: "XML"
    description: "GroupDocs.Parser menyediakan deteksi tabel yang andal di berbagai jenis file. Berikut adalah daftar format dokumen yang paling umum didukung untuk ekstraksi tabel."
    items: 
        # format loop 1
        - name: "Menganalisis PDF"
          format: "PDF"
          link: "/parser/java/extract-table/pdf/"
          description: "(Format Dokumen Portabel)"
          
        # format loop 2
        - name: "Menganalisis DOCX"
          format: "DOCX"
          link: "/parser/java/extract-table/docx/"
          description: "(Dokumen Word Office 2007+)"
          
        # format loop 3
        - name: "Menganalisis PPTX"
          format: "PPTX"
          link: "/parser/java/extract-table/pptx/"
          description: "(Format Presentasi Open XML)"
          
        # format loop 4
        - name: "Menganalisis XLSX"
          format: "XLSX"
          link: "/parser/java/extract-table/xlsx/"
          description: "(Workbook Open XML)"
          
        # format loop 5
        - name: "Menganalisis TXT"
          format: "TXT"
          link: "/parser/java/extract-table/txt/"
          description: "(File Teks)"
          
        # format loop 6
        - name: "Menganalisis RTF"
          format: "RTF"
          link: "/parser/java/extract-table/rtf/"
          description: "(Format Teks Kaya)"
          
        # format loop 7
        - name: "Menganalisis XML"
          format: "XML"
          link: "/parser/java/extract-table/xml/"
          description: "(Bahasa Markup yang Dapat Diperluas)"
          
        # format loop 8
        - name: "Menganalisis EPUB"
          format: "EPUB"
          link: "/parser/java/extract-table/epub/"
          description: "(File eBook Terbuka)"
         
          

---