def mergesort(a):
    def sortr(l, r, arr):
        if r - l <= 1:
            return

        m = (l + r) // 2

        sortr(l, m, arr)
        sortr(m, r, arr)
        merge(l, m, r, arr)

    def merge(l, m, r, arr):
        buffer = [0] * (r - l)
        index_l, index_m, cur = l, m, 0

        while index_l < m or index_m < r:
            if index_l < m and (index_m == r or (arr[index_l] < arr[index_m])):
                buffer[cur] = arr[index_l]
                index_l += 1
            else:
                buffer[cur] = arr[index_m]

                index_m += 1
            cur += 1

        for i in range(l, r):
            arr[i] = buffer[i - l]


    sortr(0, len(a), a)
    return a

arr = [1, 6, 2, 9, 4, -1]
print(mergesort(arr))
