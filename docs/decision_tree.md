## L'algorithme de Décision Tree

- **I**. La fonction entropy(y)

- **II**. La fonction information_gain(y, y_left, y_right)

- **III**. La fonction best_split(X, y)

- **IV**. La fonction build_tree(X, y)

## Introduction

En résumé, ce code implémente un algorithme d'arbre de décision à partir de zéro en utilisant Python, sans utiliser de bibliothèques externes telles que scikit-learn. Il calcule d'abord l'entropie d'un ensemble de données pour mesurer l'incertitude, puis utilise le gain d'information pour trouver le meilleur split pour séparer les données. Il construit ensuite l'arbre de décision en séparant récursivement les données en utilisant la fonction `best_split()` et en créant des noeuds pour chaque split. Le résultat final est un arbre de décision qui peut être utilisé pour faire des prédictions en parcourant l'arbre à partir de la racine jusqu'à une feuille en suivant les branches gauche ou droite en fonction des valeurs de la feature sélectionnée.

### I. La fonction entropy(y)

La fonction `entropy(y)` calcule l'entropie d'un ensemble de données `y`. Elle prend en entrée un vecteur de labels `y` et renvoie la valeur d'entropie. L'entropie est utilisée pour mesurer l'incertitude d'un ensemble de données. Elle est utilisée pour déterminer quelle feature est la plus informative pour séparer les données.

La fonction calcule d'abord le nombre d'éléments dans l'ensemble de données `n` et le nombre d'échantillons positifs `s` en sommant les valeurs du vecteur de labels. Ensuite, elle vérifie si tous les échantillons sont dans la classe positive ou aucun ne l'est, dans ce cas, elle renvoie 0, car l'entropie est nulle dans ces cas. Ensuite, elle calcule la proportion d'échantillons positifs et l'entropie de l'ensemble de données.

### II. La fonction information_gain(y, y_left, y_right)

La fonction `information_gain(y, y_left, y_right)` calcule le gain d'information d'un split. Elle prend en entrée le vecteur de labels complet `y`, le vecteur de labels de la branche gauche `y_left` et le vecteur de labels de la branche droite `y_right`. Elle renvoie la différence entre l'entropie de l'ensemble complet et la somme pondérée des entropies des branches gauche et droite. Le gain d'information est utilisé pour déterminer le meilleur split pour séparer les données.

### III. La fonction best_split(X, y)

La fonction `best_split(X, y)` trouve le meilleur split pour séparer les données. Elle prend en entrée la matrice de features `X` et le vecteur de labels `y`. Elle teste toutes les combinaisons de feature et de valeur pour trouver le meilleur split en calculant le gain d'information pour chaque split et renvoie la feature, la valeur, la matrice de features et le vecteur de labels des branches gauche et droite du meilleur split.

### IV. La fonction build_tree(X, y)

La fonction `build_tree(X, y)` construit l'arbre de décision en séparant récursivement les données en utilisant la fonction `best_split()`. Elle prend en entrée la matrice de features `X` et le vecteur de labels `y`. Elle vérifie si le vecteur de labels est vide, si c'est le cas, elle renvoie None. Sinon, elle utilise la fonction `best_split()` pour trouver la feature et la valeur qui séparent le mieux les données, et crée un noeud de l'arbre avec ces informations. Ensuite, elle appelle récursivement la fonction `build_tree()` en utilisant les données de la branche gauche et de la branche droite pour construire les sous-arbres correspondants. Le résultat final est un arbre de décision qui peut être utilisé pour faire des prédictions en parcourant l'arbre à partir de la racine jusqu'à une feuille en suivant les branches gauche ou droite en fonction des valeurs de la feature sélectionnée.