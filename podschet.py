def podsort(a):
    m = max(a)
    counter = [0]*(m+1)
    line = ''
    for number in a:
        counter[number] += 1
    
    for i in range(m+1):
        line += str(i) * counter[i] + " "
    arr = list(map(int,line.split()))
    return arr







arr = [1,4,3,7]
print(podsort(arr))