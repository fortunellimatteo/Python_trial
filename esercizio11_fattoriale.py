# funzione ricorsiva che calcola fattoriale di un numero, cioè che dato 4 fa 4 * 3 * 2 * 1


def funzione_fattoriale(numero):
    fattoriale = numero
    while True:
        if numero != 1:
            fattoriale = fattoriale * (numero-1)
            numero-=1
        else:
            break
    return fattoriale


numero = int(input("Scrivi un numero per fare il fattoriale:\n"))
print(f"Il fattoriale del numero {numero} è: " + str(funzione_fattoriale(numero)))