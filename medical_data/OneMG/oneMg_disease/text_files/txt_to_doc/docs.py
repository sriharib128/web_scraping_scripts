from docx import Document
import os
import fileinput

def txt_to_docx(input_txt, output_docx):
    document = Document()
    with open(input_txt, 'r') as txt_file:
        text = txt_file.read()
        document.add_paragraph(text)
    document.save(output_docx)

if __name__ == "__main__":
    input_txt_file = "corpus_telugu.txt"  # Replace with your input.txt file
    output_docx_file = f'corpus_telugu.docx'  # Replace with desired output.docx file
    txt_to_docx(input_txt_file, output_docx_file)
    
