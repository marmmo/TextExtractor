from pypdf import PdfReader
from pathlib import Path
from PIL import Image
import pytesseract
import os


def pdf_extract(pdf_path):
    """ This function extracts the text from a PDF file and returns the content in a dictionary
    with the file name and the extracted text.

    Args:
        pdf_path(str): Path to the PDF file that is to be converted"""
    try:
        content = PdfReader(pdf_path)
        text = ""
        for page in content.pages:
            text += page.extract_text() + "\n"

        name = Path(pdf_path).name

        print(f"Successfully extracted text from {name}!")
        return {"document": {name}, "content": {text}}

    except Exception as e:
        print(f"Error extracting text from {name}: {e}")


def image_extract(img_path):
    """This function extracts the text from an image file (.jpeg, .png, .tiff, .gif, .bmp etc.) and
    returns a dictionary containing the file name and the extracted text.

     Args:
        img_path(str): Path to the PDF file that is to be converted."""

    try:
        image = Image.open(img_path)
        text = pytesseract.image_to_string(image)

        name = Path(img_path).name

        print(f"Successfully extracted text from {name}!")
        return {"document": {name}, "content": {text}}

    except Exception as e:
        print(f"Error extracting text from {name}: {e}")


def excel_extract():
    pass

def text_file_extract():
    pass


current_dir = os.path.dirname(os.path.abspath(__file__))

for filename in current_dir:
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(current_dir, filename)
        pdf_extract(pdf_path)
    elif filename.endswith(".jpg", ".png", ".tiff", ".bmp"):
        image_extract()
    elif filename.endswith(".docx", ".txt", ".pages"):
        text_file_extract()
    elif filename.endswith(".xls"):
        excel_extract()
    else:
        print("Unfortunately this file format is not supported. Please try again with a PDF,"
              " image (.jpg, .png, .giff etc), Excel or Word file.")



