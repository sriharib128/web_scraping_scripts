from docx import Document

# Read the content of the text file
with open('max_procedures.txt', 'r', encoding='utf-8') as file:
    text_content = file.read()

# Create a new Word document
doc = Document()

# Add the text content to the document
doc.add_paragraph(text_content[:len(text_content)//2])

# Save the document to a file
doc.save('output.docx')

print('Conversion completed successfully.')
