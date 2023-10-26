# https://www.programmareinpython.it/esercizi-python/
consonanti = ['B', 'C', 'D', 'F', 'G', 'H', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'Z']

while True:
    parola = str(input("Inserisci una parola oppure una frase da tradurre in rövarspråket:\n"))
    parola = parola.upper()
    word_rövarspråket = ''
    for letter in parola:
        flg = False
        for consonante in consonanti:
            if letter == consonante:
                word_rövarspråket+=letter+'O'+letter
                flg=True
        if flg==False:
            word_rövarspråket+=letter

    print("La parola o frase tradotta in rövarspråket è: "+word_rövarspråket)
    if input("\nDesideri tradurre un'altra frase? ") == "no":
        break