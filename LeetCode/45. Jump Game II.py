class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [float('inf')]*len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(1, nums[i] + 1):
                if i + j < len(nums):
                    dp[i + j] = min(dp[i + j], dp[i]+1)
        return dp[-1]


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_end = cur_farthest = jump = 0
        for i in range(len(nums)-1):
            cur_farthest = max(cur_farthest, nums[i]+i)
            if cur_end == i:
                cur_end = cur_farthest
                jump += 1
        return jump