# possono avere diversi tipi di dato, ordinate con uno specifico indice per semplificare l'accesso
my_list = [9.9, 'pasta', 22] # definizione

# puoi anche aggiungere liste dentro lista
new_list = [33,'carne', my_list]

# gli indici delle liste iniziano da zero
print(new_list[1]) # per stampare la lista nella new_list

# per stampare l'ultimo valore
print(my_list[-1])

# accedere su doppie liste
print(new_list[2][1])

# per aggiungere valore a lista
my_list.append('addddddd')
print(my_list)

# per passare valori di una lista ad un altra
zia=[]
zio=[2,34,12,352,5,'mao']
zia.extend(zio)
print(zia)

# slicing di una lista
primi = [2,3,5,7,11,13,17,19]
print(primi[4:7]) # prende dalla posizione 4 alla 10

print(primi[4:]) # prende dalla posizione 4 fino alla fine

print(primi[:3]) # prende dall'inizio fino alla posizione data'

# ciclo con lista
match = 5
for elem in primi:
    if elem == match:
        print("trovato")
    else:
        print("avanti")

# ordinare una lista
alfabeto = ['b','z','a']
numeri = [2,56,8,3,12,3,778]
alfabeto.sort()
print(alfabeto) # asc
numeri.sort()
print(numeri)
alfabeto.sort(reverse=True)
print(alfabeto) # desc
numeri.sort(reverse=True)
print(numeri)

# per ricavare indice da valore
print(numeri.index(778))

# per sostituire valore di una lista ad un altro tremite indice
spesa = ['carne','pasta']
spesa[1] = 'verduera'
print(spesa)

# per rimuovere valore lista per indice
del spesa[0]
print(spesa)

# eliminare ultimo elemento di una lista
daje = [3,4,6,6,2,23,6,34,62,3,5,2444]
daje.pop()
print(daje)

# eliminare per valore, ti elimina primo valore trovato per 6 in questo caso, non ti elimina tutti i 6
daje.remove(6)
print(daje)