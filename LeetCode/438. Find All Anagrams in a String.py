# class Solution(object):
#     def findAnagrams(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: List[int]
#         """
#         output = []
#         d1 = {}
#         d2 = {}
#         for i in range(len(s)-len(p)+1):
#             for j in s[i:i+len(p)]:
#                if d1.get(j,0) == 0:
#                    d1[j] = 1
#                else:
#                    d1[j] += 1
#
#             for k in p:
#                if d2.get(k, 0) == 0:
#                    d2[k] = 1
#                else:
#                    d2[k] += 1
#             if d1 == d2:
#                 output.append(i)
#             d1 = {}
#             d2 = {}
#         return output

from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        pCounter = Counter(p)
        sCounter = Counter(s[:len(p) - 1])
        for i in range(len(p) - 1, len(s)):
            sCounter[s[i]] += 1  # include a new char in the window
            if sCounter == pCounter:  # This step is O(1), since there are at most 26 English letters
                res.append(i - len(p) + 1)  # append the starting index
            sCounter[s[i - len(p) + 1]] -= 1  # decrease the count of oldest char in the window
            if sCounter[s[i - len(p) + 1]] == 0:
                del sCounter[s[i - len(p) + 1]]  # remove the count if it is 0
        return res

s = "cbaebabacd"
p = "abc"
s1 = "abab"
p1 = "ab"
s2 = "ababababab"
p2 = "aab"
test = Solution()
print(test.findAnagrams(s, p))
print(test.findAnagrams(s1, p1))
print(test.findAnagrams(s2, p2))