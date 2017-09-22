class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        r = []
        d = dict()
        if len(s) < 10:
            return r

        for i in range(len(s)-10+1):

            if d.get(s[i:i + 10], -1) == -1:
                d[s[i:i + 10]] = 1
            else:
                d[s[i:i + 10]] += 1

        for k, v in d.items():
            if v > 1:
                r.append(k)
        return r




s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
s2 = "AAAAAAAAAAA"
test = Solution()
print(test.findRepeatedDnaSequences(s))
print(test.findRepeatedDnaSequences(s2))
