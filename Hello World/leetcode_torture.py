def twoSum(nums, target):
    index_return = []
    i = 0
    j = 0
    for num1 in nums:
        j = 0
        for num2 in nums:
            if i == j:
                j += 1
                continue
            if num1 + num2 == target:
                index_return.append(i)
                index_return.append(j)
                return index_return
            j += 1
        i += 1

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3, 3], 6))