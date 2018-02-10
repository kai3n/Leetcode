# TLE

class Solution:
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def helper(s, left, right):
            if right > left:
                return False
            if left == right and not s:
                return True
            elif left != right and not s:
                return False
            else:
                if s[0] == '*':
                    return helper(s[1:], left, right) or helper(s[1:], left + 1, right) or helper(s[1:], left,
                                                                                                  right + 1)
                elif s[0] == '(':
                    return helper(s[1:], left + 1, right)
                elif s[0] == ')':
                    return helper(s[1:], left, right + 1)
                else:
                    return False

        return helper(s, 0, 0)

# O(n)

class Solution:
    def checkValidString(self, s):
        cmin = cmax = 0
        for i in s:
            if i == '(':
                cmax += 1
                cmin += 1
            if i == ')':
                cmax -= 1
                cmin = max(cmin - 1, 0)
            if i == '*':
                cmax += 1
                cmin = max(cmin - 1, 0)
            if cmax < 0:
                return False
        return cmin == 0
