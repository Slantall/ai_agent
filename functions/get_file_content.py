import os
from google.genai import types

def get_file_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    abs_joined_path = os.path.abspath(os.path.join(abs_working_directory, file_path))
    
    if not abs_joined_path.startswith(abs_working_directory):
        return (f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
    
    if not os.path.isfile(abs_joined_path):
        return (f'Error: File not found or is not a regular file: "{file_path}"')
    try:
        file = open(abs_joined_path)
        
        txt = file.read(10001)
        if len(txt) > 10000:
            txt = txt[:10000]
            txt += '[...File "{file_path}" truncated at 10000 characters]'
        file.close()
        return txt
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'
    

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read the file contents truncated at 10000 characters, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to the file that should be read, relative to the working directory.",
            ),
        },
    ),
)
