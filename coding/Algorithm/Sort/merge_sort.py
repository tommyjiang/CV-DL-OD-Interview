def merge(A, B):
    res = []
    i = j = 0

    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            res.append(A[i])
            i += 1
        else:
            res.append(B[j])
            j += 1

    if i == len(A):
        res.extend(B[j:])
    else:
        res.extend(A[i:])

    return res


def merge_sort(A):
    if len(A) <= 1:
        return A
    m = len(A) // 2

    l = merge_sort(A[:m])
    r = merge_sort(A[m:])

    return merge(l, r)

A = [8, 1, 3, 5, 2, 7, 4, 9, 0, 6]
print(merge_sort(A))
