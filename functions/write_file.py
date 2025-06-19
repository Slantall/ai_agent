import os

def write_file(working_directory, file_path, content):

    abs_working_directory = os.path.abspath(working_directory)
    abs_joined_path = os.path.abspath(os.path.join(abs_working_directory, file_path))
    
    if not abs_joined_path.startswith(abs_working_directory):
        return (f'Error: Cannot list "{file_path}" as it is outside the permitted working directory')
    
    try:
        if not os.path.exists(abs_joined_path):
            dirs = os.path.dirname(abs_joined_path)
            if not os.path.exists(dirs):
                os.makedirs(os.path.dirname(abs_joined_path))
            f = open(abs_joined_path, "x")
            f.close()


        with open(abs_joined_path, "w") as f:
            f.write(content)
        return (f'Successfully wrote to "{file_path}" ({len(content)} characters written)')

    except Exception as e:
        return f"Error listing files: {e}"