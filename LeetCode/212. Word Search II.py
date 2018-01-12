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

# Trie and DFS
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.flag = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.result = []

    def insert(self, word):
        node = self.root
        for letter in word:
            node = node.children[letter]
        node.flag = True

    def findWords(self, board, words):
        for w in words:
            self.insert(w)
        for j in range(len(board)):
            for i in range(len(board[0])):
                self.dfs(self.root, board, j, i)
        return self.result

    def dfs(self, node, board, j, i, word=''):
        if node.flag:
            self.result.append(word)
            node.flag = False
        if 0 <= j < len(board) and 0 <= i < len(board[0]):
            char = board[j][i]
            child = node.children.get(char)
            if child is not None:
                word += char
                board[j][i] = None
                self.dfs(child, board, j + 1, i, word)
                self.dfs(child, board, j - 1, i, word)
                self.dfs(child, board, j, i + 1, word)
                self.dfs(child, board, j, i - 1, word)
                board[j][i] = char