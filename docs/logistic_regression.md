## L'algorithme de Logistic Regression

- **I**. La fonction sigmoid(x)

- **II**. La fonction initialisation(X)

- **III**. La fonction forward_propagation(X, W, b)

- **IV**. La fonction log_loss(y, A)

- **V**. La fonction gradients(X, A, y)

- **VI**. La fonction optimisation(X, W, b, A, y, learning_rate)

- **VII**. La fonction predict(X, W, b)

- **VIII**. La fonction visualisation(X, y, W, b)

- **IX**. La fonction regression_logistique(X, y, learning_rate, n_iter)

## Introduction

En résumé, ce code implémente un modèle de régression logistique en utilisant la méthode de descente de gradient en Python.

### I. La fonction sigmoid(x)

La fonction `sigmoid(x)` calcule la fonction sigmoïde pour une entrée `x`. La fonction sigmoïde est utilisée pour convertir une entrée numérique en une probabilité entre 0 et 1.

### II. La fonction initialisation(X)

La fonction `initialisation(X)` initialise les paramètres de poids W et le biais b pour le modèle en utilisant des valeurs aléatoires générées par la fonction `np.random.randn()` pour des données d'entrée X.

### III. La fonction forward_propagation(X, W, b)

La fonction `forward_propagation(X, W, b)` calcule les prédictions pour un ensemble de données `X` en utilisant les paramètres `W` et `b` en utilisant la notation "dot product" pour calculer la somme des produits des éléments de X par les éléments de W, et en ajoutant le biais b. Il utilise la fonction sigmoid pour convertir les prédictions en probabilités.

### IV. La fonction log_loss(y, A)

La fonction `log_loss(y, A)` calcule la fonction de coût pour un ensemble de labels `y` et les prédictions `A`. Il utilise la formule de la log-loss pour calculer la somme des produits des labels par les logarithmes des prédictions et des (1 - labels) par les logarithmes des (1 - prédictions) puis divise par le nombre d'échantillons.

### V. La fonction gradients(X, A, y)

La fonction `gradients(X, A, y)` calcule les gradients pour les paramètres `W` et `b`. Il utilise la notation "dot product" pour calculer la somme des produits des éléments de X transposé par la différence entre les prédictions et les labels réels, puis divise par le nombre d'échantillons. Il retourne les gradients pour `W` et `b` sous forme de tuple.

### VI. La fonction optimisation(X, W, b, A, y, learning_rate)

La fonction `optimisation(X, W, b, A, y, learning_rate)` utilise les gradients pour mettre à jour les paramètres `W` et `b` en utilisant la formule de la descente de gradient. Elle prend en entrée les données `X`, les paramètres `W`, `b`, les prédictions `A`, les labels `y` et le taux d'apprentissage `learning_rate`. Elle retourne les paramètres mis à jour.

### VII. La fonction predict(X, W, b)

La fonction `predict(X, W, b)` calcule les prédictions pour un ensemble de données `X` en utilisant les paramètres `W` et `b` en utilisant la fonction `forward_propagation()` et retourne les prédictions sous forme de booléen en comparant les prédictions avec 0,5.

### VIII. La fonction visualisation(X, y, W, b)

La fonction `visualisation(X, y, W, b)` utilise les données `X`, les labels `y`, les paramètres `W` et `b` pour tracer les prédictions du modèle sur un graphique en utilisant la fonction `predict()` et `plt.contour()` pour tracer les limites de décision.

### IX. La fonction regression_logistique(X, y, learning_rate, n_iter)

La fonction `regression_logistique(X, y, learning_rate, n_iter)` utilise les fonctions précédentes pour entraîner le modèle de régression logistique sur les données `X`, les labels `y`, avec un taux d'apprentissage `learning_rate` et un nombre d'itérations `n_iter`. Il utilise la fonction `initialisation()` pour initialiser les paramètres, `forward_propagation()` et `log_loss()` pour calculer les prédictions et les coûts, `gradients()` et `optimisation()` pour mettre à jour les paramètres en utilisant la descente de gradient, `predict()` et `visualisation()` pour afficher les prédictions sur un graphique, et enfin tracer l'évolution des erreurs dans un graphique de log_loss contre n_iteration .