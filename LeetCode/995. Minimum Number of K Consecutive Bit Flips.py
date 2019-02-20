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

class Solution(object):
    def minKBitFlips(self, A, K):
        N = len(A)
        hint = [0] * N
        ans = flip = 0

        for i, x in enumerate(A):
            flip ^= hint[i]
            if x ^ flip == 0:
                ans += 1
                if i + K > N:
                    return -1
                flip ^= 1
                if i + K < N:
                    hint[i + K] = 1
        return ans