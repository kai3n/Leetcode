class Solution(object):
    def indexPairs(self, text, words):
        """
        :type text: str
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = []
        for word in words:
            try:
                cur_idx = 0
                while text.index(word, cur_idx) >= 0:
                    i = text.index(word, cur_idx)
                    res.append([i, i + len(word) - 1])
                    cur_idx = i + 1
            except:
                continue
        res.sort()
        return res
