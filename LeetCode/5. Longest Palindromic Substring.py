
class Solution(object):
    lo = 0
    maxLen = -1
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if l < 2:
            return s
        for i in range(l-1):
            self.extendPalindrome(s, i, i)
            self.extendPalindrome(s, i, i+1)
        return s[self.lo:self.lo+self.maxLen]

    def extendPalindrome(self, s, j, k):
        while j >= 0 and k < len(s) and s[j] == s[k]:
            j -= 1
            k += 1
        if self.maxLen < k - j - 1:
            self.lo = j + 1
            self.maxLen = k - j - 1






# Brute Force Algorithm
# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         if len(s) < 1:
#             return ''
#         curString = s[0]
#         for i in range(len(s)):
#             for j in range(i+1, len(s)):
#                 if s[i:j+1] == s[i:j+1][::-1] and j+1-i > len(curString):
#                     curString = s[i:j+1]
#         return curString

test = Solution()
# print(test.longestPalindrome('babad'))
# print(test.longestPalindrome('aasdjlkasdlhhrukvenrkvndfjkekajdnqwdnavgb'))
print(test.longestPalindrome('aasdjlkasdlhhrukvenrkvndfjkekajdnqwdnavgb'))



