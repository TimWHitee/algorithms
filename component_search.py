graph = {
    "A": ['S'],
    "B": ['D', 'S'],
    "C": ['J'],
    "D": ['B', 'S'],
    "E": ['S'],
    "F": ['G', 'H'],
    "G": ['F', 'H', 'J'],
    "H": ['F', 'G', 'I'],
    "I": ['H', 'J'],
    "J": ['C', 'G', 'I'],
    "S": ['A', 'B', 'D', 'E']
}
used,component,components = [],[],[]




def dfs(vertex, graph=graph):

    used.append(vertex)
    component.append(vertex) # добавляем вершину в текущую компаненту

    for v in graph[vertex]:
        if v not in used:
            dfs(v)

for vertex in graph:
    if vertex not in used:
        dfs(vertex)
        components.append(component) # добавляем найденную компаненту ко всем компанентам
        component = [] # и обнуляем текущую компоненту после добавления

print(*components)      # перечисление вершин компонент связности
print(len(components))  # кол-во компонент связности
