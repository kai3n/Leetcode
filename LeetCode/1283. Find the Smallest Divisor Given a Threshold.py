class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        total = sum(nums)
        left = 1
        right = total
        def helper(nums, divisor):
            return sum(map(int, map(ceil, [float(num)/divisor for num in nums])))
        
        while left < right:
            mid = (left + right) // 2
            res = helper(nums, mid)
            if res > threshold:
                left = mid + 1
            elif res <= threshold:
                right = mid
        return right
