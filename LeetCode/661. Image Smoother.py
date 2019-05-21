class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        new_matrix = [[0 for j in range(len(M[0]))] for i in range(len(M))]

        for i in range(len(M)):
            for j in range(len(M[0])):
                count = 0
                one_count = 0
                for dx in range(-1, 1 + 1):
                    for dy in range(-1, 1 + 1):
                        if 0 <= i + dx < len(M) and 0 <= j + dy < len(M[0]):
                            one_count += M[i + dx][j + dy]
                            count += 1
                new_matrix[i][j] = int(float(one_count) / float(count))
        return new_matrix