import bisect
def countSmaller(self, nums):
    counts, sortednums = [], []
    for i in range(len(nums)-1,-1, -1):
        position = bisect.bisect_left(sortednums, nums[i])
        sortednums.insert(position, nums[i])
        counts.append(position)
    return counts[::-1]