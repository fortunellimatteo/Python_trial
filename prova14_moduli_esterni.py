# package index, risorsa dove ci sono progetti, librerie
# pip, programma dove si installano librerie package index
# i package vengono installati a livello globale nel sistema, è sconsigliato
# ambienti virtuali, sono spazi indipendenti fra di loro, servono per separare le librerie utilizzate, 
# perchè si potrebbero utilizzare stesse librerie per + progetti ma con versioni diverse

# per creare ambienti virtuali utilizzare il comando
# python -m venv my_env (vuol dire: python utilizza il modulo venv, crea una cartella per il funzionamento della macchina virtuale con nome my_env),
# la cartella può essere creata su C:\utenti\tuo_utente

# per usare ambiente virtuale bisogna attivarlo, spostati su cartella create e digita .\Scripts\activate, per disattivarlo deactivate

# per utilizzarlo installando nuovi package, pip install django

# sempre da prompt stessa cartella ATTIVA, digitare python
# import django
# django.VERSION

# per utilizzare ambiente virtuale con librerie e moduli tipo django, andare su VSC, ctrl+shift+P, Python seleziona interprete, da file system,
# e aggiungere il file C:\Users\mfortunelli\my_env\Scripts\python.exe

# come creare un progetto che utilizza moduli e librerie tipo django con specifieche versioni di essi?comando in shel integrata VSC, pip freeze > requirements.txt,
# il nome del file requirements lo decidi te

# per reinstallare i package del file requirements.txt in un nuovo ambiente virtuale digitare il comando (su path cartella nuovo ambiente virtuale),
# pip install -r .\requirements.txt

# per consultare tutte le librerie e moduli esterni andare su: https://pypi.org/

import django

print(django.VERSION)