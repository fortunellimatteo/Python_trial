# funzione che restituisce parola inversa a quella data
def parola_inversa():
    inversa = ''
    start = -1
    end = 0
    for letter in parola:
        if end == 0:
            inversa+=parola[start:]
        else:
            inversa+=parola[start:end]
        start-=1
        end-=1
    return inversa

parola = str(input("Inserisci la parola da invertire:\n"))
print('La parola inversa da quella data è: '+parola_inversa())