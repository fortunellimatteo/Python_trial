# Il ROT-13 è un semplice cifrario monoalfabetico, in cui ogni lettera del messaggio da cifrare viene 
# sostituita con quella posta 13 posizioni più avanti nell'alfabeto.
# Scrivi una semplice funzione in grado di criptare una stringa passata, o decriptarla se la stringa è già stata precedentemente codificata.

cifrario = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u',
            'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c',
            'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k',
            'y': 'l', 'z': 'm', 'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S',
            'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A',
            'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I',
            'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'}

def basic_rot(stringa):
    nuova_stringa = ""
    for carattere in stringa:
        if carattere in cifrario:
            nuova_stringa += cifrario[carattere]
        else:
            nuova_stringa += carattere
    return nuova_stringa

#####

import codecs

def lib_rot(stringa):
    print(codecs.encode(stringa, 'rot_13'))