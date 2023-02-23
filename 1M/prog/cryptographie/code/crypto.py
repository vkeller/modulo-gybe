# ==============================================
# Cryptographie
#
# Vincent Keller, Gymnase de Beaulieu (c) 2023
# ==============================================

from math import *

phrase_a_1 = "Arise, you have nothing to lose but your barbed wire fences!"
phrase_a_2 = "If privacy is outlawed, only outlaws will have privacy"
phrase_a_3 = "Show me a person who has nothing to hide, and I’ll show you a person who is either exceedingly dull or an exhibitionist"
phrase_a_4 = "One of the best ways to achieve justice is to expose injustice"
phrase_a_5 = "I am a future-hacker ; I am trying to get root access to the futur. I want to ride its system of thought"
phrase_a_6 = "Girls need modems"

phrase_f_1 = "La valeur d’un trésor réside dans son secret"
phrase_f_2 = "La cryptographie est la forme la plus aboutie de l’action directe non-violente"
phrase_f_3 = "L’argent c’est du temps, sauf si vous n’avez pas l’un ou l’autre"
phrase_f_4 = "Un téléphone portable émet des signaux de localisation. Lorsqu’on a un téléphone portable, le réseau sait toujours où l’on se trouve"
phrase_f_5 = "Si vous posséder une bibliothèque et un jardin, vous avez tout ce qu’il vous faut"
phrase_f_6 = "Combien de vous n’ont pas violé de loi ce mois-ci ?"
phrase_f_7 = "Si vous surveillez tout le monde, vous ne surveillez personne"
phrase_f_d1 = "Bonjour (ou plutôt bonsoir) Damien,"
phrase_f_d2 = "Bravo ! Vous avez démontré que vous maîtrisiez les tests conditionnels"
phrase_f_d3 = "que nous avons vu ce matin durant les TP"
phrase_f_d4 = "Ne manque maintenant plus qu'a tester aussi les autres conditions avec elif"
phrase_f_d5 = "Puisque vous sembliez intéressé par le sujet du prochain cours"
phrase_f_d6 = "voici un petit teaser qui, j'en suis certain, vous intéressera"
phrase_f_d7 = "Les phrases L1 à L9 sont codées, saurez-vous retrouver la valeur de ma clef ?"
phrase_f_d8 = "... et mieux encore : mon algorithme ?"
phrase_f_d9 = "La réponse est dans le code. Bonne chance !"

def chiffre(texte_clair,saut):
    texte_chiffre = ''
    pos = 0
    dec = 0
    pos_c = 0
    l = len(texte_clair)
    while pos != l:
        if (pos_c > l-1):
            dec += 1
            pos_c = dec
#        pos_c + dec
        texte_chiffre += texte_clair[pos_c]
        pos_c = pos_c + saut
        pos += 1
    return texte_chiffre    

def dechiffre(texte_chiffre,saut):
    l = len(texte_chiffre)
    pos = 0
    pos_c = 0
    dec = 0
    ret = ['' for _ in range(l)]
    while pos != l:
        if (pos_c > l-1):
            dec += 1
            pos_c = dec
        ret[pos_c] = texte_chiffre[pos]
        pos_c = pos_c + saut
        pos += 1
    return ''.join(ret)

texte_clair = phrase_f_1
texte_chiffre = ''
texte_dechiffre = ''

longueur = len(texte_clair)

#print("Texte clair : "+texte_clair)

#for s in range(3,10):
#    texte_chiffre = chiffre(texte_clair,s)
#    print('[C] '+str(s)+"   : "+texte_chiffre)
#    texte_dechiffre = dechiffre(texte_chiffre,s)
#    print('[D] '+str(s)+"   : "+texte_dechiffre)

print(phrase_f_d7)
print(chiffre(phrase_f_d7,5))

#print("Longueur de la chaîne : "+str(longueur))