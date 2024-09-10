pyinstaller --onefile --hidden-import PyPDF2 --hidden-import PIL --hidden-import pdf2docx --hidden-import tkinter --add-data "Images;Images" -i "Images/pdf.ico" Functions/app.py
