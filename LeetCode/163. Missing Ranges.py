class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if not nums:
            if lower == upper:
                return ["{}".format(lower)]
            else:
                return ["{}->{}".format(lower, upper)]
        res = []
        if lower == upper:
            if lower in nums:
                return []
            else:
                return [str(lower)]
        if lower == nums[0]-1:
            res.append('{}'.format(lower))
        if lower < nums[0]-1:
            res.append('{}->{}'.format(lower, nums[0]-1))
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1 or nums[i+1] - nums[i] == 0:
                continue
            elif nums[i+1] - nums[i] == 2:
                res.append(str(nums[i]+1))
            else:
                res.append('{}->{}'.format(nums[i]+1, nums[i+1]-1))
        if upper == nums[-1]+1:
            res.append('{}'.format(upper))
        if upper > nums[-1]+1:
            res.append('{}->{}'.format(nums[-1]+1, upper))
        return res

test = Solution()
print(test.findMissingRanges([0, 1, 3, 50, 75], 0, 99))
print(test.findMissingRanges([], 1, 10))
print(test.findMissingRanges([], 1, 1))
print(test.findMissingRanges([1, 1, 1], 1, 1))
print(test.findMissingRanges([1, 1, 1], 2, 2))
print(test.findMissingRanges([-2147483648, -2147483648, 0, 2147483647, 2147483647], -2147483648, 2147483647))