used = []
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5],
    4: [2, 5],
    5: [3, 4]
}

def dfs(node, parent):
    used.append(node)
    for nei in graph[node]:
        if nei not in used:
            dfs(nei, node)
        elif  nei != parent:
            return True
    return False

for node in graph:
    if node not in used:
        if dfs(node, None):
            print("Cycle detected")
            exit()
print("No cycle detected")
