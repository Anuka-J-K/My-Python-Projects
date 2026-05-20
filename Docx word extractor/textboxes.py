import win32com.client

def get_textbox_text_simple(docx_path):
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    doc = word.Documents.Open(docx_path)
    
    text = ""
    for shape in doc.Shapes:
        if shape.Type == 17:  # msoTextBox
            if shape.TextFrame.HasText:
                text += shape.TextFrame.TextRange.Text + "\n"
    
    doc.Close()
    word.Quit()
    return text

# Usage
text = get_textbox_text_simple("textboxes.docx")
print(text)