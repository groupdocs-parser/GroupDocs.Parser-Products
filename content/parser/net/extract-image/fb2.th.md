


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:34
draft: false
lang: th
format: Fb2
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "ดึงภาพจากไฟล์ FB2 ในแอป C#"
head_description: "ใช้ GroupDocs.Parser เพื่อตรวจจับและดึงภาพจากไฟล์ FB2 ใน C# โดยไม่ต้องใช้เครื่องมือเพิ่มเติม."

############################# Header ############################
title: "ดึงภาพจาก FB2 โดยใช้ C#" 
description: "ค้นหาและดึงภาพที่ฝังอยู่จาก PDF, เอกสาร Word, แผ่น Excel และประเภทไฟล์อื่น ๆ โดยใช้ GroupDocs.Parser ในแอป .NET ของคุณ."
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "ดาวน์โหลดทดลองใช้ฟรี"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "เกี่ยวกับ API ของ GroupDocs.Parser for .NET"
    link: "/parser/net/"
    link_title: "เรียนรู้เพิ่มเติม"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/) 是一个强大的文档解析库，为 .NET 开发者提供服务。它สามารถใช้ในการดึงภาพ ข้อความ ลิงก์ และข้อมูลที่มีโครงสร้างจากประเภทไฟล์ยอดนิยมเช่น PDF, DOCX, XLSX, PPTX และอื่น ๆ โดยไม่จำเป็นต้องใช้แอพพลิเคชั่นจากภายนอก.

############################# Steps ############################
steps:
    enable: true
    title: "ขั้นตอนในการดึงภาพจาก Fb2 ใน C#"
    content: |
      ด้วย [GroupDocs.Parser](/parser/net/) คุณสามารถดึงภาพจากเอกสาร FB2 ในโปรเจกต์ .NET ของคุณได้ในไม่กี่ขั้นตอน:
      
      1. เริ่มต้น Parser ด้วยไฟล์ FB2.
      2. ดึงส่วนภาพจากเอกสาร.
      3. ใช้ภาพที่ถูกดึงออกไปตามต้องการในเส้นทางการทำงานของคุณ.
   
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
        // เปิดเอกสารที่มีภาพโดยใช้ Parser
        using (Parser parser = new Parser("input.fb2")) {

            // ดึงภาพที่ฝังอยู่ทั้งหมดจากไฟล์
            IEnumerable<PageImageArea> images = parser.GetImages();

            // จัดการกรณีที่ไม่มีภาพ
            if (images == null)
            {
                return;
            }

            // ประมวลผลหรือบันทึกภาพที่ดึงมา
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
  title: "การดึงข้อมูลเนื้อหาเอกสารอย่างครอบคลุม"
  description: "GroupDocs.Parser เสนอมากกว่าการดึงภาพ — คุณยังสามารถดึงข้อความดิบ ลิงก์ เมตาดาต้า และเนื้อหาที่มีโครงสร้างสำหรับการสร้างระบบอัตโนมัติขั้นสูง."
  image: "/img/parser/features_extract-image.webp" # 500x500 px
  image_description: "การดึงภาพและกระบวนการ parsing เอกสาร"
  features:
    # feature loop
    - title: "ดึงภาพจากหลายรูปแบบ"
      content: "ดึงภาพที่ฝังอยู่จากหลากหลายรูปแบบไฟล์ รวมถึง DOCX, PDF, PPTX, XLSX และไฟล์ภาพเช่น PNG, JPG และ TIFF."

    # feature loop
    - title: "รักษาคุณภาพภาพต้นฉบับ"
      content: "ภาพถูกรวบรวมด้วยความชัดเจนสูง รักษาความละเอียด รูปแบบ และโปรไฟล์สีเดิม."

    # feature loop
    - title: "ตัวเลือกการดึงขั้นสูง"
      content: "ปรับแต่งการดึงภาพด้วยการกรองตามหน้า รูปแบบ หรือความละเอียด และสนับสนุนเอกสารหลายหน้า."
      
  code_samples:
    # code sample loop
    - title: "วิธีดึงและบันทึกภาพจากเอกสาร PDF"
      content: |
        ตัวอย่างนี้แสดงให้เห็นวิธีดึงทรัพย์สินภาพทั้งหมดจากไฟล์ PDF และบันทึกลงในระบบไฟล์ท้องถิ่น.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  โหลด PDF โดยใช้คลาส Parser
        using (Parser parser = new Parser("input.pdf"))
        {
            // ดึงภาพที่ฝังอยู่จากไฟล์
            IEnumerable<PageImageArea> images = parser.GetImages();

            // ตั้งค่ารูปแบบเอาต์พุตและตัวเลือกภาพ (เช่น PNG)
            ImageOptions options = new ImageOptions(ImageFormat.Png);

            // เขียนภาพที่ถูกดึงมาไปยังดิสก์
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
    title: "รูปแบบที่รองรับสำหรับการดึงภาพ"
    exclude: "FB2"
    description: "GroupDocs.Parser ช่วยให้การดึงภาพจากเอกสารและรูปแบบภาพต่าง ๆ เป็นไปอย่างแม่นยำ ตรวจสอบรายการด้านล่างเพื่อดูประเภทที่รองรับทั่วไป."
    items: 
        # format loop 1
        - name: "解析 PDF"
          format: "PDF"
          link: "/parser/net/extract-image/pdf/"
          description: "(รูปแบบเอกสารแบบพกพา)"
          
        # format loop 2
        - name: "解析 DOCX"
          format: "DOCX"
          link: "/parser/net/extract-image/docx/"
          description: "(เอกสาร Word 2007+)"
          
        # format loop 3
        - name: "解析 PPTX"
          format: "PPTX"
          link: "/parser/net/extract-image/pptx/"
          description: "(รูปแบบการนำเสนอ Open XML)"
          
        # format loop 4
        - name: "解析 XLSX"
          format: "XLSX"
          link: "/parser/net/extract-image/xlsx/"
          description: "(สมุดงาน Open XML)"
          
        # format loop 5
        - name: "解析 ODT"
          format: "ODT"
          link: "/parser/net/extract-image/odt/"
          description: "(เอกสารข้อความ OpenDocument)"
          
        # format loop 6
        - name: "解析 ODS"
          format: "ODS"
          link: "/parser/net/extract-image/ods/"
          description: "(สเปรดชีต OpenDocument)"
          
        # format loop 7
        - name: "解析 ODP"
          format: "ODP"
          link: "/parser/net/extract-image/odp/"
          description: "(การนำเสนอ OpenDocument)"
          
        # format loop 8
        - name: "解析 EPUB"
          format: "EPUB"
          link: "/parser/net/extract-image/epub/"
          description: "(ไฟล์ eBook แบบเปิด)"
          
        # format loop 9
        - name: "解析 FB2"
          format: "FB2"
          link: "/parser/net/extract-image/fb2/"
          description: "(eBook FictionBook)"
         
          

---