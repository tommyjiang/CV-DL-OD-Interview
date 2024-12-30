import numpy as np

def softmax(x):
    y = np.exp(x - x.max())
    return y / y.sum()

x = np.array([1, 2, 3])
print(softmax(x))
