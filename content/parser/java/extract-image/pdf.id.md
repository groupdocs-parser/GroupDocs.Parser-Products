


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:30
draft: false
lang: id
format: Pdf
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Ekstrak gambar dari file PDF dalam aplikasi Java"
head_description: "Dengan GroupDocs.Parser, Anda dapat mengekstrak gambar dari file PDF dalam Java tanpa kesulitan, tanpa perlu alat pihak ketiga."

############################# Header ############################
title: "Ekstrak gambar dari PDF menggunakan Java" 
description: "Ambil gambar yang tertanam dari file seperti PDF, Word, Excel, dan lainnya menggunakan GroupDocs.Parser dalam lingkungan pengembangan Java Anda."
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
    title: "Apa itu GroupDocs.Parser for Java?"
    link: "/parser/java/"
    link_title: "Pelajari lebih lanjut"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) adalah API pengolahan yang kaya fitur, dirancang untuk pengembang Java. Ini memungkinkan ekstraksi gambar, teks, tautan, dan elemen terstruktur dari berbagai format file termasuk DOCX, XLSX, PDF, PNG, JPG, dan banyak lainnya — semuanya tanpa memerlukan pustaka atau aplikasi eksternal.

############################# Steps ############################
steps:
    enable: true
    title: "Cara mengekstrak gambar dari Pdf dalam Java"
    content: |
      Ikuti langkah-langkah ini untuk mengekstrak gambar dari dokumen PDF menggunakan [GroupDocs.Parser](/parser/java/) dalam aplikasi Java Anda:
      
      1. Buat instance Parser dan muat file PDF.
      2. Ekstrak data gambar dari dokumen yang dimuat.
      3. Gunakan atau ekspor gambar yang diekstrak sesuai kebutuhan.
   
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
        // Inisialisasi parser dan muat dokumen dengan gambar menggunakan Parser
        try (Parser parser = new Parser("input.pdf"))
        {
            // Kumpulkan semua elemen gambar yang tertanam dalam dokumen
            Iterable<PageImageArea> images = parser.getImages();

            // Lewati pemrosesan jika dokumen tidak memiliki gambar
            if (images == null) {
                return;
            }

            // Tangani setiap gambar sesuai kebutuhan
            for (PageImageArea image : images) {
                System.out.println(String.format("Page: %d, R: %s, Type: %s", image.getPage().getIndex(), 
                    image.getRectangle(), image.getFileType()));
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "Kemampuan parsing dokumen lebih lanjut"
  description: "Selain ekstraksi gambar, GroupDocs.Parser juga memungkinkan Anda untuk mengekstrak konten mentah seperti teks, tautan, metadata, dan data terstruktur untuk pemrosesan dan analisis."
  image: "/img/parser/features_extract-image.webp" # 500x500 px
  image_description: "Ekstrak gambar dan konten dari dokumen"
  features:
    # feature loop
    - title: "Bekerja dengan berbagai format"
      content: "Ekstrak gambar dari berbagai jenis dokumen termasuk PDF, DOCX, PPTX, XLSX, dan format gambar seperti PNG, JPEG, dan GIF."

    # feature loop
    - title: "Pertahankan kejernihan dan resolusi gambar"
      content: "Semua gambar yang diekstrak mempertahankan resolusi dan tipe file aslinya untuk memastikan kualitas dan kegunaan yang konsisten."

    # feature loop
    - title: "Opsi konfigurasi yang fleksibel"
      content: "Kustomisasi proses ekstraksi gambar dengan menyaring gambar berdasarkan tipe, ukuran, indeks halaman, atau format file."
      
  code_samples:
    # code sample loop
    - title: "Ekstrak dan simpan gambar dari file PDF"
      content: |
        Contoh ini menunjukkan cara mengekstrak gambar dari dokumen PDF dan menyimpannya secara individual di perangkat Anda.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Gunakan Parser untuk membuka file PDF
        try (Parser parser = new Parser("input.pdf"))
        {
            // Ambil gambar dari konten dokumen
            Iterable<PageImageArea> images = parser.getImages();

            // Tetapkan parameter output seperti format (misalnya, JPEG atau PNG)
            ImageOptions options = new ImageOptions(ImageFormat.Png);

            // Simpan gambar yang diekstrak ke direktori lokal
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
    title: "Jenis file yang didukung untuk ekstraksi gambar"
    exclude: "PDF"
    description: "GroupDocs.Parser mendukung ekstraksi gambar dari berbagai dokumen dan gambar. Jelajahi format yang biasa didukung di bawah ini."
    items: 
        # format loop 1
        - name: "Menganalisis PDF"
          format: "PDF"
          link: "/parser/java/extract-image/pdf/"
          description: "(Format Dokumen Portabel)"
          
        # format loop 2
        - name: "Menganalisis DOCX"
          format: "DOCX"
          link: "/parser/java/extract-image/docx/"
          description: "(Dokumen Word Office 2007+)"
          
        # format loop 3
        - name: "Menganalisis PPTX"
          format: "PPTX"
          link: "/parser/java/extract-image/pptx/"
          description: "(Format Presentasi Open XML)"
          
        # format loop 4
        - name: "Menganalisis XLSX"
          format: "XLSX"
          link: "/parser/java/extract-image/xlsx/"
          description: "(Workbook Open XML)"
          
        # format loop 5
        - name: "Menganalisis ODT"
          format: "ODT"
          link: "/parser/java/extract-image/odt/"
          description: "(Dokumen teks OpenDocument)"
          
        # format loop 6
        - name: "Menganalisis ODS"
          format: "ODS"
          link: "/parser/java/extract-image/ods/"
          description: "(Spreadsheet OpenDocument)"
          
        # format loop 7
        - name: "Menganalisis ODP"
          format: "ODP"
          link: "/parser/java/extract-image/odp/"
          description: "(Presentasi OpenDocument)"
          
        # format loop 8
        - name: "Menganalisis EPUB"
          format: "EPUB"
          link: "/parser/java/extract-image/epub/"
          description: "(File eBook Terbuka)"
          
        # format loop 9
        - name: "Menganalisis FB2"
          format: "FB2"
          link: "/parser/java/extract-image/fb2/"
          description: "(eBook FictionBook)"
         
          

---