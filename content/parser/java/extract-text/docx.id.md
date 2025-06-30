


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:45
draft: false
lang: id
format: Docx
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Ambil teks dari file DOCX dalam aplikasi Java"
head_description: "Manfaatkan GroupDocs.Parser untuk mengekstrak konten teks yang tidak terstruktur atau terstruktur dari dokumen DOCX dalam Java, tanpa ketergantungan eksternal."

############################# Header ############################
title: "Ambil teks dari DOCX menggunakan Java" 
description: "Dengan mulus tarik teks yang dapat dibaca atau terstruktur dari file seperti PDF, Word, Excel, dan lainnya menggunakan GroupDocs.Parser dalam proyek pengembangan Java Anda."
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Unduh Uji Coba Gratis"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "Memperkenalkan API GroupDocs.Parser for Java"
    link: "/parser/java/"
    link_title: "Pelajari lebih lanjut"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) adalah pengurai dokumen yang kuat dan scalable yang dirancang untuk pengembang Java. Ini menawarkan kemampuan untuk mengekstrak teks, tabel, gambar, dan komponen terstruktur secara akurat dari berbagai format termasuk PDF, DOCX, XLSX, PPTX, dan lainnya—tanpa bergantung pada utilitas eksternal.

############################# Steps ############################
steps:
    enable: true
    title: "Cara mengambil teks dari Docx menggunakan Java"
    content: |
      Ikuti langkah-langkah berikut untuk mengekstrak teks dari file DOCX menggunakan [GroupDocs.Parser](/parser/java/) dalam proyek Java Anda:
      
      1. Muat dokumen DOCX menggunakan kelas Parser.
      2. Lakukan ekstraksi teks dari konten file.
      3. Periksa apakah teks berhasil diambil.
      4. Gunakan data teks dalam sistem pencarian, analitik, atau automasi.
   
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
        // Inisialisasi Parser dengan dokumen Anda
        try (Parser parser = new Parser("input.docx"))
        {
            // Baca dan ekstrak semua data teks
            try (TextReader reader = parser.getText())
            {
                // Kembalikan null jika konten teks tidak ada
                // Integrasikan teks yang diekstrak ke dalam alur kerja Anda
                System.out.println(reader == null ? 
                    "Lewati format ekstraksi teks yang tidak didukung" : reader.readToEnd());
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "Fungsionalitas ekstraksi teks yang kaya"
  description: "GroupDocs.Parser melampaui ekstraksi teks sederhana—mendukung pengambilan gambar, metadata, dan data terstruktur untuk meningkatkan tugas pemrosesan konten."
  image: "/img/parser/features_extract-text.webp" # 500x500 px
  image_description: "Ekstrak dan strukturkan konten teks dari dokumen"
  features:
    # feature loop
    - title: "Bekerja di berbagai format dokumen"
      content: "Tangkap baik teks mentah maupun terstruktur dari DOCX, XLSX, PPTX, PDF, HTML, dan berbagai format."

    # feature loop
    - title: "Ekstrak teks dari konten visual dan tekstual"
      content: "Parsing teks dari dokumen yang dipindai, slide, spreadsheet, dan tipe file lain sambil mempertahankan struktur logis."

    # feature loop
    - title: "Kontrol detail atas proses ekstraksi"
      content: "Konfigurasikan rentang halaman, zona tata letak, dan parameter akurasi untuk parsing teks yang lebih tepat."
      
  code_samples:
    # code sample loop
    - title: "Contoh: Mengekstrak daerah teks dari dokumen PPTX"
      content: |
        Contoh ini menunjukkan cara mengekstrak blok teks bersamaan dengan koordinat spasialnya dari presentasi PowerPoint menggunakan GroupDocs.Parser.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Muat file PPTX Anda dengan API Parser
        try (Parser parser = new Parser("input.pptx"))
        {
            // Dapatkan semua zona teks berbentuk persegi
            IEnumerable<PageTextArea> areas = parser.GetTextAreas();

            // Keluar jika fitur ini tidak didukung
            if (areas == null)
            {
                return;
            }

            // Loop melalui area teks per halaman
            for (PageTextArea a : areas)
            {
                // Proses setiap blok teks dengan nomor halamannya dan batas persegi
                System.out.println(String.format("Page: %d, R: %s, Text: %s", a.getPage().getIndex(), a.getRectangle(), a.getText()));
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
    title: "Jenis file yang didukung untuk ekstraksi teks"
    exclude: "DOCX"
    description: "GroupDocs.Parser mampu menarik konten teks dari banyak format file dan gambar. Berikut adalah jenis yang paling umum digunakan yang didukung."
    items: 
        # format loop 1
        - name: "Menganalisis PDF"
          format: "PDF"
          link: "/parser/java/extract-text/pdf/"
          description: "(Format Dokumen Portabel)"
          
        # format loop 2
        - name: "Menganalisis DOCX"
          format: "DOCX"
          link: "/parser/java/extract-text/docx/"
          description: "(Dokumen Word Office 2007+)"
          
        # format loop 3
        - name: "Menganalisis PPTX"
          format: "PPTX"
          link: "/parser/java/extract-text/pptx/"
          description: "(Format Presentasi Open XML)"
          
        # format loop 4
        - name: "Menganalisis XLSX"
          format: "XLSX"
          link: "/parser/java/extract-text/xlsx/"
          description: "(Workbook Open XML)"
          
        # format loop 5
        - name: "Menganalisis TXT"
          format: "TXT"
          link: "/parser/java/extract-text/txt/"
          description: "(File Teks)"
          
        # format loop 6
        - name: "Menganalisis RTF"
          format: "RTF"
          link: "/parser/java/extract-text/rtf/"
          description: "(Format Teks Kaya)"
          
        # format loop 7
        - name: "Menganalisis XML"
          format: "XML"
          link: "/parser/java/extract-text/xml/"
          description: "(Bahasa Markup yang Dapat Diperluas)"
          
        # format loop 8
        - name: "Menganalisis EPUB"
          format: "EPUB"
          link: "/parser/java/extract-text/epub/"
          description: "(File eBook Terbuka)"
         
          

---