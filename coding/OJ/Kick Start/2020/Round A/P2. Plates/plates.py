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
    前缀和 + 背包 DP，时间复杂度 O(nkp)，空间复杂度 O(p)
    """
    set_debug(True)
    t = int(input())
    for ti in range(1, t + 1):
        n, k, p = [int(s) for s in input().split()]
        A = [[0 for _ in range(k)] for _ in range(n)]
        for i in range(n):
            A[i] = [int(s) for s in input().split()]

        f = [0 for _ in range(p+1)]
        g = [0 for _ in range(p+1)]

        for i in range(n):
            cur = 0
            for j in range(k):
                cur += A[i][j]
                for l in range(p, j, -1):
                    g[l] = max(g[l], f[l-j-1] + cur)

            f = g[:]

        print("Case #{}: {}".format(ti, f[p]))
