graph = {
    "A": ['S'],
    "B": ['C', 'D', 'S'],
    "C": ['B', 'J'],
    "D": ['B', 'G', 'S'],
    "E": ['G', 'S'],
    "F": ['G', 'H'],
    "G": ['D', 'E', 'F', 'H', 'J'],
    "H": ['F', 'G', 'I'],
    "I": ['H', 'J'],
    "J": ['C', 'G', 'I'],
    "S": ['A', 'B', 'D', 'E']
}
def bfs(graph=graph, start='A'):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        
        if node not in visited:
            visited.append(node)
            print(node)
            queue.extend(graph[node])

    

bfs()
