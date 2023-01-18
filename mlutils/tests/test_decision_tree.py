import numpy as np
import sys
import os

mlutils_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/mlutils/')
sys.path.append(mlutils_dir)

from mlutils.decision_tree import build_tree

# Load the dataset
X = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12]])
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

# Build the decision tree
tree = build_tree(X, y)

# Make a prediction for a new sample
sample = np.array([2, 3, 4])
def predict(sample, tree):
    if tree is None:
        return -1 # or raise an exception
    feature = tree['feature']
    value = tree['value']
    if sample[feature] < value:
        return predict(sample, tree['left'])
    else:
        return predict(sample, tree['right'])

# check if the tree is not None
if tree is not None:
    prediction = predict(sample, tree)
    print(prediction)
else:
    print("The tree is empty")

# Return None

# Load the dataset
X = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9]])
y = np.array([0, 0, 1, 1, 1, 1, 1])

# Build the decision tree
tree = build_tree(X, y)

# check if the tree is not None
if tree is not None:
    prediction = predict(sample, tree)
    print(prediction)
else:
    print("The tree is empty")