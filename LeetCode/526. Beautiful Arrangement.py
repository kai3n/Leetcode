cnt = 0
class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        available = [True] * (N + 1)

        def dfs(N, available, pos):
            global cnt
            if pos > N:
                cnt += 1

            for i in range(1, N+1):
                if available[i] and (pos % i == 0 or i % pos == 0):
                    available[i] = False
                    dfs(N,available, pos+1)
                    available[i] = True
        dfs(N,available,1)
        return cnt

test = Solution()
print(test.countArrangement(1))
print(test.countArrangement(10))

'''
def countArrangement(self, N):
    return (1, 2, 3, 8, 10, 36, 41, 132, 250, 700, 750, 4010, 4237, 10680, 24679)[N - 1]
'''