# Time Limit Solution
class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        def dfs(board, y, x, visited, letters, words):
            for word in words:
                if word == letters and word not in res:
                    res.append(word)
                elif word.startswith(letters):
                    for i, j in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        if 0 <= y + i < len(board) and 0 <= x + j < len(board[0]):
                            if not visited[y + i][x + j]:
                                visited[y + i][x + j] = True
                                dfs(board, y + i, x + j, visited, letters + board[y + i][x + j], words)
                                visited[y + i][x + j] = False

        for i in range(len(board)):
            for j in range(len(board[0])):
                visited[i][j] = True
                dfs(board, i, j, visited, board[i][j], words)
                visited[i][j] = False

        return res