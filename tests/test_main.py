import unittest
from main import extract_txt, extract_image, extract_pdf, extract_docx


class TestExtractors(unittest.TestCase):
    def test_extract_txt(self):
        result = extract_txt("test_files/Quote of the day.txt")
        self.assertEqual(result, ["There is nothing permanent except change. - Heraclitus"])

    def test_extract_image(self):
        result = extract_image("test_files/quote-image.png")
        self.assertEqual(result, "#Lifeism\n\nDo all\nthings\nwith\n\nkindness.\n")

    def test_extract_pdf(self):
        result = extract_pdf("test_files/pdf-test.pdf")
        self.assertEqual(result, " \n  \n   \nThis is a test PDF document. \nIf you can read this,"
                                 " you have Adobe Acrobat Reader installed on your computer. \n")


if __name__ == '__main__':
    unittest.main()
