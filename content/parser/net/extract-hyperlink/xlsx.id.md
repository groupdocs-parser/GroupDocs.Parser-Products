


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:26
draft: false
lang: id
format: Xlsx
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "Ekstrak hyperlink dari file XLSX dalam aplikasi C#"
head_description: "Gunakan GroupDocs.Parser untuk mendeteksi dan mengekstrak hyperlink dari file XLSX dalam C# tanpa alat atau perangkat lunak tambahan."

############################# Header ############################
title: "Ekstrak hyperlink dari XLSX menggunakan C#" 
description: "Deteksi dan ekstrak URL serta hyperlink dari PDF, Word, Excel, dan berbagai jenis dokumen lain menggunakan GroupDocs.Parser dalam aplikasi .NET Anda."
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
       [GroupDocs.Parser](/parser/net/) adalah API parsing dokumen yang serbaguna untuk pengembang .NET. Ini mendukung ekstraksi hyperlink, teks, gambar, dan konten terstruktur dari berbagai format file seperti PDF, Word, Excel, HTML, dan lainnya—tanpa bergantung pada perangkat lunak eksternal.

############################# Steps ############################
steps:
    enable: true
    title: "Langkah-langkah untuk mengekstrak hyperlink dari Xlsx dalam C#"
    content: |
      [GroupDocs.Parser](/parser/net/) memungkinkan pengembang .NET untuk mengekstrak hyperlink dari file XLSX dengan mengikuti langkah-langkah sederhana ini:
      
      1. Muat file XLSX menggunakan instance Parser.
      2. Periksa apakah dokumen mendukung ekstraksi hyperlink.
      3. Ambil daftar hyperlink dari dokumen.
      4. Loop melalui hasil dan bekerja dengan URL yang diekstrak.
   
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
        // Muat dokumen yang berisi hyperlink menggunakan kelas Parser
        using (Parser parser = new Parser("input.xlsx")) {

            // Verifikasi bahwa file mendukung ekstraksi hyperlink
            if (!parser.Features.Hyperlinks)
            {
                Console.WriteLine("Ekstraksi hyperlink tidak tersedia untuk file ini");
                return;
            }

            // Ambil dan proses hyperlink yang diekstrak
            IEnumerable<PageHyperlinkArea> hyperlinks = parser.GetHyperlinks();

            foreach (PageHyperlinkArea h in hyperlinks)
            {
                Console.WriteLine(h.Text);
                Console.WriteLine(h.Url);
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "Kemampuan parsing dokumen yang canggih"
  description: "Selain ekstraksi hyperlink, GroupDocs.Parser memungkinkan Anda untuk mengekstrak teks, metadata, gambar, dan data terstruktur—mendukung alur kerja pemrosesan data yang kuat."
  image: "/img/parser/features_extract-hyperlink.webp" # 500x500 px
  image_description: "Deteksi hyperlink dan parsing dokumen"
  features:
    # feature loop
    - title: "Deteksi hyperlink dari dokumen"
      content: "Ekstrak URL dan anotasi tautan dari dokumen seperti PDF, file Word, spreadsheet, dan lainnya dengan cepat."

    # feature loop
    - title: "Dukungan untuk tautan web dan embedded"
      content: "Deteksi dan ekstrak baik URL web standar maupun tautan dokumen ter嵌入 di berbagai format."

    # feature loop
    - title: "Opsi parsing yang fleksibel"
      content: "Sesuaikan pengaturan ekstraksi untuk memindai bagian atau halaman tertentu untuk meningkatkan kinerja dan akurasi."
      
  code_samples:
    # code sample loop
    - title: "Cara mengekstrak hyperlink dari PDF menggunakan opsi tautan"
      content: |
        Contoh kode ini menunjukkan cara mengekstrak semua hyperlink dari file PDF menggunakan opsi kustom.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Inisialisasi Parser dengan dokumen PDF
        using (Parser parser = new Parser("input.docx"))
        {
            // Periksa apakah ekstraksi hyperlink didukung
            if (!parser.Features.Hyperlinks)
            {
                return;
            }

            // Tetapkan opsi ekstraksi tautan untuk mempersempit hasil
            PageAreaOptions options = new PageAreaOptions(new Rectangle(new Point(380, 90), new Size(150, 50)));

            // Ekstrak data hyperlink dari dokumen
            IEnumerable<PageHyperlinkArea> hyperlinks = parser.GetHyperlinks(options);

            // Tangani daftar tautan yang diekstrak
            foreach (PageHyperlinkArea h in hyperlinks)
            {
                Console.WriteLine(h.Text);
                Console.WriteLine(h.Url);
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
    title: "Format yang didukung untuk ekstraksi hyperlink"
    exclude: "XLSX"
    description: "GroupDocs.Parser dapat mengekstrak hyperlink dari berbagai jenis dokumen. Lihat di bawah untuk format yang umum didukung."
    items: 
        # format loop 1
        - name: "Menganalisis PDF"
          format: "PDF"
          link: "/parser/net/extract-hyperlink/pdf/"
          description: "(Format Dokumen Portabel)"
          
        # format loop 2
        - name: "Menganalisis DOCX"
          format: "DOCX"
          link: "/parser/net/extract-hyperlink/docx/"
          description: "(Dokumen Word Office 2007+)"
          
        # format loop 3
        - name: "Menganalisis PPTX"
          format: "PPTX"
          link: "/parser/net/extract-hyperlink/pptx/"
          description: "(Format Presentasi Open XML)"
          
        # format loop 4
        - name: "Menganalisis XLSX"
          format: "XLSX"
          link: "/parser/net/extract-hyperlink/xlsx/"
          description: "(Workbook Open XML)"
          
        # format loop 5
        - name: "Menganalisis TXT"
          format: "TXT"
          link: "/parser/net/extract-hyperlink/txt/"
          description: "(File Teks)"
          
        # format loop 6
        - name: "Menganalisis RTF"
          format: "RTF"
          link: "/parser/net/extract-hyperlink/rtf/"
          description: "(Format Teks Kaya)"
          
        # format loop 7
        - name: "Menganalisis XML"
          format: "XML"
          link: "/parser/net/extract-hyperlink/xml/"
          description: "(Bahasa Markup yang Dapat Diperluas)"
          
        # format loop 8
        - name: "Menganalisis EPUB"
          format: "EPUB"
          link: "/parser/net/extract-hyperlink/epub/"
          description: "(File eBook Terbuka)"
         
          

---