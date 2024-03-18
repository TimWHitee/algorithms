a = [1,7,3,4,2,6]


def bubble(array):
    flag = True
    for i in range(len(array)):
        flag = False
        for j in range(len(array) - i -1):

            if array[j] > array[j+1]:
                temp  = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                flag = True
        if not flag: break
    return array

print(bubble(a))
