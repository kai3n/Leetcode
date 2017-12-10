class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 2:
            return 0

        result = 0
        product = 1
        i = 0
        right = 0

        while right < len(nums):
            product *= nums[right]
            while i < len(nums) and product >= k:
                product /= nums[i]
                i += 1
            result += right - i + 1
            right += 1
        return result

