from PyPDF2 import PdfReader, PdfWriter
from tkinter import Tk, filedialog
import os

def split_pdf(path, name_of_split):
    pdf = PdfReader(path)
    
    for page_num in range(len(pdf.pages)):  # Obter o número total de páginas
        pdf_writer = PdfWriter()
        pdf_writer.add_page(pdf.pages[page_num])

        output = f'{name_of_split}{page_num + 1}.pdf'
        with open(output, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

def select_file():
    root = Tk()
    root.withdraw()  # Ocultar a janela principal
    file_path = filedialog.askopenfilename(title="Selecionar arquivo PDF")
    return file_path

def select_output_directory():
    root = Tk()
    root.withdraw()  # Ocultar a janela principal
    directory = filedialog.askdirectory(title="Selecionar diretório para salvar PDFs divididos")
    return directory

def main():
    input_path = select_file()
    if input_path:
        output_directory = select_output_directory()
        if output_directory:
            # Altere o diretório de trabalho para onde os PDFs divididos serão salvos
            os.chdir(output_directory)
            name_of_split = os.path.join(output_directory, 'page_')
            split_pdf(input_path, name_of_split)
            print(f"PDF dividido e salvo em {output_directory}")
        else:
            print("Operação de salvar cancelada.")
    else:
        print("Nenhum arquivo PDF selecionado.")

if __name__ == "__main__":
    main()
