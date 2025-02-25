def replace_backslashes(input_string: str) -> str:
    """Replace backslashes with double backslashes."""
    return input_string.replace('\\', '\\\\')

def get_file_path() -> str:
    """Prompt the user for the user ID."""
    return replace_backslashes(input("Enter file path: "))

def get_key_value() -> str:
    """Prompt the user for the user ID."""
    return input("Key value to modify: ")

def get_new_value() -> str:
    """Prompt the user for the user ID."""
    return input("New Value: ")