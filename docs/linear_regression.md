## L'algorithme de Linear Regression

- **I**. La fonction model(X, theta)

- **II**. La fonction cost_function(X, y, theta)

- **III**. La fonction grad(X, y, theta)

- **IV**. La fonction gradient_descent(X, y, theta, learning_rate, n_iterations)

- **V**. La fonction coef_determination(y, pred)

- **VI**. La phase d'entraînement

## Introduction

En résumé, ce code implémente un modèle de régression linéaire en utilisant la méthode de descente de gradient en Python. Il calcule d'abord la prédiction pour un ensemble de données en utilisant les paramètres, puis calcule la fonction de coût en utilisant la formule de l'erreur quadratique moyenne pour mesurer la différence entre les prédictions et les labels réels. Il calcule ensuite les gradients pour les paramètres et utilise la descente de gradient pour optimiser les paramètres. Il enregistre également l'historique des coûts pour suivre l'évolution de la performance du modèle. Il calcule également le coefficient de détermination pour mesurer la qualité de la prédiction du modèle.

### I. La fonction model(X, theta)

La fonction `model(X, theta)` calcule la prédiction pour un ensemble de données X en utilisant les paramètres `theta`. Il utilise la notation "dot product" pour calculer la somme des produits des éléments de X par les éléments de theta.

### II. La fonction cost_function(X, y, theta)

La fonction `cost_function(X, y, theta)` calcule la fonction de coût pour un ensemble de données `X`, des labels `y` et des paramètres `theta`. Il utilise la formule de l'erreur quadratique moyenne pour calculer la différence entre les prédictions et les labels réels, puis la somme de ces différences et la divise par 2 fois le nombre d'échantillons.

### III. La fonction grad(X, y, theta)

La fonction `grad(X, y, theta)` calcule les gradients pour les paramètres `theta`. Il utilise la notation "dot product" pour calculer la somme des produits des éléments de X transposé par la différence entre les prédictions et les labels réels, puis la divise par le nombre d'échantillons.

### IV. La fonction gradient_descent(X, y, theta, learning_rate, n_iterations)

La fonction `gradient_descent(X,y, theta, learning_rate, n_iterations)` effectue la descente de gradient pour optimiser les paramètres `theta`. Elle prend en entrée les données `X`, les labels `y`, les paramètres initiaux `theta`, le taux d'apprentissage `learning_rate`, et le nombre d'itérations `n_iterations`. Elle utilise une boucle pour mettre à jour les paramètres `theta` en utilisant la formule de la descente de gradient, et enregistre chaque valeur de la fonction de coût dans un tableau `cost_history`. Elle retourne les paramètres optimisés et l'historique des coûts.

### V. La fonction coef_determination(y, pred)

La fonction `coef_determination(y, pred)` calcule le coefficient de détermination, qui mesure la qualité de la prédiction du modèle. Il utilise la formule de (1 - (somme des erreurs au carré) / (somme des écarts à la moyenne au carré)) pour calculer le coefficient de détermination.

### VI. La phase d'entraînement

La phase d'entraînement utilise `n_iterations` = 1000 et un `learning_rate` = 0.01 pour entraîner le modèle en utilisant les fonctions `gradient_descent()` et `cost_function()`.