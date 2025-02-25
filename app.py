import re
import modules.input_functions as input_functions
def update_reg_value(file_path: str, key: str, new_value: str):
    with open(file_path, 'r', encoding='utf-16') as file:
        content = file.read()

    # Regular expression to find the key and update its value
    pattern = re.compile(r'("{}"=")([^"]*)(")'.format(re.escape(key)))
    updated_content = pattern.sub(r'\g<1>{}\g<3>'.format(new_value), content)

    with open(file_path, 'w', encoding='utf-16') as file:
        file.write(updated_content)

# Example usage
if __name__ == "__main__":
    file_path = input_functions.get_file_path()
    key_string = input_functions.get_key_value()
    new_value = input_functions.get_new_value()
    update_reg_value(file_path, key_string, new_value)