class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []

        def is_palindrome(s):
            return s == s[::-1]

        def dfs(s, p):
            if not s:
                res.append(p)
            for i in range(len(s)):
                if is_palindrome(s[:i + 1]):
                    dfs(s[i + 1:], p + [s[:i + 1]])

        dfs(s, [])
        return res