class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        s = list(map(str, s))
        for i in range(len(s)-1):
            if s[i] == "+" and s[i+1] == "+":
                s[i] = s[i + 1] = "-"
                res.append(''.join(s))
                s[i] = s[i + 1] = "+"
        return res

s = "++++"

test = Solution()
print(test.generatePossibleNextMoves(s))
"""
[
  "--++",
  "+--+",
  "++--"
]
"""