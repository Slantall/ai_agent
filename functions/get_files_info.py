import os
from google.genai import types

def get_files_info(working_directory, directory=None):
    abs_working_directory = os.path.abspath(working_directory)
    abs_joined_path = abs_working_directory
    if directory:
        abs_joined_path = os.path.abspath(os.path.join(working_directory, directory))
    
    if not abs_joined_path.startswith(abs_working_directory):
        return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')

    if not os.path.isdir(abs_joined_path):
        return (f'Error: "{directory}" is not a directory')
    try:
        file_list = os.listdir(abs_joined_path)
        formatted_file_info = []
        for file in file_list:
            file_path = os.path.abspath(os.path.join(abs_joined_path,file))
            size = os.path.getsize(file_path)
            is_file = not os.path.isfile(file_path)
            full_str = (f"- {file}: file_size={size} bytes, is_dir={is_file}")
            formatted_file_info.append(full_str)
        return "\n".join(formatted_file_info)
    except Exception as e:
        return f"Error listing files: {e}"

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)