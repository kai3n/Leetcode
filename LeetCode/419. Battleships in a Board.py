class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """

        extendedBoard = [["O" for _ in range(len(board[0])+2)] for _ in range(len(board)+2)]
        visitCheck = [[False for _ in range(len(board[0])+2)] for _ in range(len(board)+2)]
        for a in range(len(board[0])):
            for b in range(len(board)):
                extendedBoard[b+1][a+1] = board[b][a]
        stack = []
        count = 0
        for a in range(1,len(extendedBoard[0])-1):
            for b in range(1, len(extendedBoard)-1):
                if len(stack) == 0:
                    if extendedBoard[b][a] == "X" and visitCheck[b][a] == False:
                        visitCheck[b][a] = True
                        count += 1
                        stack.append((b,a))

                while len(stack) != 0:
                    j, i = stack.pop()

                    if extendedBoard[j][i-1] == "X" and visitCheck[j][i-1] == False:
                        stack.append((j,i-1))
                    visitCheck[j][i-1] = True
                    if extendedBoard[j][i+1] == "X" and visitCheck[j][i+1] == False:
                        stack.append((j,i+1))
                    visitCheck[j][i+1] = True
                    if extendedBoard[j-1][i] == "X" and visitCheck[j-1][i] == False:
                        stack.append((j-1,i))
                    visitCheck[j-1][i] = True
                    if extendedBoard[j+1][i] == "X" and visitCheck[j+1][i] == False:
                        stack.append((j+1,i))
                    visitCheck[j+1][i] = True
        return count


board = ["XOOX",
         "OOOX",
         "OOOX"]

test = Solution()
print(test.countBattleships(board))


# simple solution
class Solution(object):
    def countBattleships(self, board):
        if len(board) == 0: return 0
        m, n = len(board), len(board[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and (i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1] == '.'):
                    count += 1
        return count