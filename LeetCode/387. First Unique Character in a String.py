class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        sDic = dict()

        for i in s:
            if sDic.get(i) == None:
                sDic[i] = 1
            else:
                sDic[i] += 1

        for i, letter in enumerate(s):
            if sDic[letter] == 1:
                return i
        return -1

