class Solution(object):
    def multiply(self, A, B):
        mA, nA, nB = len(A), len(A[0]), len(B[0])
        res = [[0] * len(B[0]) for _ in range(mA)]
        for i in range(mA):
            for j in range(nA):
                if A[i][j]:
                    for k in range(nB):
                        res[i][k] += A[i][j] * B[j][k]
        return res

A = [
  [ 1, 2, 3],
  [-1, 4, 3]
]

B = [
  [ 7, 1, 2 ],
  [ 1, 2, 3 ],
  [ 4, 2, 1 ]
]


ans = [[21,11,11],
       [9,13,13]]


test = Solution()
test.multiply(A, B)

# Another Solution

class Solution:
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        tmp = 0
        for i in range(len(A)):
            k = 0
            row_res = []
            for _ in range(len(B[0])):
                for j in range(len(A[0])):
                    tmp += A[i][j] * B[j][k]
                row_res.append(tmp)
                tmp = 0
                k += 1
            res.append(row_res)
        return res

