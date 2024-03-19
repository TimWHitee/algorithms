def find_sharnirs(adj):
    n = len(adj)
    visited = [False] * n
    tin = [float("inf")] * n
    fup = [float("inf")] * n
    timer = 0

    def dfs(v, parent):
        nonlocal timer
        children = 0
        visited[v] = True
        tin[v] = fup[v] = timer
        timer += 1

        for u in adj[v]:
            if u == parent:
                continue

            if visited[u]:
                fup[v] = min(fup[v], tin[u])
            else:
                children += 1
                dfs(u, v)
                fup[v] = min(fup[v], fup[u])

                if fup[u] >= tin[v] and parent != -1:
                    print(f"{v} is a sharnir")

        if parent == -1 and children > 1:
            print(f"{v} is a sharnir")

    for i in range(n):
        if not visited[i]:
            dfs(i, -1)

graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2, 4],
    4: [3, 5],
    5: [4]
}

find_sharnirs(graph)