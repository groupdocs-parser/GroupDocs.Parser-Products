---
layout: "product"
date: 2022-07-07T12:44:18+03:00
draft: false

product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

head_title: ".NET Parsing API, ekstrak Metadata Gambar Teks dari PDF Word Excel"
head_description: "C# .NET document parsing API untuk mengekstrak teks, gambar, metadata & encoding dari database, PDF, Word, Excel, presentasi, web, email, EPUB & format file zip."

title: ".NET API untuk Mengekstrak Data Dokumen"
description: "Ekstrak gambar, teks mentah atau diformat, dan metadata dari dokumen, spreadsheet, presentasi, email & arsip dari dalam aplikasi .NET."
button:
    enable: true

submenu:
    enable: true
    
    left:
        img_alt: "GroupDocs.Parser for .NET"
        image: "https://www.groupdocs.cloud/templates/groupdocs/images/product-logos/groupdocs-parser-net.png"
        product: "GroupDocs.Parser"
        platform: ".NET"

    middle:
        button:
            - link: "#overview"
              text: "Ringkasan"

            - link: "#features"
              text: "Fitur"

            - link: "#support"
              text: "Mendukung"

            - link: "https://products.groupdocs.app/parser"
              text: "Demo Langsung"

            - link: "https://purchase.groupdocs.com/pricing/parser/net"
              text: "Harga"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/net/"
        link_buy: "https://purchase.groupdocs.com"

overview:
    enable: true
    content: |
      GroupDocs.Parser untuk .NET adalah API ekstraktor teks, metadata, dan gambar untuk aplikasi bisnis yang dikembangkan menggunakan C#, ASP.NET, dan teknologi .NET lainnya. Ini mendukung ekstraksi teks mentah, diformat & terstruktur serta metadata dari file format yang didukung. Melalui GroupDocs.Parser untuk .NET, aplikasi Anda juga dapat melakukan penguraian dokumen yang dilindungi kata sandi untuk format populer, seperti dokumen pemrosesan Word, spreadsheet Excel, presentasi PowerPoint, OneNote, file PDF, dan arsip ZIP.
    tabs:
      enable: true
      
      tab_one:
        description: |
          Berikut ini adalah ikhtisar GroupDocs.Parser untuk .NET:
      
        left:
          enable: true
          icon: "fas fa-tools"
          title: "Fitur"
          content: |
            * Ekstrak Gambar
            * Ekstrak Teks Mentah
            * Ekstrak Teks Terformat
            * Ekstrak Teks Terstruktur
            * Ekstrak Metadata
            * Ekstrak dari File dalam file ZIP
            * Ekstrak dengan Mencari
            * Ekstrak dengan Pemformat Teks
            * Deteksi Standar Pengkodean
            * Deteksi Jenis Media
        
        right:
          enable: true
          icon: "fab fa-html5"
          title: "API"
          content: |
            * Mendapat File Masukan
            * Mengambil Teks Mentah atau Terformat
            * Mengambil Metadata
      
      tab_two:
        description: |
          GroupDocs.Parser untuk .NET mendukung [format file dokumen](https://docs.groupdocs.com/parser/net/supported-document-formats/ berikut):

        left:
          enable: true
          table:
            - title: "Ekstraksi Teks"
              content: |
                * **Teks**: DOC, DOCX, DOT, DOTM, DOTX, DOCM, RTF, ODT, OTT, TXT, MD, WordprocessingML (XML)
                * **Spreadsheet**: XLS, XLSX, CSV, XLSM, XLSB, ODS, SpreadsheetML (XML), XLT, XLTX, XLTM, OTS, XLA,, XLAM, TSV
                * **Presentasi**: PPT, PPTX, PPTM, PPS, PPSX, PPSM, POT, POTX, POTM, ODP, OTP
                * **OneNote**: SATU
                * **Email**: MSG, EML, EMLX, PST, OST, MS EXCHANGE SERVER, POP, IMAP
                * **Penerbitan Elektronik**: EPUB, FB2
                * **Dokumen Portabel**: PDF, Portofolio PDF, PDF Terenkripsi
                * **Berbasis DOM**: XML, HTML, XHTML, MHTML
                * **Kompresi & Kemasan**: ZIP, CHM
                * **Database**: ADO.NET

            - title: "Deteksi Pengkodean"
              content: |
                * **BOM**: UTF32 LE, UTF32 BE, UTF16 LE, UTF16 BE, UTF8, dan UTF7
                * **Konten**: UTF32 LE, UTF32 BE, UTF16 LE, UTF16 BE, UTF8, dan ANSI

        right:
          enable: true
          table:
            - title: "Ekstraksi Metadata"
              content: |
                * **Teks**: DOC, DOCX, DOT, DOTX, DOTM, OTT, ODT
                * **Spreadsheet**: XLS, XLSX, XLT, XLTX, XLTM, XLA, XLAM, OTS, ODS
                * **Presentasi**: PPT, PPTX, POT, POTX, POTM, PPSM, PPTM, OTP, ODP
                * **Email**: MSG, EML, EMLX
                * **Penerbitan Elektronik**: EPUB, FB2
                * **Lainnya**: PDF

            - title: "Ekstraksi Teks & Metadata"
              content: |
                * **Templat**: DOTX, POTX
                * **Template Berkemampuan Makro**: DOTM, POTM, PPSM, PPTM
                * **Template OpenDocument**: OTT

            - title: "Ekstraksi Gambar"
              content: |
                * **Teks**: DOC, DOCX, DOCM, RTF, DOT, DOTM, DOTX, ODT
                * **Spreadsheet**: XLS, XLSX, XLSM, XLSB, ODS, XLT, XLTM, XLTX
                * **Presentasi**: PPT, PPTX, PPTM, ODP, POT, POTM, POTX, PPS, PPSX, PPSM
                * **Dokumen Portabel**: PDF, POT, POTM, POTX
                * **Ebook**: CHM, EPUB, FB2
                * **Markup**: HTML

      tab_three:
        description: |
          GroupDocs.Parser untuk .NET mendukung Sistem Operasi, Kerangka & Manajer Paket berikut:
        
        left:
          enable: true
          table:
            - icon: "fab fa-windows"
              title: "Sistem operasi"
              content: |
                * Desktop Windows
                * Windows Server
                * Windows Azure
                * Linux

            - icon: "fas fa-code"
              title: "Kerangka yang Didukung"
              content: |
                * .NET Framework 2.0 atau lebih tinggi
                * Kerangka Mono 1.2 atau lebih tinggi
                * .NET Standar 2.0
                * .NET Core 2.0

        right:
          enable: true
          table:
            - icon: "fas fa-box"
              title: "Manajer Paket"
              content: |
                * NuGet

            - icon: "fas fa-tools"
              title: "Lingkungan Pengembangan"
              content: |
                * Microsoft Visual Studio
                * Xamarin.Android
                * Xamarin.IOS
                * Xamarin.Mac
                * MonoDevelop

features:
    enable: true
    title: "GroupDocs.Parser untuk .NET Fitur"

    feature:
      - icon: "fas fa-copy"
        content: "Hitung Secara Statistik Kemunculan Kata dalam Satu atau Beberapa File"

      - icon: "fas fa-eye"
        content: "Ekstrak Teks dan Metadata dari Lembar Kerja Excel dan Template Presentasi"

      - icon: "fas fa-bolt"
        content: "Ekstrak Konten Teks dari File atau Aliran tanpa Menginstal Pembaca Dokumen"
      
      - icon: "fas fa-file-powerpoint"
        content: "Dapatkan Teks Terformat dari Dokumen menggunakan Mode Ekstraksi Teks Cepat atau Standar"

      - icon: "fas fa-code"
        content: "Deteksi Jenis Media Dokumen XML yang Dilindungi Kata Sandi & Tarik Teks darinya"

      - icon: "fas fa-cloud"
        content: "Secara terprogram Dapatkan Teks Terformat dari Dalam Email & Lampiran"

      - icon: "fas fa-remove-format"
        content: "Gambarkan Teks dari Satu atau Beberapa Halaman Dokumen OneNote"

      - icon: "fas fa-comment-slash"
        content: "Ekstrak Data dari PDF, MS Word, Excel, dan Dokumen Presentasi"

      - icon: "fas fa-location-arrow"
        content: "Ekstrak Data dari Formulir PDF & Keluarkan Teks dari File PDF Sederhana atau Dokumen Portofolio PDF"

      - icon: "fas fa-border-all"
        content: "Dapatkan Teks Terformat dari Presentasi PowerPoint atau Keluarkan Teks dari Slide Tertentu"

      - icon: "fas fa-wrench"
        content: "Kumpulkan Teks Mentah atau Diformat dari Sel, Baris, dan Kolom dari Excel Spreadsheet"

      - icon: "fas fa-columns"
        content: "Ekstrak Teks Berformat Mentah atau HTML dari Dokumen Word"

      - icon: "fas fa-file-word"
        content: "HTML Formatter Mendukung Pemformatan Paragraf, Hyperlink, Font, Judul, Daftar & Tabel"

      - icon: "fas fa-envelope"
        content: "Tarik Satu Kalimat atau Seluruh Teks dari File EPUB, CHM, Penurunan Harga & FB2"

      - icon: "fas fa-print"
        content: "Kutipan Daftar Isi dari Database, PDF, EPUB, CHM & Dokumen Pengolah Kata"

      - icon: "fas fa-file-archive"
        content: "Tarik Teks dengan Struktur Kontennya Utuh & Kutipan Teks yang Disorot dari Dokumen"

      - icon: "fas fa-lock"
        content: "Dapatkan Area Teks dari Dokumen untuk Analisis & Gambarkan Metadata dari Format Dokumen yang Didukung"

      - icon: "fas fa-file-code"
        content: "Dapatkan Semua atau Gambar yang Dipilih dari Format yang Didukung & Putar Gambar yang Diekstraksi"
      
      - icon: "fas fa-fill-drip"
        content: "Keluarkan Teks dari File dalam Arsip Zip & Kontainer OST & Deteksi jenis file Item Kontainer ZIP"

      - icon: "fas fa-file-excel"
        content: "Dapatkan Data dari Wadah Email (Exchange Web Server, POP3, IMAP)"

      - icon: "fas fa-heading"
        content: "Cari Teks Sederhana, Seluruh Kata & Ekspresi Reguler dalam Dokumen"

      - icon: "fas fa-project-diagram"
        content: "Siapkan Template Dokumen, Ekstrak Data dari Dokumen dan Analisis Bidang & Tabel Data"

      - icon: "fas fa-cube"
        content: "Cari dan Ekstrak Ekspresi yang Disorot dalam Dokumen"

      - icon: "fab fa-uncharted"
        content: "Dapatkan Teks dengan Pemformat Teks Biasa (Sederhana & ASCII) atau dengan Pemformat Penurunan Harga"

      - icon: "fab fa-uncharted"
        content: "Pemformat Penurunan Harga Mendukung Pemformatan Font, Hyperlink, Judul, Daftar & Tabel"

      - icon: "fab fa-uncharted"
        content: "Lakukan Pemformatan Kustom dengan Tepi, Sudut, dan Persimpangan untuk Memformat Teks Biasa"

      - icon: "fab fa-uncharted"
        content: "Pindahkan Tata Letak Tabel & Deteksi Tabel di Area Persegi Panjang dengan Pemisah Kolom"

      - icon: "fab fa-uncharted"
        content: "Ekstrak Teks dari Bentuk, Objek WordArt & Kotak Teks dalam Format File Microsoft Office"

      - icon: "fab fa-uncharted"
        content: "Ekstrak Gambar ke File – Simpan ke Format JPG, PNG, GIF, BMP, PNG atau WEBP"

    more_feature:
      - title: "Mengekstrak Teks dari Dokumen"
        content: |
          Menggunakan GroupDocs.Parser untuk .NET API untuk mengekstrak teks dari dokumen sederhana dan dicapai hanya dengan beberapa baris kode:

          ```cs
          // Buat turunan dari kelas Parser
          using(Parser parser = new Parser("sample.docx"))
          {
            // Ekstrak teks ke dalam pembaca
            using(TextReader reader = parser.GetText())
            {
              // Mencetak teks dari dokumen
              // Jika ekstraksi teks tidak didukung, pembaca adalah null
              Console.WriteLine(reader == null ? "Text extraction isn't supported." : reader.ReadToEnd());
            }
          }
          ```

support:
    enable: true

solutions:
    enable: true
    title: "GroupDocs.Parser menawarkan API tampilan dokumen untuk lingkungan pengembangan populer lainnya"

    solution:
        - img_alt: "GroupDocs.Parser for Java"
          image: "https://www.groupdocs.cloud/templates/groupdocs/images/product-logos/groupdocs-parser-java.png"
          product: "GroupDocs.Parser"
          platform: "Java"
          link: "/parser/java/"

back_to_top:
  enable: true
---
