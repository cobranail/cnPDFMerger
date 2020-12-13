import sys
from PyPDF2 import PdfFileReader, PdfFileWriter

def merge_pdfs(pdf1, rev1, pdf2, rev2, mode, output):
    pdf_writer = PdfFileWriter()
    pdf1_reader = PdfFileReader(pdf1)
    pdf2_reader = PdfFileReader(pdf2)
    pdf1_pages=list(range(pdf1_reader.getNumPages()))
    pdf2_pages=list(range(pdf2_reader.getNumPages()))
    if rev1:
        pdf1_pages.reverse()
    if rev2:
        pdf2_pages.reverse()
    if mode==0:
        for i in range(max(len(pdf1_pages), len(pdf2_pages))):
            if i < len(pdf1_pages):
                pdf_writer.addPage(pdf1_reader.getPage(pdf1_pages[i]))
            if i < len(pdf2_pages):
                pdf_writer.addPage(pdf2_reader.getPage(pdf2_pages[i]))
    if mode==1:
        for i in range(len(pdf1_pages)):
            if i < len(pdf1_pages):
                pdf_writer.addPage(pdf1_reader.getPage(pdf1_pages[i]))
        for i in range(len(pdf1_pages)):
            if i < len(pdf2_pages):
                pdf_writer.addPage(pdf2_reader.getPage(pdf2_pages[i]))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)

if __name__ == '__main__':
    paths = [sys.argv[1], sys.argv[2]]
    merge_pdfs(paths, output=sys.argv[3])