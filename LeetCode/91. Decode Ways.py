class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)
        if n == 0:
            return 0

        memo = [0 for _ in range(n+1)]
        memo[n] = 1
        memo[n-1] = 1 if s[n-1] != '0' else 0

        for i in range(n - 2, -1, -1):
            if s[i] == '0':
                continue
            else:
                memo[i] = memo[i + 1] + memo[i + 2] if int(s[i:i + 2]) <= 26 else memo[i + 1]
        return memo[0]


s1 = "13322"
s2 = "0"
s3 = "00"
s4 = "01"
s5 = "110"
s6 = "10"
s7 = "111"
test = Solution()
print(test.numDecodings(s1))
print(test.numDecodings(s2))
print(test.numDecodings(s3))
print(test.numDecodings(s4))
print(test.numDecodings(s5))
print(test.numDecodings(s6))
print(test.numDecodings(s7))

