import random

def nettoyer_texte(texte):
    """Optionnel : met en minuscules et supprime certains signes."""
    texte = texte.lower()
    # On garde les espaces et lettres ; on remplace . ? ! par espaces
    for ponct in ".!?:;,":
        texte = texte.replace(ponct, " ")
    return " ".join(texte.split())  # supprime les espaces multiples

def construire_markov_ordre1(texte):
    """Construit un dictionnaire : mot -> [mots_suivants]"""
    mots = texte.split()
    markov = {}
    for i in range(len(mots) - 1):
        courant, suivant = mots[i], mots[i + 1]
        if courant not in markov:
            markov[courant] = []
        markov[courant].append(suivant)
    return markov

def generer_texte(markov, debut, longueur=15):
    """Génère une séquence de mots à partir d'un mot de départ."""
    if debut not in markov:
        return f"Le mot '{debut}' n'est pas dans le modèle."
    resultat = [debut]
    for _ in range(longueur - 1):
        mot = resultat[-1]
        if mot in markov:
            suivant = random.choice(markov[mot])
            resultat.append(suivant)
        else:
            break
    return " ".join(resultat) + "."

# -----------------------------
# Exemple d'utilisation
# -----------------------------
corpus = """
Maître Corbeau, sur un arbre perché,
Tenait en son bec un fromage.
Maître Renard, par l’odeur alléché,
Lui tint à peu près ce langage :
Hé ! bonjour, Monsieur du Corbeau.
Que vous êtes joli ! que vous me semblez beau !
Sans mentir, si votre ramage
Se rapporte à votre plumage,
Vous êtes le Phénix des hôtes de ces bois.
"""

corpus_nettoye = nettoyer_texte(corpus)
modele = construire_markov_ordre1(corpus_nettoye)

print("Mots possibles au départ :", list(modele.keys())[:10], "...")
print("\nPhrases générées :\n")

for _ in range(5):
    debut = random.choice(list(modele.keys()))
    print("-", generer_texte(modele, debut, longueur=12))