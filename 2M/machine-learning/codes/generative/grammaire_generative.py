import random

regles = {
    "<phrase>": ["<sujet> <verbe> <complement>"],
    "<sujet>": ["le chat", "le robot", "l'IA", "mon prof"],
    "<verbe>": ["mange", "rêve de", "génère", "analyse"],
    "<complement>": ["des données", "un poème", "du fromage", "l'avenir"]
}

def generer(symbole="<phrase>"):
    if symbole not in regles:
        return symbole
    expansion = random.choice(regles[symbole])
    mots = expansion.split()
    resultat = [generer(mot) for mot in mots]
    return " ".join(resultat)

# Génération
for _ in range(5):
    print("-", generer().capitalize() + ".")