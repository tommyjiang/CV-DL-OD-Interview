class UF:
    def __init__(self, n):
        self.count = n
        self.id = [x for x in range(n)]
        self.size = [1 for _ in range(n)]


    def find(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p


    def connected(self, p, q):
        return self.find(p) == self.find(q)


    def union(self, p, q):
        p = self.find(p)
        q = self.find(q)

        if not self.connected(p, q):
            if self.size[p] < self.size[q]:
                self.id[p] = q
                self.size[q] += self.size[p]
            else:
                self.id[q] = p
                self.size[p] += self.size[q]
            self.count -= 1


    def __repr__(self):
        res = ''
        for i in range(len(self.id)):
            res += str(self.id[i]) + ' '
        return res[:-1]


uf = UF(5)
print(uf)
uf.union(1, 2)
uf.union(3, 4)
print(uf)
print(uf.count)
