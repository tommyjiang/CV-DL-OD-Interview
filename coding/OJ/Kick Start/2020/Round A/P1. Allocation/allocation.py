import sys

def set_debug(debug_mode=False):
    if debug_mode:
        fin = open('input.txt', 'r')
        fout = open('output.txt', 'w')

        sys.stdin = fin
        sys.stdout = fout


if __name__ == '__main__':
    """
    排序后贪心，时间复杂度 O(nlogn)，空间复杂度 O(1)
    """
    set_debug(True)

    t = int(input())
    for ti in range(1, t + 1):
        k, total = [int(s) for s in input().split()]
        prices = [int(s) for s in input().split()]

        prices.sort()

        cur = 0
        count = 0
        for x in prices:
            if cur + x > total:
                break
            else:
                cur += x
                count += 1

        print("Case #{}: {}".format(ti, count))
