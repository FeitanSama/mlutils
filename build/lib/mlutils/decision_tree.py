import numpy as np

# Calculate the entropy of a dataset
def entropy(y):
    n = len(y)
    s = np.sum(y)
    if s == 0 or s == n:
        return 0
    p = s / n
    e = -p * np.log2(p) - (1 - p) * np.log2(1 - p)
    if np.isinf(e):
        return 0
    return e

# Split the dataset based on a given feature and value
def split(X, y, feature, value):
    mask = X[:, feature] >= value
    X_left = X[~mask]
    y_left = y[~mask]
    X_right = X[mask]
    y_right = y[mask]
    return X_left, y_left, X_right, y_right

def information_gain(y, y_left, y_right):
    p = len(y_left) / len(y)
    return entropy(y) - p * entropy(y_left) - (1 - p) * entropy(y_right)

def best_split(X, y):
    best_feature = None
    best_value = None
    best_score = 0
    n_features = X.shape[1]
    for feature in range(n_features):
        for value in np.unique(X[:, feature]):
            mask = X[:, feature] >= value
            y_left = y[~mask]
            y_right = y[mask]
            score = information_gain(y, y_left, y_right)
            if score > best_score:
                best_feature = feature
                best_value = value
                best_score = score
    if best_feature is None:
        return None, None, None, None, None, None
    mask = X[:, best_feature] >= best_value
    X_left = X[~mask]
    y_left = y[~mask]
    X_right = X[mask]
    y_right = y[mask]
    return best_feature, best_value, X_left, y_left, X_right, y_right

# Build the decision tree

# def build_tree(X, y):
#     if len(y) == 0:
#         return None
#     feature, value, X_left, y_left, X_right, y_right = best_split(X, y)
#     if feature is None:
#         return y[0]
#     tree = {'feature': feature, 'value': value}
#     tree['left'] = build_tree(X_left, y_left)
#     tree['right'] = build_tree(X_right, y_right)

def build_tree(X, y):
    if len(y) == 0:
        return None

    # Calculate the initial entropy
    entropy_initial = entropy(y)

    best_info_gain = 0
    best_feature = None
    best_value = None
    best_split = None

    # Iterate over all features and values to find the best split
    for feature in range(X.shape[1]):
        for value in np.unique(X[:, feature]):
            X_left, y_left, X_right, y_right = split(X, y, feature, value)

            # Calculate the entropy of the split
            entropy_left = entropy(y_left)
            entropy_right = entropy(y_right)
            entropy_split = len(y_left) / len(y) * entropy_left + len(y_right) / len(y) * entropy_right

            # Calculate the information gain of the split
            info_gain = entropy_initial - entropy_split

            # Update the best split if the information gain is higher
            if info_gain > best_info_gain:
                best_info_gain = info_gain
                best_feature = feature
                best_value = value
                best_split = (X_left, y_left, X_right, y_right)

    # Stop building the tree if the information gain is zero
    if best_info_gain == 0:
        return None

    # Build the tree recursively
    X_left, y_left, X_right, y_right = best_split
    tree = {'feature': best_feature, 'value': best_value}