class Solution:
    def maxPower(self, s: str) -> int:
        res = 1
        count = 1
        prev = 0
        for i in range(1, len(s)):
            if s[prev] == s[i]:
                count += 1
                res = max(res, count)
            else:
                count = 1
            prev = i
        return res