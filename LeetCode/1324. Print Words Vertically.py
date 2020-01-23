class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        s = s.split()
        m = max(map(len, s))
        r = []
        for i in range(m):
            l = []
            for w in s:
                l.append(w[i] if i < len(w) else ' ')
            r.append(''.join(l).rstrip())
        return r