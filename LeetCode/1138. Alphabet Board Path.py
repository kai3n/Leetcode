class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        dic = defaultdict(tuple)
        res = ""
        cur = (0, 0)
        for i in range(len(board)):
            for j in range(len(board[i])):
                dic[board[i][j]] = (i, j)
        for i in range(len(target)):
            if target[i] == board[cur[0]][cur[1]]:
                res += "!"
                continue
            topdown = dic[target[i]][0] - cur[0]
            leftright = dic[target[i]][1] - cur[1]
            if board[cur[0]][cur[1]] == "z":
                if topdown > 0:
                    res += "D"*topdown
                elif topdown < 0:
                    res += "U"*-topdown
                if leftright > 0:
                    res += "R"*leftright
                elif leftright < 0:
                    res += "L"*-leftright
            else:
                if leftright > 0:
                    res += "R"*leftright
                elif leftright < 0:
                    res += "L"*-leftright
                if topdown > 0:
                    res += "D"*topdown
                elif topdown < 0:
                    res += "U"*-topdown
            res += "!"
            cur = (dic[target[i]][0], dic[target[i]][1])
        return res
                
            
