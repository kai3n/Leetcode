class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = max(nums)
        max_idx = 0
        for i, num in enumerate(nums):
            if num == max_num:
                max_idx = i
                continue
            if num * 2 > max_num:
                return -1
        return max_idx


