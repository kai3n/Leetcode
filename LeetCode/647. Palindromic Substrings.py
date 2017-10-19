# class Solution(object):
#     def countSubstrings(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         # Brute Force Algorithm
#         count = 0
#         for i in range(len(s)):
#             for j in range(len(s)-i):
#                 if s[j:j+i+1] == s[j:j+i+1][::-1]:
#                     count += 1
#         return count
#
# test = Solution()
# print(test.countSubstrings("abcgqadbbggrfeeetjioeeqdk"))
#
# def countSubstrings(self, S):
#     N = len(S)
#     ans = 0
#     for center in range(2*N - 1):
#         left = center / 2
#         right = left + center % 2
#         while left >= 0 and right < N and S[left] == S[right]:
#             ans += 1
#             left -= 1
#             right += 1
#     return ans
#
class Solution(object):
    def countSubstrings(self, s):

        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        count = 0
        k = 0
        for i in range(len(s)):
            for j in range(len(s) - k):
                if k == 0:
                    dp[j][j + k] = True
                elif k == 1 and s[j] == s[j + k]:
                    dp[j][j + k] = True
                elif s[j] != s[j + k]:
                    continue
                else:  # same character
                    if 0 <= j + 1 < len(s) and 0 <= j + k - 1 < len(s):
                        dp[j][j + k] = dp[j + 1][j + k - 1]
            k += 1

        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if dp[i][j] == True:
                    count += 1

        return count

test = Solution()
print(test.countSubstrings('abaabc'))