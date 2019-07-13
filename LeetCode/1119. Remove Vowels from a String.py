class Solution(object):
    def removeVowels(self, S):
        """
        :type S: str
        :rtype: str
        """
        S = S.replace('a','')
        S = S.replace('e','')
        S = S.replace('i','')
        S = S.replace('o','')
        S = S.replace('u','')
        return S