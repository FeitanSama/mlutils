import numpy as np
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt

# Dataset

np.random.seed(0) # pour toujours reproduire le meme dataset
x, y = make_regression(n_samples=100, n_features=1, noise=10)
# plt.scatter(x, y) # afficher les résultats. X en abscisse et y en ordonnée

print(x.shape)
print(y.shape)

# redimensionner y
y = y.reshape(y.shape[0], 1)

print(y.shape)

X = np.hstack((x, np.ones(x.shape)))
print(X.shape)

np.random.seed(0) # pour produire toujours le meme vecteur theta aléatoire
theta = np.random.randn(2, 1)
print(theta)

# Modele Linéaire

def model(X, theta):
    return X.dot(theta)

# plt.scatter(x, y)
# plt.plot(x, model(X, theta), c='r')

# Fonction Cout : Erreur Quadratique moyenne

def cost_function(X, y, theta):
    m = len(y)
    return 1/(2*m) * np.sum((model(X, theta) - y)**2)

print(cost_function(X, y, theta))

# Gradients et Descente de Gradient

def grad(X, y, theta):
    m = len(y)
    return 1/m * X.T.dot(model(X, theta) - y)

def gradient_descent(X, y, theta, learning_rate, n_iterations):
    
    cost_history = np.zeros(n_iterations) # création d'un tableau de stockage pour enregistrer l'évolution du Cout du modele
    
    for i in range(0, n_iterations):
        theta = theta - learning_rate * grad(X, y, theta) # mise a jour du parametre theta (formule du gradient descent)
        cost_history[i] = cost_function(X, y, theta) # on enregistre la valeur du Cout au tour i dans cost_history[i]
        
    return theta, cost_history

# Phase d'entrainement

n_iterations = 1000
learning_rate = 0.01

theta_final, cost_history = gradient_descent(X, y, theta, learning_rate, n_iterations)

print(theta_final) # voici les parametres du modele une fois que la machine a été entrainée

# création d'un vecteur prédictions qui contient les prédictions de notre modele final
predictions = model(X, theta_final)

# Affiche les résultats de prédictions (en rouge) par rapport a notre Dataset (en bleu)
# plt.scatter(x, y)
# plt.plot(x, predictions, c='r')

# Courbes d'apprentissage

# plt.plot(range(n_iterations), cost_history)

# Evaluation finale du modele

def coef_determination(y, pred):
    u = ((y - pred)**2).sum()
    v = ((y - y.mean())**2).sum()
    return 1 - u/v

print(coef_determination(y, predictions))