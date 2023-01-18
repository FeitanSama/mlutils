import numpy as np
from sklearn.datasets import make_regression
from mlutils.linear_regression import *

# Load the dataset

np.random.seed(0) # pour toujours reproduire le meme dataset
x, y = make_regression(n_samples=100, n_features=1, noise=10)
# plt.scatter(x, y) # afficher les résultats. X en abscisse et y en ordonnée

print('X Shape origine :',x.shape)
print('y Shape origine :',y.shape)

# redimensionner y
y = y.reshape(y.shape[0], 1)

print('y Shape redimensionne :',y.shape)

X = np.hstack((x, np.ones(x.shape)))
print('X Shape redimensionne :',X.shape)

np.random.seed(0) # pour produire toujours le meme vecteur theta aléatoire
theta = np.random.randn(2, 1)
print('Theta :',theta)

print('Function Cost :',cost_function(X, y, theta))

theta_final, cost_history = gradient_descent(X, y, theta, learning_rate, n_iterations)

print('Paramètres finaux du model :',theta_final) # voici les parametres du modele une fois que la machine a été entrainée

# création d'un vecteur prédictions qui contient les prédictions de notre modele final
predictions = model(X, theta_final)

print('Coef determination :',coef_determination(y, predictions))