# il cifrario di cesare

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J', 'K', 'L', 'M', 'N' ,'O' ,'P', 'Q', 'R', 'S', 'T' ,'U', 'V','W', 'X', 'Y' ,'Z']

nr_cifratura = int(input("Inserisci un numero di cifratura per utilizzare il cifrario di cesare: "))
parola = str(input("Inserisci la parola da cifrare: ")).upper()
parola_cifrata = ''

for letter in parola:
    indice_letter = alfabeto.index(letter)
    nuovo_indice = (indice_letter + nr_cifratura) % 26
    letter_cifrata = alfabeto[nuovo_indice]
    parola_cifrata+=letter_cifrata

print("La parola cifrata é: " + parola_cifrata.lower())