class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        def helper(s, p):
            if s == "":
                res.append(p)
                return
            if s[0].isdigit():
                helper(s[1:], p+s[0])
            else:
                helper(s[1:], p+s[0].upper())
                helper(s[1:], p+s[0].lower())
        helper(S, "")
        return res