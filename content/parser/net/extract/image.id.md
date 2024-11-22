---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:10
draft: false
otherformats: doc docm docx dot dotm dotx epub html mht mhtml odp ods odt one otp ott pdf

############################# Head ############################
head_title: "Ekstrak Gambar dari Excel, Word, PDF & Dokumen atau Halaman Lain melalui .NET"
head_description: "GroupDocs.Parser .NET API memungkinkan pemrogram perangkat lunak untuk mengekstrak gambar dari berbagai dokumen seperti MS Excel, Word, PowerPoint, PDF & lainnya di dalam Aplikasi .NET mereka."

############################# Header ############################
title: "Ekstrak Gambar dari PDF, DOCX, PPTX, MSG, XLSX Dokumen & Halaman melalui C#.NET API"
description: "GroupDocs.Parser .NET API memungkinkan programmer mengekstrak gambar dari PDF, DOC, DOCX, PPT, PPTX, EML, MSG, XLS, XLSX, CSV , ODT, RTF & EPUB dokumen atau Halaman dokumen."
bg_image: "https://cms.admin.containerize.com/templates/aspose/App_Themes/V3/images/bg/header1.png"
bg_overlay: false
button:
    enable: true
    icon: "fas fa-arrow-down"
    label: "Unduh Uji Coba Gratis"
    link: "https://downloads.groupdocs.com/parser/net"

############################# SubMenu ############################
submenu:
    enable: true

    left:
        img_alt: "GroupDocs.Parser for .NET"
        image: "https://cms.admin.containerize.com/templates/groupdocs/images/product-logos/90x90-noborder/groupdocs-parser-net.png"
        product: "GroupDocs.Parser"
        platform: ".NET"

    middle:
        button:

            # button loop
            - link: "https://apireference.groupdocs.com/parser/net"
              text: "Referensi API"

            # button loop
            - link: "https://github.com/groupdocs-parser"
              text: "Contoh Kode"

            # button loop
            - link: "https://products.groupdocs.app/parser/family"
              text: "Demo Langsung"

            # button loop
            - link: "https://purchase.groupdocs.com/pricing/parser/net"
              text: "Harga"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/net"
        link_buy: "https://purchase.groupdocs.com"

############################# About ############################
about:
    enable: true
    title: "Bagaimana cara Mengekstrak Gambar dari dokumen melalui .NET?"
    content: |
        Gambar dapat digunakan untuk menyampaikan informasi sedemikian rupa sehingga mungkin tidak dapat diungkapkan dengan kata-kata. Gambar membantu kami menarik perhatian pengguna dan menjelaskan konsep sulit dengan mudah. Terkadang saat membaca dokumen, jurnal atau mengambil manfaat dari presentasi kita sering menemukan beberapa gambar yang menarik dan ingin mendownloadnya. GroupDocs.Parser for .NET adalah API andal yang membantu pengguna mengembangkan aplikasi berguna untuk mengekstraksi gambar dari berbagai jenis dokumen dan menyimpannya dalam format PNG, JPEG, WebP, GIF, BMP, dan lainnya. API telah menyertakan dukungan untuk teks serta ekstraksi gambar dari beberapa format file yang paling umum digunakan, seperti PDF, Email, Ebook, Microsoft Office format: Word (DOC, DOCX), { 284} (PPT, PPTX), Excel (XLS, XLSX), format LibreOffice, dan banyak lagi. API juga mendukung penuh penguraian dokumen, mengekstraksi teks biasa dan terstruktur, pencarian teks dengan kata kunci, mengekstrak metadata atau gambar, wadah serta lampiran dan banyak lagi.
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: "Ekstrak gambar dari dokumen di .NET"
    content_left: |
        [GroupDocs.Parser for .NET](/id/parser/net/) memudahkan pengembang C# untuk mengekstrak gambar dari dokumen dengan menerapkan beberapa langkah mudah.
        
        * Membuat instance objek [Parser](https://reference.groupdocs.com/net/parser/groupdocs.parser/parser) untuk dokumen awal;
        * Panggil metode [GetImages](https://reference.groupdocs.com/net/parser/groupdocs.parser/parser/methods/getimages) dan dapatkan kumpulan objek gambar;
        * Periksa apakah pembaca tidak *null* (ekstraksi gambar didukung untuk dokumen);
        * Ulangi koleksi dan dapatkan ukuran, jenis gambar, dan konten gambar.

    title_right: "Pelajari lebih lanjut tentang ekstraksi gambar"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/net/extract-images-from-document/">Cara mengekstrak gambar dari dokumen</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-images-from-document-page/">Cara mengekstrak gambar dari halaman dokumen</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-images-from-document-page-area/">Cara mengekstrak gambar dari area halaman dokumen</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-images-to-files/">Cara mengekstrak gambar ke file</a>

    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="Cara mengekstrak gambar dari dokumen menggunakan kode contoh C#">}}

        ```csharp    
        // Ekstrak gambar dari dokumen menggunakan GroupDocs.Parser API
        // Buat instance kelas Parser
        using (Parser parser = new Parser(filePath)) {
            // Ekstrak gambar
            IEnumerable<PageImageArea> images = parser.GetImages();
            // Periksa apakah ekstraksi gambar didukung
            if (images == null) {
                Console.WriteLine("Ekstraksi gambar tidak didukung");
                return;
            }
            // Ulangi gambar
            foreach (PageImageArea image in images) {
                // Cetak indeks halaman, persegi panjang, dan jenis gambar:
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Type: {2}", image.Page.Index, image.Rectangle, image.FileType));
            }
        }
        ```
     {{< /parser/code-parser >}}

############################# More ############################
more:
    enable: true
    title_left: "Persyaratan sistem"
    content_left: |
        GroupDocs.Parser for .NET API didukung di semua platform dan sistem operasi utama. Sebelum menjalankan kode di bawah ini, harap pastikan bahwa Anda telah menginstal prasyarat berikut di sistem Anda.
        
        * Sistem Operasi: Microsoft Windows, Linux, MacOS
        * Lingkungan Pengembangan: Microsoft Visual Studio, Xamarin, MonoDevelop
        * Kerangka kerja
        * Unduh versi terbaru GroupDocs.Parser for .NET dari [Nuget](https://www.nuget.org/packages/groupdocs.parser)

    title_right: "Mengapa Menggunakan GroupDocs.Parser for .NET"
    content_right: |
        * Dukungan ekstraksi teks biasa dari dokumen yang didukung    
        * Penguraian dokumen melalui templat yang ditentukan pengguna    
        * Sepenuhnya mendukung ekstraksi teks terstruktur    
        * Pencarian teks melalui kata kunci serta ekspresi reguler    
        * Ekstrak teks yang diformat, metadata, gambar, wadah, dan lampiran    
        * Ekstrak daftar isi untuk beberapa format dokumen yang didukung    
        * Mengurai data formulir dari PDF dokumen    
        * Ekstrak hyperlink dari dokumen   

############################# Demos ############################
demos:
    enable: true
    title: "Demo Langsung - Ekstrak gambar dari dokumen Online"
    content: |
       Ekstrak gambar dari dokumen sekarang juga dengan mengunjungi situs web [GroupDocs.Parser Demo Langsung](https://products.groupdocs.app/parser/images/).
       Demo langsung memiliki manfaat berikut.
        
############################# About Formats ############################
about_formats:
    enable: true

############################# More Formats ############################
more_formats:
    enable: true
    title: "Ekstrak Gambar Dari Format Dokumen Lain"
    content: |
        .NET penguraian dokumen & API ekstraksi gambar untuk format file dan gambar. Ekstrak data untuk beberapa format file populer seperti yang dinyatakan di bawah ini.

############################# Back to top ###############################
back_to_top:
    enable: true
---