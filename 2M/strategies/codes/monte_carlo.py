# Approximation du nombre Pi avec une méthode de Monte-Carlo
# Dans un carré de côté 1, on tire des nombres au hasard
# Si ils sont à une distance de 1 du centre, alors ils
# appartiennent à l'intérieur du cercle inscrit dans le carré
# sinon, ils sont en dehors.
import random
nb_exp = 10000
succes = 0
for i in range(nb_exp):
    x = random.random()
    y = random.random()
    if x * x + y * y <= 1:
        succes = succes + 1
nb_succ = 4 * succes / nb_exp
print(nb_succ)
