# 📄 Image to PDF Converter

A simple image-to-PDF converter built with Python.

## 🚀 Features

✅ Convert one or multiple images into a PDF file.  
✅ Supports common image formats (JPEG, PNG, etc.).  
✅ Easy to use via command line.  
✅ Tested with `unittest` for reliability.

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-repo/img_to_pdf_converter.git
cd img_to_pdf_converter
```

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv env
source env/bin/activate  # Mac/Linux
env\Scripts\activate     # Windows
```

### 3️⃣ Install dependencies

```bash
pip install
```

## 🛠️ Usage

### 4️⃣ Use the tool

To convert one or more images into a PDF, you can use the provided run_converter.py script.

**Convert a single image to PDF:**

```bash
python run_converter.py image.jpg output.pdf
```

**Convert multiple images into a single PDF:**

```bash
python run_converter.py "image1.jpg image2.png image3.jpeg" output.pdf
```

**Run tests:**

```bash
python run_tests.py
```

## 📁 Project Structure

```bash
img_to_pdf_converter/
├── converter.py         # Core logic for image to PDF conversion
├── main.py              # Main script for user interaction
├── run_converter.py     # Script to execute conversion
├── run_tests.py         # Script to run tests
├── tests/
│   └── test_converter.py # Unit tests
├── requirements.txt     # Dependencies list
├── README.md            # Project documentation
```
