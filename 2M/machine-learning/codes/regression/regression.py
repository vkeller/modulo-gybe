# Code provenant de Apprendre le Machine Learning en une semaine

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# simulation des donées

np.random.seed(0)
m = 100
X = np.random.randn(m).reshape(-1,1)
y = 1.5 * X + 3 + np.random.randn(m).reshape(-1,1)

plt.scatter(X,y)
# plt.show()

# Création du modèle de régression
model = LinearRegression()
model.fit(X,y)

new_data = np.linspace(-3,3).reshape(-1,1)
predictions = model.predict(new_data)

plt.scatter(X,y)
plt.plot(new_data , predictions )
plt.show()
