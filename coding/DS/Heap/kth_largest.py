import random

def partition(A, l, r):
    p = random.randint(l, r)
    A[p], A[r] = A[r], A[p]

    i = l

    for j in range(l, r):
        if A[j] <= A[r]:
            A[i], A[j] = A[j], A[i]
            i += 1

    A[i], A[r] = A[r], A[i]
    return i


def kth_largest(A, l, r, k):
    if k > 0 and k <= r - l + 1:
        p = partition(A, l, r)

        if p - l == k - 1:
        	return A[p]

        if p - l > k - 1:
            return kth_largest(A, l, p-1, k)
        else:
            return kth_largest(A, p+1, r, k - (p - l + 1))

A = [1, 3, 5, 2, 4]
k = 3
print(kth_largest(A, 0, len(A)-1, len(A)-k+1))
