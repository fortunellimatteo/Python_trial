# variabili globali e locali

x = 5

def prova_variabile_globale():
    global x # per rendere visibile x in una funzione va inserita la seguente istruzione, sennò non vede la variabile globale
    x+=1
    return x

def prova_variabile_locale(): # le variaibli locali di una funzione possono essere recuperate restituendole da una funzione come output
    y = 333
    return y

print(prova_variabile_locale()+333)