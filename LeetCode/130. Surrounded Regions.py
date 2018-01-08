#AC Solution

class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def dfs(board, y, x):
            if board[y][x] == "X":
                return
            else:
                board[y][x] = "Y"
                for i, j in [1, 0], [-1, 0], [0, 1], [0, -1]:
                    if 0 <= y + i < len(board) and 0 <= x + j < len(board[0]):
                        if board[y + i][x + j] == "O":
                            dfs(board, y + i, x + j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1:
                    dfs(board, i, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "Y":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"


