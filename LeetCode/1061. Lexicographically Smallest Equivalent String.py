class Solution(object):
    def smallestEquivalentString(self, A, B, S):
        """
        :type A: str
        :type B: str
        :type S: str
        :rtype: str
        """
        self.l = range(26)

        def find(x):
            if self.l[x] != x:
                self.l[x] = find(self.l[x])
            return self.l[x]

        def union(x, y):
            xr = find(x)
            yr = find(y)
            if xr > yr:
                self.l[xr] = yr
            else:
                self.l[yr] = xr

        for a, b in zip(A, B):
            union(ord(a) - 97, ord(b) - 97)
        print(self.l)
        res = ""
        for s in S:
            res += chr(find(ord(s) - 97) + 97)
        return res

