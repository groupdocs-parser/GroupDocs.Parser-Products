---
############################# Static ############################
layout: "landing"
date: 2025-12-09T14:10:41
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
    # supported_platforms loop
    - title: "Python"
      tag: "python-net"

############################# Head ############################
head_title: "GroupDocs.Parser for .NET Document Parser SDK สำหรับ .NET"
head_description: "Document Parser SDK ที่มีประสิทธิภาพสูงสำหรับ .NET. สกัดข้อความ, รูปภาพ, metadata, barcodes, ตารางและข้อมูลอื่น ๆ จาก PDF, Word, Excel, อีเมลและรูปแบบเอกสารกว่า 50 แบบ"

############################# Header ############################
title: "Document Parser SDK สำหรับ .NET"
description: "เพิ่มการแปลงเอกสารที่รวดเร็วและแม่นยำให้กับแอป .NET ของคุณและสกัดข้อความ, รูปภาพ, metadata และข้อมูลเชิงโครงสร้างจากเอกสารและภาพ"
words:
  for: "สำหรับ"

actions:
  main: "Nuget ดาวน์โหลด"
  main_link: "https://www.nuget.org/packages/GroupDocs.Parser"
  alt: "การให้สิทธิ์ใช้"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/net/"
  title: "พร้อมเริ่มต้นแล้วหรือยัง?"
  description: "ลองใช้ฟีเจอร์ของ GroupDocs.Parser ฟรีหรือขอรับใบอนุญาต"

release:
  title: "เวอร์ชัน {0} ปล่อยแล้ว"
  notes: "ดูว่ามีอะไรใหม่"
  downloads: "ดาวน์โหลด"

code:
  title: "แยกเนื้อหาเอกสารอย่างรวดเร็วด้วย SDK"
  more: "ตัวอย่างเพิ่มเติม"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
  install: "dotnet add package GroupDocs.Parser"
  content: |
    ```csharp {style=abap}   
    // ส่งไฟล์ต้นฉบับไปยังอินสแตนซ์ของ Parser
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
  title: "GroupDocs.Parser อย่างคร่าวๆ"
  description: "Document Parser SDK สำหรับการแปลงเอกสารด้วยความแม่นยำสูงในแอปพลิเคชัน .NET"
  features:
    # feature loop
    - title: "สกัดข้อมูลจากเอกสาร"
      content: "GroupDocs.Parser for .NET API ช่วยให้คุณดึงข้อความ, metadata และรูปภาพจากรูปแบบไฟล์หลากหลาย เช่น เอกสาร Office, อีเมล, ไฟล์แนบและไฟล์เก็บข้อมูล เครื่องมือนี้ช่วยให้คุณเข้าถึงและประมวลผลข้อมูลสำคัญในไฟล์เหล่านี้ได้อย่างมีประสิทธิภาพสำหรับการใช้งานต่าง ๆ เช่น การวิเคราะห์ข้อมูล, การทำดัชนีเครื่องมือค้นหา หรือระบบจัดการเนื้อหา"

    # feature loop
    - title: "แปลงเอกสาร"
      content: "สกัดส่วนประกอบต่าง ๆ เช่น ลิงก์, ตาราง, QR Code, barcode และข้อมูลจากแบบฟอร์ม PDF. นอกจากนี้ยังสามารถแปลงข้อมูลที่ต้องการจากเอกสารโดยใช้เทมเพลตที่กำหนดเอง"

    # feature loop
    - title: "ปรับแต่งผลลัพธ์"
      content: ".NET API ช่วยให้คุณดึงข้อมูลในรูปแบบต่าง ๆ เช่น raw, structured, HTML หรือ Markdown. นอกจากนี้ API ยังมีฟังก์ชันการค้นหาเพื่อหาคำหรือวลีเฉพาะในข้อความของเอกสาร"

############################# Platforms ############################
platforms:
  enable: true
  title: "ความเป็นอิสระของแพลตฟอร์ม"
  description: "GroupDocs.Parser for .NET รองรับระบบปฏิบัติการ, เฟรมเวิร์ก และผู้จัดการแพ็คเกจต่อไปนี้"
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
    GroupDocs.Parser for .NET รองรับการทำงานกับ [รูปแบบไฟล์](https://docs.groupdocs.com/parser/net/supported-document-formats/) ต่อไปนี้.
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
        ### รูปภาพและรูปแบบอื่น ๆ
        * **พกพา:** PDF 
        * **รูปภาพ:** JPG, BMP, PNG, TIFF, GIF
        * **รูปแบบ Office อื่น ๆ:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### รูปแบบอื่น ๆ
        * **เว็บ:** HTML, MHTML 
        * **ไฟล์เก็บข้อมูล:** ZIP, TAR, 7Z 
        * **อีบุ๊ค:** CHM, EPUB, FB2, MOBI 
        
        

############################# Features ############################
features:
  enable: true
  title: "คุณลักษณะของ GroupDocs.Parser for .NET"
  description: "สกัดข้อมูลจาก PDF, เอกสาร Office, ภาพและรูปแบบอื่น ๆ อย่างรวดเร็วและแม่นยำด้วย .NET Document Parser SDK ของเรา"

  items:
    # feature loop
    - icon: "text"
      title: "สกัดข้อความ"
      content: "สกัดข้อมูลข้อความจากรูปแบบไฟล์ต่าง ๆ เช่น เอกสาร Office, ไฟล์ PDF และภาพ เพื่อความอ่านง่ายและการวิเคราะห์"

    # feature loop
    - icon: "image"
      title: "สกัดรูปภาพ"
      content: "ดึงเนื้อหาภาพจากแหล่งต่าง ๆ เช่น เอกสาร Office, ไฟล์ PDF เพื่อการเข้าถึงและใช้ประโยชน์ได้สะดวก"

    # feature loop
    - icon: "qr"
      title: "สแกน QR Code"
      content: "ตรวจจับและถอดรหัส QR Code ที่อยู่ในเอกสาร Office, ไฟล์ PDF หรือเนื้อหาภาพ เพื่อการเรียกคืนข้อมูลอย่างมีประสิทธิภาพ"

    # feature loop
    - icon: "email"
      title: "สกัดข้อมูลจากไฟล์แนบอีเมลและไฟล์เก็บข้อมูล"
      content: "รวบรวมข้อมูลที่มีคุณค่าจากข้อความอีเมล, ไฟล์แนบ และแหล่งข้อมูลที่บีบอัดเพื่อการวิเคราะห์และใช้งานอย่างมีประสิทธิภาพ."

    # feature loop
    - icon: "table"
      title: "ดึงตาราง"
      content: "ระบุและดึงข้อมูลแบบตารางจากเอกสาร PDF เพื่อการวิเคราะห์และการใช้งานอย่างเป็นระบบ."

    # feature loop
    - icon: "hyperlink"
      title: "ดึงไฮเปอร์ลิงก์"
      content: "ค้นหาและดึงไฮเปอร์ลิงก์และที่อยู่อีเมลภายในเอกสาร Office หรือไฟล์ PDF เพื่อการเข้าถึงอย่างมีประสิทธิภาพ."

    # feature loop
    - icon: "pdf"
      title: "แยกวิเคราะห์แบบฟอร์ม PDF"
      content: "แบบฟอร์ม PDF คือเอกสารดิจิทัลที่มีฟิลด์ที่สามารถกรอกได้เพื่อการโต้ตอบของผู้ใช้ ให้ผู้ใช้ป้อนข้อมูลแบบอิเล็กทรอนิกส์ได้ API ของ .NET สามารถใช้เพื่อดึงข้อมูลจากแบบฟอร์มเหล่านี้เพื่อการประมวลผลที่มีประสิทธิภาพ."

    # feature loop
    - icon: "template"
      title: "แยกวิเคราะห์ข้อมูลโดยใช้เทมเพลต"
      content: "สร้างเทมเพลตที่กำหนดเองและใช้ร่วมกับ API ของ .NET เพื่อนำมาวิเคราะห์ข้อมูลเฉพาะจากไฟล์ PDF ทำให้กระบวนการดึงข้อมูลง่ายขึ้น."

    # feature loop
    - icon: "search"
      title: "ค้นหาข้อความในเอกสาร"
      content: "ค้นหาคำหรือรูปแบบเฉพาะในเอกสารได้อย่างรวดเร็ว."


############################# Code samples ############################
code_samples:
  enable: true
  title: "ตัวอย่างโค้ด"
  description: "ตัวอย่างการใช้งานทั่วไปของ GroupDocs.Parser for .NET"
  items:
    # code sample loop
    - title: "ดึงภาพจากเอกสาร PDF"
      content: |
        GroupDocs.Parser for .NET ทำให้ผู้พัฒนา C# สามารถดึงภาพจาก [เอกสาร](https://docs.groupdocs.com/parser/net/extract-images-from-documents/) ได้อย่างง่ายดาย:
        {{< landing/code title="สกัดภาพจากเอกสาร PDF ด้วย C#">}}
        ```csharp {style=abap}
        // สร้างอินสแตนซ์ของคลาส Parser
        using (var parser = new Parser("source.pptx"))
        {
            // สกัดภาพ
            var images = parser.GetImages();

            // ตรวจสอบว่ามีการสกัดข้อมูลหรือไม่
            if (images == null)
            {
                return;
            }
            // วนลูปผ่านภาพ
            foreach (PageImageArea image in images)
            {
                // พิมพ์ดัชนีหน้าที่, สี่เหลี่ยมและประเภทของภาพ
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Type: {2}", 
                    image.Page.Index, image.Rectangle, image.FileType));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "ดึงบาร์โค้ดจากภาพ"
      content: |
        ใช้ API .NET ของเราเพื่อดึง [บาร์โค้ด](https://docs.groupdocs.com/parser/net/extract-barcodes-from-document/) จากภาพ:
        {{< landing/code title="สกัดบาร์โค้ดจากภาพด้วย C#">}}
        ```csharp {style=abap}   
        // โหลดภาพต้นฉบับเข้าสู่ Parser
        using (var parser = new Parser("source.jpg"))
        {
            // ตรวจสอบว่าไฟล์รองรับการสกัดบาร์โค้ดหรือไม่
            if (parser.Features.Barcodes)
            {
                // สกัดบาร์โค้ดจากไฟล์
                var barcodes = parser.GetBarcodes();

                // วนลูปผ่านบาร์โค้ด
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
