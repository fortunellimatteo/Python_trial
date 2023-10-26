# calcolatrice
from math import sqrt
from math import pow

while True:
    number1 = int(input("Inserisci il numero... \n"))
    operation = str(input("Inserisci l' operazione tra:\n +(addizione),\n -(sottrazione),\n *(moltiplicazione),\n /(divisione),\n e(esponente),\n r(radice)... \n"))
    if (operation == '+'):
        number2 = int(input("Inserisci il numero... \n"))
        result = number1 + number2
        print('la somma è: ' + str(result))
    elif (operation == '-'):
        number2 = int(input("Inserisci il numero... \n"))
        result = number1 - number2
        print('la sottrazione è: ' + str(result))
    elif (operation == '*'):
        number2 = int(input("Inserisci il numero... \n"))
        result = number1 * number2
        print('la moltiplicazione è: ' + str(result))
    elif (operation == '/'):
        number2 = int(input("Inserisci il numero... \n"))
        result = number1 / number2
        print('la divisione è: ' + str(result))
    elif (operation == 'e'):
        number2 = int(input("Inserisci l esponente... \n"))
        print('l esponente è: ' + str(pow(number1, number2)))
    elif (operation == 'r'):
        print('la radice è: ' + str(sqrt(number1)))
    else:
        print('L operazione inserita non è valida')

    decision = str(input('Vuoi continuare? SI o NO?...'))
    if decision == 'SI':
        continue
    else:
        break


        

