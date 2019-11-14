class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        count = 0
        res = 0
        d = {}
        for c in keyboard:
            d[c] = count
            count += 1
        res += d[word[0]]
        for i in range(1, len(word)):
            res += abs(d[word[i]]-d[word[i-1]])
        return res