class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        "1 1 2 2 3 7"
        if not A:
            return 0

        A.sort()
        d = {}
        res = 0
        cur_num = A[0]  # 1
        d[A[0]] = 1
        for i in range(1, len(A)):
            if cur_num < A[i]:
                cur_num = A[i]
            else:
                c = 1 if cur_num == A[i] else cur_num - A[i]
                while d.get(A[i] + c):
                    c += 1
                res += c
                d[A[i] + c] = 1
                cur_num = A[i] + c

        return res