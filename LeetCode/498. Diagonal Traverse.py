class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict
        result = []
        dd = defaultdict(list)
        if not matrix: return result

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                dd[i+j+1].append(matrix[i][j])

        for k, v in dd.iteritems():
            if k%2==1: dd[k].reverse()
            result += dd[k]
        return result