class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        s = s.lower()

        while left < right:
            if not s[left].isalpha() and not s[left].isdigit():
                left += 1
            elif not s[right].isalpha() and not s[right].isdigit():
                right -= 1
            elif s[left] == s[right]:
                left += 1
                right -= 1
            elif s[left] != s[right]:
                return False
        return True

# concise solution
class Solution:
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1;
            r -= 1
        return True
