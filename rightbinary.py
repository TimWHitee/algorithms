a = [1,2,3,4,5,5,5,5,5,5,5,5,5]

l,r = 0,len(a)-1
x = 5
while l < r:

    mid = (r + l) // 2

    if a[mid] <= x: l = mid
    else: r = mid - 1

print(r)