class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        nums = [1, 7, 3, 6, 5, 6]
        left_dp =  [1, 8, 11, 17, 22, 28]
        right_dp = [28, 27, 20, 17, 11, 6]
        """
        if not nums:
            return -1
        if len(nums) == 1:
            return 0

        left_dp = [i for i in nums]
        right_dp = [i for i in nums]

        for i in range(1, len(left_dp)):
            left_dp[i] += left_dp[i - 1]
        for i in range(len(right_dp) - 2, -1, -1):
            right_dp[i] += right_dp[i + 1]
        for i in range(len(nums)):
            if left_dp[i] == right_dp[i]:
                return i
        return -1
