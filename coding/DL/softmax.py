import numpy as np

def softmax(x):
    y = np.exp(x - np.max(x, axis=1, keepdims=True))
    return y / np.sum(y, axis=1, keepdims=True)

x = np.array([[1, 2, 3], [2, 4, 6]])
print(softmax(x))
