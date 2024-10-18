from pypdf import PdfReader
from pathlib import Path
from PIL import Image
import pytesseract
import os
from docx import Document


def pdf_extract(pdf_path):
    """ This function extracts the text from a PDF file and returns the content in a string.

    Args:
        pdf_path(str): Path to the PDF file that is to be converted"""
    name = Path(pdf_path).name

    try:
        content = PdfReader(pdf_path)
        text = ""
        for page in content.pages:
            text += page.extract_text() + "\n"

        print(f"Successfully extracted text from {name}!")
        return text

    except Exception as e:
        print(f"Error extracting text from {name}: {e}")


def image_extract(img_path):
    """This function extracts the text from an image file (.jpeg, .png, .tiff, .gif, .bmp etc.) and
    returns the content in a string.

     Args:
        img_path(str): Path to the Image file that is to be converted."""

    name = Path(img_path).name

    try:
        image = Image.open(img_path)
        text = pytesseract.image_to_string(image)

        print(f"Successfully extracted text from {name}!")
        return text

    except Exception as e:
        print(f"Error extracting text from {name}: {e}")


def docx_extract(word_file_path):
    """This function extracts the text from a Word file (.docx) and
       returns the content in a string.

        Args:
           word_file_path(str): Path to the Word file that is to be converted."""

    name = Path(word_file_path).name

    try:
        text = ""
        document = Document(word_file_path)

        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"

            print(f"Successfully extracted text from {name}!")
            return text

    except Exception as e:
        print(f"Error extracting text from {name}: {e}")


def txt_extract(txt_file_path):
    """This function extracts the text from a text file (.txt) and
       returns the content in a string.

        Args:
           txt_file_path(str): Path to the Word file that is to be converted."""

    name = Path(txt_file_path).name

    try:
        with open(txt_file_path, "r") as file:
            text = file.read()

            print(f"Successfully extracted text from {name}!")
            return text

    except Exception as e:
        print(f"Error extracting text from {name}: {e}")


def excel_extract():
    pass


current_dir = os.path.dirname(os.path.abspath(__file__))

files_dict = {}

for filename in os.listdir(current_dir):

    if filename.endswith(".pdf"):
        pdf_path = os.path.join(current_dir, filename)
        pdf_text = pdf_extract(pdf_path)
        if pdf_text:
            files_dict[filename] = pdf_text

    elif filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".tiff") or filename.endswith(
            ".bmp"):
        image_path = os.path.join(current_dir, filename)
        image_text = image_extract(image_path)
        if image_text:
            files_dict[filename] = image_text

    elif filename.endswith(".txt"):
        txt_path = os.path.join(current_dir, filename)
        txt_text = txt_extract(txt_path)
        if txt_text:
            files_dict[filename] = txt_text

    elif filename.endswith(".docx"):
        docx_path = os.path.join(current_dir, filename)
        docx_text = docx_extract(docx_path)
        if docx_text:
            files_dict[filename] = docx_text

    elif filename.endswith(".xls"):
        excel_extract()

    else:
        print("Unfortunately this file format is not supported. Please try again with a PDF,"
              " image (.jpg, .png, .giff etc), Excel or Word file.")

print(files_dict)
