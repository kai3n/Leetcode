class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        num_sum = i = j = 0
        min_len = len(nums) + 1
        while j < len(nums):
            num_sum += nums[j]
            while num_sum >= s:
                min_len = min(min_len, j-i+1)
                num_sum -= nums[i]
                i += 1
            j += 1
        return min_len % (len(nums) + 1)