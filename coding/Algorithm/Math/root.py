# 求平方根、立方根等题目
# 牛拉法求非线性方程 f(x) = 0 的根
# 当前值为 x_k，则对应的点为 (x_k, f(x_k))
# 切线方程 y - f(x_k) = f'(x_k)(x - x_k)
# 迭代后的值 x_(k+1) 对应的点为 (x_(k+1), 0)，满足切线方程
# 可以得到迭代方程为 x_(k+1) = x_k - f(x_k) / f'(x_k)

# 求平方根 f(x) = x^2 - a
a = 2

x_cur = 2
x_pre = float('inf')
eps = 1e-4

while abs(x_cur - x_pre) > eps:
    x_pre = x_cur
    x_cur = x_cur - (x_cur * x_cur - a) / (2 * x_cur)

print(x_cur ** 2, x_pre ** 2)

# 求立方根 f(x) = x^3 - a
a = 2

x_cur = 2
x_pre = float('inf')
eps = 1e-4

while abs(x_cur - x_pre) > eps:
    x_pre = x_cur
    x_cur = x_cur - (x_cur * x_cur * x_cur - a) / (3 * x_cur * x_cur)

print(x_cur ** 3, x_pre ** 3)
