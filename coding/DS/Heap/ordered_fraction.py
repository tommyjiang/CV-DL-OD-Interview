import heapq

N = 8
a = 1
b = N

pq = [(a / b, a, b)]
heapq.heapify(pq)

visit = set()
visit.add((a, b))

res = []

n = N * (N-1) // 2

while len(res) < n:
    cur, a, b = heapq.heappop(pq)
    res.append((cur, a, b))

    if a+1 < b and (a+1, b) not in visit:
        heapq.heappush(pq, ((a+1)/b, a+1, b))
        visit.add((a+1, b))
    if b-1 > 0 and (a, b-1) not in visit:
        heapq.heappush(pq, (a/(b-1), a, b-1))
        visit.add((a, b-1))

print(res)
