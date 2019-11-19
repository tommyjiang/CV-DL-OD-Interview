def any_bs(A, target):
    l, r = 0, len(A) - 1

    while l < r:
        m = l + (r - l) // 2
        if A[m] == target:
            return m
        elif A[m] < target:
            l = m + 1
        else:
            r = m - 1
    return l if A[l] == target else -1


def first_bs(A, target):
    l, r = 0, len(A) - 1

    while l < r:
        m = l + (r - l) // 2
        if A[m] < target:
            l = m + 1
        else:
            r = m

    return l if A[l] == target else -1


def last_bs(A, target):
    l, r = 0, len(A) - 1

    while l < r:
        m = l + (r - l) // 2 + 1
        if A[m] > target:
            r = m - 1
        else:
            l = m

    return l if A[l] == target else -1


A = [1, 2, 3, 7, 7, 7, 9, 12, 12]
print(any_bs(A, 1))
print(any_bs(A, 12))
print(any_bs(A, 8))
print(first_bs(A, 7))
print(last_bs(A, 7))
print(last_bs(A, 8))
print(last_bs(A, 12))
