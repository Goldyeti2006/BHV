import os
import uuid
from pathlib import Path
from werkzeug.utils import secure_filename

def allowed_file(filename, allowed_extensions):
    """Checks if filename has a valid extension in a case-insensitive way."""
    if '.' not in filename:
        return False
    
    extension = filename.rsplit('.', 1)[1].lower()
    return extension in allowed_extensions

def sanitize_filename(filename):
    """Removes unsafe characters and limits filename length."""
    filename = secure_filename(filename)
    # Redundant replace line removed here
    name, ext = os.path.splitext(filename)
    if len(name) > 100:
        name = name[:100]
    return f"{name}{ext}"

def generate_unique_filename(original_filename):
    """Generates a random UUID filename to prevent overwriting existing files."""
    ext = Path(original_filename).suffix.lower()
    unique_name = f"{uuid.uuid4().hex}{ext}"
    return unique_name

def validate_file_size(file_size, max_size):
    """
    Improved validation to catch 'An empty file (size 0)' 
    and 'MAX_FILE_SIZE' constraints in a single expression.
    """
    return 0 < file_size <= max_size