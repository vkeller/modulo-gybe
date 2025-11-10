# Simulation pédagogique (pas un vrai transformer !)
phrase = ["le", "chat", "mange", "du", "fromage"]
cible = "fromage"

# On "décide" que les mots les plus proches sont plus importants
importance = {
    "le": 1,
    "chat": 2,
    "mange": 5,   # très important !
    "du": 4,
    "fromage": 0  # c'est le mot à prédire, donc pas dans le contexte
}
print(phrase)
print("Mots les plus 'attentifs' :", [m for m, i in importance.items() if i > 3])
# → ['mange', 'du']