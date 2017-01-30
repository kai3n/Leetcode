class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        N = S.replace('-','').upper()
        R = ""
        C = 0
        i = len(N)-1
        while i != -1:
            if C == K:
                R += "-"
                C = 0
                continue
            C += 1
            R += N[i]
            i -= 1
        return R[::-1]


test = Solution()
print(test.licenseKeyFormatting("2-4A0r7-4k",3))
print(test.licenseKeyFormatting("2-4A0r7-4k",4))