from docx import Document

def get_word_count(docx_path):
    doc = Document(docx_path)
    text = "\n".join([p.text for p in doc.paragraphs])
    words = text.split()          # Simple split by whitespace
    return len(words), text

# Usage
count, extracted_text = get_word_count("textboxes.docx")
print(f"Total words: {count}")
print("\n--- Extracted Text ---")
print(extracted_text)