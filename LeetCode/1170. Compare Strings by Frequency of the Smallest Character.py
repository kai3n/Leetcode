class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        words_score = [word.count(min(word)) for word in words]
        queries_score = [word.count(min(word)) for word in queries]
        answer = [sum(q < w for w in words_score) for q in queries_score]

        return answer

        # f = sorted(w.count(min(w)) for w in words)
        # return [len(f) - bisect.bisect(f, q.count(min(q))) for q in queries]