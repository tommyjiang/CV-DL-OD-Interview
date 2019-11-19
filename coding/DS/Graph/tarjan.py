def bridge(graph, u, visited, parent, low, dfs):



node = 5
edges = [[1, 0], [0, 2], [2, 1], [0, 3], [3, 4]]
graph = [[] for _ in range(node)]

for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])
print(graph)

visited = [False for _ in range(node)]
low = [float('inf') for _ in range(node)]
parent = [-1 for _ in range(node)]
dfs = [-1 for _ in range(node)]
