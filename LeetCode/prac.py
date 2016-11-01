def twoSum(nums, target):
    dic = {}
    for i, num in enumerate(nums):
        if num in dic:
            return [dic[num], i]
        else:
            dic[target - num] = i

print(twoSum([3,7,2,4], 9))