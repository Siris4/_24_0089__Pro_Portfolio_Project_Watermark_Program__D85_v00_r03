import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def load_image():
    file_path = filedialog.askopenfilename(
    filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")]
    )
    if file_path:
        # loads the image using Pillow:
        img = Image.open(file_path)
        img.thumbnail((300, 300))  #resizing for the display
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk)  #displays image in a label
        image_label.image = img_tk  #keeps reference to avoid garbage collection


root = tk.Tk()
root.title("Siris Image Loader")

# label to display the image:
image_label = tk.Label(root)
image_label.pack()

# button to load the image:
load_button = tk.Button(root, text="Load Image", command=load_image)
load_button.pack

root.mainloop()