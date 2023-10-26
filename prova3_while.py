# ciclo while
counter = 0
skip = 5
while counter < 10:
    counter+=1
    if counter == skip:
        print('Salto il numero ' + str(skip))
        continue # ignora il pezzo di codice successivo
    if counter == 9:
        print('********************** Paolobello trovato **********************')
        break # stoppa il ciclo while
    print('CONITNUA')
