


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:40
draft: false
lang: id
format: Rtf
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "Ekstrak tabel dari file RTF dalam aplikasi C#"
head_description: "Gunakan GroupDocs.Parser untuk menemukan dan mengekstrak data tabel terstruktur dari file RTF dalam aplikasi C# tanpa dependensi tambahan."

############################# Header ############################
title: "Ekstrak tabel dari RTF menggunakan C#" 
description: "Identifikasi dengan cepat dan ekstrak struktur tabel dari PDF, Word, Excel, dan format file lainnya menggunakan GroupDocs.Parser dalam proyek .NET Anda."
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
       [GroupDocs.Parser](/parser/net/) adalah API penguraian dokumen yang komprehensif dibangun untuk pengembang .NET. API ini memungkinkan ekstraksi teks, tabel, gambar, hyperlink, dan elemen terstruktur lainnya secara akurat dari format seperti PDF, DOCX, XLSX, PPTX, dan banyak lagi—tanpa perlu perangkat lunak pihak ketiga.

############################# Steps ############################
steps:
    enable: true
    title: "Langkah-langkah untuk ekstrak tabel dari Rtf dalam C#"
    content: |
      Ikuti instruksi ini untuk mengekstrak tabel dari file RTF menggunakan [GroupDocs.Parser](/parser/net/) dalam lingkungan .NET Anda:
      
      1. Inisialisasi instance Parser dan muat dokumen RTF Anda.
      2. Periksa apakah ekstraksi tabel didukung untuk format input.
      3. Ekstrak konten tabel dari file.
      4. Gunakan data tabel terstruktur untuk pelaporan, otomatisasi, atau analitik.
   
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
        // Buka dokumen yang berisi data tabel menggunakan Parser
        using (Parser parser = new Parser("input.rtf")) {

            // Periksa apakah format mendukung pengenalan tabel
            if (!parser.Features.Tables) {
                Console.WriteLine("Tangani dokumen yang tidak mendukung penguraian tabel");
                return;
            }

            // Tentukan bagaimana struktur tabel harus dikenali
            TemplateTableLayout layout = new TemplateTableLayout(
                new double[] { 50, 95, 275, 415, 485, 545 },
                new double[] { 325, 340, 365, 395 });

            // Tentukan parameter ekstraksi untuk data tabel
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            //  Ekstrak tabel dari konten file
            IEnumerable<PageTableArea> tables = parser.GetTables(options);

            //  Jelajahi setiap tabel yang terdeteksi
            foreach (PageTableArea t in tables)
            {
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "Kemampuan ekstraksi data yang kuat"
  description: "Selain penguraian tabel, GroupDocs.Parser dapat mengekstrak konten kaya seperti blok teks, gambar, metadata, dan data terstruktur lainnya untuk memfasilitasi otomatisasi dokumen."
  image: "/img/parser/features_extract-table.webp" # 500x500 px
  image_description: "Pengenalan tabel dan ekstraksi konten"
  features:
    # feature loop
    - title: "Deteksi tabel multi-format yang akurat"
      content: "Ekstrak data tabular dari DOCX, XLSX, PDF, HTML, dan format serupa dengan presisi tinggi."

    # feature loop
    - title: "Analisis struktur tabel dari file"
      content: "Ambil data tabel dari dokumen dan spreadsheet secara efisien tanpa kehilangan format."

    # feature loop
    - title: "Konfigurasi ekstraksi tabel yang fleksibel"
      content: "Sesuaikan deteksi tata letak, penyelarasan kolom, dan opsi header/footer untuk kontrol tepat atas hasil."
      
  code_samples:
    # code sample loop
    - title: "Cara mengekstrak tabel dari spreadsheet Excel"
      content: |
        Contoh kode ini menunjukkan cara membaca dan menjelajahi data tabel dalam file XLSX menggunakan GroupDocs.Parser.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Buka file Excel menggunakan API Parser
        using (Parser parser = new Parser("input.xlsx"))
        {
            // Keluar jika tabel tidak dapat diekstrak dari file
            if (!parser.Features.Tables)
            {
                return;
            }

            // Gunakan aturan tata letak untuk menemukan konten tabular
            TemplateTableLayout layout = new TemplateTableLayout(
                    new double[] { 50, 95, 275, 415, 485, 545 },
                    new double[] { 325, 340, 365, 395 });

            // Atur parameter ekstraksi untuk tabel
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            // Lakukan operasi ekstraksi tabel
            IEnumerable<PageTableArea> tables = parser.GetTables(options);

            // Jelajahi setiap struktur tabel yang terdeteksi
            foreach (PageTableArea t in tables)
            {
                // Iterasi melalui setiap baris dalam tabel
                for (int row = 0; row < t.RowCount; row++)
                {
                    // Jelajahi sel-sel dalam setiap baris
                    for (int column = 0; column < t.ColumnCount; column++)
                    {
                        // Akses sel tabel saat ini
                        PageTableAreaCell cell = t[row, column];
                        if (cell != null)
                        {
                            // Tampilkan konten teks dari setiap sel
                            Console.Write(cell.Text);
                            Console.Write(" | ");
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
    title: "Format yang didukung untuk ekstraksi tabel"
    exclude: "RTF"
    description: "GroupDocs.Parser dapat mengekstrak data tabel dari berbagai jenis dokumen. Berikut adalah format yang paling sering digunakan untuk penguraian tabel terstruktur."
    items: 
        # format loop 1
        - name: "Menganalisis PDF"
          format: "PDF"
          link: "/parser/net/extract-table/pdf/"
          description: "(Format Dokumen Portabel)"
          
        # format loop 2
        - name: "Menganalisis DOCX"
          format: "DOCX"
          link: "/parser/net/extract-table/docx/"
          description: "(Dokumen Word Office 2007+)"
          
        # format loop 3
        - name: "Menganalisis PPTX"
          format: "PPTX"
          link: "/parser/net/extract-table/pptx/"
          description: "(Format Presentasi Open XML)"
          
        # format loop 4
        - name: "Menganalisis XLSX"
          format: "XLSX"
          link: "/parser/net/extract-table/xlsx/"
          description: "(Workbook Open XML)"
          
        # format loop 5
        - name: "Menganalisis TXT"
          format: "TXT"
          link: "/parser/net/extract-table/txt/"
          description: "(File Teks)"
          
        # format loop 6
        - name: "Menganalisis RTF"
          format: "RTF"
          link: "/parser/net/extract-table/rtf/"
          description: "(Format Teks Kaya)"
          
        # format loop 7
        - name: "Menganalisis XML"
          format: "XML"
          link: "/parser/net/extract-table/xml/"
          description: "(Bahasa Markup yang Dapat Diperluas)"
          
        # format loop 8
        - name: "Menganalisis EPUB"
          format: "EPUB"
          link: "/parser/net/extract-table/epub/"
          description: "(File eBook Terbuka)"
         
          

---