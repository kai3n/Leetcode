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