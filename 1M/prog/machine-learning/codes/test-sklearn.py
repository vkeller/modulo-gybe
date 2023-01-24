# ------------------------------------------------------
# Petit script de test pour un réseau neuronal simple
# de classification du MINST dataset des chiffres manuscrits
# Lib utilisée : https://scikit-learn.org/stable/
# ------------------------------------------------------

from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load des images
digits = datasets.load_digits()

#print(digits.images[0])
x = digits.images.reshape((len(digits.images), -1))
y = digits.target

# Mise à l'échelle des données
# Création d'un scaler
scaler = StandardScaler()

# Création du réseau neuronal à une seule couche à 10 neurones
#mlp = MLPClassifier(hidden_layer_sizes=(15,))
#mlp = MLPClassifier(verbose=True,solver='sgd', alpha=1e-5,hidden_layer_sizes=(8,3), random_state=1, max_iter=1000)
mlp = MLPClassifier(
    hidden_layer_sizes=(20,),
    max_iter=100,
    alpha=1e-4,
    solver="lbfgs",
    verbose=10,
    random_state=1,
    learning_rate_init=0.2,
)



# Définition des datasets d'entraînement et de test
x_train = x[:1000]
y_train = y[:1000]
x_test = x[1000:]
y_test = y[1000:]


# Calcul de la fonction de fitness
mlp.fit(x_train, y_train)

#print(x[0])

# Affichage d'une image
#plt.imshow(digits.images[0],cmap='binary')
#plt.title(digits.target[0])
#plt.axis('off')
#plt.show()

# Prédiction en fonction du réseau entraîné
mlp.predict(x_test[:10])

print(y_test[:10])

# Evaluation du réseau sur l'entier du dataset de test
y_pred = mlp.predict(x_test)

# Calcul de l'erreur
error = (y_pred != y_test)
print(np.sum(error) / len(y_test))

# Sélection d'une erreur et affichage
#x_error = x_test[error].reshape((-1, 8,8))
#y_error = y_test[error]
#y_pred_error = y_pred[error]
#i = 10
#plt.imshow(x_error[i],cmap='binary')
#plt.title(f'cible: {y_error[i]}, prediction: {y_pred_error[i]}')
#plt.axis('off')
#plt.show()
