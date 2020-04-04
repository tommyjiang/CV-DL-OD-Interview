import sys

def set_debug(debug_mode=False):
    if debug_mode:
        fin = open('input.txt', 'r')
        fout = open('output.txt', 'w')

        sys.stdin = fin
        sys.stdout = fout


if __name__ == '__main__':
    # set_debug(True)

    t = int(input())
    for _ in range(t):
        a, b, c, d = map(int, input().split())
        x, y, x1, y1, x2, y2 = map(int, input().split())
        if (x1 <= x+b-a <= x2 and y1 <= y+d-c <= y2) and not ((x1 == x2 and a+b > 0) or (y1 == y2 and d+c > 0)):
            print("YES")
        else:
            print("NO")
