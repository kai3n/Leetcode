def dfs2(board, visited_list, node):
    stack = [node]
    visited_list[node] = 1
    while stack:
        n = stack.pop()
        for i in range(len(board[n])):
            if i != n and board[n][i] == 1 and visited_list[i] == 0:
                visited_list[i] = 1
                stack.append(i)

def dfs(board, visited_list, node):
    if visited_list[node] == 0:
        visited_list[node] = 1
        for i in range(len(board[node])):
            if i != node and board[node][i] == 1 and visited_list[i] == 0:
                dfs(board, visited_list, i)

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if len(M) == 1:
            return 1
        visited_list = [0] * len(M)
        count = 0
        for i in range(len(visited_list)):
            if visited_list[i] == 1:
                continue
            dfs(M, visited_list, i)
            count += 1
        return count



M = [[1,1,0],
     [1,1,0],
     [0,0,1]]


test = Solution()
print(test.findCircleNum(M))
