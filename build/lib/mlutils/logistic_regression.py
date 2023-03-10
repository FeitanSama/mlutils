import numpy as np
import matplotlib.pyplot as plt

# Modele Logistique

def sigmoid(x):
  return 1 / (1 + np.exp(-x))

def initialisation(X):
  W = np.random.randn(X.shape[1], 1)
  b = np.random.randn(1)
  return (W, b)
     
def forward_propagation(X, W, b):
  Z = X.dot(W) + b
  A = sigmoid(Z)
  return A

# Fonction Cout

def log_loss(y, A):
  return 1/len(y) * np.sum(-y * np.log(A) - (1 - y) * np.log(1 - A))

# Gradients et Descente de Gradient

def gradients(X, A, y):
  dW = 1/len(y) * np.dot(X.T, A - y)
  db = 1/len(y) * np.sum(A - y)
  return (dW, db)

def optimisation(X, W, b, A, y, learning_rate):
  dW, db = gradients(X, A, y)
  W = W - learning_rate * dW
  b = b - learning_rate * db
  return (W, b)

# Prédiction et visualisation

def predict(X, W, b):
  A = forward_propagation(X, W, b)
  return A >= 0.5

def visualisation(X, y, W, b):
  resolution = 300
  fig, ax = plt.subplots(figsize=(9, 6))
  ax.scatter(X[:, 0], X[:, 1], c=y, s=50, edgecolor='k')

  #limites du graphique
  xlim = ax.get_xlim()
  ylim = ax.get_ylim()

  # meshgrid
  x1 = np.linspace(xlim[0], xlim[1], resolution)
  x2 = np.linspace(ylim[0], ylim[1], resolution)
  X1, X2 = np.meshgrid(x1, x2)

  # assembler les 2 variables
  XX = np.vstack((X1.ravel(), X2.ravel())).T

  # Prédictions
  Z = predict(XX, W, b)
  Z = Z.reshape((resolution, resolution))

  ax.pcolormesh(X1, X2, Z, zorder=0, alpha=0.1)
  ax.contour(X1, X2, Z, colors='g')

# Evaluation finale du modele

def regression_logistique(X, y, learning_rate=0.1, n_iter=100):
  
  # Initialisation
  W, b = initialisation(X)
  loss_history = []

  # Entrainement
  for i in range(n_iter):
    A = forward_propagation(X, W, b)
    loss_history.append(log_loss(y, A))
    W, b = optimisation(X, W, b, A, y, learning_rate=0.1)

  # Prediction
  visualisation(X, y, W, b)
  plt.figure(figsize=(9, 6))
  plt.plot(loss_history)
  plt.xlabel('n_iteration')
  plt.ylabel('Log_loss')
  plt.title('Evolution des erreurs')