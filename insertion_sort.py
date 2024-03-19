def insertion_sort(x):
    n = len(x)
    for i in range(n):
        j = i
        while j > 0:
            if x[j] < x[j-1]:
                x[j], x[j-1] = x[j-1], x[j]
                
            j -= 1
    return x

my_array = [12, 11, 13, 5, 6]
insertion_sort(my_array)
print("Отсортированный массив:", my_array)