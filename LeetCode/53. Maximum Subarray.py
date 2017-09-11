# class Solution(object):
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if len(nums) == 1:
#             return nums[0]
#         if max(nums) <= 0:
#             return max(nums)
#
#         maxCur = 0
#         maxSofar = 0
#
#         for i in range(len(nums)):
#             maxCur += nums[i]
#             maxCur = max(0, maxCur)
#             maxSofar = max(maxCur, maxSofar)
#         return maxSofar

class Solution:
    # @param A, a list of integers
    # @return an integer
    # 6:57
    def maxSubArray(self, A):
        if not A:
            return 0

        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum

nums = [-2,-1,-3,-4,-1,-2,-1,-5,-4]

test = Solution()
print(test.maxSubArray(nums))