import re
from tkinter import filedialog, messagebox

def update_reg_value(file_path: str, key: str, new_value: str):
    try:
        with open(file_path, 'r', encoding='utf-16') as file:
            content = file.read()

        # Regular expression to find the key and update its value
        pattern = re.compile(r'("{}"=")([^"]*)(")'.format(re.escape(key)))
        updated_content = pattern.sub(r'\g<1>{}\g<3>'.format(new_value), content)

        with open(file_path, 'w', encoding='utf-16') as file:
            file.write(updated_content)
        
        messagebox.showinfo("Success", "Registry value updated successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")