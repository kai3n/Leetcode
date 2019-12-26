from collections import defaultdict
import bisect as bi


class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        count = 0
        for word in words:
            if self.isSubsequence(s, word):
                count += 1
        return count

    def isSubsequence(self, s, word):
        idx = defaultdict(list)
        for i, c in enumerate(s):
            idx[c].append(i)
        prev = 0
        for i, c in enumerate(word):
            j = bi.bisect_left(idx[c], prev)
            if j == len(idx[c]): return False
            prev = idx[c][j] + 1
        return True