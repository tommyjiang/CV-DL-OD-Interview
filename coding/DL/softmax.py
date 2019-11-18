import numpy as np

def softmax(x):
    m = max(x)
    x = [x_i - m for x_i in x]

    ex = np.exp(x)
    return ex / sum(ex)

