class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        board2 = []
        for i in board:
            board2.append(list(i))
        board = board2

        y = click[0]
        x = click[1]
        q = []
        if board[y][x] == 'M':
            board[y][x] = 'X'
            board2 = []

            for i in board:
                board2.append(''.join(i))
            board = board2

            return board
        else:
            q.append((y, x))
            seen = {(y, x)}
            while len(q) != 0:
                y, x = q.pop(0)
                m = 0
                for i in range(y - 1, y + 2):
                    for j in range(x - 1, x + 2):
                        if 0 <= i < len(board) and 0 <= j < len(board[0]) and (i != y or j != x):
                            if board[i][j] == 'E' and (i, j) not in seen:
                                q.append((i, j))
                            if board[i][j] == 'M':
                                m += 1
                            seen.add((i, j))
                if m == 0:
                    board[y][x] = 'B'
                else:
                    board[y][x] = str(m)

            board2 = []
            for i in board:
                board2.append(''.join(i))
            board = board2

            return board







input = [['E', 'E', 'E', 'E', 'E'],
         ['E', 'E', 'M', 'E', 'E'],
         ['E', 'E', 'E', 'E', 'E'],
         ['E', 'E', 'E', 'E', 'E']]

input2 = [['B', '1', 'E', '1', 'B'],
         ['B', '1', 'M', '1', 'B'],
         ['B', '1', '1', '1', 'B'],
         ['B', 'B', 'B', 'B', 'B']]

input3 = ["EEEEE","EEMEE","EEEEE","EEEEE"]


test = Solution()
print(test.updateBoard(input3, [3,0]))


"""
class Solution(object):
    def updateBoard(self, A, click):
        click = tuple(click)
        R, C = len(A), len(A[0])

        def neighbors(r, c):
            for dr in xrange(-1, 2):
                for dc in xrange(-1, 2):
                    if (dr or dc) and 0 <= r + dr < R and 0 <= c + dc < C:
                        yield r + dr, c + dc

        stack = [click]
        seen = {click}
        while stack:
            r, c = stack.pop()
            if A[r][c] == 'M':
                A[r][c] = 'X'
            else:
                mines_adj = sum( A[nr][nc] in 'MX' for nr, nc in neighbors(r, c) )
                if mines_adj:
                    A[r][c] = str(mines_adj)
                else:
                    A[r][c] = 'B'
                    for nei in neighbors(r, c):
                        if A[nei[0]][nei[1]] in 'ME' and nei not in seen:
                            stack.append(nei)
                            seen.add(nei)
        return A
"""