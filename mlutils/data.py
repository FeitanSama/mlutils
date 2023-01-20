import csv
import numpy as np
import math
import pandas as pd
from functools import reduce

def load_data(file_path):
    data = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data

def head(data, n=5):
    return data[1:n+1]

def index(data):
    return list(range(len(data)))

def columns(data):
    return data[0]

def shape(data):
    return ((len(data)-1), len(data[0]))

def sum(data, axis=None):
    if axis is None or axis == 0:
        return [reduce(lambda x, y: x + y, row) for row in data]
    elif axis == 1:
        return [reduce(lambda x, y: x + y, col) for col in zip(*data)]
    else:
        raise ValueError("Invalid axis, use None, 0 or 1")

def isna(data):
    def _isna(val):
        if val == 'None' or val == 'none' or val == 'NONE' or val is None or val == 'NaN' or val == 'nan' or val == 'NAN' or val == np.nan:
            return True
        elif isinstance(val, (str, bool)):
            return False
        else:
            return pd.isna(val)

    data = pd.DataFrame(data)
    return data.applymap(_isna)