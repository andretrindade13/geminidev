import os
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_filepath = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not abs_filepath.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if os.path.isdir(abs_filepath):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    
    parent_dir = os.path.dirname(abs_filepath)
    if not os.path.isdir(parent_dir):
        try:
            os.makedirs(parent_dir)
        except Exception as e:
            return f"Could not create parent dirs: {parent_dir}: {e}"
    
    try:
        with open(abs_filepath, 'w') as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e: 
        return f"Failed to write to file: {file_path}: {e}"
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file, creating parent directories if needed",
    parameters= types.Schema(
        type= types.Type.OBJECT,
        properties = {
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Relative path to the file (e.g., 'src/utils/helper.ts')",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The text content to write to the file",
            )
        },
        required=["file_path", "content"]
    )
)