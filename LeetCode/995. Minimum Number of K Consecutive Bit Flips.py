# Brute Force
class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        def flip(A, start, K):
            for i in range(start, start+K):
                if A[i] == 0:
                    A[i] = 1
                else:
                    A[i] = 0
        i = 0
        count = 0
        while i+K-1 < len(A):
            if A[i] == 0:
                if i+K-1 < len(A):
                    flip(A, i, K)
                    count += 1
            i += 1
        print(A)
        for i in range(len(A)-K, len(A)):
            if A[i] == 0:
                return -1
        return count