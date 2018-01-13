import bisect

def countSmaller(nums):
    counts, sortednums = [], []
    for i in range(len(nums)-1,-1, -1):
        position = bisect.bisect_left(sortednums, nums[i])
        sortednums.insert(position, nums[i])
        counts.append(position)
    return counts[::-1]

nums = [5, 2, 6, 1]
print(countSmaller(nums))


#Brilliant Soltuion

def countSmaller(self, nums):
    def sort(enum):
        half = len(enum) / 2
        if half:
            left, right = sort(enum[:half]), sort(enum[half:])
            for i in range(len(enum))[::-1]:
                if not right or left and left[-1][1] > right[-1][1]:
                    smaller[left[-1][0]] += len(right)
                    enum[i] = left.pop()
                else:
                    enum[i] = right.pop()
        return enum
    smaller = [0] * len(nums)
    sort(list(enumerate(nums)))
    return smaller