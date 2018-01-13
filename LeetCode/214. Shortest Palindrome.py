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

        for i in range(len(s)-1, -1, -1):
            if is_palindrome(s[:i+1]):
                return s[i + 1:][::-1] + s
        return s[i + 1:][::-1] + s

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''

        l = 0
        r = len(s) - 1
        k = r

        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                l = 0
                r = k-1
                k = r
        return s[k+1:][::-1] + s

def shortestPalindrome(self, s):
    r = s[::-1]
    for i in range(len(s) + 1):
        if s.startswith(r[i:]):
            return r[:i] + s

s = "aacecaaa"
test = Solution()
print(test.shortestPalindrome(s))

# KMP Algorithm
def shortestPalindrome(s):
    A=s+"*"+s[::-1]
    cont=[0]
    for i in range(1,len(A)):
        index=cont[i-1]
        while(index>0 and A[index]!=A[i]):
            index=cont[index-1]
        cont.append(index+(1 if A[index]==A[i] else 0))
    return s[cont[-1]:][::-1]+s

s = "aacecaaa"
print(shortestPalindrome(s))
