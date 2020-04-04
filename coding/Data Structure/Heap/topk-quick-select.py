import random
import heapq


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


def heap_kth_smallest(A, k):
    pq = []
    heapq.heapify(pq)

    for x in A:
        if len(pq) < k:
            heapq.heappush(pq, -x)
        else:
            heapq.heappushpop(pq, -x)

    return -pq[0]


def heap_kth_smallest(A, k):
    pq = []
    heapq.heapify(pq)

    for x in A:
        if len(pq) < k:
            heapq.heappush(pq, x)
        else:
            heapq.heappushpop(pq, x)

    return pq[0]


def heap_all_kth_smallest(A, k):
    heapq.heapify(A)

    for i in range(k):
        res = heapq.heappop(A)

    return res


A = [5, 2, 4, 1, 3]
k = 2
# res = kth_smallest(A, 0, len(A)-1, k)
# res = heap_kth_smallest(A, k)
res = heap_all_kth_smallest(A, k)
print(res)
