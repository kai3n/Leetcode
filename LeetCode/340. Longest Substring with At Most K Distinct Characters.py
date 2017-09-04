# Brute Force Solution - time limit
# class Solution(object):
#     def lengthOfLongestSubstringKDistinct(self, s, k):
#         """
#         :type s: str
#         :type k: int
#         :rtype: int
#         """
#         if not s:
#             return 0
#         if not k:
#             return 0
#         maxlen = 1
#         for i in range(len(s)):
#             for j in range(i+1, len(s)):
#                 if len(set(s[i:j+1])) <= k:
#                     maxlen = max(maxlen, j-i+1)
#         return maxlen
#
# test = Solution()
# print(test.lengthOfLongestSubstringKDistinct("ece", 2))
# print(test.lengthOfLongestSubstringKDistinct("a", 1))
# print(test.lengthOfLongestSubstringKDistinct("a", 0))
# print(test.lengthOfLongestSubstringKDistinct("aa", 2))

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        d = {}
        low, ret = 0, 0
        for i, c in enumerate(s):
            d[c] = i
            if len(d) > k:
                low = min(d.values())
                del d[s[low]]
                low += 1
            ret = max(i - low + 1, ret)
        return ret

test = Solution()
print(test.lengthOfLongestSubstringKDistinct("eceadddea", 2))
print(test.lengthOfLongestSubstringKDistinct("a", 1))
print(test.lengthOfLongestSubstringKDistinct("a", 0))
print(test.lengthOfLongestSubstringKDistinct("aa", 2))

# easy version
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        charCount, left, distinct, result = [0] * 128, 0, 0, 0
        for right, ch in enumerate(s):
            ascii = ord(ch)
            if not charCount[ascii]: distinct += 1
            charCount[ascii] += 1
            while distinct > k:
                ascii = ord(s[left])
                if charCount[ascii] == 1: distinct -= 1
                charCount[ascii] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result

test = Solution()
print(test.lengthOfLongestSubstringKDistinct("eceadddea", 2))
print(test.lengthOfLongestSubstringKDistinct("a", 1))
print(test.lengthOfLongestSubstringKDistinct("a", 0))
print(test.lengthOfLongestSubstringKDistinct("aa", 2))

