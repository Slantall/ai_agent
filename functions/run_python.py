import os
import subprocess

def run_python_file(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    abs_joined_path = os.path.abspath(os.path.join(abs_working_directory, file_path))
    
    if not abs_joined_path.startswith(abs_working_directory):
        return (f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
    
    if not os.path.isfile(abs_joined_path):
        return (f'Error: File "{file_path}" not found.')
    
    if abs_joined_path[-3:] != ".py":
        return (f'Error: "{file_path}" is not a Python file.')
    try:
        runcmd = ["python3", file_path]
        ran = subprocess.run(runcmd, capture_output=True, timeout=30, cwd=abs_working_directory)
        output = ""
        STDOUT = str(ran.stdout, 'utf-8')
        STDERR = str(ran.stderr, 'utf-8')
        if STDOUT == "" and STDERR == "" and ran.returncode == 0:
            return "No output produced."
        if  STDOUT != "":
            output += (f"STDOUT: {STDOUT}\n")
        if STDERR != "":
            output += (f"STDERR: {STDERR}\n")
        if ran.returncode != 0:
            output += (f"Process exited with code {ran.returncode}")

        return output
    except Exception as e:
        return (f"Error: executing Python file: {e}")