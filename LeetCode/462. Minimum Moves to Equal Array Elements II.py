class Solution(object):
    def minMoves2(self, nums):
        nums.sort()
        count = 0
        for num in nums:
            count += abs(num - nums[len(nums)//2])
        return count

test = Solution()
print(test.minMoves2([1, 2, 3]))