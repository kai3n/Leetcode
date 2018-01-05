class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        m = 0
        left = -1
        for j in range(len(s)):
            if s[j] == "(":
                stack.append(j)
            else:
                if not stack:
                    left = j
                else:
                    stack.pop()
                    if not stack:
                        m = max(m, j - left)
                    else:
                        m = max(m, j - stack[-1])
        return m