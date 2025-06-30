


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:33
draft: false
lang: id
format: Ods
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "Ekstrak gambar dari file ODS dalam aplikasi C#"
head_description: "Gunakan GroupDocs.Parser untuk mendeteksi dan mengekstrak gambar dari file ODS dalam C# tanpa alat tambahan."

############################# Header ############################
title: "Ekstrak gambar dari ODS menggunakan C#" 
description: "Temukan dan ekstrak gambar ter嵌 dalam PDF, dokumen Word, lembar Excel, dan jenis file lainnya menggunakan GroupDocs.Parser dalam aplikasi .NET Anda."
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
       [GroupDocs.Parser](/parser/net/) adalah pustaka parsing dokumen yang kuat untuk pengembang .NET. Ini memungkinkan Anda untuk mengekstrak gambar, teks, superlink, dan data terstruktur dari format file populer seperti PDF, DOCX, XLSX, PPTX, dan lainnya — semua tanpa memerlukan aplikasi pihak ketiga.

############################# Steps ############################
steps:
    enable: true
    title: "Langkah-langkah untuk mengekstrak gambar dari Ods di C#"
    content: |
      Dengan [GroupDocs.Parser](/parser/net/), Anda dapat mengekstrak gambar dari dokumen ODS dalam proyek .NET Anda hanya dalam beberapa langkah:
      
      1. Inisialisasi Parser dengan file ODS.
      2. Ambil elemen gambar dari dokumen.
      3. Gunakan gambar yang diekstrak sesuai kebutuhan dalam alur kerja Anda.
   
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
        // Buka dokumen yang berisi gambar menggunakan Parser
        using (Parser parser = new Parser("input.ods")) {

            // Ekstrak semua gambar yang ter嵌 dari file
            IEnumerable<PageImageArea> images = parser.GetImages();

            // Tangani kasus di mana tidak ada gambar yang ditemukan
            if (images == null)
            {
                return;
            }

            // Olah atau simpan gambar yang diperoleh
            foreach (PageImageArea image in images)
            {
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Type: {2}", 
                    image.Page.Index, image.Rectangle, image.FileType));
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "Ekstraksi konten dokumen yang komprehensif"
  description: "GroupDocs.Parser menawarkan lebih dari sekadar ekstraksi gambar — Anda juga dapat mengekstrak teks mentah, superlink, metadata, dan konten terstruktur untuk skenario otomatisasi lanjutan."
  image: "/img/parser/features_extract-image.webp" # 500x500 px
  image_description: "Alur kerja ekstraksi gambar dan parsing dokumen"
  features:
    # feature loop
    - title: "Ekstrak gambar dari berbagai format"
      content: "Ambil gambar ter嵌 dari berbagai format file, termasuk DOCX, PDF, PPTX, XLSX, dan file gambar seperti PNG, JPG, dan TIFF."

    # feature loop
    - title: "Pertahankan kualitas gambar asli"
      content: "Gambar diekstraksi dengan fidelity tinggi, mempertahankan resolusi asli, format, dan profil warna."

    # feature loop
    - title: "Opsi ekstraksi lanjutan"
      content: "Sesuaikan ekstraksi gambar dengan penyaringan berdasarkan halaman, format, atau resolusi, dan dukungan untuk dokumen multi-halaman."
      
  code_samples:
    # code sample loop
    - title: "Cara mengekstrak dan menyimpan gambar dari dokumen PDF"
      content: |
        Contoh ini menunjukkan cara mengekstrak semua aset gambar dari file PDF dan menyimpannya ke sistem file lokal.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Muat PDF menggunakan kelas Parser
        using (Parser parser = new Parser("input.pdf"))
        {
            // Ekstrak gambar ter嵌 dari file
            IEnumerable<PageImageArea> images = parser.GetImages();

            // Atur format output dan opsi gambar (misalnya, PNG)
            ImageOptions options = new ImageOptions(ImageFormat.Png);

            // Tulis gambar yang diekstrak ke disk
            int imageNumber = 0;
            foreach (PageImageArea image in images)
            {
                image.Save(imageNumber.ToString() + ".png", options);
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
    title: "Format yang didukung untuk ekstra gambar"
    exclude: "ODS"
    description: "GroupDocs.Parser memungkinkan ekstraksi gambar yang akurat dari berbagai format dokumen dan gambar. Lihat daftar di bawah ini untuk jenis yang umum didukung."
    items: 
        # format loop 1
        - name: "Menganalisis PDF"
          format: "PDF"
          link: "/parser/net/extract-image/pdf/"
          description: "(Format Dokumen Portabel)"
          
        # format loop 2
        - name: "Menganalisis DOCX"
          format: "DOCX"
          link: "/parser/net/extract-image/docx/"
          description: "(Dokumen Word Office 2007+)"
          
        # format loop 3
        - name: "Menganalisis PPTX"
          format: "PPTX"
          link: "/parser/net/extract-image/pptx/"
          description: "(Format Presentasi Open XML)"
          
        # format loop 4
        - name: "Menganalisis XLSX"
          format: "XLSX"
          link: "/parser/net/extract-image/xlsx/"
          description: "(Workbook Open XML)"
          
        # format loop 5
        - name: "Menganalisis ODT"
          format: "ODT"
          link: "/parser/net/extract-image/odt/"
          description: "(Dokumen teks OpenDocument)"
          
        # format loop 6
        - name: "Menganalisis ODS"
          format: "ODS"
          link: "/parser/net/extract-image/ods/"
          description: "(Spreadsheet OpenDocument)"
          
        # format loop 7
        - name: "Menganalisis ODP"
          format: "ODP"
          link: "/parser/net/extract-image/odp/"
          description: "(Presentasi OpenDocument)"
          
        # format loop 8
        - name: "Menganalisis EPUB"
          format: "EPUB"
          link: "/parser/net/extract-image/epub/"
          description: "(File eBook Terbuka)"
          
        # format loop 9
        - name: "Menganalisis FB2"
          format: "FB2"
          link: "/parser/net/extract-image/fb2/"
          description: "(eBook FictionBook)"
         
          

---