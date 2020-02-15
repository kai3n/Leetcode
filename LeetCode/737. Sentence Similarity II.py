class Solution:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False

        from collections import defaultdict

        d = defaultdict(set)
        for pair in pairs:
            d[pair[0]].add(pair[1])
            d[pair[1]].add(pair[0])

        g = {}

        def dfs(n, r):
            for nn in d[n]:
                if nn not in g.keys():
                    g[nn] = r
                    dfs(nn, r)

        for n in d.keys():
            if n not in g.keys():
                g[n] = n
                dfs(n, n)

        for i, j in zip(words1, words2):
            if g.get(i, i) != g.get(j, j):
                return False
        return True


class Solution:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        if len(words1) != len(words2):
            return False
        graph = collections.defaultdict(list)
        for w1, w2 in pairs:
            graph[w1].append(w2)
            graph[w2].append(w1)

        for w1, w2 in zip(words1, words2):
            stack, seen = [w1], {w1}
            while stack:
                word = stack.pop()
                if word == w2:
                    break
                for nei in graph[word]:
                    if nei not in seen:
                        seen.add(nei)
                        stack.append(nei)
            else:
                return False
        return True