import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

def load_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")]
    )
    if file_path:
        global base_image
        base_image = Image.open(file_path).convert("RGBA")  # Ensure we use RGBA for transparency
        base_image.thumbnail((300, 300))  # resizing for display
        img_tk = ImageTk.PhotoImage(base_image)
        image_label.config(image=img_tk)
        image_label.image = img_tk

def load_watermark():
    file_path = filedialog.askopenfilename(
        filetypes=[("PNG files", "*.png")]
    )
    if file_path:
        global watermark_image
        watermark_image = Image.open(file_path).convert("RGBA")  # Load PNG with transparency
        apply_watermark()

def apply_watermark():
    if base_image and watermark_image:
        # Make a copy of the base image
        img_with_watermark = base_image.copy()

        # Get the opacity from the slider (scale from 0 to 255)
        opacity = int(opacity_slider.get() * 2.55)  # Convert to 0-255 range

        # Resize watermark to fit on the base image
        watermark_resized = watermark_image.resize(img_with_watermark.size, Image.ANTIALIAS)

        # Adjust watermark opacity
        watermark_with_opacity = watermark_resized.copy()
        alpha = watermark_with_opacity.split()[3]  # Get the alpha channel
        alpha = alpha.point(lambda p: p * (opacity / 255))  # Apply opacity
        watermark_with_opacity.putalpha(alpha)

        # Composite watermark on top of the base image
        img_with_watermark.paste(watermark_with_opacity, (0, 0), watermark_with_opacity)

        # Display the image with watermark
        img_tk = ImageTk.PhotoImage(img_with_watermark)
        image_label.config(image=img_tk)
        image_label.image = img_tk

# Initialize the tkinter window
root = tk.Tk()
root.title("Siris Image Loader and Watermark")

# Set the initial size of the window (width x height)
root.geometry("400x500")

# Label to display the image
image_label = tk.Label(root)
image_label.pack()

# Button to load the image
load_button = tk.Button(root, text="Load Image", command=load_image)
load_button.pack(pady=10)

# Button to load the watermark
watermark_button = tk.Button(root, text="Load Watermark", command=load_watermark)
watermark_button.pack(pady=10)

# Opacity slider
opacity_slider = tk.Scale(root, from_=0, to=100, orient="horizontal", label="Opacity")
opacity_slider.pack(pady=10)

# Variables to hold images
base_image = None
watermark_image = None

# Start the main loop
root.mainloop()
