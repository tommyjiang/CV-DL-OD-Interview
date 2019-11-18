import numpy as np
def batch_norm(x, gamma, beta):
    """
    x: [N, C, H, W]
    """
    eps = 1e-5

    x_mean = np.mean(x, axis=(0, 2, 3), keepdims=True)
    x_var = np.var(x, axis=(0, 2, 3), keepdims=True)

    x_norm = (x - x_mean) / np.sqrt(x_var + eps)
    res = gamma * x_norm + beta

    return res


def group_norm(x, gamma, beta, G=16):
    """
    x: [N, C, H, W]
    """
    eps = 1e-5
    x = np.reshape(x, (x.shape[0], G, x.shape[1]//G, x.shape[2], x.shape[3]))

    x_mean = np.mean(x, axis=(2, 3, 4), keepdims=True)
    x_var = np.var(x, axis=(2, 3, 4), keepdims=True)
    x_normalized = (x - x_mean) / np.sqrt(x_var + eps)
    results = gamma * x_normalized + beta
    res = res.reshape(res, (x.shape[0], x.shape[1], x.shape[2], x.shape[3]))
    return res

