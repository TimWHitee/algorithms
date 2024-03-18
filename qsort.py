import random

def quicksort(nums):
    if len(nums) <= 1: return nums


    else:
        random_pivot = random.choice(nums)

        left_nums = [num for num in nums if num < random_pivot]

        right_nums = [num for num in nums if num > random_pivot]
 
        eq_nums = [random_pivot] * nums.count(random_pivot)

        

        return quicksort(left_nums) + eq_nums + quicksort(right_nums)

a = [0, 1, 1, 9, 16, 25, 0, 4, 8, 27, 64, 125]

print(quicksort(a))