class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        if nums[0] > target:
            return 0
        while i < len(nums):
            if nums[i] >= target:
                return i
            i += 1
        return len(nums)