def insertion_sort(A):
    # 逆序时 O(n^2)
    # 基本有序 接近 O(n)
    for i in range(1, len(A)):
        cur = A[i]
        j = i

        while j > 0 and A[j-1] > cur:
            A[j] = A[j-1]
            j -= 1

        A[j] = cur


A = [8, 3, 5, 1, 0, 6, 9, 2, 7, 4]
insertion_sort(A)
print(A)
