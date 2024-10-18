import pytesseract
from PIL import Image
import tkinter as tk
from tkinter import Text, messagebox
import os

# Specify the Tesseract path (Windows-specific)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this if your path is different

# Absolute path of the input image (ensure this is correct)
image_path = r"C:\Users\320264203\OneDrive - Philips\Documents\ocr\image.jfif"  # Ensure the file name and path are correct

# Function to read text from an image
def extract_text_from_image(image_path):
    print("Checking if image exists at:", image_path)  # Debugging statement
    if not os.path.exists(image_path):
        return "Image file not found. Please check the path."
    
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        print("Extracted Text:", text)  # Debugging statement
        return text
    except Exception as e:
        return f"Error: {str(e)}"

# Function to display extracted text
def display_image_text():
    text = extract_text_from_image(image_path)
    display_text.delete(1.0, tk.END)  # Clear previous text
    display_text.insert(tk.END, text)  # Insert extracted text
    if "not found" in text or "Error:" in text:
        messagebox.showerror("Error", text)

# Create the Tkinter window
root = tk.Tk()
root.title("Image to Text Converter")
root.geometry("600x400")

# Button to display text from image
load_button = tk.Button(root, text="Display Text from Image", command=display_image_text)
load_button.pack(pady=10)

# Text widget to display extracted text
display_text = Text(root, wrap=tk.WORD, font=("Helvetica", 12))
display_text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
