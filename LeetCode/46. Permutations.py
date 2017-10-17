# class Solution(object):
#     def permute(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         return [[n] + p
#                  for i, n in enumerate(nums)
#                     for p in self.permute(nums[:i]+nums[i+1:]) or [[]]]
#
# test = Solution()
# print(test.permute([1,2,3]))

#list(itertools.permutations(nums))

# DFS
class Solution(object):
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res


    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)

test = Solution()
print(test.permute([1,2,3]))