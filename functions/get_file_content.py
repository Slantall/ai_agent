import os

def get_file_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    abs_joined_path = os.path.abspath(os.path.join(abs_working_directory, file_path))
    
    if not abs_joined_path.startswith(abs_working_directory):
        return (f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
    
    if os.path.isdir(abs_joined_path):
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