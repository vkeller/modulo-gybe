import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier

X, y = make_blobs(n_samples = 50, centers=2, n_features=2, random_state=0, cluster_std=1)

X_new = np.random.uniform(low=X.min() , high=X.max(), size=(10 ,2))

plt.scatter(X[:,0], X[:,1], c=y , cmap="bwr" )
plt.scatter(X_new[:,0] , X_new[:,1], c='white', edgecolor='k')
#plt.show()

model = KNeighborsClassifier(n_neighbors =3)
model.fit(X,y)

predictions = model.predict(X_new)

plt.scatter(X[:,0], X[:,1], c=y ,alpha=0.4)
plt.scatter(X_new[:,0], X_new[:,1], c=predictions, edgecolor='k' )
plt.show()

