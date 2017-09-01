class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Brute Force Algorithm
        count = 0
        for i in range(len(s)):
            for j in range(len(s)-i):
                if s[j:j+i+1] == s[j:j+i+1][::-1]:
                    count += 1
        return count

test = Solution()
print(test.countSubstrings("abcgqadbbggrfeeetjioeeqdk"))

def countSubstrings(self, S):
    N = len(S)
    ans = 0
    for center in range(2*N - 1):
        left = center / 2
        right = left + center % 2
        while left >= 0 and right < N and S[left] == S[right]:
            ans += 1
            left -= 1
            right += 1
    return ans