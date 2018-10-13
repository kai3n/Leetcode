class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        res = 0
        i = j = 0
        d = dict()
        while i < len(s):
            if d.get(s[i], -1) != -1:
                j = max(j, d.get(s[i])+1)
            d[s[i]] = i
            res = max(res, i - j + 1)
            i += 1
        return res


class Solution:
    def lengthOfLongestSubstring(self, s):
        d = {}
        start = 0
        max_len = 0

        for i in range(len(s)):
            if d.get(s[i]) is not None and start <= d.get(s[i]):
                start = d.get(s[i]) + 1
            d[s[i]] = i
            max_len = max(max_len, i - start + 1)
        return max_len