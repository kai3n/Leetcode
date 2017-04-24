class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        nums = sorted(nums)
        for i in range(len(nums)):
            if i % 2 == 0:
                sum += nums[i]
        return sum
        # return sum(sorted(nums)[::2])

test = Solution()
print(test.arrayPairSum([]))
print(test.arrayPairSum([1,4,3,2]))
print(test.arrayPairSum([1,4,3,2,5,6]))