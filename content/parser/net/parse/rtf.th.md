


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:53
draft: false
lang: th
format: Rtf
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "RTF ไฟล์ข้อมูลการแยกวิเคราะห์ในแอป C#"
head_description: "ใช้ GroupDocs.Parser เพื่อดึงข้อความ รูปภาพ ตาราง และข้อมูลอื่น ๆ จากไฟล์ RTF ในแอป C# โดยไม่พึ่งพาเครื่องมือของบุคคลที่สาม."

############################# Header ############################
title: "แยกวิเคราะห์เอกสาร RTF โดยใช้ C#" 
description: "ดึงข้อมูล ข้อมูลเมตา ตาราง และรูปภาพจากไฟล์ PDF Word Excel และไฟล์รูปภาพอย่างมีประสิทธิภาพโดยใช้ GroupDocs.Parser ในโปรเจกต์ .NET ของคุณ."
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
       [GroupDocs.Parser](/parser/net/) เป็น API การแยกวิเคราะห์เอกสารที่มีฟีเจอร์ครบครันที่ออกแบบมาสำหรับนักพัฒนา .NET สามารถดึงข้อมูลข้อความแบบธรรมดาและมีโครงสร้าง ข้อมูลเมตา รูปภาพ ตาราง และบาร์โค้ดจากรูปแบบที่นิยม เช่น PDF, DOCX, XLSX, PPTX และอื่น ๆ — ทั้งหมดนี้โดยไม่ต้องพึ่งพาซอฟต์แวร์เพิ่มเติม.

############################# Steps ############################
steps:
    enable: true
    title: "ขั้นตอนในการดึงข้อมูลจาก Rtf ใน C#"
    content: |
      ปฏิบัติตามขั้นตอนเหล่านี้เพื่อแยกเนื้อหาจากเอกสาร RTF ในแอป .NET ของคุณโดยใช้ [GroupDocs.Parser](/parser/net/):
      
      1. โหลดเอกสาร RTF โดยใช้อินสแตนซ์ของ Parser.
      2. ดึงเนื้อหาที่ต้องการเช่น ข้อความ ตาราง หรือข้อมูลเมตา.
      3. ตรวจสอบว่าข้อมูลที่ดึงมาใช้ได้.
      4. ใช้ผลลัพธ์ที่แยกวิเคราะห์ในกระบวนการต่อไป ระบบอัตโนมัติ หรือระบบธุรกิจของคุณ.
   
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
        using (Parser parser = new Parser("input.rtf")) {

            // ดึงข้อมูลข้อความทั้งหมดจากไฟล์
            using (TextReader reader = parser.GetText()) 
            {
                // หากข้อความไม่สามารถดึงได้ ผลลัพธ์จะเป็น null
                // ใช้ข้อความที่ดึงได้ในแอปของคุณ
                Console.WriteLine(reader == null ? 
                    "การดึงข้อมูลข้อความไม่รองรับสำหรับรูปแบบนี้" : reader.ReadToEnd());
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "ความสามารถในการแยกวิเคราะห์เอกสารที่ครอบคลุม"
  description: "GroupDocs.Parser รองรับมากกว่าเพียงการอ่านข้อความ — ยังสนับสนุนการดึงข้อมูลบาร์โค้ด การแยกรูปภาพ การเข้าถึงข้อมูลเมตา และการประมวลผลข้อมูลแบบมีโครงสร้างเพื่อการทำงานอัตโนมัติและการวิเคราะห์ข้อมูลที่ทันสมัย."
  image: "/img/parser/features_parse.webp" # 500x500 px
  image_description: "ความสามารถในการดึงข้อมูลและการแยกวิเคราะห์เอกสาร"
  features:
    # feature loop
    - title: "รองรับประเภทเนื้อหาของไฟล์ที่หลากหลาย"
      content: "ดึงข้อมูลรวมถึงข้อความ รูปภาพ ตาราง และฟิลด์จากรูปแบบเอกสารเช่น PDF Word Excel HTML และอื่น ๆ."

    # feature loop
    - title: "ทำงานกับไฟล์สแกนและดิจิทัล"
      content: "แยกข้อมูลจากเอกสารที่ถูกสแกนและไฟล์ที่สร้างขึ้นโดยดิจิทัล มีการสนับสนุน OCR และการแยกข้อมูลที่รู้จักรูปแบบ."

    # feature loop
    - title: "พารามิเตอร์การแยกวิเคราะห์ที่ปรับแต่งได้"
      content: "ปรับตรรกะการแยกวิเคราะห์ด้วยตัวเลือกที่ยืดหยุ่นเช่น การเลือกช่วงหน้า การกำหนดเป้าหมายพื้นที่ และแม่แบบการตรวจจับฟิลด์."
      
  code_samples:
    # code sample loop
    - title: "วิธีการแยกวิเคราะห์ PDF โดยใช้แม่แบบ"
      content: |
        ตัวอย่างนี้แสดงวิธีการดึงข้อมูลที่มีโครงสร้างจาก PDF โดยใช้แม่แบบการแยกวิเคราะห์ที่กำหนดไว้ล่วงหน้าด้วย GroupDocs.Parser.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  โหลดไฟล์ PDF ด้วยคลาส Parser
        using (Parser parser = new Parser("input.pdf"))
        {
            // แยกวิเคราะห์เอกสารตามแม่แบบ
            DocumentData data = parser.ParseByTemplate(GetTemplate());

            // ตรวจสอบว่าการดึงข้อมูลฟอร์มได้รับการสนับสนุนหรือไม่
            if (data == null)
            {
                return;
            }

            // ประมวลผลฟิลด์ที่ได้รับ
            for (int i = 0; i < data.Count; i++)
            {
                Console.Write(data[i].Name + ": ");
                PageTextArea area = data[i].PageArea as PageTextArea;
                Console.WriteLine(area == null ? "Not a template field" : area.Text);
            }
        }

        private static Template GetTemplate()
        {
            // สร้างพารามิเตอร์ตรวจจับสำหรับตาราง 'รายละเอียด'
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
    title: "รูปแบบที่รองรับสำหรับการดึงข้อมูล"
    exclude: "RTF"
    description: "GroupDocs.Parser รองรับการแยกวิเคราะห์ในกลุ่มที่หลากหลายของเอกสารและรูปแบบภาพ สำรวจประเภทไฟล์ที่รองรับที่ใช้กันทั่วไปในกระบวนการดึงข้อมูล."
    items: 
        # format loop 1
        - name: "解析 PDF"
          format: "PDF"
          link: "/parser/net/parse/pdf/"
          description: "(รูปแบบเอกสารแบบพกพา)"
          
        # format loop 2
        - name: "解析 DOCX"
          format: "DOCX"
          link: "/parser/net/parse/docx/"
          description: "(เอกสาร Word 2007+)"
          
        # format loop 3
        - name: "解析 PPTX"
          format: "PPTX"
          link: "/parser/net/parse/pptx/"
          description: "(รูปแบบการนำเสนอ Open XML)"
          
        # format loop 4
        - name: "解析 XLSX"
          format: "XLSX"
          link: "/parser/net/parse/xlsx/"
          description: "(สมุดงาน Open XML)"
          
        # format loop 5
        - name: "解析 TXT"
          format: "TXT"
          link: "/parser/net/parse/txt/"
          description: "(ไฟล์ข้อความ)"
          
        # format loop 6
        - name: "解析 RTF"
          format: "RTF"
          link: "/parser/net/parse/rtf/"
          description: "(รูปแบบข้อความที่มีความรวย)"
          
        # format loop 7
        - name: "解析 XML"
          format: "XML"
          link: "/parser/net/parse/xml/"
          description: "(ภาษาเครื่องหมายขยาย)"
          
        # format loop 8
        - name: "解析 EPUB"
          format: "EPUB"
          link: "/parser/net/parse/epub/"
          description: "(ไฟล์ eBook แบบเปิด)"
         
          

---