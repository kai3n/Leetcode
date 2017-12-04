class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        if words1 == words2:
            return True

        for w1, w2 in zip(words1, words2):
            if w1 == w2 or [w1, w2] in pairs or [w2, w1] in pairs:
                continue
            else:
                return False
        return True




