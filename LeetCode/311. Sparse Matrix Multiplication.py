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