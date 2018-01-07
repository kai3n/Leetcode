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

# another solution
def shortestWordDistance(self, words, word1, word2):
    """
    :type words: List[str]
    :type word1: str
    :type word2: str
    :rtype: int
    """
    p1, p2 = -1, -1
    dis = float("inf")
    flip = True
    for i,w in enumerate(words):
        if w==word1 and flip:
            if word1==word2: flip = False
            p1 = i
        elif w==word2:
            if word1==word2: flip = True
            p2 = i
        if p1!=-1 and p2!=-1:
            dis = min(dis, abs(p1-p2))
    return dis
