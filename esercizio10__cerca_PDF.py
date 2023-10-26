# cerca file PDF

import os
from pathlib import Path
import pathlib

path = str(input("Fornisci path dove cercare file PDF:\n"))
totPDF = 0
# valida path
if Path(path).is_dir():
    files = list(pathlib.Path(path).glob('**\*.pdf'))
    for file in files:
        totPDF+=1
        print(f" -  {file}")
    print(f"I file trovati sono: {totPDF}")
else:
    print("Path non esistente...")