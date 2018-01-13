"""
Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".
"""

# Time Limit Solution
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''

        def is_palindrome(s):
            return s == s[::-1]

        idx = -1
        for i in range(len(s)):
            if is_palindrome(s[:i+1]):
                idx = i
        return s[idx+1:][::-1] + s

s = "ab"
test = Solution()
print(test.shortestPalindrome(s))


