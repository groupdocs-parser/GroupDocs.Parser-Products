<% configRef "..\\configs\\table\\format_net.yml" %>
<% include "..\\data\\format_data.md" %>

---
############################# Static ############################
layout: "format"
date:  <% date "utcnow" %>
draft: false
lang: <% lower ( get "lang") %>
format: <% get "FileformatCap" %>
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "<% (dict "head.title") %>"
head_description: "<% (dict "head.description") %>"

############################# Header ############################
title: "<% (dict "header.title") %>" 
description: "<% (dict "header.description") %>"
subtitle: "<% (dict "header.subtitle") %>" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "<% (dict "header.action_title") %>"
      link: "<% get "ReleaseDownloads" %>"
      
############################# About ############################
about:
    enable: true
    title: "<% (dict "about.title") %>"
    link: "/parser/<% get "ProdCode" %>/"
    link_title: "<% "{common-content.texts.learn_more}" %>"
    picture: "about_parser.svg" # 480 X 400
    content: |
       <% (dict "about.content") %>

############################# Steps ############################
steps:
    enable: true
    title: "<% "{steps.title}" %>"
    content: |
      <% "{steps.content.title}" %>
      
      1. <% "{steps.content.step_1}" %>
      2. <% "{steps.content.step_2}" %>
      3. <% "{steps.content.step_3}" %>
      4. <% "{steps.content.step_4}" %>
   
    code:
      platform: "net"
      copy_title: "<% "{common-content.format-code.copy_title}" %>"
      install:
        command: |
        command: "dotnet add package GroupDocs.Parser"
        copy_tip: "<% "{common-content.format-code.copy_tip}" %>"
        copy_done: "<% "{common-content.format-code.copy_done}" %>"
      links:
        #  loop
        - title: "<% "{common-content.format-code.links.title_1}" %>"
          link: "<% get "MoreLink" %>"
        #  loop
        - title: "<% "{common-content.format-code.links.title_2}" %>"
          link: "<% get "DocsUrl" %>"
          
      content: |
        ```csharp {style=abap}
        // <% "{examples.comment_1}" %>
        using (Parser parser = new Parser("input.<% get "fileformat" %>")) {

            // <% "{examples.comment_2}" %>
            if (!parser.Features.Tables) {
                Console.WriteLine("<% "{examples.comment_3}" %>");
                return;
            }

            // <% "{examples.comment_4}" %>
            TemplateTableLayout layout = new TemplateTableLayout(
                new double[] { 50, 95, 275, 415, 485, 545 },
                new double[] { 325, 340, 365, 395 });

            // <% "{examples.comment_5}" %>
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            //  <% "{examples.comment_6}" %>
            IEnumerable<PageTableArea> tables = parser.GetTables(options);

            //  <% "{examples.comment_7}" %>
            foreach (PageTableArea t in tables)
            {
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "<% "{more_features.title}" %>"
  description: "<% "{more_features.description}" %>"
  image: "/img/parser/features_extract-table.webp" # 500x500 px
  image_description: "<% "{more_features.image_description}" %>"
  features:
    # feature loop
    - title: "<% "{more_features.feature_1.title}" %>"
      content: "<% "{more_features.feature_1.content}" %>"

    # feature loop
    - title: "<% "{more_features.feature_2.title}" %>"
      content: "<% "{more_features.feature_2.content}" %>"

    # feature loop
    - title: "<% "{more_features.feature_3.title}" %>"
      content: "<% "{more_features.feature_3.content}" %>"
      
  code_samples:
    # code sample loop
    - title: "<% "{more_features.code_1.title}" %>"
      content: |
        <% "{more_features.code_1.content}" %>
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  <% "{more_features.code_1.comment_1}" %>
        using (Parser parser = new Parser("input.xlsx"))
        {
            // <% "{more_features.code_1.comment_2}" %>
            if (!parser.Features.Tables)
            {
                return;
            }

            // <% "{more_features.code_1.comment_3}" %>
            TemplateTableLayout layout = new TemplateTableLayout(
                    new double[] { 50, 95, 275, 415, 485, 545 },
                    new double[] { 325, 340, 365, 395 });

            // <% "{more_features.code_1.comment_4}" %>
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            // <% "{more_features.code_1.comment_5}" %>
            IEnumerable<PageTableArea> tables = parser.GetTables(options);

            // <% "{more_features.code_1.comment_6}" %>
            foreach (PageTableArea t in tables)
            {
                // <% "{more_features.code_1.comment_7}" %>
                for (int row = 0; row < t.RowCount; row++)
                {
                    // <% "{more_features.code_1.comment_8}" %>
                    for (int column = 0; column < t.ColumnCount; column++)
                    {
                        // <% "{more_features.code_1.comment_9}" %>
                        PageTableAreaCell cell = t[row, column];
                        if (cell != null)
                        {
                            // <% "{more_features.code_1.comment_10}" %>
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
  title: "<% "{common-content.format-actions.title}" %>"
  description: "<% "{common-content.format-actions.description}" %>"
  items:
    #  loop
    - title: "<% "{common-content.format-actions.comment_1}" %>"
      link: "<% get "ReleaseDownloads" %>"
      color: "red"
        #  loop
    - title: "<% "{common-content.format-actions.comment_2}" %>"
      link: "<% get "PricesUrl" %>"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "<% (dict "formats.title") %>"
    exclude: "<% get "FileFormatUp" %>"
    description: "<% (dict "formats.description") %>"
<% include "..\\data\\format_others.md" %>

---