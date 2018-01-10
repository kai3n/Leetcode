class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        t = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                t += 1
                nums[t] = nums[i]
        return t + 1