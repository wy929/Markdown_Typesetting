# Markdown_Typesetting
A script to beautify the layout of markdown files

## What can be done?

1. Add anchors to your headers for cross-referencing, and change the font.

   Before:

   ```markdown
   # Title1
   
   ## Title1.1
   
   # Title2
   ```

   After:

   ```markdown
   # <a name="t1"><font face="Times New Roman">Title1</font></a>
   
   ## <a name="t1.1"><font face="Times New Roman">Title1.1</font></a>
   
   # <a name="t2"><font face="Times New Roman">Title2</font></a>
   ```

   Use the following code as a template to build reference anchors.

   ```markdown
   <a href="#t1">Title1</a>
   ```

2. Adding footnotes to charts

   Please label your chart names as written in the example.

   Before:

   ```markdown
   <FIG> my figure 1
   
   <TAB> my table 1
   ```

   After:

   ```markdown
   <center style="color:#C0C0C0;text-decoration:underline"><font face="Cambria"><a name="fig1.1">Figure[1.1]</a>: my figure 1</font></center>
   
   <center style="color:#C0C0C0;text-decoration:underline"><font face="Cambria"><a name="tab1.1">Table[1.1]</a>: my table 1</font></center>
   ```

3. Modify the font of the body text.

   Before:

   ```
   Alice
   ```

   After:

   ```markdown
   <font face="Cambria">Alice</font>
   ```

## How to use

Using the `main.py` to convert your markdown file.







