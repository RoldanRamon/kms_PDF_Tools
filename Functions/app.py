import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import os
import sys
from split_function import split_pdf  # Importando a função de divisão de PDF
from merge_function import merge_pdfs  # Importando a função de juntar PDFs
from rotate_function import rotate_pages  # Função de rotação de PDF
from convert_function import convert_pdf_to_word  # Função de conversão de PDF para Word

# Função para conversão de PDF para Word
def convert_rules():
    input_path = filedialog.askopenfilename(title="Selecionar arquivo PDF para converter", filetypes=[("PDF files", "*.pdf")])
    if input_path:
        try:
            convert_pdf_to_word(input_path)  # Passa apenas o caminho do PDF, conforme a função espera
            message.config(text=f"PDF convertido com sucesso: {input_path[:-3] + 'docx'}")
        except Exception as e:
            message.config(text=f"Erro ao converter o PDF: {e}")
    else:
        message.config(text="Nenhum arquivo PDF selecionado.")

# Função para dividir o PDF
def split_rules():
    input_path = filedialog.askopenfilename(title="Selecionar arquivo PDF")
    if input_path:
        output_directory = filedialog.askdirectory(title="Selecionar diretório para salvar PDFs divididos")
        if output_directory:
            try:
                split_pdf(input_path, os.path.join(output_directory, 'page_'))  # Chama a função split_pdf
                message.config(text=f"PDF dividido e salvo em: {output_directory}")
            except Exception as e:
                message.config(text=f"Erro ao dividir o PDF: {e}")
        else:
            message.config(text="Operação de salvar cancelada.")
    else:
        message.config(text="Nenhum arquivo PDF selecionado.")

# Função para juntar PDFs
def merge_rules():
    input_paths = filedialog.askopenfilenames(title="Selecionar arquivos PDF para juntar", filetypes=[("PDF Files", "*.pdf")])
    if input_paths:
        output_path = filedialog.asksaveasfilename(defaultextension=".pdf", title="Salvar como", filetypes=[("PDF Files", "*.pdf")])
        if output_path:
            try:
                merge_pdfs(output_path, input_paths)  # Passando output_path primeiro, depois input_paths
                message.config(text=f"PDFs juntados e salvos em: {output_path}")
            except Exception as e:
                message.config(text=f"Erro ao juntar os PDFs: {e}")
        else:
            message.config(text="Operação de salvar cancelada.")
    else:
        message.config(text="Nenhum arquivo PDF selecionado.")

# Função para rotacionar PDFs
def rotate_documents():
    input_path = filedialog.askopenfilename(title="Selecionar arquivo PDF para girar", filetypes=[("PDF Files", "*.pdf")])
    if input_path:
        output_path = filedialog.asksaveasfilename(defaultextension=".pdf", title="Salvar como", filetypes=[("PDF Files", "*.pdf")])
        if output_path:
            try:
                rotate_pages(input_path, output_path)  # Certifique-se de passar os argumentos corretamente
                message.config(text=f"PDF rotacionado e salvo em: {output_path}")
            except Exception as e:
                message.config(text=f"Erro ao rotacionar o PDF: {e}")
        else:
            message.config(text="Operação de salvar cancelada.")
    else:
        message.config(text="Nenhum arquivo PDF selecionado.")

# Função para carregar e redimensionar uma imagem
def load_image(file_name, width, height):
    # Determinar o caminho correto no ambiente de desenvolvimento ou executável
    if getattr(sys, 'frozen', False):
        # Se o aplicativo estiver empacotado, usamos o sys._MEIPASS para encontrar os arquivos
        base_path = sys._MEIPASS
    else:
        # No ambiente de desenvolvimento, usamos o caminho atual do sistema
        base_path = os.path.abspath(".")
    
    icon_path = os.path.join(base_path, 'Images', file_name)

    # Verifica se o arquivo de ícone existe
    if os.path.exists(icon_path):
        image = Image.open(icon_path)
        image = image.resize((width, height))
        return ImageTk.PhotoImage(image)
    else:
        messagebox.showerror("Erro", f"Arquivo não encontrado: {icon_path}")
        return None  # Retorna None caso o arquivo não exista

# Criando a janela principal
window = tk.Tk()
window.title('PDF Tools')

# Estilo para os botões
button_style = ttk.Style()
button_style.configure('Button.TButton', font=('Arial', 12, 'bold'))

# Frame para os botões superiores
upper_buttons_frame = tk.Frame(window)
upper_buttons_frame.pack()

# Frame para os botões inferiores
lower_buttons_frame = tk.Frame(window)
lower_buttons_frame.pack()

# Carregando ícones
convert_icon = load_image('word.ico', 30, 30)
merge_icon = load_image('merge.ico', 30, 30)
rotate_icon = load_image('rotate.ico', 30, 30)
split_icon = load_image('split.ico', 30, 30)

# Botão para Converter PDF para Word
convert_button = ttk.Button(upper_buttons_frame, text='PDF to Word', image=convert_icon, compound=tk.LEFT, command=convert_rules, style='Button.TButton')
convert_button.pack(side=tk.LEFT, padx=5, pady=5)

# Botão para Juntar PDFs
merge_button = ttk.Button(upper_buttons_frame, text='Merge', image=merge_icon, compound=tk.LEFT, command=merge_rules, style='Button.TButton')
merge_button.pack(side=tk.LEFT, padx=5, pady=5)

# Botão para Dividir PDFs (agora na parte inferior)
split_button = ttk.Button(lower_buttons_frame, text='Split', image=split_icon, compound=tk.LEFT, command=split_rules, style='Button.TButton')
split_button.pack(side=tk.LEFT, padx=5, pady=5)

# Botão para Rotacionar PDF
rotate_button = ttk.Button(lower_buttons_frame, text='Rotate 90º', image=rotate_icon, compound=tk.LEFT, command=rotate_documents, style='Button.TButton')
rotate_button.pack(side=tk.LEFT, padx=5, pady=5)

# Mensagem de feedback
message = tk.Label(window, text='')
message.pack()

# Executando o GUI
window.mainloop()
