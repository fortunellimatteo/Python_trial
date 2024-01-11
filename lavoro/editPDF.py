from PyPDF4 import PdfFileWriter, PdfFileReader

originalfile = "C:\\Users\\mfortunelli\\my_ipfabric\\Input.pdf"
watermark = "C:\\Users\\mfortunelli\\my_ipfabric\\Image.pdf"
watermarkedfile = "C:\\Users\\mfortunelli\\my_ipfabric\\Output.pdf"

watermark = PdfFileReader(watermark)
watermarkpage = watermark.getPage(0)
pdf = PdfFileReader(originalfile)
pdfwrite = PdfFileWriter()
for page in range(pdf.getNumPages()):
    pdfpage = pdf.getPage(page)
    pdfpage.mergePage(watermarkpage)
    pdfwrite.addPage(pdfpage)
with open(watermarkedfile, 'wb') as fh:
    pdfwrite.write(fh)