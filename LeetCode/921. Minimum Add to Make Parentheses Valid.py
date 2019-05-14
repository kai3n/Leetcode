class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        need = 0
        stack = []
        for i in range(len(S)):
            if S[i] == "(":
                stack.append(S[i])
            else:
                if stack:
                    stack.pop()
                else:
                    need += 1
        need += len(stack)
        return need