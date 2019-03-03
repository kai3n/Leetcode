class Solution(object):
    def isValid(self, S):
        """
        :type S: str
        :rtype: bool
        """
        if len(S) < 3:
            return False

        stack = [S[0], S[1]]
        for i in range(2, len(S)):
            stack.append(S[i])
            if len(stack) >= 3 and stack[-3] == "a" and stack[-2] == "b" and stack[-1] == "c":
                stack.pop()
                stack.pop()
                stack.pop()

        return True if len(stack) == 0 else False