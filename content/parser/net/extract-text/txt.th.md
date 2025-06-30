


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:47
draft: false
lang: th
format: Txt
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "ดึงข้อความจากไฟล์ TXT ในแอป C#"
head_description: "ใช้ GroupDocs.Parser ในการดึงข้อความที่เป็นแบบธรรมดาหรือมีโครงสร้างจากไฟล์ TXT ในแอป C# โดยไม่ต้องใช้เครื่องมือภายนอก."

############################# Header ############################
title: "ดึงข้อความจาก TXT โดยใช้ C#" 
description: "ดึงข้อความที่อ่านได้และมีโครงสร้างจากไฟล์ PDF, Word, Excel และประเภทไฟล์อื่นๆ โดยใช้ GroupDocs.Parser ในโซลูชัน .NET ของคุณ."
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
    title: "เกี่ยวกับ API GroupDocs.Parser for .NET"
    link: "/parser/net/"
    link_title: "เรียนรู้เพิ่มเติม"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/) เป็น API การแยกเอกสารที่มีประสิทธิภาพสูงสำหรับนักพัฒนา .NET มันทำให้การดึงข้อความ, รูปภาพ, ตาราง, และเนื้อหาที่มีโครงสร้างจากหลายประเภทไฟล์รวมถึง PDF, DOCX, XLSX, PPTX และอื่นๆ เป็นเรื่องง่าย—โดยไม่ต้องพึ่งพาไลบรารีของบุคคลที่สาม.

############################# Steps ############################
steps:
    enable: true
    title: "ขั้นตอนการดึงข้อความจาก Txt ใน C#"
    content: |
      คุณสามารถดึงข้อความที่สะอาดและมีโครงสร้างจากเอกสาร TXT ในแอพ .NET โดยใช้ [GroupDocs.Parser](/parser/net/) ตามขั้นตอนเหล่านี้:
      
      1. เปิดเอกสาร TXT โดยใช้ตัวอย่าง Parser.
      2. ดึงข้อความจากเนื้อหาของไฟล์.
      3. ตรวจสอบผลลัพธ์เพื่อยืนยันว่าการดึงข้อความสำเร็จ.
      4. ใช้ข้อความที่ดึงออกมาในตรรกะธุรกิจ, การจัดทำดัชนี, หรือข้อมูลท่อ.
   
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
        // โหลดเอกสารของคุณเข้าสู่ Parser
        using (Parser parser = new Parser("input.txt")) {

            // ดึงเนื้อหาข้อความทั้งหมดจากไฟล์
            using (TextReader reader = parser.GetText()) 
            {
                // หากไม่พบข้อความ ผลลัพธ์จะเป็น null
                // ใช้ข้อความที่ดึงออกมาในแอปพลิเคชันของคุณ
                Console.WriteLine(reader == null ? 
                    "การดึงข้อความไม่รองรับสำหรับรูปแบบนี้" : reader.ReadToEnd());
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "คุณสมบัติการแยกเนื้อหาที่ครอบคลุม"
  description: "นอกจากข้อความธรรมดาแล้ว GroupDocs.Parser ยังสามารถดึงภาพ, องค์ประกอบที่มีโครงสร้าง, และข้อมูลเมตาเพื่อสนับสนุนการวิเคราะห์เนื้อหา, การแปลง, และการทำงานอัตโนมัติ."
  image: "/img/parser/features_extract-text.webp" # 500x500 px
  image_description: "การรู้จำข้อความและการแยกเอกสารที่มีโครงสร้าง"
  features:
    # feature loop
    - title: "การดึงข้อความจากไฟล์หลายประเภท"
      content: "รับข้อความที่เป็นแบบธรรมดาหรือมีโครงสร้างจากรูปแบบต่างๆ เช่น PDF, DOCX, XLSX, PPTX, HTML และรูปแบบอื่นๆ."

    # feature loop
    - title: "ประมวลผลข้อความจากเอกสารและภาพ"
      content: "ดึงข้อความจากภาพที่สแกน, ภาพนิ่ง, แผ่นงาน, และเอกสารดิจิทัล โดยยังคงรักษาโครงสร้าง."

    # feature loop
    - title: "การตั้งค่าการดึงข้อความขั้นสูง"
      content: "ปรับแต่งวิธีการตรวจจับข้อความ—กำหนดช่วงหน้ากระดาษ, พื้นที่เลย์เอาต์, และปรับผลลัพธ์เพื่อความแม่นยำสูงสุด."
      
  code_samples:
    # code sample loop
    - title: "วิธีการดึงพื้นที่ข้อความจากไฟล์ PPTX"
      content: |
        ตัวอย่างโค้ดนี้แสดงวิธีการเรียกคืนเนื้อหาข้อความพร้อมด้วยพิกัดพื้นที่จากไฟล์ PowerPoint โดยใช้ GroupDocs.Parser.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  โหลดการนำเสนอ PowerPoint ด้วย Parser
        using (Parser parser = new Parser("input.pptx"))
        {
            // ดึงสี่เหลี่ยมผืนผ้าของพื้นที่ข้อความทั้งหมดจากเอกสาร
            IEnumerable<PageTextArea> areas = parser.GetTextAreas();

            // ออกจากระบบหากการดึงพื้นที่ข้อความไม่สามารถใช้ได้
            if (areas == null)
            {
                return;
            }

            // วนรอบแต่ละพื้นที่ข้อความของแต่ละหน้า
            foreach (PageTextArea a in areas)
            {
                // เข้าถึงดัชนีหน้า, สี่เหลี่ยมผืนผ้าของพื้นที่, และค่าข้อความ
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Text: {2}", a.Page.Index, a.Rectangle, a.Text));
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
    title: "รูปแบบที่รองรับสำหรับการดึงข้อความ"
    exclude: "TXT"
    description: "GroupDocs.Parser สามารถดึงข้อความจากเอกสารและประเภทภาพที่หลากหลาย สำรวจรูปแบบที่รองรับที่พบบ่อยซึ่งระบุไว้ด้านล่าง."
    items: 
        # format loop 1
        - name: "解析 PDF"
          format: "PDF"
          link: "/parser/net/extract-text/pdf/"
          description: "(รูปแบบเอกสารแบบพกพา)"
          
        # format loop 2
        - name: "解析 DOCX"
          format: "DOCX"
          link: "/parser/net/extract-text/docx/"
          description: "(เอกสาร Word 2007+)"
          
        # format loop 3
        - name: "解析 PPTX"
          format: "PPTX"
          link: "/parser/net/extract-text/pptx/"
          description: "(รูปแบบการนำเสนอ Open XML)"
          
        # format loop 4
        - name: "解析 XLSX"
          format: "XLSX"
          link: "/parser/net/extract-text/xlsx/"
          description: "(สมุดงาน Open XML)"
          
        # format loop 5
        - name: "解析 TXT"
          format: "TXT"
          link: "/parser/net/extract-text/txt/"
          description: "(ไฟล์ข้อความ)"
          
        # format loop 6
        - name: "解析 RTF"
          format: "RTF"
          link: "/parser/net/extract-text/rtf/"
          description: "(รูปแบบข้อความที่มีความรวย)"
          
        # format loop 7
        - name: "解析 XML"
          format: "XML"
          link: "/parser/net/extract-text/xml/"
          description: "(ภาษาเครื่องหมายขยาย)"
          
        # format loop 8
        - name: "解析 EPUB"
          format: "EPUB"
          link: "/parser/net/extract-text/epub/"
          description: "(ไฟล์ eBook แบบเปิด)"
         
          

---