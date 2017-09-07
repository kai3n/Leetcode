class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                countSum = sum([board[im][jn] % 2 for im in range(i - 1, i + 2) for jn in range(j - 1, j + 2) if
                                0 <= im < m and 0 <= jn < n]) - board[i][j]
                if board[i][j] == 0 or board[i][j] == 2:
                    if countSum == 3:
                        board[i][j] = 2
                else:
                    if countSum < 2 or countSum > 3:
                        board[i][j] = 3
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2: board[i][j] = 1
                if board[i][j] == 3: board[i][j] = 0


test = Solution()
print(test.gameOfLife([[0]]))