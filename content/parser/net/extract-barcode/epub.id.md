


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:20
draft: false
lang: id
format: Epub
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "Ekstrak kode batang dari file EPUB dalam aplikasi C#"
head_description: "Gunakan GroupDocs.Parser untuk mendeteksi dan mengekstrak data kode batang dari file EPUB dalam C# tanpa perangkat lunak tambahan."

############################# Header ############################
title: "Ekstrak kode batang dari EPUB menggunakan C#" 
description: "Deteksi dan ekstrak informasi kode batang dari file PDF, Word, Excel, dan gambar menggunakan GroupDocs.Parser dalam aplikasi .NET Anda."
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Unduh Uji Coba Gratis"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "Tentang API GroupDocs.Parser for .NET"
    link: "/parser/net/"
    link_title: "Pelajari lebih lanjut"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/) adalah API pemrosesan dokumen yang kuat untuk pengembang .NET. API ini memungkinkan ekstraksi teks, gambar, konten terstruktur, dan kode batang dari berbagai format file termasuk PDF, Word, Excel, PowerPoint, dan lainnya — semua tanpa bergantung pada alat eksternal.

############################# Steps ############################
steps:
    enable: true
    title: "Langkah untuk mengekstrak kode batang dari Epub dalam C#"
    content: |
      [GroupDocs.Parser](/parser/net/) memungkinkan Anda mengekstrak data kode batang dari file EPUB dalam aplikasi .NET dengan mengikuti langkah-langkah sederhana berikut:
      
      1. Muat file EPUB menggunakan instance Parser.
      2. Verifikasi bahwa dokumen mendukung ekstraksi kode batang.
      3. Ambil daftar kode batang dari dokumen.
      4. Iterasi melalui hasil dan gunakan nilai kode batang yang diekstrak.
   
    code:
      platform: "net"
      copy_title: "Salin"
      install:
        command: |
        command: "dotnet add package GroupDocs.Parser"
        copy_tip: "klik untuk menyalin"
        copy_done: "disalin"
      links:
        #  loop
        - title: "Lebih banyak contoh"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
        #  loop
        - title: "Dokumentasi"
          link: "https://docs.groupdocs.com/parser/net/"
          
      content: |
        ```csharp {style=abap}
        // Muat dokumen yang berisi kode batang menggunakan kelas Parser
        using (Parser parser = new Parser("input.epub")) {

            // Verifikasi bahwa file mendukung ekstraksi kode batang
            if (!parser.Features.Barcodes) {
                Console.WriteLine("Ekstraksi kode batang tidak didukung");
                return;
            }

            // Ambil dan proses kode batang yang diekstrak
            IEnumerable<PageBarcodeArea> barcodes = parser.GetBarcodes();

            foreach (PageBarcodeArea barcode in barcodes) {
                Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                Console.WriteLine("Value: " + barcode.Value);
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "Fitur pemrosesan dokumen lanjutan"
  description: "Selain ekstraksi kode batang, GroupDocs.Parser memungkinkan Anda mengekstrak teks biasa, gambar, dan data terstruktur untuk mendukung otomatisasi dan alur kerja pemrosesan data yang lebih canggih."
  image: "/img/parser/features_extract-barcode.webp" # 500x500 px
  image_description: "Pengajuan kode batang dan pemrosesan dokumen"
  features:
    # feature loop
    - title: "Dukungan untuk berbagai format kode batang"
      content: "Mengenali jenis kode batang umum termasuk QR Code, Code 128, Data Matrix, EAN, Aztec, dan lainnya."

    # feature loop
    - title: "Ekstrak kode batang dari dokumen dan gambar"
      content: "Baca kode batang dari dokumen PDF, Word, Excel, dan format gambar seperti JPEG, PNG, dan BMP."

    # feature loop
    - title: "Pengaturan ekstraksi yang dapat disesuaikan"
      content: "Konfigurasi opsi deteksi seperti wilayah pemindaian dan pemrosesan dokumen multi-halaman."
      
  code_samples:
    # code sample loop
    - title: "Cara mengekstrak kode batang dari PDF menggunakan opsi kode batang"
      content: |
        Contoh ini menunjukkan cara mengekstrak kode batang dari file PDF menggunakan opsi ekstraksi kode batang tertentu.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Muat file PDF dengan kelas Parser
        using (Parser parser = new Parser("input.pdf"))
        {
            // Pastikan ekstraksi kode batang didukung
            if (!parser.Features.Barcodes)
            {
                return;
            }

            // Gunakan opsi kode batang untuk memfilter hasil
            BarcodeOptions options = new BarcodeOptions(QualityMode.Low, QualityMode.Low, "QR");

            // Ambil data kode batang dari dokumen
            IEnumerable<PageBarcodeArea> barcodes = parser.GetBarcodes(options);

            // Proses daftar kode batang yang diekstrak
            foreach (PageBarcodeArea barcode in barcodes)
            {
                Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                Console.WriteLine("Value: " + barcode.Value);
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
    - title: "Unduh Nuget"
      link: "https://releases.groupdocs.com/parser/net/"
      color: "red"
        #  loop
    - title: "Lisensi"
      link: "https://purchase.groupdocs.com/pricing/parser/net/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "Format yang Didukung untuk ekstraksi kode batang"
    exclude: "EPUB"
    description: "GroupDocs.Parser mendukung deteksi kode batang dalam berbagai format dokumen dan gambar. Lihat di bawah untuk jenis file yang umum didukung."
    items: 
        # format loop 1
        - name: "Menganalisis PDF"
          format: "PDF"
          link: "/parser/net/extract-barcode/pdf/"
          description: "(Format Dokumen Portabel)"
          
        # format loop 2
        - name: "Menganalisis DOCX"
          format: "DOCX"
          link: "/parser/net/extract-barcode/docx/"
          description: "(Dokumen Word Office 2007+)"
          
        # format loop 3
        - name: "Menganalisis PPTX"
          format: "PPTX"
          link: "/parser/net/extract-barcode/pptx/"
          description: "(Format Presentasi Open XML)"
          
        # format loop 4
        - name: "Menganalisis XLSX"
          format: "XLSX"
          link: "/parser/net/extract-barcode/xlsx/"
          description: "(Workbook Open XML)"
          
        # format loop 5
        - name: "Menganalisis ODT"
          format: "ODT"
          link: "/parser/net/extract-barcode/odt/"
          description: "(Dokumen teks OpenDocument)"
          
        # format loop 6
        - name: "Menganalisis ODS"
          format: "ODS"
          link: "/parser/net/extract-barcode/ods/"
          description: "(Spreadsheet OpenDocument)"
          
        # format loop 7
        - name: "Menganalisis ODP"
          format: "ODP"
          link: "/parser/net/extract-barcode/odp/"
          description: "(Presentasi OpenDocument)"
          
        # format loop 8
        - name: "Menganalisis EPUB"
          format: "EPUB"
          link: "/parser/net/extract-barcode/epub/"
          description: "(File eBook Terbuka)"
          
        # format loop 9
        - name: "Menganalisis FB2"
          format: "FB2"
          link: "/parser/net/extract-barcode/fb2/"
          description: "(eBook FictionBook)"
         
          

---