


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:24
draft: false
lang: id
format: Docx
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Ekstrak hyperlink dari file DOCX dalam aplikasi Java"
head_description: "Gunakan GroupDocs.Parser untuk menemukan dan mengekstrak tautan URL dari dokumen DOCX dalam proyek Java—tanpa perangkat lunak tambahan."

############################# Header ############################
title: "Ekstrak hyperlink dari DOCX dengan Java" 
description: "Ambil tautan web dan hyperlink dari file PDF, dokumen Word, lembar Excel, dan dokumen lainnya menggunakan GroupDocs.Parser di lingkungan Java Anda."
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
    title: "Tentang API GroupDocs.Parser for Java"
    link: "/parser/java/"
    link_title: "Pelajari lebih lanjut"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) adalah API ekstraksi konten yang kuat yang dirancang untuk pengembang Java. Ini menawarkan alat untuk mengekstrak hyperlink, data terstruktur, gambar, dan teks dari format populer seperti DOCX, XLSX, PDF, HTML, dan banyak lagi—semua tanpa memerlukan plugin eksternal.

############################# Steps ############################
steps:
    enable: true
    title: "Cara mengekstrak hyperlink dari Docx dalam Java"
    content: |
      [GroupDocs.Parser](/parser/java/) menyederhanakan ekstraksi hyperlink dari file DOCX dalam aplikasi Java dengan langkah-langkah dasar berikut:
      
      1. Buka file DOCX menggunakan instance dari Parser.
      2. Pastikan ekstraksi hyperlink tersedia untuk format file.
      3. Ekstrak semua hyperlink menggunakan metode yang sesuai.
      4. Iterasikan hasil dan proses setiap tautan sesuai kebutuhan.
   
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
        // Muat file yang mungkin berisi hyperlink menggunakan Parser
        try (Parser parser = new Parser("input.docx")) {

            // Periksa apakah format dokumen mendukung penguraian hyperlink
            if (!parser.getFeatures().isHyperlinks()) {
                System.out.println("Ekstraksi hyperlink tidak tersedia untuk file ini");
                return;
            }

            // Ekstrak dan gunakan data hyperlink dari dokumen
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
  title: "Alat pemrosesan dokumen yang komprehensif"
  description: "Selain mengekstrak hyperlink, GroupDocs.Parser memungkinkan Anda mengumpulkan konten berguna lainnya seperti teks biasa, media terbenam, dan data terstruktur untuk digunakan dalam alur kerja otomatis."
  image: "/img/parser/features_extract-hyperlink.webp" # 500x500 px
  image_description: "Ekstraksi hyperlink dan analisis dokumen"
  features:
    # feature loop
    - title: "Deteksi tautan yang akurat"
      content: "Tangkap semua jenis hyperlink dari berbagai tata letak dokumen, termasuk teks yang dapat diklik dan URL tersembunyi."

    # feature loop
    - title: "Bekerja dengan dokumen dan konten web"
      content: "Ambil tautan dari file PDF, DOCX, XLSX, HTML, dan file gambar yang berisi hyperlink terbenam."

    # feature loop
    - title: "Perilaku ekstraksi khusus"
      content: "Sempurnakan cara hyperlink diekstrak menggunakan opsi seperti rentang halaman, jenis tautan, atau filter konten."
      
  code_samples:
    # code sample loop
    - title: "Contoh: mengekstrak hyperlink dari PDF dengan opsi khusus"
      content: |
        Contoh ini menunjukkan cara mengekstrak semua tautan dari file PDF menggunakan pengaturan ekstraksi tautan.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Buka PDF menggunakan kelas Parser
        try (Parser parser = new Parser("input.docx"))
        {
            // Verifikasi bahwa dukungan hyperlink diaktifkan untuk dokumen ini
            if (!parser.getFeatures().isHyperlinks()) {
                return;
            }

            // Terapkan opsi untuk memfilter tautan
            PageAreaOptions options = new PageAreaOptions(new Rectangle(new Point(380, 90), new Size(150, 50)));

            // Gunakan parser untuk mendapatkan data hyperlink
            Iterable<PageHyperlinkArea> hyperlinks = parser.getHyperlinks(options);

            // Iterasikan tautan dan tangani sesuai kebutuhan
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
    title: "Format dokumen yang mendukung ekstraksi hyperlink"
    exclude: "DOCX"
    description: "Dengan GroupDocs.Parser, Anda dapat mengekstrak hyperlink dari banyak format file yang umum digunakan. Berikut adalah daftar format yang biasanya didukung."
    items: 
        # format loop 1
        - name: "Menganalisis PDF"
          format: "PDF"
          link: "/parser/java/extract-hyperlink/pdf/"
          description: "(Format Dokumen Portabel)"
          
        # format loop 2
        - name: "Menganalisis DOCX"
          format: "DOCX"
          link: "/parser/java/extract-hyperlink/docx/"
          description: "(Dokumen Word Office 2007+)"
          
        # format loop 3
        - name: "Menganalisis PPTX"
          format: "PPTX"
          link: "/parser/java/extract-hyperlink/pptx/"
          description: "(Format Presentasi Open XML)"
          
        # format loop 4
        - name: "Menganalisis XLSX"
          format: "XLSX"
          link: "/parser/java/extract-hyperlink/xlsx/"
          description: "(Workbook Open XML)"
          
        # format loop 5
        - name: "Menganalisis TXT"
          format: "TXT"
          link: "/parser/java/extract-hyperlink/txt/"
          description: "(File Teks)"
          
        # format loop 6
        - name: "Menganalisis RTF"
          format: "RTF"
          link: "/parser/java/extract-hyperlink/rtf/"
          description: "(Format Teks Kaya)"
          
        # format loop 7
        - name: "Menganalisis XML"
          format: "XML"
          link: "/parser/java/extract-hyperlink/xml/"
          description: "(Bahasa Markup yang Dapat Diperluas)"
          
        # format loop 8
        - name: "Menganalisis EPUB"
          format: "EPUB"
          link: "/parser/java/extract-hyperlink/epub/"
          description: "(File eBook Terbuka)"
         
          

---