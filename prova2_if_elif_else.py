# prova if , elif, else
age = int(input("Dimmi la tua età: \n"))

if age >= 18 and age <= 70:
    print("Sei maggiorenne")
elif age >=70 and age <= 90:
    print("Sei paolobello")
elif age <= 18:
    print("Sei troppo piccolo")
else:
    print("Sei azzarone")