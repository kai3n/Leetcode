class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = [-1 for _ in range(len(nums)+1)]
        for i in nums:
            l[i] = 1
        for a in range(len(nums)+1):
            if l[a] == -1:
                return a

# better idea
def missingNumber(self, nums):
    n = len(nums)
    return n * (n+1) / 2 - sum(nums)