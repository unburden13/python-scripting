import PyPDF2
import sys

with open('./files/dummy.pdf', 'rb') as file:  # rb: read binary, so the pdf reader can read it
    reader = PyPDF2.PdfReader(file)
    print(len(reader.pages))
    page = reader.pages[0]
    page.rotate(90)
    writer = PyPDF2.PdfWriter()
    writer.add_page(page)
    with open('./files/rotated.pdf', 'wb') as new_file:
        writer.write(new_file)


inputs = sys.argv[1:]
def pdf_combiner(pdf_list):  # exec: python pdf_processor.py dummy.pdf rotated.pdf twopage.pdf
    pdf_paths = list(map(lambda pdf_file: f'./files/{pdf_file}', pdf_list))
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_paths:
        merger.append(pdf)
    merger.write('./files/merged_files.pdf')


def add_watermark():
    pdf_file = './files/merged_files.pdf'
    watermark = './files/wtr.pdf'
    merged = './files/merged_files_watermark.pdf'

    with open(pdf_file, 'rb') as input_file, open(watermark, 'rb') as watermark_file:
        input_pdf = PyPDF2.PdfReader(input_file)
        watermark_pdf = PyPDF2.PdfReader(watermark_file)
        watermark_page = watermark_pdf.pages[0]

        output = PyPDF2.PdfWriter()

        for i in range(len(input_pdf.pages)):
            pdf_page = input_pdf.pages[i]
            pdf_page.merge_page(watermark_page)
            output.add_page(pdf_page)

        with open(merged, 'wb') as merged_file:
            output.write(merged_file)


add_watermark()

