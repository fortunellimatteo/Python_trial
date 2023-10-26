# rimario, lista di n parole, input di una e confronta le ultime 5 lettere della parola data con ultime 3 parole elenco, mostrale in output
matches = []
rimario = []
while True:
    rima = str(input("Scrivi una parola da inserire nel rimario: \n"))
    rimario.append(rima)
    decision = str(input("Vuoi inserire ancora parole nel rimario? S/N\n"))
    if decision == 'N':
        break

parola = str(input("Scrivi una parola da controllare con l'elenco per trovare le rime: \n"))
for rim in rimario:
    endRima = ''
    endParola = ''
    endParola = parola[-3:]
    endRima = rim[-3:]
    if endParola == endRima:
        matches.append(rim)


print(f'Ecco tutte le rime trovate nel rimario per la parola data {parola}:')
for match in matches:
    print(match)