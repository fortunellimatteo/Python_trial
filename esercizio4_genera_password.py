# funzione generatrice password semplice o complessa
import random, string

def crea_password(tipo_pass):
    if tipo_pass == 'semplice':
        x = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        return x
    else:
        x = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
        return x
    
tipo_pass = str(input("Inserire il tipo di password:\n  -   semplice\n  -   complessa\n"))
print(f'Password {tipo_pass}: '+crea_password(tipo_pass))