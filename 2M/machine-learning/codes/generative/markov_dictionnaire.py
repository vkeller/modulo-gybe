import random

def construire_dictionnaire_markov(texte):
    """Construit un dictionnaire de transitions à partir d'un texte."""
    mots = texte.split()
    markov = {}

    # Parcourir les paires de mots consécutifs
    for i in range(len(mots) - 1):
        mot_actuel = mots[i]
        mot_suivant = mots[i + 1]

        if mot_actuel not in markov:
            markov[mot_actuel] = []
        markov[mot_actuel].append(mot_suivant)

    return markov

def generer_phrase(markov, debut, longueur_max=10):
    """Génère une phrase en suivant les transitions du dictionnaire."""
    phrase = [debut]
    mot_courant = debut

    for _ in range(longueur_max - 1):
        if mot_courant in markov:
            # Choisir un mot suivant au hasard parmi les options
            mot_suivant = random.choice(markov[mot_courant])
            phrase.append(mot_suivant)
            mot_courant = mot_suivant
        else:
            # Plus de suite possible → on arrête
            break

    return " ".join(phrase) + "."

# --- Texte d'exemple (à modifier ou agrandir) ---
texte_apprentissage = """
le renard et le corbeau
le renard mange du fromage
le corbeau chante sur un arbre
le renard flatte le corbeau
le corbeau laisse tomber le fromage
le renard rit
"""

# --- Construction du modèle ---
modele = construire_dictionnaire_markov(texte_apprentissage)

# --- Génération de phrases ---
print("Modèle de Markov construit à partir du texte :")
print(texte_apprentissage.strip())
print("\nPhrases générées :")

for _ in range(5):
    debut = random.choice(list(modele.keys()))
    phrase = generer_phrase(modele, debut, longueur_max=8)
    print("-", phrase)