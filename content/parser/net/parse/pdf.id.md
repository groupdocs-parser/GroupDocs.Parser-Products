


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:53
draft: false
lang: id
format: Pdf
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "Mengurai data dari file PDF dalam aplikasi C#"
head_description: "Gunakan GroupDocs.Parser untuk mengekstrak teks, gambar, tabel, dan data lainnya dari file PDF dalam C# tanpa bergantung pada alat pihak ketiga."

############################# Header ############################
title: "Mengurai dokumen PDF menggunakan C#" 
description: "Ekstrak teks, metadata, tabel, dan gambar secara efisien dari file PDF, Word, Excel, dan gambar menggunakan GroupDocs.Parser dalam proyek .NET Anda."
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
       [GroupDocs.Parser](/parser/net/) adalah API penguraian dokumen yang kaya fitur, dirancang untuk pengembang .NET. API ini mendukung ekstraksi teks biasa dan terstruktur, metadata, gambar, tabel, dan barcode dari format populer seperti PDF, DOCX, XLSX, PPTX, dan lainnya — semua tanpa ketergantungan perangkat lunak tambahan.

############################# Steps ############################
steps:
    enable: true
    title: "Langkah-langkah untuk mengekstrak data dari Pdf dalam C#"
    content: |
      Ikuti langkah-langkah ini untuk mengurai konten dari dokumen PDF dalam aplikasi .NET Anda menggunakan [GroupDocs.Parser](/parser/net/):
      
      1. Muat dokumen PDF menggunakan instance Parser.
      2. Ekstrak konten yang diinginkan seperti teks, tabel, atau metadata.
      3. Verifikasi bahwa data yang diekstrak valid.
      4. Gunakan output yang telah diurai dalam pemrosesan lanjutan, otomatisasi, atau sistem bisnis Anda.
   
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
        // Muat dokumen Anda ke dalam Parser
        using (Parser parser = new Parser("input.pdf")) {

            // Ekstrak semua konten teks dari file
            using (TextReader reader = parser.GetText()) 
            {
                // Jika teks tidak tersedia, hasilnya akan null
                // Gunakan teks yang diekstrak dalam aplikasi Anda
                Console.WriteLine(reader == null ? 
                    "Ekstraksi teks tidak didukung untuk format ini" : reader.ReadToEnd());
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "Kemampuan penguraian dokumen yang komprehensif"
  description: "GroupDocs.Parser tidak hanya mendukung pembacaan teks — ia mendukung ekstraksi barcode, penguraian gambar, akses metadata, dan pemrosesan data terstruktur untuk otomatisasi dan analisis data yang lebih canggih."
  image: "/img/parser/features_parse.webp" # 500x500 px
  image_description: "Ekstraksi konten dokumen dan kemampuan penguraian"
  features:
    # feature loop
    - title: "Dukungan untuk berbagai jenis konten file"
      content: "Ekstrak data termasuk teks, gambar, tabel, dan bidang dari format dokumen seperti PDF, Word, Excel, HTML, dan lainnya."

    # feature loop
    - title: "Bekerja dengan file hasil pemindaian dan digital"
      content: "Mengurai data dari dokumen hasil pemindaian dan file digital, dengan dukungan untuk OCR dan ekstraksi yang memperhitungkan tata letak."

    # feature loop
    - title: "Parameter ekstraksi yang dapat dikonfigurasi"
      content: "Sesuaikan logika penguraian dengan opsi fleksibel seperti pemilihan rentang halaman, penargetan wilayah, dan template deteksi bidang."
      
  code_samples:
    # code sample loop
    - title: "Cara mengurai PDF menggunakan template"
      content: |
        Contoh ini menunjukkan cara mengekstrak data terstruktur dari PDF menggunakan template penguraian yang telah ditentukan dengan GroupDocs.Parser.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Muat file PDF dengan kelas Parser
        using (Parser parser = new Parser("input.pdf"))
        {
            // Urutkan dokumen berdasarkan template
            DocumentData data = parser.ParseByTemplate(GetTemplate());

            // Periksa apakah ekstraksi formulir didukung
            if (data == null)
            {
                return;
            }

            // Proses bidang yang diperoleh
            for (int i = 0; i < data.Count; i++)
            {
                Console.Write(data[i].Name + ": ");
                PageTextArea area = data[i].PageArea as PageTextArea;
                Console.WriteLine(area == null ? "Not a template field" : area.Text);
            }
        }

        private static Template GetTemplate()
        {
            // Buat parameter deteksi untuk tabel 'Detail'
            TemplateTableParameters detailsTableParameters = 
                new TemplateTableParameters(new Rectangle(new Point(35, 320), new Size(530, 55)), null);

            TemplateItem[] templateItems = new TemplateItem[]
            {
                new TemplateTable(detailsTableParameters, "details", null)
            };

            Template template = new Template(templateItems);
            return template;
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
    title: "Format yang didukung untuk ekstraksi data"
    exclude: "PDF"
    description: "GroupDocs.Parser memungkinkan pemrosesan data dari berbagai format dokumen dan gambar. Jelajahi jenis file yang didukung yang umum digunakan dalam alur kerja ekstraksi data."
    items: 
        # format loop 1
        - name: "Menganalisis PDF"
          format: "PDF"
          link: "/parser/net/parse/pdf/"
          description: "(Format Dokumen Portabel)"
          
        # format loop 2
        - name: "Menganalisis DOCX"
          format: "DOCX"
          link: "/parser/net/parse/docx/"
          description: "(Dokumen Word Office 2007+)"
          
        # format loop 3
        - name: "Menganalisis PPTX"
          format: "PPTX"
          link: "/parser/net/parse/pptx/"
          description: "(Format Presentasi Open XML)"
          
        # format loop 4
        - name: "Menganalisis XLSX"
          format: "XLSX"
          link: "/parser/net/parse/xlsx/"
          description: "(Workbook Open XML)"
          
        # format loop 5
        - name: "Menganalisis TXT"
          format: "TXT"
          link: "/parser/net/parse/txt/"
          description: "(File Teks)"
          
        # format loop 6
        - name: "Menganalisis RTF"
          format: "RTF"
          link: "/parser/net/parse/rtf/"
          description: "(Format Teks Kaya)"
          
        # format loop 7
        - name: "Menganalisis XML"
          format: "XML"
          link: "/parser/net/parse/xml/"
          description: "(Bahasa Markup yang Dapat Diperluas)"
          
        # format loop 8
        - name: "Menganalisis EPUB"
          format: "EPUB"
          link: "/parser/net/parse/epub/"
          description: "(File eBook Terbuka)"
         
          

---