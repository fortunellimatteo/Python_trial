from PyPDF4 import PdfFileWriter, PdfFileReader
import sys

pdfIn=sys.argv[1]
timbroIn=sys.argv[2]

watermarkedfile = "C:\\Users\\mfortunelli\\my_ipfabric\\Output.pdf"
watermark = PdfFileReader(timbroIn)

watermarkpage = watermark.getPage(0)
pdf = PdfFileReader(pdfIn)
pdfwrite = PdfFileWriter()

for page in range(pdf.getNumPages()):
    pdfpage = pdf.getPage(page)
    pdfpage.mergePage(watermarkpage)
    pdfwrite.addPage(pdfpage)
with open(watermarkedfile, 'wb') as fh:
    pdfwrite.write(fh)