import random
def quick_sort(A, l, r):
    if l < r:
        q = partition(A, l, r)
        # print(A, A[q])
        quick_sort(A, l, q - 1)
        quick_sort(A, q + 1, r)


def partition(A, l, r):
    s = random.randint(l, r)
    A[s], A[r] = A[r], A[s]

    x = A[r]
    i = l - 1
    for j in range(l, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i+1]

    return i + 1


A = [8, 3, 5, 1, 0, 6, 9, 2, 7, 4]
quick_sort(A, 0, len(A)-1)
print(A)

