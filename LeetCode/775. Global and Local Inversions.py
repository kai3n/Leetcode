# TLE
class Solution:
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        g_num = 0
        l_num = 0

        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if A[i] > A[j]:
                    g_num += 1

        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                l_num += 1

        return g_num == l_num


# AC

class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        for i in range(len(A)):
            if abs(A[i] - i) >= 2: return False
        return True