import pytesseract
from PyPDF2 import PdfFileMerger
from pdf2image import convert_from_path

GIRDI_DOSYA_ADI = "ornek.pdf"
CIKTI_DOSYA_ADI = "cikti.pdf"
SAYFA_SAYISI = 0


def pdfToJPG(ilkGirdiPDF):
    # Store Pdf with convert_from_path function
    images = convert_from_path(ilkGirdiPDF)
    SAYFA_SAYISI = len(images)
    for i in range(1,len(images)+1):
        # Save pages as images in the pdf
        images[i-1].save(str(i).zfill(4) + '.jpg', 'JPEG')


def jpgToPDF():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    for dosya in dosya_adlari:
        pdf = pytesseract.image_to_pdf_or_hocr(dosya,lang="tur")
        with open(dosya+'.pdf', 'w+b') as f:
            f.write(pdf)

def mergePDF(cikti):
    pdfs = [file+".pdf" for file in dosya_adlari]
    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(pdf)
    merger.write(cikti)
    merger.close()

print("Converting and divorcing to JPG parts")
pdfToJPG(GIRDI_DOSYA_ADI)
dosya_adlari = [str(i).zfill(4)+".jpg" for i in range(1,SAYFA_SAYISI+1)]
print("Converting JPGs to PDFs")
jpgToPDF()
print("Merging PDFs to one PDF")
mergePDF(CIKTI_DOSYA_ADI)
print("DONE!!!")