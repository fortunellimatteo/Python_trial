# tupla è insieme di elementi, sono verie e proprie classi di tipo, come String, int
my_tuple = (2,5,9,13,25) # possono essere scritte in entrambe i modi, il risultato è lo stesso
my_tuple2 = 2,5,9,13,25
print(my_tuple)
print(my_tuple2)

# l'indice parte da 0 come le liste
print(my_tuple[1])

# la differenza tra tuple e liste è che sono immutabili le tuple, non si possono modificare

# Set è insieme di elementi, sono verie e proprie classi di tipo, come String, int
my_set = {"spam", "eggs", "bacon"}
# non supportano i doppioni
my_set = {"spam", "eggs", "bacon","bacon"}
print(my_set)
# possiamo però aggiungere o togliere elementi
my_set.add("pasta")
print(my_set)