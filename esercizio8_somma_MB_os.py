# Scrivi una funzione che calcoli la somma (espressa in MB) delle dimensioni dei file presenti nella cartella di lavoro utilizzando il modulo os.

import os

path = 'C:\\PythonRepos'
files = os.listdir(path)
total_size = 0
for file in files:
    file_size = os.path.getsize(file)
    total_size+=file_size

print(f'La somma della dimensione dei file per il path {path} è {total_size/1048576} MB')