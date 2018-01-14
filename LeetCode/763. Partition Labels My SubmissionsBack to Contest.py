class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res = []
        def helper(s):
            if not s:
                return
            ss = s[::-1]
            l = 0
            r = len(ss) - ss.index(s[l]) - 1
            while l < r:
                l += 1
                if len(ss) - ss.index(s[l]) - 1 > r:
                    r = len(ss) - ss.index(s[l]) - 1
            res.append(r+1)
            helper(s[r+1:])
        helper(S)
        return res