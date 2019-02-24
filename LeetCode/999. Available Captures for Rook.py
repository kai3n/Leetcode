class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        rook_x = 0
        rook_y = 0
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "R":
                    rook_y = i
                    rook_x = j

        for w in range(rook_x - 1, -1, -1):
            if board[rook_y][w] == "B":
                break
            if board[rook_y][w] == "p":
                count += 1
                break
        for e in range(rook_x + 1, len(board[0])):
            if board[rook_y][e] == "B":
                break
            if board[rook_y][e] == "p":
                count += 1
                break
        for n in range(rook_y - 1, -1, -1):
            if board[n][rook_x] == "B":
                break
            if board[n][rook_x] == "p":
                count += 1
                break
        for s in range(rook_y + 1, len(board)):
            if board[s][rook_x] == "B":
                break
            if board[s][rook_x] == "p":
                count += 1
                break
        return count