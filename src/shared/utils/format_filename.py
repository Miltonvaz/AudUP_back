
from datetime import datetime
import os


def generate_filename(file_type:str, extension: str) -> str:
    
    
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    filename = f"{file_type}_{timestamp}.{extension}"
   
    
    
    return os.path.join(filename)