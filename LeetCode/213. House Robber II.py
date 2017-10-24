def helper(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    dp = [0] * (len(nums))
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(1, len(nums)):
        if i - 2 >= 0:
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        else:
            dp[i] = max(dp[i - 1], nums[i])
    return dp[-1]

class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[:-1]), helper(nums[1:]))

nums = [1,3,2,6,7,4,2,4]
nums = [1]
test = Solution()
print(test.rob(nums))
"""
1 3 2 6
1 3 3 9
"""