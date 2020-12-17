class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        res = 0
        def helper(mat, i, j):
            bound = len(mat[0])
            count = 0
            for y in range(i, len(mat)):
                for x in range(j, bound):
                    if mat[y][x]:
                        count += 1
                    else:
                        bound = x
                        break
            return count

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                res += helper(mat, i, j)
        return res
