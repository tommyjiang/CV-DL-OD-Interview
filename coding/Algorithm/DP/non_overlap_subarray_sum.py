def max_presum(A):
    pre = [0] * (len(A) + 1)

    for i in range(1, len(A)):
        pre[i] = pre[i-1] + A[i-1]

    min_id, max_id, min_before = 0, 1, 0

    cur_max = pre[1] - pre[0]

    res = [0] * len(A)

    for i in range(1, len(A)):
        if pre[i] < pre[min_id]:
            min_id = i
        else:
            if pre[i] - pre[min_id] > cur_max:
                min_before = min_id
                max_id = i
            elif pre[i] > pre[max_id]:
                max_id = i

        res[i-1] = pre[max_id] - pre[min_before]
        cur_max = max(cur_max, res[i-1])

    return res


def max_non_overlap_sum(A):
    pre = max_presum(A)
    A = A[::-1]
    suc = max_presum(A)
    suc = suc[::-1]

    res = pre[0] + suc[1]
    for i in range(1, len(A)-1):
        cur = pre[i] + suc[i+1]
        res = max(res, cur)

    return res


def max_pre_qq(A):
    n = len(A)

    left_max, left_tail_max, right_max, right_tail_max = [0] * n, [0] * n, [0] * n, [0] * n

    for i in range(n-1):
        left_tail_max[i+1] = max(left_tail_max[i], 0) + A[i]
        left_max[i+1] = A[i] if i == 0 else max(left_max[i], left_tail_max[i+1])

    for i in range(n-2, -1, -1):
        right_tail_max[i] = max(right_tail_max[i+1], 0) + A[i+1]
        right_max[i] = A[i+1] if i == n - 2 else max(right_max[i+1], right_tail_max[i])

    res = -float('inf')
    for i in range(1, n):
        res = max(res, left_max[i] + right_max[i-1])

    return res


A = [1, 2, 3, -1, 3, -4, 5, 6, 7]
# A = [-1, 1, 1, -1]
# A = [1, -1]
print(max_pre_qq(A))
