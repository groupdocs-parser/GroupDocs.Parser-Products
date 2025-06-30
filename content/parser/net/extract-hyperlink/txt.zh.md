


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:27
draft: false
lang: zh
format: Txt
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "在C#应用程序中从TXT文件提取超链接"
head_description: "使用GroupDocs.Parser在C#中检测并提取TXT文件的超链接，无需额外的工具或软件。"

############################# Header ############################
title: "使用C#从TXT提取超链接" 
description: "通过在您的.NET应用程序中使用GroupDocs.Parser，检测并提取PDF、Word、Excel及其他文档类型中的URL和超链接。"
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "下载免费试用"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "关于GroupDocs.Parser for .NET API"
    link: "/parser/net/"
    link_title: "了解更多"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/)是一个适用于.NET开发者的多功能文档解析API。它支持从各种文件格式（如PDF、Word、Excel、HTML等）提取超链接、文本、图像和结构化内容，无需依赖外部软件。

############################# Steps ############################
steps:
    enable: true
    title: "在C#中从Txt提取超链接的步骤"
    content: |
      [GroupDocs.Parser](/parser/net/)使.NET开发者能够通过以下简单步骤从TXT文件中提取超链接：
      
      1. 使用Parser实例加载TXT文件。
      2. 检查文档是否支持超链接提取。
      3. 从文档中检索超链接列表。
      4. 循环遍历结果并处理提取的URL。
   
    code:
      platform: "net"
      copy_title: "复制"
      install:
        command: |
        command: "dotnet add package GroupDocs.Parser"
        copy_tip: "点击以复制"
        copy_done: "已复制"
      links:
        #  loop
        - title: "更多示例"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
        #  loop
        - title: "文档"
          link: "https://docs.groupdocs.com/parser/net/"
          
      content: |
        ```csharp {style=abap}
        // 使用Parser类加载包含超链接的文档
        using (Parser parser = new Parser("input.txt")) {

            // 验证文件是否支持超链接提取
            if (!parser.Features.Hyperlinks)
            {
                Console.WriteLine("该文件不支持超链接提取");
                return;
            }

            // 检索并处理提取的超链接
            IEnumerable<PageHyperlinkArea> hyperlinks = parser.GetHyperlinks();

            foreach (PageHyperlinkArea h in hyperlinks)
            {
                Console.WriteLine(h.Text);
                Console.WriteLine(h.Url);
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "高级文档解析功能"
  description: "除了超链接提取之外，GroupDocs.Parser还允许您提取文本、元数据、图像和结构化数据，支持强大的数据处理工作流。"
  image: "/img/parser/features_extract-hyperlink.webp" # 500x500 px
  image_description: "超链接检测和文档解析"
  features:
    # feature loop
    - title: "文档中的超链接检测"
      content: "快速提取PDF、Word文件、电子表格等文档中的URL和链接注释。"

    # feature loop
    - title: "支持网络和嵌入链接"
      content: "检测并提取多种格式中的标准网页URL和嵌入文档链接。"

    # feature loop
    - title: "灵活的解析选项"
      content: "自定义提取设置以扫描特定部分或页面，以提高性能和准确性。"
      
  code_samples:
    # code sample loop
    - title: "如何使用链接选项从PDF提取超链接"
      content: |
        本代码示例展示了如何使用自定义选项从PDF文件中提取所有超链接。
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  用PDF文档初始化Parser
        using (Parser parser = new Parser("input.docx"))
        {
            // 检查是否支持超链接提取
            if (!parser.Features.Hyperlinks)
            {
                return;
            }

            // 设置链接提取选项以缩小结果范围
            PageAreaOptions options = new PageAreaOptions(new Rectangle(new Point(380, 90), new Size(150, 50)));

            // 从文档中提取超链接数据
            IEnumerable<PageHyperlinkArea> hyperlinks = parser.GetHyperlinks(options);

            // 处理提取的链接列表
            foreach (PageHyperlinkArea h in hyperlinks)
            {
                Console.WriteLine(h.Text);
                Console.WriteLine(h.Url);
            }
        }
        ```
        {{< /landing/code >}}


############################# Actions ############################

actions:
  enable: true
  title: "准备好开始了吗？"
  description: "免费试用 GroupDocs.Parser 功能或请求许可证"
  items:
    #  loop
    - title: "Nuget 下载"
      link: "https://releases.groupdocs.com/parser/net/"
      color: "red"
        #  loop
    - title: "许可信息"
      link: "https://purchase.groupdocs.com/pricing/parser/net/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "支持的超链接提取格式"
    exclude: "TXT"
    description: "GroupDocs.Parser可以从多种文档类型中提取超链接。请查看下面常见的支持格式。"
    items: 
        # format loop 1
        - name: "解析 PDF"
          format: "PDF"
          link: "/parser/net/extract-hyperlink/pdf/"
          description: "(可移植文档格式)"
          
        # format loop 2
        - name: "解析 DOCX"
          format: "DOCX"
          link: "/parser/net/extract-hyperlink/docx/"
          description: "(Office 2007+ Word 文档)"
          
        # format loop 3
        - name: "解析 PPTX"
          format: "PPTX"
          link: "/parser/net/extract-hyperlink/pptx/"
          description: "(Open XML 演示格式)"
          
        # format loop 4
        - name: "解析 XLSX"
          format: "XLSX"
          link: "/parser/net/extract-hyperlink/xlsx/"
          description: "(Open XML 工作簿)"
          
        # format loop 5
        - name: "解析 TXT"
          format: "TXT"
          link: "/parser/net/extract-hyperlink/txt/"
          description: "(文本文件)"
          
        # format loop 6
        - name: "解析 RTF"
          format: "RTF"
          link: "/parser/net/extract-hyperlink/rtf/"
          description: "(富文本格式)"
          
        # format loop 7
        - name: "解析 XML"
          format: "XML"
          link: "/parser/net/extract-hyperlink/xml/"
          description: "(可扩展标记语言)"
          
        # format loop 8
        - name: "解析 EPUB"
          format: "EPUB"
          link: "/parser/net/extract-hyperlink/epub/"
          description: "(开放电子书文件)"
         
          

---