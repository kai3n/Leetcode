class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        from collections import Counter
        C = A + B
        c = Counter(C)
        max_val = 0
        max_key = 0
        for k, v in c.items():
            if max_val < v:
                max_val = v
                max_key = k
        for i in range(len(A)):
            if A[i] == max_key or B[i] == max_key:
                continue
            else:
                return -1
        res = 0
        res2 = 0
        for i in range(len(A)):
            if A[i] != max_key:
                res += 1
            if B[i] != max_key:
                res2 += 1
        return min(res, res2)