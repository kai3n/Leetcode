class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        total_len = 2 ** len(nums)

        bin_arr = []
        res = []
        for i in range(total_len):
            bin_arr.append(bin(i)[2:].zfill(len(nums)))
        for each in bin_arr:
            subset = []
            for j in range(len(each)):
                if each[j] == "1":
                    subset.append(nums[j])
            res.append(subset)
        return res


# DFS recursively
def subsets1(self, nums):
    res = []
    self.dfs(sorted(nums), 0, [], res)
    return res


def dfs(self, nums, index, path, res):
    res.append(path)
    for i in range(index, len(nums)):
        self.dfs(nums, i + 1, path + [nums[i]], res)