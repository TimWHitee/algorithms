visited = []

def dfs(graph,V):
    visited.append(V)
    print(V,end=" ")
    for neighbor in graph[V]:
        if neighbor not in visited:
            dfs(graph,V=neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

dfs(graph, 'A')
