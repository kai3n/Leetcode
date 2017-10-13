class Solution(object):
    def canWin(self, s):
        s = list(map(str, s))
        for i in range(len(s)-1):
            if s[i] == "+" and s[i+1] == "+":
                s[i] = s[i+1] = "-"
                wins = not self.canWin(s)
                s[i] = s[i+1] = "+"
                if wins:
                    return True
        return False