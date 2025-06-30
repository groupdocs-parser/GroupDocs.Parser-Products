


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:41
draft: false
lang: th
format: Txt
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "ดึงตารางจากไฟล์ TXT ในแอพ C#"
head_description: "ใช้ GroupDocs.Parser เพื่อตรวจจับและดึงข้อมูลตารางที่มีโครงสร้างจากไฟล์ TXT ในแอพ C# โดยไม่ต้องพึ่งพาไลบรารีภายนอก."

############################# Header ############################
title: "ดึงตารางจาก TXT โดยใช้ C#" 
description: "ระบุและดึงโครงสร้างตารางจาก PDF, Word, Excel และรูปแบบไฟล์อื่น ๆ อย่างรวดเร็วโดยใช้ GroupDocs.Parser ในโปรเจกต์ .NET ของคุณ."
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
       [GroupDocs.Parser](/parser/net/) เป็น API ที่ครอบคลุมสำหรับการแยกเนื้อหาในเอกสาร ซึ่งสร้างขึ้นสำหรับนักพัฒนา .NET ช่วยให้สามารถดึงข้อมูลที่ถูกต้องของข้อความ, ตาราง, รูปภาพ, ลิงก์ และองค์ประกอบที่มีโครงสร้างอื่น ๆ จากรูปแบบต่าง ๆ เช่น PDF, DOCX, XLSX, PPTX และอื่น ๆ โดยไม่ต้องใช้ซอฟต์แวร์ของบุคคลที่สาม.

############################# Steps ############################
steps:
    enable: true
    title: "ขั้นตอนในการดึงตารางจาก Txt ใน C#"
    content: |
      ทำตามคำแนะนำเหล่านี้เพื่อลดการดึงตารางจากไฟล์ TXT โดยใช้ [GroupDocs.Parser](/parser/net/) ภายในสภาพแวดล้อม .NET ของคุณ:
      
      1. สร้างอินสแตนซ์ของ Parser และโหลดเอกสาร TXT ของคุณ.
      2. ตรวจสอบว่าการดึงตารางถูกสนับสนุนสำหรับรูปแบบข้อมูลนำเข้า.
      3. ดึงเนื้อหาตารางจากไฟล์.
      4. ใช้ข้อมูลตารางที่มีโครงสร้างสำหรับการรายงาน การทำงานอัตโนมัติ หรือการวิเคราะห์.
   
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
        // เปิดเอกสารที่มีข้อมูลตารางโดยใช้ Parser
        using (Parser parser = new Parser("input.txt")) {

            // ตรวจสอบว่ารูปแบบสนับสนุนการจดจำตารางหรือไม่
            if (!parser.Features.Tables) {
                Console.WriteLine("จัดการกับเอกสารที่ไม่สนับสนุนการวิเคราะห์ตาราง");
                return;
            }

            // กำหนดว่าโครงสร้างตารางจะถูกระบุอย่างไร
            TemplateTableLayout layout = new TemplateTableLayout(
                new double[] { 50, 95, 275, 415, 485, 545 },
                new double[] { 325, 340, 365, 395 });

            // กำหนดพารามิเตอร์การดึงข้อมูลสำหรับข้อมูลตาราง
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            //  ดึงตารางจากเนื้อหาไฟล์
            IEnumerable<PageTableArea> tables = parser.GetTables(options);

            //  วนซ้ำผ่านแต่ละตารางที่ตรวจพบ
            foreach (PageTableArea t in tables)
            {
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "ความสามารถในการดึงข้อมูลที่ทรงพลัง"
  description: "นอกจากการวิเคราะห์ตารางแล้ว GroupDocs.Parser ยังสามารถดึงเนื้อหาที่หลากหลาย เช่น บล็อกข้อความ รูปภาพ เมตาดาต้า และข้อมูลที่มีโครงสร้างอื่น ๆ เพื่อตอบสนองความต้องการในการทำงานอัตโนมัติของเอกสาร."
  image: "/img/parser/features_extract-table.webp" # 500x500 px
  image_description: "การจดจำตารางและการดึงเนื้อหา"
  features:
    # feature loop
    - title: "การตรวจจับตารางหลายรูปแบบที่แม่นยำ"
      content: "ดึงข้อมูลตารางจาก DOCX, XLSX, PDF, HTML และรูปแบบที่คล้ายกันด้วยความแม่นยำสูง."

    # feature loop
    - title: "วิเคราะห์โครงสร้างตารางจากไฟล์"
      content: "ดึงข้อมูลตารางจากเอกสารและสเปรดชีตได้อย่างมีประสิทธิภาพโดยไม่สูญเสียรูปแบบ."

    # feature loop
    - title: "การกำหนดค่าการดึงตารางที่ยืดหยุ่น"
      content: "ปรับแต่งการตรวจจับลักษณะ การจัดเรียงคอลัมน์ และตัวเลือกหัว/ท้ายเพื่อควบคุมผลลัพธ์อย่างแม่นยำ."
      
  code_samples:
    # code sample loop
    - title: "วิธีการดึงตารางจากสเปรดชีต Excel"
      content: |
        ตัวอย่างโค้ดนี้แสดงวิธีการอ่านและวนซ้ำผ่านข้อมูลตารางในไฟล์ XLSX โดยใช้ GroupDocs.Parser.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  เปิดไฟล์ Excel โดยใช้ API Parser
        using (Parser parser = new Parser("input.xlsx"))
        {
            // ออกจากงานถ้าไม่สามารถดึงตารางจากไฟล์ได้
            if (!parser.Features.Tables)
            {
                return;
            }

            // ใช้กฎจัดรูปแบบเพื่อค้นหาข้อมูลตาราง
            TemplateTableLayout layout = new TemplateTableLayout(
                    new double[] { 50, 95, 275, 415, 485, 545 },
                    new double[] { 325, 340, 365, 395 });

            // กำหนดพารามิเตอร์การดึงข้อมูลสำหรับตาราง
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            // ดำเนินการดึงข้อมูลตาราง
            IEnumerable<PageTableArea> tables = parser.GetTables(options);

            // ตรวจสอบแต่ละโครงสร้างตารางที่ตรวจจับได้
            foreach (PageTableArea t in tables)
            {
                // วนผ่านแต่ละแถวในตาราง
                for (int row = 0; row < t.RowCount; row++)
                {
                    // วนซ้ำผ่านเซลล์ในแต่ละแถว
                    for (int column = 0; column < t.ColumnCount; column++)
                    {
                        // เข้าถึงเซลล์ตารางปัจจุบัน
                        PageTableAreaCell cell = t[row, column];
                        if (cell != null)
                        {
                            // แสดงเนื้อหาข้อความในแต่ละเซลล์
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
    title: "รูปแบบที่รองรับสำหรับการดึงตาราง"
    exclude: "TXT"
    description: "GroupDocs.Parser สามารถดึงข้อมูลตารางจากเอกสารหลายประเภทได้ ด้านล่างคือรูปแบบที่ใช้บ่อยที่สุดสำหรับการวิเคราะห์ตารางที่มีโครงสร้าง."
    items: 
        # format loop 1
        - name: "解析 PDF"
          format: "PDF"
          link: "/parser/net/extract-table/pdf/"
          description: "(รูปแบบเอกสารแบบพกพา)"
          
        # format loop 2
        - name: "解析 DOCX"
          format: "DOCX"
          link: "/parser/net/extract-table/docx/"
          description: "(เอกสาร Word 2007+)"
          
        # format loop 3
        - name: "解析 PPTX"
          format: "PPTX"
          link: "/parser/net/extract-table/pptx/"
          description: "(รูปแบบการนำเสนอ Open XML)"
          
        # format loop 4
        - name: "解析 XLSX"
          format: "XLSX"
          link: "/parser/net/extract-table/xlsx/"
          description: "(สมุดงาน Open XML)"
          
        # format loop 5
        - name: "解析 TXT"
          format: "TXT"
          link: "/parser/net/extract-table/txt/"
          description: "(ไฟล์ข้อความ)"
          
        # format loop 6
        - name: "解析 RTF"
          format: "RTF"
          link: "/parser/net/extract-table/rtf/"
          description: "(รูปแบบข้อความที่มีความรวย)"
          
        # format loop 7
        - name: "解析 XML"
          format: "XML"
          link: "/parser/net/extract-table/xml/"
          description: "(ภาษาเครื่องหมายขยาย)"
          
        # format loop 8
        - name: "解析 EPUB"
          format: "EPUB"
          link: "/parser/net/extract-table/epub/"
          description: "(ไฟล์ eBook แบบเปิด)"
         
          

---