class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        prev = -1
        for i in range(len(nums)):
            if nums[i]:
                if prev == -1:
                    prev = i
                else:
                    if i - prev <= k:
                        return False
                    prev = i
        return True
