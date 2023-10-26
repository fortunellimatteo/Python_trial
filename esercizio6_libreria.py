# dato il libro richiesto controlla se disponibile, se si vendilo e decrementa il numero di copie, se finiscono le copie cancellalo.
# se non è presente il libro inseriscilo in una lista di libri da comprare

libreria = {'1984': 4,'Cent anni di solitudine': 2, 'Il Decamerone': 7, 'Delitto e castigo': 1, 'Odissea': 3}
libri_da_comprare = []

def libreria_function(libro):
    res = libreria.get(libro, False)
    if res == False:
        libri_da_comprare.append(libro)
        return False
    else:
        nrLibriRimasti = libreria[libro]
        if nrLibriRimasti == 1:
            libri_da_comprare.append(libro)
            del libreria[libro]
        else:
            libreria[libro] = nrLibriRimasti=nrLibriRimasti-1
        return True


libro = str(input("Inserire il libro da cercare: \n"))
result = libreria_function(libro)
if result == True:
    print('Libro venduto')
else:
    print('Libro non venduto')

print(libreria)
print(libri_da_comprare)