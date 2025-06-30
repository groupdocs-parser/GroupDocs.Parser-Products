


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:20
draft: false
lang: th
format: Docx
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "ดึงข้อมูลบาร์โค้ดจากไฟล์ DOCX ในแอปพลิเคชัน C#"
head_description: "ใช้ GroupDocs.Parser ในการตรวจจับและดึงข้อมูลบาร์โค้ดจากไฟล์ DOCX ใน C# โดยไม่ต้องใช้ซอฟต์แวร์เพิ่มเติม."

############################# Header ############################
title: "ดึงข้อมูลบาร์โค้ดจาก DOCX โดยใช้ C#" 
description: "ตรวจจับและดึงข้อมูลบาร์โค้ดจากไฟล์ PDF, Word, Excel และไฟล์ภาพโดยใช้ GroupDocs.Parser ในแอปพลิเคชัน .NET ของคุณ."
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "ดาวน์โหลดรุ่นทดลองใช้ฟรี"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "เกี่ยวกับ API ของ GroupDocs.Parser for .NET"
    link: "/parser/net/"
    link_title: "เรียนรู้เพิ่มเติม"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/) เป็น API สำหรับการแยกเอกสารที่มีประสิทธิภาพสำหรับนักพัฒนา .NET ซึ่งช่วยให้สามารถดึงข้อความ, รูปภาพ, เนื้อหาที่มีโครงสร้าง, และบาร์โค้ดจากรูปแบบไฟล์ต่าง ๆ รวมถึง PDF, Word, Excel, PowerPoint และอื่น ๆ — ทั้งหมดนี้สามารถทำได้โดยไม่ต้องอิงเครื่องมือภายนอก.

############################# Steps ############################
steps:
    enable: true
    title: "ขั้นตอนในการดึงข้อมูลบาร์โค้ดจาก Docx ใน C#"
    content: |
      [GroupDocs.Parser](/parser/net/) ช่วยให้คุณสามารถดึงข้อมูลบาร์โค้ดจากไฟล์ DOCX ในแอปพลิเคชัน .NET โดยทำตามขั้นตอนง่าย ๆ เหล่านี้:
      
      1. โหลดไฟล์ DOCX โดยใช้อินสแตนซ์ Parser.
      2. ตรวจสอบว่าเอกสารสนับสนุนการดึงข้อมูลบาร์โค้ด.
      3. ดึงรายชื่อบาร์โค้ดจากเอกสาร.
      4. วนรอบผ่านผลลัพธ์และใช้ค่าบาร์โค้ดที่ถูกดึงข้อมูล.
   
    code:
      platform: "net"
      copy_title: "คัดลอก"
      install:
        command: |
        command: "dotnet add package GroupDocs.Parser"
        copy_tip: "คลิกเพื่อคัดลอก"
        copy_done: "คัดลอกแล้ว"
      links:
        #  loop
        - title: "ตัวอย่างเพิ่มเติม"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
        #  loop
        - title: "เอกสารประกอบ"
          link: "https://docs.groupdocs.com/parser/net/"
          
      content: |
        ```csharp {style=abap}
        // โหลดเอกสารที่มีบาร์โค้ดโดยใช้คลาส Parser
        using (Parser parser = new Parser("input.docx")) {

            // ตรวจสอบว่าไฟล์สนับสนุนการดึงข้อมูลบาร์โค้ด
            if (!parser.Features.Barcodes) {
                Console.WriteLine("ไม่สามารถดึงข้อมูลบาร์โค้ดได้");
                return;
            }

            // ดึงและประมวลผลบาร์โค้ดที่ถูกดึงข้อมูล
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
  title: "คุณสมบัติการแยกเอกสารขั้นสูง"
  description: "นอกเหนือจากการดึงข้อมูลบาร์โค้ดแล้ว GroupDocs.Parser ยังช่วยให้คุณสามารถดึงข้อความธรรมดา, รูปภาพ และข้อมูลที่มีโครงสร้างเพื่อสนับสนุนการทำงานอัตโนมัติและกระบวนการจัดการข้อมูลที่ซับซ้อน."
  image: "/img/parser/features_extract-barcode.webp" # 500x500 px
  image_description: "การรู้จำบาร์โค้ดและการแยกเอกสาร"
  features:
    # feature loop
    - title: "สนับสนุนรูปแบบบาร์โค้ดหลายรูปแบบ"
      content: "รับรู้ประเภทบาร์โค้ดที่พบมากรวมถึง QR Code, Code 128, Data Matrix, EAN, Aztec และอื่น ๆ."

    # feature loop
    - title: "ดึงบาร์โค้ดจากเอกสารและภาพ"
      content: "อ่านบาร์โค้ดจากเอกสาร PDF, Word, Excel และรูปแบบภาพเช่น JPEG, PNG และ BMP."

    # feature loop
    - title: "การตั้งค่าการดึงข้อมูลที่ปรับแต่งได้"
      content: "กำหนดตัวเลือกการตรวจจับเช่น พื้นที่การสแกนและการประมวลผลเอกสารหลายหน้า."
      
  code_samples:
    # code sample loop
    - title: "วิธีดึงข้อมูลบาร์โค้ดจาก PDF โดยใช้ตัวเลือกบาร์โค้ด"
      content: |
        ตัวอย่างนี้แสดงวิธีการดึงข้อมูลบาร์โค้ดจากไฟล์ PDF โดยใช้ตัวเลือกการดึงข้อมูลบาร์โค้ดที่เฉพาะเจาะจง.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  โหลดไฟล์ PDF ด้วยคลาส Parser
        using (Parser parser = new Parser("input.pdf"))
        {
            // ยืนยันว่าการดึงข้อมูลบาร์โค้ดได้รับการสนับสนุน
            if (!parser.Features.Barcodes)
            {
                return;
            }

            // ใช้ตัวเลือกบาร์โค้ดเพื่อกรองผลลัพธ์
            BarcodeOptions options = new BarcodeOptions(QualityMode.Low, QualityMode.Low, "QR");

            // ดึงข้อมูลบาร์โค้ดจากเอกสาร
            IEnumerable<PageBarcodeArea> barcodes = parser.GetBarcodes(options);

            // ประมวลผลรายชื่อบาร์โค้ดที่ถูกดึงข้อมูล
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
  title: "พร้อมเริ่มต้นหรือยัง?"
  description: "ลองฟีเจอร์ของ GroupDocs.Parser ฟรี หรือติดต่อขอใบอนุญาต"
  items:
    #  loop
    - title: "ดาวน์โหลด Nuget"
      link: "https://releases.groupdocs.com/parser/net/"
      color: "red"
        #  loop
    - title: "การอนุญาต"
      link: "https://purchase.groupdocs.com/pricing/parser/net/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "รูปแบบที่รองรับสำหรับการดึงข้อมูลบาร์โค้ด"
    exclude: "DOCX"
    description: "GroupDocs.Parser รองรับการตรวจจับบาร์โค้ดในรูปแบบเอกสารและภาพที่หลากหลาย ดูด้านล่างสำหรับประเภทไฟล์ที่รองรับโดยทั่วไป."
    items: 
        # format loop 1
        - name: "解析 PDF"
          format: "PDF"
          link: "/parser/net/extract-barcode/pdf/"
          description: "(รูปแบบเอกสารแบบพกพา)"
          
        # format loop 2
        - name: "解析 DOCX"
          format: "DOCX"
          link: "/parser/net/extract-barcode/docx/"
          description: "(เอกสาร Word 2007+)"
          
        # format loop 3
        - name: "解析 PPTX"
          format: "PPTX"
          link: "/parser/net/extract-barcode/pptx/"
          description: "(รูปแบบการนำเสนอ Open XML)"
          
        # format loop 4
        - name: "解析 XLSX"
          format: "XLSX"
          link: "/parser/net/extract-barcode/xlsx/"
          description: "(สมุดงาน Open XML)"
          
        # format loop 5
        - name: "解析 ODT"
          format: "ODT"
          link: "/parser/net/extract-barcode/odt/"
          description: "(เอกสารข้อความ OpenDocument)"
          
        # format loop 6
        - name: "解析 ODS"
          format: "ODS"
          link: "/parser/net/extract-barcode/ods/"
          description: "(สเปรดชีต OpenDocument)"
          
        # format loop 7
        - name: "解析 ODP"
          format: "ODP"
          link: "/parser/net/extract-barcode/odp/"
          description: "(การนำเสนอ OpenDocument)"
          
        # format loop 8
        - name: "解析 EPUB"
          format: "EPUB"
          link: "/parser/net/extract-barcode/epub/"
          description: "(ไฟล์ eBook แบบเปิด)"
          
        # format loop 9
        - name: "解析 FB2"
          format: "FB2"
          link: "/parser/net/extract-barcode/fb2/"
          description: "(eBook FictionBook)"
         
          

---