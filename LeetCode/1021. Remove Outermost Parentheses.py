class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return ""
        i = 0
        count = 0
        is_outer = True
        res = ""
        while i < len(S):
            if is_outer:
                i += 1
                is_outer = False
            else:
                if S[i] == "(":
                    res += "("
                    count += 1
                else:
                    count -= 1
                    if count < 0:
                        is_outer = True
                        count = 0
                        i += 1
                        continue
                    res += ")"
                i += 1
        return res

