import re
import modules.input_functions as input_functions
import modules.reg_functions as rf
from tkinter import filedialog, messagebox

# Example usage
if __name__ == "__main__":
    file_path, key_string, new_value = input_functions.get_inputs()
    rf.update_reg_value(file_path, key_string, new_value)