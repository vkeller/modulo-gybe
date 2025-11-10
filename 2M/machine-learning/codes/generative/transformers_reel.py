# generer_ia_transformer.py
from transformers import pipeline

# Charger un petit modèle de langage (environ 300 Mo)
print("Chargement du modèle... (cela peut prendre quelques secondes)")
generateur = pipeline("text-generation", model="distilgpt2")

# Texte de départ (prompt)
prompt = "L'intelligence artificielle"

# Générer du texte
resultats = generateur(
    prompt,
    max_length=50,        # longueur maximale de la séquence
    num_return_sequences=2,  # nombre de propositions
    temperature=0.9,      # créativité (0 = déterministe, 1 = très aléatoire)
    do_sample=True
)

print("\n✨ Texte généré par un vrai Transformer :\n")
for i, resultat in enumerate(resultats, 1):
    texte = resultat['generated_text']
    # Nettoyer : garder jusqu'au premier point après le prompt (optionnel)
    print(f"{i}. {texte.strip()}")
print("\n💡 Comparez avec votre générateur de Markov !")