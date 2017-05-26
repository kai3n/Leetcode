class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        return (sum(numSet) * 3 - sum(nums)) // 2

input = [1]
test = Solution()
print(test.singleNumber(input))