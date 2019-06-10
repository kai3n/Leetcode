class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        0 0 1 1 2 2
        0 1 2 3 4 5
        if n %2 == 0 n/2:

        """
        B = [[0 for _ in range(len(A))] for _ in range(len(A[0]))]
        count = 0
        for i in range(len(B)):
            for j in range(len(B[0])):
                B[i][j] = A[count % len(A)][count / len(A)]
                count += 1
        return B