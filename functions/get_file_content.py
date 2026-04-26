import os
MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    abs_working_directory =  os.path.abspath(working_directory)
    abs_filepath = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_filepath.startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_filepath):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(abs_filepath, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            
            if len(file_content_string) >= MAX_CHARS:
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        
        return file_content_string
    except Exception as e:
        return f"Exception reading file: {e}"
