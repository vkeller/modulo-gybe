import matplotlib.pyplot as plt

p_contamination = 0.000005 # probabilité de contamination par jour, prendre 0.2 pour la version avancée
p_guerison = 0.1 # probabilité de guérison par jour
p_deces = 0.0001 # probabilité de deces par jour
nb_rencontre = 10 # nombres de personnes r

susceptibles = 100000
infections = 0
guerisons = 0
deces = 0

malades = 1
gueris = 0
morts = 0
courbe_infection = []
for i in range(100):
    # modele de base 
    infections = p_contamination * malades * susceptibles
    guerisons = p_guerison * malades
    deces = p_deces * malades

    ## une version un peu plus élaborée qui tient compte du pourcentage de malades
    ## dans nos contacts plutôt que du nombre total de malades pour déterminer le risque d'être infecté. 
    # infections = p_contamination * malades/(malades+gueris+susceptibles) *nb_rencontre * susceptibles


    # pour éviter les nombres négatifs dus à la méthode d'Euler (à ajouter ensuite)
    infections = min(infections,susceptibles)
    deces = min(deces,malades)
    guerisons = min(guerisons,malades)


    susceptibles = susceptibles - infections
    malades = malades + infections - deces - guerisons
    morts = morts + deces
    gueris = gueris + guerisons
    courbe_infection.append(infections)

print("Susceptibles : " + str(int(susceptibles)))
print("Malades      : " + str(int(malades)))
print("Gueris       : " + str(int(gueris)))
print("Morts        : " + str(int(morts)))

print(courbe_infection)

plt.plot(courbe_infection,'-')
plt.xlabel('jours')
plt.ylabel("nombre d'infections")
plt.show()