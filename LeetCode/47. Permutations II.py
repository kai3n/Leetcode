def dfs(nums, path, res):
    if not nums:
        res.add(tuple(path))
    for i in range(len(nums)):
        dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        path = []
        dfs(nums, path, res)
        return list(map(list, res))

test = Solution()
print(test.permuteUnique([3,3,0,0,2,3,2]))


def permuteUnique(self, nums):
    if not nums: return []
    return [list(t) for t in self.perm(nums, 0)]


# returns a set of tuples, representing the unique permutations of
# the numbers which appear after (including) the index "start"
def perm(self, nums, start):
    if start == len(nums) - 1: return {(nums[start],)}
    s = set()
    for r in self.perm(nums, start + 1):
        # generate new permutations by inserting the current element into different positions of r
        for i in range(len(nums) - start):
            s.add(r[:i] + (nums[start],) + r[i:])
    return s
