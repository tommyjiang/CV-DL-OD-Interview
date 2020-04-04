def cal_next_index(p):
    next_index = [-1] * len(p)
    i, j = 0, -1

    while i < len(p) - 1:
        if j == -1 or p[i] == p[j]:
            i += 1
            j += 1
            next_index[i] = j if p[i] != p[j] else next_index[j]
        else:
            j = next_index[j]

    return next_index


def kmp(s, p):
    i, j = 0, 0
    next_index = cal_next_index(p)

    while i < len(s) and j < len(p):
        if j == -1 or s[i] == p[j]:
            i += 1
            j += 1
        else:
            j = next_index[j]

    if j == len(p):
        return i - j
    else:
        return -1

print(kmp('cdababc', 'ab'))
print(kmp('abababzababab', 'zababab'))
