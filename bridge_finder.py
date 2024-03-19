def dfs(v, graph, visited, tin, fup, timer, parent):
    visited[v] = True
    tin[v] = fup[v] = timer
    timer += 1
    for u in graph[v]:
        if not visited[u]:
            dfs(u, graph, visited, tin, fup, timer, v)
            fup[v] = min(fup[v], fup[u])
            if fup[u] > tin[v]:
                print(f"Edge ({v}, {u}) is a bridge.")
        elif u != parent:
            fup[v] = min(fup[v], tin[u])


n = 7 
edges = [(0, 1), (1, 2), (2, 0), (1, 3), (1, 4), (3, 5), (4, 6)]
graph = [[] for _ in range(n)]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * n
tin = [0] * n
fup = [0] * n
timer = 0

for i in range(n):
    if not visited[i]:
        dfs(i, graph, visited, tin, fup, timer, -1)