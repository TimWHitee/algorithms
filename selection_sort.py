def choice_sort(x):
    n = len(x)
    for i in range(n):
        index_of_min = i
        min_val = x[index_of_min]
        for j in range(i+1,n):
            if min_val > x[j]:
                index_of_min = j
                min_val = x[j]
        x[i],x[index_of_min]=x[index_of_min],x[i]

    return x

a = [2,6,1,3,7,0,3,0,1,3]

print(choice_sort(a))
        
