---
############################# Static ############################
layout: "landing"
date: 2025-06-30T10:26:00
draft: false

lang: th
product: "Parser"
product_tag: "parser"
platform: "Net"
platform_tag: "net"

############################# Drop-down ############################
supported_platforms:
  items:
    # supported_platforms loop
    - title: ".NET"
      tag: "net"
    # supported_platforms loop
    - title: "Java"
      tag: "java"

############################# Head ############################
head_title: "GroupDocs.Parser for .NET แอพพลิเคชันการแยกเอกสาร"
head_description: "รับโซลูชันการแยกเอกสารแบบครบวงจรสำหรับแอพพลิเคชัน .NET แยกข้อมูลจากรูปแบบเอกสารออนไลน์ด้วยคุณสมบัติการลากและวางที่ง่ายดาย"

############################# Header ############################
title: "วิเคราะห์เอกสารผ่าน .NET API"
description: "แยกข้อมูลจากเอกสารและภาพในทุกแพลตฟอร์มโดยใช้ API ที่ยืดหยุ่นและโซลูชันที่ใช้แอพสำหรับโปรแกรมเมอร์และผู้ใช้ทั่วไป"
words:
  for: "สำหรับ"

actions:
  main: "ดาวน์โหลด Nuget"
  main_link: "https://www.nuget.org/packages/GroupDocs.Parser"
  alt: "การอนุญาต"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/net/"
  title: "พร้อมเริ่มต้นแล้วหรือยัง?"
  description: "ลองใช้ฟีเจอร์ของ GroupDocs.Parser ฟรีหรือขอใบอนุญาต"

release:
  title: "เวอร์ชัน {0} วางจำหน่ายแล้ว"
  notes: "ดูว่าอะไรใหม่"
  downloads: "ดาวน์โหลด"

code:
  title: "วิเคราะห์เนื้อหาเอกสารอย่างรวดเร็ว"
  more: "ตัวอย่างเพิ่มเติม"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
  install: "dotnet add package GroupDocs.Parser"
  content: |
    ```csharp {style=abap}   
    // ส่งไฟล์ต้นทางไปยังอินสแตนซ์ของ Parser
    using (var parser = new Parser("source.pdf"))
    {
        // ส่งข้อความเอกสารไปยัง TextReader
        using (var textReader = parser.GetText())
        {
            // ประมวลผลข้อความเอกสาร
            Console.WriteLine(textReader?.ReadToEnd());
        }
    }  
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser ภาพรวม"
  description: "API สำหรับการดำเนินการแยกเอกสารในแอพพลิเคชัน .NET"
  features:
    # feature loop
    - title: "แยกข้อมูลจากเอกสาร"
      content: "GroupDocs.Parser for .NET API ช่วยให้คุณสามารถดึงข้อความ เมตาดาตา และรูปภาพจากรูปแบบไฟล์ที่หลากหลาย เช่น เอกสาร Office, อีเมล, ไฟล์แนบ และเอกสารเก็บถาวร เครื่องมือที่ทรงพลังนี้ช่วยให้คุณเข้าถึงและประมวลผลข้อมูลที่มีค่าในไฟล์เหล่านี้ได้อย่างมีประสิทธิภาพสำหรับแอพพลิเคชันต่างๆ เช่น การวิเคราะห์ข้อมูล, การจัดทำดัชนีเสิร์ชเอนจิน หรือระบบการจัดการเนื้อหา"

    # feature loop
    - title: "วิเคราะห์เอกสาร"
      content: "แยกองค์ประกอบต่างๆ เช่น ลิงก์, ตาราง, QR โค้ด, บาร์โค้ด และข้อมูลจากแบบฟอร์ม PDF นอกจากนี้ยังสามารถวิเคราะห์ข้อมูลเฉพาะจากเอกสารโดยใช้แม่แบบที่กำหนดเอง"

    # feature loop
    - title: "ปรับแต่งผลลัพธ์"
      content: ".NET API ช่วยให้คุณสามารถดึงข้อมูลในรูปแบบที่หลากหลาย เช่น แบบดิบ, แบบมีโครงสร้าง, HTML หรือ Markdown นอกจากนี้ API ยังมีฟังก์ชันการค้นหาที่ช่วยในการค้นหาคำหรือวลีเฉพาะภายในข้อความของเอกสาร"

############################# Platforms ############################
platforms:
  enable: true
  title: "อิสระต่อแพลตฟอร์ม"
  description: "GroupDocs.Parser for .NET รองรับระบบปฏิบัติการ เฟรมเวิร์ก และแพ็คเกจจัดการดังต่อไปนี้"
  items:
    # platform loop
    - title: "Amazon"
      image: "amazon"
    # platform loop
    - title: "Docker"
      image: "docker"
    # platform loop
    - title: "Azure"
      image: "azure"
    # platform loop
    - title: "VS Code"
      image: "vs_code"
    # platform loop
    - title: "ReSharper"
      image: "resharper"
    # platform loop
    - title: "macOS"
      image: "finder"
    # platform loop
    - title: "Linux"
      image: "linux"
    # platform loop
    - title: "NuGet"
      image: "nuget"

############################# File formats ############################
formats:
  enable: true
  title: "รูปแบบไฟล์ที่รองรับ"
  description: |
    GroupDocs.Parser for .NET รองรับการดำเนินการกับ [รูปแบบไฟล์](https://docs.groupdocs.com/parser/net/supported-document-formats/) ต่อไปนี้
  groups:
    # group loop
    - color: "green"
      content: |
        ### รูปแบบ Microsoft Office
        * **Word:** DOCX, DOC, DOCM, DOT, DOTX, DOTM, RTF
        * **Excel:** XLSX, XLS, XLSM, XLSB, XLTM, XLT, XLTM, XLTX, XLAM, SXC, SpreadsheetML
        * **PowerPoint:** PPT, PPTX, PPS, PPSX, PPSM, POT, POTM, POTX, PPTM
    # group loop
    - color: "blue"
      content: |
        ### รูปภาพ & รูปแบบอื่นๆ
        * **พกพาได้:** PDF 
        * **รูปภาพ:** JPG, BMP, PNG, TIFF, GIF
        * **รูปแบบสำนักงานอื่นๆ:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### รูปแบบอื่นๆ
        * **เว็บ:** HTML, MHTML 
        * **เอกสารเก็บถาวร:** ZIP, TAR, 7Z 
        * **สมุดอิเล็กทรอนิกส์:** CHM, EPUB, FB2, MOBI 
        
        

############################# Features ############################
features:
  enable: true
  title: "GroupDocs.Parser for .NET คุณสมบัติ"
  description: "แยกข้อมูลจาก PDFs, เอกสาร Office และภาพได้อย่างรวดเร็วและแม่นยำ"

  items:
    # feature loop
    - icon: "text"
      title: "แยกข้อความ"
      content: "ดึงข้อมูลข้อความจากรูปแบบไฟล์ต่างๆ เช่น เอกสาร Office, ไฟล์ PDF และภาพเพื่อความอ่านง่ายและการวิเคราะห์"

    # feature loop
    - icon: "image"
      title: "แยกรูปภาพ"
      content: "กู้คืนเนื้อหาภาพจากแหล่งที่หลากหลาย เช่น เอกสาร Office, ไฟล์ PDF เพื่อความสะดวกในการเข้าถึงและใช้งาน"

    # feature loop
    - icon: "qr"
      title: "สแกน QR โค้ด"
      content: "ตรวจจับและถอดรหัส QR โค้ดที่มีอยู่ในเอกสาร Office, ไฟล์ PDF หรือเนื้อหาภาพเพื่อการเรียกคืนข้อมูลที่มีประสิทธิภาพ"

    # feature loop
    - icon: "email"
      title: "แยกข้อมูลจากไฟล์แนบและเอกสารเก็บถาวร"
      content: "รวบรวมข้อมูลที่มีค่าจากข้อความอีเมล ไฟล์แนบ และแหล่งข้อมูลที่ถูกบีบอัดเพื่อการวิเคราะห์และการใช้งานที่มีประสิทธิภาพ"

    # feature loop
    - icon: "table"
      title: "แยกตาราง"
      content: "ระบุและแยกข้อมูลในตารางจากเอกสาร PDF สำหรับการวิเคราะห์และการใช้งานที่เป็นระเบียบ"

    # feature loop
    - icon: "hyperlink"
      title: "แยกลิงก์"
      content: "ค้นหาและแยกลิงก์และที่อยู่อีเมลภายในเอกสาร Office หรือไฟล์ PDF เพื่อเข้าถึงอย่างมีประสิทธิภาพ"

    # feature loop
    - icon: "pdf"
      title: "วิเคราะห์แบบฟอร์ม PDF"
      content: "แบบฟอร์ม PDF เป็นเอกสารดิจิตอลที่มีฟิลด์กรอกข้อมูลเพื่อให้ผู้ใช้สามารถกรอกข้อมูลได้ทางอิเล็กทรอนิกส์ API ของ .NET สามารถใช้ในการดึงข้อมูลจากแบบฟอร์มเหล่านี้เพื่อการประมวลผลที่มีประสิทธิภาพ"

    # feature loop
    - icon: "template"
      title: "วิเคราะห์ข้อมูลตามแบบฟอร์ม"
      content: "สร้างแม่แบบกำหนดเองและใช้ร่วมกับ API .NET เพื่อดึงข้อมูลเฉพาะจากไฟล์ PDF ซึ่งทำให้การแยกข้อมูลเป็นเรื่องง่าย"

    # feature loop
    - icon: "search"
      title: "ค้นหาข้อความในเอกสาร"
      content: "ค้นหาคำหรือรูปแบบเฉพาะในเอกสารได้อย่างรวดเร็ว"


############################# Code samples ############################
code_samples:
  enable: true
  title: "ตัวอย่างโค้ด"
  description: "กรณีการใช้งานบางประการจากการดำเนินการที่เป็นที่นิยมใน GroupDocs.Parser for .NET"
  items:
    # code sample loop
    - title: "แยกรูปภาพจากเอกสาร PDF"
      content: |
        GroupDocs.Parser for .NET ทำให้การแยกรูปภาพจาก [เอกสาร](https://docs.groupdocs.com/parser/net/extract-images-from-documents/) เป็นเรื่องง่ายสำหรับนักพัฒนาที่ใช้ C#:
        {{< landing/code title="แยกรูปภาพจากเอกสาร PDF ใน C#">}}
        ```csharp {style=abap}
        // สร้างอินสแตนซ์ของคลาส Parser
        using (var parser = new Parser("source.pptx"))
        {
            // แยกรูปภาพ
            var images = parser.GetImages();

            // ตรวจสอบว่ามีการแยกรูปภาพบางอย่าง
            if (images == null)
            {
                return;
            }
            // วนรอบรูปภาพ
            foreach (PageImageArea image in images)
            {
                // พิมพ์ดัชนีหน้า สี่เหลี่ยม และประเภทของรูปภาพ
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Type: {2}", 
                    image.Page.Index, image.Rectangle, image.FileType));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "แยกรูปบาร์โค้ดจากภาพ"
      content: |
        ใช้ API .NET ของเราเพื่อแยก [บาร์โค้ด](https://docs.groupdocs.com/parser/net/extract-barcodes-from-document/) จากภาพ:
        {{< landing/code title="แยกรูปบาร์โค้ดจากรูปภาพใน C#">}}
        ```csharp {style=abap}   
        // โหลดภาพต้นฉบับไปยัง Parser
        using (var parser = new Parser("source.jpg"))
        {
            // ตรวจสอบว่าไฟล์รองรับการแยกรูปบาร์โค้ด
            if (parser.Features.Barcodes)
            {
                // แยกรูปบาร์โค้ดจากไฟล์
                var barcodes = parser.GetBarcodes();

                // วนรอบรูปบาร์โค้ด
                foreach (var barcode in barcodes)
                {
                    // พิมพ์ดัชนีหน้า
                    Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                    // พิมพ์ค่าบาร์โค้ด
                    Console.WriteLine("Value: " + barcode.Value);
                }
            }
        }
        ```
        {{< /landing/code >}}

---
