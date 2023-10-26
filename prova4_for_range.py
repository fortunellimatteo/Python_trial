# ciclo for, numero variabile scelto da noi
# funzione range, include numero che inizia a contare da 0

for numero in range(11):
    print(numero)

# range, si possono passare 3 variabili:
# start - indice di inizio da cui far partire il ciclo
# stop - indice di fine da cui far finire il ciclo
# step - step di avanzamento

for numero in range(3, 11, 2):
    print(numero)

# il ciclo in basso ti fa vedere come andare all'incontrario su un ciclo, esempio: da 10 a 0
# il - indica che si parte dal fondo dell'iteratore

for numero in range(10, -1, -1):
    print(numero)