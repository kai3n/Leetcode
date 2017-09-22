class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        arr = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if j == 0 or i == 0:
                    arr[i][j] = 1
                else:
                    if 0 <= i-1 < m and 0 <= j-1 < n:
                        arr[i][j] = arr[i-1][j] + arr[i][j-1]
        return arr[-1][-1]

test = Solution()
print(test.uniquePaths(3, 7))


