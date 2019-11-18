class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        def helper(s1, s2, s3):
            if not s1 and not s2 and not s3:
                return True
            elif not s1:
                if s2 == s3:
                    return True
            elif not s2:
                if s1 == s3:
                    return True
            elif s1[0] == s2[0] == s3[0]:
                return helper(s1[1:], s2, s3[1:]) or helper(s1, s2[1:], s3[1:])
            elif s1[0] == s3[0]:
                return helper(s1[1:], s2, s3[1:])
            elif s2[0] == s3[0]:
                return helper(s1, s2[1:], s3[1:])
            else:
                return False

        return helper(s1, s2, s3)


