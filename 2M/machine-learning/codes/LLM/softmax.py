# -----------------------------------------------------
# Quelques tests des fonctions principales présentes dans
# les LLM.
# Vincent Keller, (c) 2025, Gymnase de Beaulieu, Lausanne
# -----------------------------------------------------
import random
import math
import numpy
import matplotlib.pyplot as plt

# Fonction softmax maison
def softmax_m(z):
    somme_exp = 0
    ret = []
    for i in range(len(z)):
        somme_exp = somme_exp + math.exp(z[i])
    for i in range(len(z)):
        ret.append(math.exp(z[i])/somme_exp)
    return ret

# Fonction softmax avec numpy (donc avec des np.arrays)
def softmax_np(x):
    e_x = numpy.exp(x - numpy.max(x))
    return e_x / e_x.sum(axis=0)

# Vérification maison (avec des listes)
def verif_m(vec):
    ret = 0
    for i in range(len(vec)):
        ret = ret + vec[i]
    return ret

# Vérification avec numpy arrays
def verif_np(vec_np):
    return numpy.sum(vec_np)


# Création d'un vecteur de taille n quelconque
n = int(input("Quelle taille de vecteur d'entrée : "))
z_min = 0
z_max = 50
z = []
for i in range(n):
    z.append(random.randint(z_min,z_max))

vec_softmax_m = softmax_m(z)
print(vec_softmax_m)
print("Vérification : ",verif_m(vec_softmax_m))

z_np = numpy.array(z)
vec_softmax_np = softmax_np(z)
print(vec_softmax_np)
print("Vérification : ",verif_np(vec_softmax_np))

plt.hist(vec_softmax_np)
plt.show()
