# Solution 1
class Solution:
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        d = {}
        for i in range(len(words)):
            if d.get(words[i], None) is None:
                d[words[i]] = [i]
            else:
                d[words[i]].append(i)

        res = float("inf")
        a = d[word1]
        b = d[word2]

        if a != b:
            for i in a:
                for j in b:
                    res = min(res, abs(j - i))
        else:
            for i in range(len(a)):
                for j in range(i + 1, len(a)):
                    res = min(res, abs(a[j] - a[i]))
        return res

