import random


def partition(A, l, r):
    pivot = random.randint(l, r)
    A[pivot], A[r] = A[r], A[pivot]
    i = l

    for j in range(l, r):
        if A[j] <= A[r]:
            A[i], A[j] = A[j], A[i]
            i += 1

    A[i], A[r] = A[r], A[i]
    return i

def kth_smallest(A, l, r, k):
    if k > 0 and k <= r - l + 1:
        index = partition(A, l, r)
        if index - l == k - 1:
            return A[index]
        if index - l > k - 1:
            return kth_smallest(A, l, index-1, k)
        else:
            return kth_smallest(A, index+1, r, k - (index - l + 1))

A = [5, 2, 4, 1, 3]
k = 5
res = kth_smallest(A, 0, len(A)-1, k)
print(res)
