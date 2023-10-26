# i dizionari sono tipi di classe, tipo String, int
# sono composti da indice e valore, con l'indice si può accedere per recuperare il valore

mio_dict = {1: "desc valore 1", 2: "desc valore 2", "primi": [2,3,5,7], "mao": 666}
print(mio_dict["primi"])

# come aggiornare valore
mio_dict[1] = "dajeeeeeee"
print(mio_dict[1])

# come aggiungere valore
mio_dict["nuova_key"] = "new value desc"
print(mio_dict)

# per vedere se ci sono quelle chiavi nel dizionario utilizzare IN o NOT IN, controlla la chiave non il valore
print(1 in mio_dict)
print(3 not in mio_dict)

# per eliminare chiave
del mio_dict[1]
print(mio_dict)

# per ottenere tutte le chiavi del dizionario
print(mio_dict.keys())
# per ottenere tutti i valori del dizionario
print(mio_dict.values())
# per ottenere tutte le coppie chiave valore, rappresentate com tuple
print(mio_dict.items())

# questi tipi che ritornano da .keys, .values, .items non sono liste normali, quindi per ricavare liste fare:
keys = (list) (mio_dict.keys())
print(keys)
values = (list) (mio_dict.values())
print(values)
items = (list) (mio_dict.items())
print(items)

# per utilizzare dizionario in for
for chiave in mio_dict.keys():
    print(chiave)

# metodo get, chiave presente o meno del dizionario, se la trova ritorna il valore sennò il messeggio scritto
print(mio_dict.get(2, "chiave non trovata"))

# setdefault(), se non c'è la chiave scritta la aggiunge, se non c'è aggiunge, sennò non fa niente
mio_dict.setdefault(2, "descrizione chiave 3")
print(mio_dict)