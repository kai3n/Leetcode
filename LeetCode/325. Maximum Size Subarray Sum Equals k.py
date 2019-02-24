class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        num_sum = 0
        num_max = 0
        d = {}

        for i in range(len(nums)):
            num_sum += nums[i]
            if num_sum == k:
                num_max = i + 1
            elif d.get(num_sum - k) is not None:
                num_max = max(num_max, i - d.get(num_sum - k))
            if d.get(num_sum) is None:
                d[num_sum] = i
        return num_max