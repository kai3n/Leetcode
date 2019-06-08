class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0
        dp = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        found = False
        for i in range(len(dp[0])):
            dp[0][i] = 1
            if obstacleGrid[0][i] == 1:
                found = True
            if found:
                dp[0][i] = 0
        found = False
        for i in range(len(dp)):
            dp[i][0] = 1
            if obstacleGrid[i][0] == 1:
                found = True
            if found:
                dp[i][0] = 0

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                else:
                    prev1 = 0 if obstacleGrid[i - 1][j] else dp[i - 1][j]
                    prev2 = 0 if obstacleGrid[i][j - 1] else dp[i][j - 1]
                    dp[i][j] = prev1 + prev2
        print(dp)
        return dp[-1][-1]
