# Image to Text Converter

This project is an **Image to Text Converter** application built using Python, Tkinter, and Tesseract OCR. It allows users to extract text from images (in JFIF format) through a simple graphical user interface (GUI).

## Features

- **Extract text** from JFIF images using Optical Character Recognition (OCR).
- **User-friendly GUI** to display the extracted text.
- **Easy setup** and installation.

## Requirements

- Python **3.x**
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed on your machine
- Python packages:
  - `pytesseract`
  - `Pillow`
  - `tkinter` (included with Python)

## Installation

1. **Clone the repository:**

- git clone https://github.com/your-username/image-to-text-converter.git
- cd image-to-text-converter
   
2. **Install the required packages:**

You can install the necessary Python packages using pip:
- pip install pytesseract Pillow
- Install Tesseract OCR:
- Download and install Tesseract OCR from the official repository.
- Add Tesseract to your system's PATH, or specify the installation path in the code (line 5 in main.py).

## Usage

1. Run the application:
- python main.py
- Click on the "Display Text from Image" button to extract text from the specified image.
- Ensure that the image path in the code is correctly set to the location of your JFIF image.
