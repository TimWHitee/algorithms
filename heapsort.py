# Процедура для преобразования в двоичную кучу поддерева с корневым узлом i, что является индексом в arr[]. n - размер кучи
def heapify(arr, n, i):
    max = i # Initialize max as root
    left= 2 * i + 1   # left = 2*i + 1
    right= 2 * i + 2   # right = 2*i + 2

  # Проверяем существует ли левый дочерний элемент больший, чем корень

    if left< n and arr[i] < arr[left]:
        max = left

    # Проверяем существует ли правый дочерний элемент больший, чем корень

    if right< n and arr[max] < arr[right]:
        max = right

    # Заменяем корень, если нужно
    if max != i:
        arr[i],arr[max] = arr[max],arr[i] # свап

        # Применяем heapify к корню.
        heapify(arr, n, max)


# Основная функция для сортировки массива заданного размера
def heapSort(arr):
    n = len(arr)

    # Построение max-heap.
    for i in range(n):
        heapify(arr, n, i)
        
    

    # Один за другим извлекаем элементы
    for i in range(n-1, 0, -1):

        arr[0], arr[i] = arr[i], arr[0] # свап 
        
        heapify(arr, i, 0)
        
    return arr

arr = [ 9,3,6,1,9,8,7]

print(heapSort(arr))
