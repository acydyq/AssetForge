import tkinter as tk
from tkinter import filedialog
import numpy_art

class AssetForgeUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AssetForge - Tech Startup Edition")
        self.root.geometry("800x600")

        # Label & Entry for description input
        self.description_label = tk.Label(root, text="Describe the Asset:")
        self.description_label.pack()
        self.description_entry = tk.Entry(root, width=50)
        self.description_entry.pack()

        # Generate NumPy-based Pixel Art Button
        self.numpy_art_button = tk.Button(root, text="Generate Pixel Art", command=self.generate_numpy_pixel_art)
        self.numpy_art_button.pack()

        # Preview Panel
        self.preview_label = tk.Label(root)
        self.preview_label.pack()

    def generate_numpy_pixel_art(self):
        description = self.description_entry.get()
        numpy_art.generate_numpy_art(description)

if __name__ == "__main__":
    root = tk.Tk()
    app = AssetForgeUI(root)
    root.mainloop()
