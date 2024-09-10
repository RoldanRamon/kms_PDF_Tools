from PyPDF2 import PdfReader, PdfWriter
from tkinter import Tk, filedialog

def rotate_pages(pdf_path, output_path):
    pdf_writer = PdfWriter()
    pdf_reader = PdfReader(pdf_path)

    # Rotacionar todas as páginas 90 graus no sentido horário
    for page in pdf_reader.pages:
        rotated_page = page.rotate(-90)  # Rotacionar 90 graus no sentido horário
        pdf_writer.add_page(rotated_page)

    # Salvar o PDF rotacionado
    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh)

def select_file():
    root = Tk()
    root.withdraw()  # Ocultar a janela principal
    file_path = filedialog.askopenfilename(title="Selecionar arquivo PDF")
    return file_path

def select_output_path():
    root = Tk()
    root.withdraw()  # Ocultar a janela principal
    output_path = filedialog.asksaveasfilename(defaultextension=".pdf", title="Salvar como")
    return output_path

def main():
    input_path = select_file()
    if input_path:
        output_path = select_output_path()
        if output_path:
            rotate_pages(input_path, output_path)
            print("PDF rotacionado e salvo com sucesso em:", output_path)
        else:
            print("Operação de salvar cancelada.")
    else:
        print("Nenhum arquivo PDF selecionado.")

if __name__ == "__main__":
    main()
