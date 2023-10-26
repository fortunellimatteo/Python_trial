# la standard library è una collezione di moduli, tipo Math di java, https://docs.python.org/3/library/
import random # importa tutta la libreria
from math import sqrt # importa una funzione specifica dal modulo math
from random import * # importa tutte le librerie di random

for number in range(10):
    val = random.randint(1, 50) # importa valori random da 1 a 50 per 10 volte come il ciclo
    print(val)
    print(sqrt(val)) # sqrt fa la radice quadrata