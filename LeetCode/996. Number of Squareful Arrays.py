class Solution(object):
    def numSquarefulPerms(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        import collections
        c = collections.Counter(A)
        cand = {i: {j for j in c if int((i + j)**0.5) ** 2 == i + j} for i in c}
        self.res = 0
        def dfs(x, left=len(A) - 1):
            c[x] -= 1
            if left == 0:
                self.res += 1
            for y in cand[x]:
                if c[y]:
                    dfs(y, left - 1)
            c[x] += 1
        for x in c:
            dfs(x)
        return self.res
