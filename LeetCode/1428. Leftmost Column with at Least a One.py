# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        res = float('inf')
        rows, cols = binaryMatrix.dimensions()
        for i in range(rows):
            l = 0
            r = cols
            while l < r:
                m = (l + r) // 2
                if binaryMatrix.get(i, m):
                    res = min(res, m)
                    r = m
                else:
                    l = m + 1
        return res if res != float('inf') else -1
