oeufs = 1
beurre = 85
sucre = 85
farine = 150
sucre_vanille = 1
levure = 1
sel = 0.5
chocolat = 350

ingredients = [oeufs,beurre,sucre,farine,sucre_vanille,levure,sel, chocolat]

nbr_personnes = int(input("Entrez le nombre de personnes : "))

for i in range(len(ingredients)):
    ingredients[i] = (nbr_personnes/6)*ingredients[i]

print("Recette pour "+str(nbr_personnes)+" personnes")
print("1. Laissez ramollir "+str(ingredients[1])+"g. de beurre à température ambiante. Dans un saladier, malaxez-le avec "+str(ingredients[2])+"g. sucre. ")
print("2. Ajoutez "+str(ingredients[0])+"oeuf et éventuellement "+str(ingredients[4])+" sachets de sucre vanillé. ")
print("3. Versez progressivement "+str(ingredients[3])+"g. de farine, "+str(ingredients[5])+" sachets de levure chimique, "+str(ingredients[6])+"cc. de sel et "+str(ingredients[7])+"g. de pépites de chocolat. Mélangez bien. ")
print("4. Beurrez une plaque allant au four ou recouvrez-la d'une plaque de silicone. À l'aide de deux cuillères à soupe ou simplement avec les mains, formez des noix de pâte en les espaçant car elles s'étaleront à la cuisson. ")
print("5. Faites cuire 8 à 10 minutes à 180°C soit thermostat 6. Il faut les sortir dès que les contours commencent à brunir.")