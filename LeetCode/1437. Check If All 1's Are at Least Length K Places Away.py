class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        left = right = 0
        while right < len(nums):
            while left < len(nums) and not nums[left]:
                left += 1
            right = left + 1
            while right < len(nums) and not nums[right]:
                right += 1
            if right >= len(nums):
                break
            if right - left > k:
                left = right
            else:
                return False
        return True
