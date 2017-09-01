class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = map(str, nums)
        if len(nums) <= 2: return '/'.join(nums)
        return '{}/({})'.format(nums[0], '/'.join(nums[1:]))

test = Solution()
print(test.optimalDivision([1000,100,10,2]))