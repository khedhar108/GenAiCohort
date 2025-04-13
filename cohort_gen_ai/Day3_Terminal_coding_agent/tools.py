import os
import subprocess

# Define the workspace directory relative to this script's location
WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'workspace'))

# Ensure the workspace directory exists
os.makedirs(WORKSPACE_DIR, exist_ok=True)

def _resolve_path(path: str) -> str:
    """Resolves a relative path to an absolute path within the workspace."""
    # Prevent escaping the workspace
    abs_path = os.path.abspath(os.path.join(WORKSPACE_DIR, path))
    if not abs_path.startswith(WORKSPACE_DIR):
        raise ValueError(f"Attempted to access path '{path}' outside of the workspace.")
    return abs_path

def create_directory(path: str) -> str:
    """Creates a directory (and any parent directories) within the workspace."""
    try:
        full_path = _resolve_path(path)
        os.makedirs(full_path, exist_ok=True)
        return f"Successfully created directory: {path}"
    except Exception as e:
        return f"Error creating directory '{path}': {e}"

def create_or_update_file(path: str, content: str) -> str:
    """Creates a new file or updates an existing file with the given content within the workspace."""
    try:
        full_path = _resolve_path(path)
        # Ensure parent directory exists
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"Successfully created/updated file: {path}"
    except Exception as e:
        return f"Error creating/updating file '{path}': {e}"

def read_file(path: str) -> str:
    """Reads the content of a file within the workspace."""
    try:
        full_path = _resolve_path(path)
        if not os.path.exists(full_path):
             return f"Error: File not found at path '{path}'"
        if not os.path.isfile(full_path):
            return f"Error: Path '{path}' is not a file."

        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return f"Content of '{path}':\n```\n{content}\n```"
    except Exception as e:
        return f"Error reading file '{path}': {e}"

def list_files(path: str = ".") -> str:
    """Lists files and directories within a specified path in the workspace."""
    try:
        full_path = _resolve_path(path)
        if not os.path.exists(full_path):
            return f"Error: Directory not found at path '{path}'"
        if not os.path.isdir(full_path):
            return f"Error: Path '{path}' is not a directory."
        
        result = []
        for root, dirs, files in os.walk(full_path):
            rel_root = os.path.relpath(root, WORKSPACE_DIR)
            if rel_root == '.':
                rel_root = ''
            else:
                result.append(f"📁 {rel_root}")
            
            for file in files:
                file_path = os.path.join(rel_root, file)
                result.append(f"📄 {file_path}")
                
            # Don't go deeper than the first level if listing the root
            if path == "." and root == full_path:
                for subdir in dirs:
                    result.append(f"📁 {subdir}/")
                break
                
        if not result:
            return f"Directory '{path}' is empty."
        return "Files and directories in workspace:\n" + "\n".join(result)
    except Exception as e:
        return f"Error listing files in '{path}': {e}"

def run_terminal_command(command: str) -> str:
    """Executes a shell command within the workspace directory."""
    try:
        # Run the command in the workspace directory
        process = subprocess.Popen(
            command,
            shell=True,
            cwd=WORKSPACE_DIR,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate()
        
        result = f"Command: {command}\n"
        if stdout:
            result += f"\nOutput:\n{stdout}"
        if stderr:
            result += f"\nErrors:\n{stderr}"
        result += f"\nExit code: {process.returncode}"
        
        return result
    except Exception as e:
        return f"Error executing command '{command}': {e}"
