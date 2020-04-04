def bridge(graph, u, visited, parent, low, dfs, count):
    visited[u] = True

    dfs[u] = count
    low[u] = count
    child = 0
    count += 1

    for v in graph[u]:
        if not visited[v]:
            parent[v] = u
            child += 1

            bridge(graph, v, visited, parent, low, dfs, count)

            low[u] = min(low[u], low[v])

            # edge
            if low[v] > dfs[u]:
                print(u, v)

            # point
            if parent[u] == -1:  # root node
                if child > 1:
                    print(u)
            else:  # not root node
                if low[v] >= dfs[u]:
                    print(u)
        else:
            if v != parent[u]:
                low[u] = min(low[u], dfs[v])


node = 5
edges = [[1, 0], [0, 2], [2, 1], [0, 3], [3, 4]]
node = 7
edges = [[0,1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3,4]]
graph = [[] for _ in range(node)]

for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])
print(graph)

visited = [False for _ in range(node)]
low = [float('inf') for _ in range(node)]
parent = [-1 for _ in range(node)]
dfs = [-1 for _ in range(node)]
count = 0

for i in range(node):
    if not visited[i]:
        bridge(graph, i, visited, parent, low, dfs, count)
