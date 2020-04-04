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

    """
    set_debug(True)
    t = int(input())
    for ti in range(1, t + 1):
        n, k = [int(s) for s in input().split()]

        strings = []
        for _ in range(n):
            strings.append(input())

        print(strings)

        print("Case #{}: {}".format(ti, 0))
