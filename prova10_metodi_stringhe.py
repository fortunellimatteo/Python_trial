# f string literal
name = 'Matteo'
numero = 33
numero2 = 5

print(f"Ciao {name} il tuo numero è il {numero}")

print(f"Il quadrato di {numero2} è {numero2*numero2}")

# startsWith e endsWith, vedono se la stringa inizia o finisce con la lettera o la parola data
print(name.startswith('m'))
print(name.endswith('teo'))

# verifica tipologia di caratteri in una stringa
# isalnum() alfanumerici
# isalpha() solo alfabetici
# isdecimal() solo numeri
# isspace() solo caratteri spazi
spam = 'asd123'
eggs = '999'
bacon = '    '
monty = 'poker '

print(spam.isalpha())
print(eggs.isdecimal())
print(bacon.isspace())
print(monty.isspace())

# upper e lower, ti danno o tutto maiuscolo o tutto minuscolo, però non cambia valore della variabile
print(name.upper())
print(name.lower())

# split e join, join concatena con un valore dato i valori della lista

to_do = ['fare pranzo','rifare letto', 'TROMBARE']
print(", ".join(to_do))

citazione = 'daje, cazzo'
print(citazione.split(","))

# lunghezza lista o stringa
print(len(to_do)) # lista
print(len(citazione)) # stringa

# in e not in per vedere se un carattere presente oppure no su stringa o lista
new_str = "forza milan 5 maggio"
print("milan" in new_str) # stringa
print("TROMBARE" in to_do) # lista

print("milan" not in new_str) # stringa
print("TROMBARE" not in to_do) # lista

# usare indici per fare slicing di una stringa, ricordo che con meno parte dal fondo
alfa = "abcdefghil..."
dots1 = alfa[-3:]
dots2 = alfa[:-3]
print(dots1)
print(dots2)

# ciclo for con le stringhe
radnom_alnum = 'asndkgh2u58923589ng'
match = 'k'
counter = 0

for char in radnom_alnum:
    if char == match:
        counter+=1

print(f"Ho trovato {counter} carattere '{match}' nella stringa {radnom_alnum}")