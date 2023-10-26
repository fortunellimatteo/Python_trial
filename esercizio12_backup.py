# Scrivi una funzione "file_backup" che sia in grado di effettuare copie di backup di determinati tipi di file, con le seguenti caratteristiche:
# Percorso da scansionare, di backup e tipologia di file da copiare dovranno essere passati dall'utente tramite input
# Il programma dovrà verificare la presenza o meno di una cartella di backup al percorso fornito, e qualora questa non fosse presente dovrà crearla
# La funzione dovrà anche gestire l'eventuale scelta da parte dell'utente, di un percorso da scansionare che non esiste

import os
import shutil

def file_backup():
    print("Ciao! Questo script effettua copie di backup per file di un'estensione passata come input.\n")
    percorso = input("Inserisci il percorso da scansionare: ")
    if not os.path.isdir(percorso):
        print(f"Il percorso inserito '{percorso}' risulta non essere un percorso idoneo. Verifica e riprova, grazie.\n")
        return file_backup()
    estensione = input("Che tipologia di file desideri salvare? [esempio: .jpg .pdf .epub]: ")
    backup_folder = input("Inserisci la cartella dove desideri salvare i tuoi file: ")
    if not os.path.isdir(backup_folder):
        os.makedirs(backup_folder)
    contatore = 0
    print(f"Sto effettuando la scansione di '{percorso}' alla ricerca di file '{estensione}'\n")
    for cartella, sottocartelle, files in os.walk(percorso):
        for file in files:
            if file.endswith(estensione):
                match = os.path.join(cartella,file)
                print(f"Trovato file {estensione}: {match}")
                shutil.copy(match,backup_folder)
                contatore += 1
    print("Copia Terminata")
    print(f"Ho trovato '{contatore}' files con estensione {estensione}, ora disponibili anche in '{backup_folder}'")

file_backup()