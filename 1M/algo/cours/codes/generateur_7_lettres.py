# -------------------------------------------------------------
# Générateur de mots aléatoires de 7 lettres
# Vincent Keller (c) 2026
# -------------------------------------------------------------
import random
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nombre = 10
i = 0
while i < nombre:
    j = 0
    mot = ""
    while j < 7:
        pos = random.randint(1,26)
        mot = mot + alphabet[pos-1]
        j = j + 1
    print(mot)
    i = i + 1