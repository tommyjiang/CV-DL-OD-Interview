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
    class Trie:
        def __init__(self):
            """
            Initialize your data structure here.
            """
            self.root = dict()

        def insert(self, word):

            cur = self.root
            for c in word:
                if not c in cur:
                    cur[c] = [dict(), 1]
                else:
                    cur[c] = [cur[c][0], cur[c][1] + 1]
                cur = cur[c][0]

    set_debug(True)
    t = int(input())
    for ti in range(1, t + 1):
        n, K = [int(s) for s in input().split()]
        strings = []

        for _ in range(n):
            strings.append(input())

        t = Trie()

        for s in strings:
            t.insert(s)

        q = collections.deque()
        q.append(t.root)

        res = 0
        while q:
            for _ in range(len(q)):
                cur = q.popleft()

                for k in cur:
                    res += cur[k][1] // K
                    q.append(cur[k][0])

        print(f'Case #{ti}: {res}')

