from copy import deepcopy
from collections import deque
class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        flatten = []
        for x in mat:
            flatten.extend(x)
        stack = deque([(flatten,0)])
        visited = set(tuple(flatten))
        while stack:
            matrix,t = stack.popleft()
            if sum(matrix)==0:
                return t
            for i in range(m):
                for j in range(n):
                    temp = deepcopy(matrix)
                    for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1),(i,j)]:
                        if x>=0 and x<m and y>=0 and y<n:
                            temp[x*n+y] = 0 if temp[x*n+y] else 1
                    if tuple(temp) not in visited:
                        visited.add(tuple(temp))
                        stack.append((temp,t+1))
        return -1