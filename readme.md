# What is this project about?
 This script contains goes through all the files in a directory, extracts the text from supported file types as string
 and returns it in a dictionary that had the filename as key and the string content as value.

Supported file types are: .pdf, .png, .jpg, .giff, .tiff , .bmp, .txt, .docx, .xlsx, .xlsm, .xltx, .xltm, .csv.

There is an additional function in a separate file that can be used to convert PDFs to image files (.jpg).

# How to run this project?

To run this project, we first install the dependencies

```shell
 pip install -r requirements.txt
```

Then we can run the project using the command 

```shell
python main.py
```
