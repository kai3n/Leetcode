class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        res = []
        even_sum = 0
        for i in range(len(A)):
            if A[i] & 1 == 0:
                even_sum += A[i]
        for i in range(len(queries)):
            # -2 -1 3 4 .. 8 6
            tmp = A[queries[i][1]]
            A[queries[i][1]] += queries[i][0]
            if A[queries[i][1]] & 1 == 0:
                if tmp & 1:
                    even_sum = even_sum + A[queries[i][1]]
                else:
                    even_sum = even_sum + queries[i][0]
            else:
                if tmp & 1 == 0:
                    even_sum = even_sum - tmp
            res.append(even_sum)
        return res
