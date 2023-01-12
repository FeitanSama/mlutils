import sys
import os
from sklearn.datasets import make_blobs

mlutils_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/mlutils/')
sys.path.append(mlutils_dir)

from Logistic_regression.logistic_regression import *

X, y = make_blobs(n_samples=100, n_features=2, centers=2, random_state=0)
y = y.reshape((y.shape[0], 1))

regression_logistique(X, y)