class Solution:
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = list(map(str, str(N)))
        print(s)
        m = len(s)
        for i in range(len(s) - 1, 0, -1):
            if s[i - 1] > s[i]:
                m = i
                s[i - 1] = chr(ord(s[i - 1]) - 1)
        for i in range(m, len(s)):
            s[i] = "9"
        return int("".join(s))
