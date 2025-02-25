import tkinter as tk
from tkinter import filedialog, messagebox

def get_inputs():
    def browse_file():
        file_path.set(filedialog.askopenfilename(title="Select .reg file", filetypes=[("Registry files", "*.reg")]))
    
    key_value = ""
    new_value = ""

    def submit():
        nonlocal file_path, key_value, new_value
        key_value = key_entry.get()
        new_value = value_entry.get()
        root.destroy()

    root = tk.Tk()
    root.title("Registry Key Editor")

    file_path = tk.StringVar()

    tk.Label(root, text="File Path:").grid(row=0, column=0)
    tk.Entry(root, textvariable=file_path, width=50).grid(row=0, column=1)
    tk.Button(root, text="Browse", command=browse_file).grid(row=0, column=2)

    tk.Label(root, text="Key value to modify:").grid(row=1, column=0)
    key_entry = tk.Entry(root)
    key_entry.grid(row=1, column=1, columnspan=2)

    tk.Label(root, text="New Value:").grid(row=2, column=0)
    value_entry = tk.Entry(root)
    value_entry.grid(row=2, column=1, columnspan=2)

    tk.Button(root, text="Submit", command=submit).grid(row=3, columnspan=3)

    root.mainloop()
    return file_path.get(), key_value, new_value