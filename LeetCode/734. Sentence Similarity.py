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






"""
from collections import defaultdict
class Solution(object):
    def areSentencesSimilarTwo(self,words1,words2,pairs):
        if len(words1)!=len(words2): return False

        connections=defaultdict(set)
        for w1,w2 in pairs:
            connections[w1].add(w2)
            connections[w2].add(w1)

        roots={}
        def dfs(word,root_word):
            if word in roots: return None
            roots[word]=root_word
            for connectedWord in connections[word]:
                dfs(connectedWord,root_word)

        for word in connections: dfs(word,word)

        for w1,w2 in zip(words1,words2):
            if roots.get(w1,w1)!=roots.get(w2,w2):
                return False
        return True

"""