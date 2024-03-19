# import random as r
# import datetime


# tasks = ('Статический массив. Динамический массив, среднее время добавления элементаwОдносвязный список, двусвязный список. Псевдокод добавления и удаленияwАТД Стек. Реализация стека на основе дин. массива, на основе списка.wАТД Очередь и Дек. Реализация на основе списка, оценка временисложности.wБинарный поиск. Задача поиска элемента в отсортированном массиве -постановка задачи, оценка сложности алгоритма. Три вида бинарногопоиска.wДвоичная куча. Описание, построение, добавление элемента, извлечениеминимума.wКвадратичные сортировки (пузырьком, вставками, выбором), сортировка спомощью двоичной кучи. Описание алгоритмов, оценка времени работы идополнительной памяти.wСортировка слиянием. Описание алгоритма, оценка времени работыwБыстрая сортировка. Описание алгоритма, оценка времени работы влучшем, среднем и худшем случае.wГраф. Хранение графа в памяти: список смежности, матрица смежности(плюсы и минусы). Оценка времени поиска всех соседей, добавлениеребра. Оценка расходуемой памяти.wВиды графов. Деревья. Связность. Циклы. Полные графы.Ориентированность.wОбход графа в ширину. Описание алгоритма, примеры задач, временнаясложность.wОбход графа в глубину. Описание алгоритма, примеры задач, временнаясложность. Свойство дерева обхода.wПоиск цикла в графе (ориентированном и неориентированном) при помощиобхода в глубину. Описание алгоритма, оценка по времени и памяти.wПоиск мостов в графе. Определение моста. Алгоритм нахождения мостов.wПоиск точек сочленения в графе. Определение точки сочленения. Алгоритмнахождения точек сочленения.'.split('w'))
# while True:
#     first = r.randint(0,9)
#     second = r.randint(0,9)
#     if first != second:
#         break

# if  first > second:
#     first,second = second,first 

# current_time = datetime.datetime.now()
# print()
# print("Текущее время:", current_time)
# print()
# print(f'{first+1}. {tasks[first].strip()}')
# print()
# print(f'{second+1}. {tasks[second].strip()}')
def has_cycle(graph):
    visited = set()
    
    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False
    
    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
    return False

# Пример использования:
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5],
    4: [2, 5],
    5: [3, 4]
}

if has_cycle(graph):
    print("Граф содержит цикл")
else:
    print("Граф не содержит цикла")