class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1
        for i in range(1, len(nums) - 1):
            if nums[i - 1] < nums[i] > nums[i + 1]:
                return i
        return len(nums) - 1 if nums[-1] > nums[0] else 0
