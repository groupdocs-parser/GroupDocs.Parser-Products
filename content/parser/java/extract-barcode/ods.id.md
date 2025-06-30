


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:17
draft: false
lang: id
format: Ods
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Baca kode batang dari file ODS dalam aplikasi Java"
head_description: "Dengan GroupDocs.Parser, ekstrak data kode batang dari dokumen ODS menggunakan Java tanpa alat eksternal."

############################# Header ############################
title: "Baca kode batang dari ODS menggunakan Java" 
description: "Ekstrak konten kode batang dari file PDF, Word, Excel, dan gambar menggunakan GroupDocs.Parser dalam aplikasi Java Anda."
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
    title: "Ikhtisar API GroupDocs.Parser for Java"
    link: "/parser/java/"
    link_title: "Pelajari lebih lanjut"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) menyediakan solusi komprehensif untuk pemrosesan dokumen dalam Java. Ini memungkinkan pengembang untuk mengekstrak kode batang, teks, gambar, dan informasi terstruktur dari berbagai format file seperti PDF, Word, Excel, PowerPoint, dan lainnya—tanpa memerlukan pustaka pihak ketiga.

############################# Steps ############################
steps:
    enable: true
    title: "Cara membaca kode batang dari Ods di Java"
    content: |
      Dengan [GroupDocs.Parser](/parser/java/), pengembang Java dapat mengekstrak kode batang dari dokumen ODS dalam beberapa langkah:
      
      1. Muatan dokumen ODS menggunakan Parser.
      2. Verifikasi bahwa dokumen mendukung ekstraksi kode batang.
      3. Gunakan API untuk mengambil data kode batang.
      4. Loop melalui hasil kode batang dan terapkan sesuai kebutuhan.
   
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
        // Buka dokumen yang mengandung kode batang menggunakan Parser
        try (Parser parser = new Parser("input.ods"))
        {
            // Periksa dukungan kode batang untuk file tersebut
            if (!parser.getFeatures().isBarcodes())
            {
                System.out.println("Tangani tipe file yang tidak didukung");
                return;
            }

            // Ekstrak dan gunakan data kode batang
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
  title: "Kemampuan pemrosesan lebih lanjut"
  description: "GroupDocs.Parser lebih dari sekadar ekstraksi kode batang—ia juga memungkinkan Anda untuk mengekstrak teks biasa, gambar, dan elemen terstruktur untuk mendukung alur kerja berbasis data."
  image: "/img/parser/features_extract-barcode.webp" # 500x500 px
  image_description: "Fitur ekstraksi kode batang dan data"
  features:
    # feature loop
    - title: "Dukungan format kode batang yang luas"
      content: "Deteksi format kode batang standar termasuk QR Code, Code 39, Data Matrix, EAN, Aztec, dan lainnya."

    # feature loop
    - title: "Baca kode batang dari berbagai sumber"
      content: "Ekstrak informasi kode batang dari dokumen Office, PDF, dan file gambar seperti PNG, JPG, dan BMP."

    # feature loop
    - title: "Pengaturan pembacaan kode batang kustom"
      content: "Sesuaikan ekstraksi kode batang dengan opsi untuk menargetkan area tertentu dan file multi-halaman."
      
  code_samples:
    # code sample loop
    - title: "Contoh: ekstrak kode batang dari PDF dengan opsi"
      content: |
        Contoh ini menunjukkan ekstraksi kode batang dari dokumen PDF menggunakan pengaturan kustom.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Inisialisasi parser dengan dokumen PDF
        try (Parser parser = new Parser("input.pdf"))
        {
            // Pastikan dokumen mendukung pembacaan kode batang
            if (!parser.getFeatures().isBarcodes())
            {
                return;
            }

            // Terapkan penyaringan dengan opsi kode batang
            BarcodeOptions options = new BarcodeOptions(QualityMode.Low, QualityMode.Low, "QR");

            // Ekstrak kode batang menggunakan parser
            Iterable<PageBarcodeArea> barcodes = parser.getBarcodes(options);

            // Tangani setiap hasil kode batang
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
    title: "Format file yang didukung untuk pembacaan kode batang"
    exclude: "ODS"
    description: "GroupDocs.Parser dapat membaca kode batang dari banyak tipe dokumen dan gambar. Berikut adalah beberapa format yang umum didukung."
    items: 
        # format loop 1
        - name: "Menganalisis PDF"
          format: "PDF"
          link: "/parser/java/extract-barcode/pdf/"
          description: "(Format Dokumen Portabel)"
          
        # format loop 2
        - name: "Menganalisis DOCX"
          format: "DOCX"
          link: "/parser/java/extract-barcode/docx/"
          description: "(Dokumen Word Office 2007+)"
          
        # format loop 3
        - name: "Menganalisis PPTX"
          format: "PPTX"
          link: "/parser/java/extract-barcode/pptx/"
          description: "(Format Presentasi Open XML)"
          
        # format loop 4
        - name: "Menganalisis XLSX"
          format: "XLSX"
          link: "/parser/java/extract-barcode/xlsx/"
          description: "(Workbook Open XML)"
          
        # format loop 5
        - name: "Menganalisis ODT"
          format: "ODT"
          link: "/parser/java/extract-barcode/odt/"
          description: "(Dokumen teks OpenDocument)"
          
        # format loop 6
        - name: "Menganalisis ODS"
          format: "ODS"
          link: "/parser/java/extract-barcode/ods/"
          description: "(Spreadsheet OpenDocument)"
          
        # format loop 7
        - name: "Menganalisis ODP"
          format: "ODP"
          link: "/parser/java/extract-barcode/odp/"
          description: "(Presentasi OpenDocument)"
          
        # format loop 8
        - name: "Menganalisis EPUB"
          format: "EPUB"
          link: "/parser/java/extract-barcode/epub/"
          description: "(File eBook Terbuka)"
          
        # format loop 9
        - name: "Menganalisis FB2"
          format: "FB2"
          link: "/parser/java/extract-barcode/fb2/"
          description: "(eBook FictionBook)"
         
          

---