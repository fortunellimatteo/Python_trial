# funzioni

def nome_della_funzione(): # senza input
    name = input("come ti chiami?\n")
    print("il tuo nome è " + name)

def addizione(a, b):# con input
    print('funzione addizione')
    res = a+b
    print("il res è "+str(res))

def addizione_con_output(a, b):# con output, richiamala come riportato sotto
    print('funzione addizione con output')
    res = a+b
    return res
#res = addizione_con_output(4,5)
#print(res)
#print(addizione_con_output(4,5))

def laptop_nuovo(ram, cpu, antivirus=False):# parametro opzionale, richiama questa funzione come riportato sotto
    print('RAM: ' + ram)
    print('CPU: ' + cpu)
    if antivirus == True:
        print('Hai comprato anche l antivirus')
#laptop_nuovo('16GB', '8GB')
#laptop_nuovo('16GB', '8GB', antivirus=True)

