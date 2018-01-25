class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        from collections import defaultdict
        hashtable = defaultdict(int)
        count = 0

        for a in A:
            for b in B:
                hashtable[a + b] += 1
        for c in C:
            for d in D:
                count += hashtable[-c - d]
        return count