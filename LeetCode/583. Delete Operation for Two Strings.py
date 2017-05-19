class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        for j in range(len(word1)):
            for i in range(len(word2)):
                dp[j + 1][i + 1] = max(dp[j][i + 1], dp[j + 1][i], dp[j][i] + (word1[j] == word2[i]))
        return len(word1) + len(word2) - 2 * dp[-1][-1]


test = Solution()
#print(test.minDistance("sea", "eat"))
print(test.minDistance("sea", "ate"))
