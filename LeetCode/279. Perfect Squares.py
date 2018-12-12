class Solution(object):
    def numSquares(self, n):
        depth = 0
        queue = [[0, depth]]
        visited = [False] * (n + 1)
        while queue:
            node, d = queue.pop(0)
            i = 1
            while i*i + node <= n:
                if i*i + node == n:
                    return d+1
                if visited[i*i + node]:
                    continue
                queue.append([i*i + node, d+1])
                visited[i*i + node] = True
                i += 1

# memory
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        q1 = [0]
        q2 = []
        level = 0
        visited = [False] * (n + 1)
        while True:
            level += 1
            for v in q1:
                i = 0
                while True:
                    i += 1
                    t = v + i * i
                    print(t, level)
                    if t == n: return level
                    if t > n: break
                    if visited[t]: continue
                    q2.append(t)
                    visited[t] = True
            q1 = q2
            q2 = []

        return 0


test = Solution()
print(test.numSquares(10000))
print(test.numSquares(1000625))

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            cur_min = float('inf')
            j = 1
            while i - j*j >= 0:
                cur_min = min(cur_min, dp[i-j*j]+1)
                j += 1
            dp[i] = cur_min
        return dp[n]