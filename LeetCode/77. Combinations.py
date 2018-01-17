#Time limit solution
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        l = range(1, n+1)
        res = []
        def helper(l, v, m, k):
            if k == 0:
                possible = True
                for j in res:
                    if set(m) == set(j):
                        possible = False
                if possible:
                    res.append(m)
                return
            for i in l:
                if i not in v:
                    v.add(i)
                    helper(l[:i] + l[i+1:], v, m + [i], k-1)
                    v.remove(i)
        helper(l, set(), [], k)
        return list(res)

# Optimized solution
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(range(1, n + 1), k, [], res)
        return res

    def dfs(self, nums, k, path, res):
        if k == 0:
            res.append(path)
            return
        if len(nums) >= k:
            for i in range(len(nums)):
                self.dfs(nums[i + 1:], k - 1, path + [nums[i]], res)
        return