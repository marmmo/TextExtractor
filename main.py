from pypdf import PdfReader
from pathlib import Path
from PIL import Image
import pytesseract
import os
from docx import Document
from openpyxl import load_workbook
import pandas as pd


# This function could further be improved to support PDF files with multiple columns and different orientations
def extract_pdf(pdf_path):
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


# This function could further be improved by pre-processing images in order for the text to be more accurately recognised
def extract_image(img_path):
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


def extract_docx(word_file_path):
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


def extract_txt(txt_file_path):
    """This function extracts the text from a text file (.txt) and
       returns the content in a string.

        Args:
           txt_file_path(str): Path to the Word file that is to be converted."""

    name = Path(txt_file_path).name

    try:
        with open(txt_file_path, "r") as file:
            text = file.readlines()

            print(f"Successfully extracted text from {name}!")
            return text

    except Exception as e:
        print(f"Error extracting text from {name}: {e}")


def extract_excel(excel_path):
    """ This function extracts the text from an Excel file (.xlsx, .xlsm, .xltx, .xltm) and returns the content
    as list of lists of strings. Each row is represented by a list of strings that contain the cell values.

        Args:
            pdf_path(str): Path to the PDF file that is to be converted"""

    name = Path(excel_path).name

    try:
        workbook = load_workbook(excel_path)
        sheets = workbook.sheetnames

        data = []

        for sheet in sheets:
            current_sheet = workbook[sheet]
            for row in current_sheet.iter_rows(values_only=True):
                row_data = [str(cell) if cell is not None else " " for cell in row]
                data.append(row_data)

        return data

    except Exception as e:
        print(f"Error extracting text from {name}: {e}")


def extract_csv(csv_path):

    name = Path(csv_path).name

    try:
        db = pd.read_csv(csv_path)

        data = []

        for row in db.iterrows():
            row_data = [str(cell) if cell is not None else " " for cell in row]
            data.append(row_data)

        return data

    except Exception as e:
        print(f"Error extracting text from {name}: {e}")



current_dir = os.path.dirname(os.path.abspath(__file__))

files_dict = {}

for filename in os.listdir(current_dir):

    if filename.endswith(".pdf"):
        pdf_path = os.path.join(current_dir, filename)
        pdf_text = extract_pdf(pdf_path)
        if pdf_text:
            files_dict[filename] = pdf_text

    elif (filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".tiff") or
          filename.endswith(".bmp")):
        image_path = os.path.join(current_dir, filename)
        image_text = extract_image(image_path)
        if image_text:
            files_dict[filename] = image_text

    elif filename.endswith(".txt"):
        txt_path = os.path.join(current_dir, filename)
        txt_text = extract_txt(txt_path)
        if txt_text:
            files_dict[filename] = txt_text

    elif filename.endswith(".docx"):
        docx_path = os.path.join(current_dir, filename)
        docx_text = extract_docx(docx_path)
        if docx_text:
            files_dict[filename] = docx_text

    elif (filename.endswith(".xlsx") or filename.endswith(".xlsm") or
          filename.endswith(".xltx") or filename.endswith(".xltm")):
        excel_path = os.path.join(current_dir, filename)
        excel_text = extract_excel(excel_path)
        if excel_text:
            files_dict[filename] = excel_text

    elif filename.endswith(".csv"):
        csv_path = os.path.join(current_dir, filename)
        csv_text = extract_csv(csv_path)
        if csv_text:
            files_dict[filename] = csv_text

    else:
        print(f"Unfortunately the file format for {filename} is not supported. Please try again with a PDF,"
              " image (.jpg, .png, .giff etc), Excel or Word file.")

print(files_dict)
