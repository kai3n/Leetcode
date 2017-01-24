# #time limit code
# class Solution(object):
#     def findTargetSumWays(self, nums, S):
#         """
#         :type nums: List[int]
#         :type S: int
#         :rtype: int
#         """
#         l = len(nums)
#         b = [bin(i)[2:].zfill(l) for i in range(2**l)]
#         cnt = 0
#         for a in b:
#             sum = 0
#             for i in range(l):
#                 if a[i] == "1":
#                     sum += nums[i]
#                 else:
#                     sum -= nums[i]
#             if sum == S:
#                 cnt += 1
#         return cnt
#
#
#
#
# DP solution
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        l = len(nums)
        d = {nums[0]:1, -nums[0]:1} if nums[0] > 0 else {0:2}
        # temporary dictionary
        td = dict()
        for i in range(1,l):
            td = dict()
            for k in d:
                td[k+nums[i]] = td.get(k+nums[i], 0) + d[k]
                td[k-nums[i]] = td.get(k-nums[i], 0) + d[k]
            d = td
        return d.get(S,0)

nums=[0,0,0,0,0,0,0,0,1]
S = 1
test = Solution()
print(test.findTargetSumWays(nums, S))
