class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        if not nums:
            return res

        for i in range(len(nums) - k + 1):
            res.append(max(nums[i:i + k]))
        return res