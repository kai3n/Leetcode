# Time Limit Exceeded
class Solution:
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def hammingDistance(num1, num2):
            return bin(num1^num2)[2:].count('1')
        total = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                total += hammingDistance(nums[i], nums[j])
        return total