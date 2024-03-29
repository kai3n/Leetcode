class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        if len(matrix) == str(1):
            if "1" in matrix[0]:
                return 1
            else:
                return 0
        if len(matrix[0]) == str(1):
            for i in range(len(matrix)):
                if matrix[i][0] == str(1):
                    return 1
            return 0

        dp = [[int(matrix[i][j]) for j in range(len(matrix[0]))] for i in range(len(matrix))]

        maxSquare = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == str(0):
                    continue
                else:
                    if 0 > i - 1 or 0 > j - 1:
                        maxSquare = max(maxSquare, dp[i][j])
                        continue
                    if dp[i - 1][j - 1] == 0:
                        dp[i][j] == 1
                    else:
                        step = dp[i - 1][j - 1]
                        c = 0
                        f = True
                        while i - c >= 0 and j - c >= 0 and c <= step:
                            if dp[i - c][j] == 0 or dp[i][j - c] == 0:
                                f = False
                                break
                            c += 1
                        if f:
                            dp[i][j] = dp[i - 1][j - 1] + 1
                        else:
                            dp[i][j] = c

                    maxSquare = max(maxSquare, dp[i][j])

        for i in range(len(dp)):
            for j in range(len(dp[0])):
                print(dp[i][j], " ", end='')
            print()
        return maxSquare ** 2

class Solution(object):
    def maximalSquare(self, matrix):
        if len(matrix) == 0:
            return 0
        res = 0
        dp = [[0 for j in range(len(matrix[0])+1)] for i in range(len(matrix)+1)]
        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + 1
                    res = max(res, dp[i][j])
        return res**2

matrix = [[1,0,1,0,0],
          [1,0,1,1,1],
          [1,1,1,1,1],
          [1,0,0,1,0]]

matrix = [["0","1"],
          ["1","0"]]

# matrix = [["0","0","0","1"],
#           ["1","1","0","1"],
#           ["1","1","1","1"],
#           ["0","1","1","1"],
#           ["0","1","1","1"]]

# matrix = [["1","0","1","0","0"],
#           ["1","0","1","1","1"],
#           ["1","1","1","1","1"],
#           ["1","0","0","1","0"]]

# matrix = [["0","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","0"],
#           ["1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
#           ["1","1","0","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],
#           ["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1"],
#           ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1"],
#           ["1","1","1","0","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1"],
#           ["1","0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1"],
#           ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0"],
#           ["0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1"],
#           ["1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1"],
#           ["1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],
#           ["0","1","1","0","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],
#           ["1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","1","1","1"],
#           ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
#           ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
#           ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","0","1"],
#           ["1","1","1","1","1","1","1","1","0","1","1","0","1","1","0","1","1","1","1"],
#           ["1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","0","1","1","1"]]
#
# matrix = [["1","0","1","0","0"],
#           ["1","0","1","1","1"],
#           ["1","1","1","1","1"],
#           ["1","0","0","1","0"]]
test = Solution()
print(test.maximalSquare(matrix))

