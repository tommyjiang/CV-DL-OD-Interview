import sys
import collections

def set_debug(debug_mode=False):
    if debug_mode:
        fin = open('input.txt', 'r')
        fout = open('output.txt', 'w')

        sys.stdin = fin
        sys.stdout = fout


if __name__ == '__main__':
    """
    二分，时间复杂度 O(nlogn)，空间复杂度 O(1)
    """
    set_debug(True)
    t = int(input())
    for ti in range(1, t + 1):
        n, k = [int(s) for s in input().split()]
        A = [int(s) for s in input().split()]

        diff = []
        for i in range(1, len(A)):
            diff.append(A[i]-A[i-1])
        diff.sort(reverse=True)

        def can(d):
            cur = 0
            for x in diff:
                if x % d == 0:
                    cur += x // d - 1
                else:
                    cur += x // d

                if cur > k:
                    return False

            return True

        l, r = 1, diff[0]
        while l < r:
            m = l + (r - l) // 2
            if can(m):
                r = m
            else:
                l = m + 1

        print("Case #{}: {}".format(ti, l))
