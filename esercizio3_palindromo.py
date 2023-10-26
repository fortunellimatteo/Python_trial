# funzione che riconosce palindromo

def palindromo_function():
    result = True
    startP=-1
    endP=0
    for letter in parola:
        end = ''
        if endP == 0:
            end = parola[startP:]
        else:
            end = parola[startP:endP]
        if letter != end:
            result = False
            return result
        startP-=1
        endP-=1
    return result

parola = str(input("Inserisci il palindroma:\n"))
booleano = palindromo_function()
if booleano == True:
    print('è palindomo')
else:
    print('non è palindromo')