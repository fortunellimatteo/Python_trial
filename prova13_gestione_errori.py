# gestione eccezioni, try, except e finally: try se va tutto bene, except se va in eccezione

def addizione():
    try:
        a = int(input('Inserisci valore 1: \n'))
        b = int(input('Inserisci valore 2: \n'))
        ris = a + b
        print(ris)
    except ValueError:
        print('coglione inserisci solo numeri')
    finally:
        print('Sto chiudendo l app')

# puoi anche prendere il messaggio di errore dell'eccezione
def sottrazione():
    try:
        a = int(input('Inserisci valore 1: \n'))
        b = int(input('Inserisci valore 2: \n'))
        ris = a - b
        print(ris)
    except ValueError as e:
        print('coglione inserisci solo numeri \n')
        print(f'allega l errore dell eccezione {e}')
    finally:
        print('Sto chiudendo l app')

sottrazione()