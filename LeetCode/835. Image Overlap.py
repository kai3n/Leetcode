class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        a = []
        b = []
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    a.append((i,j))
                if B[i][j] == 1:
                    b.append((i,j))
        res = 0
        d = collections.defaultdict(int)
        for d1 in a:
            for d2 in b:
                d3 = (d2[0]-d1[0], d2[1]-d1[1])
                d[d3] += 1
                res = max(res, d[d3])
        return res