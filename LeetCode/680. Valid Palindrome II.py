class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s)-1
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return s[i:j] == s[i:j][::-1] or s[i+1:j+1] == s[i+1:j+1][::-1]
        return True