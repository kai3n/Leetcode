class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        for i in range(len(words)):
            if any(words[i] in word for word in words[:i] + words[i+1:]):
                res.append(words[i])
        return res