graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5],
    4: [2, 5],
    5: [3, 4]
}
used = [0] * len(graph)
def dfs(v):
    used[v] = 1
    for u in graph[v]:
        if used[u] == 0:
            dfs(u)
        elif used[u] == 1:
            print('Cycle detected')
            exit()
    used[v] = 2
    return 0

for node in graph:
    if node not in used:
        dfs(node)

print('No cycle')