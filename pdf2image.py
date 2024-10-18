from PIL import Image
import pytesseract
from pdf2image import convert_from_path
from pathlib import Path
import os

def pdf_convert(pdf_path):
    """This function takes all the PDF files in a directory and converts their pages into JPEG files that are stored
    into an automatically created directory with the same name as the initial file

    Args:
        pdf_path(str): Path to the PDF file that is to be converted"""

    name = Path(pdf_path).name
    pdf_dir = os.path.dirname(os.path.abspath(__file__))

    output_dir = f"{pdf_dir}/{name[:-4]}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        pages = convert_from_path(pdf_path)
        for i in range(len(pages)):
            pages[i].save(f"{output_dir}/page"+str(i)+".jpg", "JPEG")
        print(f"Successfully converted {name} to {name[:-4]}.jpg.")
        return pages

    except Exception as e:
        print(f"Error converting {pdf_path}: {e}")

def text_extract(pages):
    pass

def combine_text(pages):
    pass


