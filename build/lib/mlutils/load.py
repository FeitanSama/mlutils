import csv

def load_data(file_path):
    data = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data

def head(data, n=5):
    if n >= 0:
        return data[:n]
    else:
        return data[n:]

def index(data):
    return list(range(len(data)))

def columns(data):
    return data[0]

def shape(data):
    return ((len(data)-1), len(data[0]))

from functools import reduce

def sum(data, axis=None):
    if axis is None or axis == 0:
        return [reduce(lambda x, y: x + y, row) for row in data]
    elif axis == 1:
        return [reduce(lambda x, y: x + y, col) for col in zip(*data)]
    else:
        raise ValueError("Invalid axis, use None, 0 or 1")

import numpy as np

def isna(data):
    return [[cell is None or isinstance(cell, (float, int)) and np.isnan(cell) for cell in row] for row in data]
