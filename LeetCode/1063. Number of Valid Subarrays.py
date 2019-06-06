class Solution(object):
    def validSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stk = [[float("-inf"), len(nums)]]
        count = 0
        for i in range(len(nums))[::-1]:
            while stk[-1][0] >= nums[i]:
                stk.pop()
            count+=stk[-1][1] - i
            stk.append([nums[i], i])
        return count