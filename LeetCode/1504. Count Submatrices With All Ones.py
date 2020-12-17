class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        res = 0
        for i in range(1, len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]:
                    mat[i][j] = mat[i - 1][j] + 1
        for i in range(len(mat)):
            res += self.helper(mat[i])
        return res
    
    def helper(self, row):
        total = [0] * len(row)
        stack = []
        for i in range(len(row)):
            while stack and row[stack[-1]] >= row[i]:
                stack.pop()
                
            if stack:
                pre_index = stack[-1]
                total[i] = total[pre_index]
                total[i] += row[i]*(i - pre_index)
            else:
                total[i] = row[i]*(i + 1)
            stack.append(i)
        return sum(total)
