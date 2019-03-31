class Solution(object):
    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """

        def check_boundary(A, i, j):
            if A[i][j] == 1:
                A[i][j] = 0
                for y, x in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    if 0 <= y + i < len(A) and 0 <= x + j < len(A[0]):
                        check_boundary(A, y + i, x + j)

        for i in range(len(A)):
            for j in range(len(A[0])):
                if i == 0 or j == 0 or i == len(A) - 1 or j == len(A[0]) - 1:
                    check_boundary(A, i, j)
        count = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]:
                    count += 1
        return count
