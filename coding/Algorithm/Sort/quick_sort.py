import random
swap = 0

def quick_sort(A, l, r):
    if l < r:
        q = partition(A, l, r)
        quick_sort(A, l, q - 1)
        quick_sort(A, q + 1, r)


def partition(A, l, r):
    global swap
    s = random.randint(l, r)
    A[s], A[r] = A[r], A[s]

    x = A[r]
    i = l
    for j in range(l, r):
        if A[j] <= x:
            A[i], A[j] = A[j], A[i]
            swap += 1
            i += 1
    A[i], A[r] = A[r], A[i]

    return i


A = [8, 3, 5, 9, 6, 1, 2, 7, 4]
quick_sort(A, 0, len(A)-1)
print(A)
print(swap)
