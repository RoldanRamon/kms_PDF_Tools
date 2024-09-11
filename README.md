# 📝 PDF Tools

🚀 **PDF Tools** is a Python project that provides a user-friendly graphical interface to perform various operations on PDF files, such as conversion, merging, splitting, and rotation. It runs locally, ensuring information security, and is compatible with Windows, Linux, and Mac.

## 🛠️ Features

- 🔄 **Convert PDF to Word**: Easily convert PDF files to DOCX format using the `pdf2docx` library.
- 🔄 **Rotate PDFs**: Change the orientation of PDF pages.
- ➕ **Merge PDFs**: Combine multiple PDF files into one document.
- ➖ **Split PDF**: Split a PDF into several files.
- 🔒 **Security**: Since the process runs locally, your files never leave your computer.

## 📋 Requirements

- 🐍 Python 3.x
- 📦 Required libraries:
  - `pdf2docx`
  - `tkinter` (usually included in the standard Python installation)

## 🔧 Installation

1. ✅ Make sure you have Python installed on your system. You can download and install Python from [python.org](https://www.python.org/).
  
2. 📥 Install the required dependencies using `pip`:
    ```bash
    pip install pdf2docx
    ```

## 🚀 How to Use

1. 📁 Clone this repository to your computer or download the ZIP file and extract it.

2. 📂 Navigate to the project directory.

3. ▶️ Run the `app.py` script:
    ```bash
    python app.py
    ```

4. 🖱️ A window will appear with the following options:
    - **Convert PDF to Word**: Select the PDF file to convert it to DOCX.
    - **Rotate PDF**: Select the PDF and the rotation angle (90, 180, 270 degrees).
    - **Merge PDFs**: Select multiple PDF files to merge them into one.
    - **Split PDF**: Select the PDF and define the pages to split.

5. ⏳ Wait for the process to complete, and the files will be saved in the same directory as the source file.

## 🌐 Compatibility

This project runs on:
- Windows
- Linux
- MacOS

As long as Python and the required libraries are installed.

## 🤝 Contributions

Contributions are welcome! Feel free to open an issue to report bugs 🐛 or request new features ✨. If you'd like to contribute code, please open a pull request 🚀.

## 📜 License

This project is licensed under the [MIT License](LICENSE).
