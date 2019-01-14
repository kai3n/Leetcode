class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """

        def dfs(N, K, L, num):
            if N == 0:
                L.append(num)
            else:
                for i in range(10):
                    if i == 0 and num == 0:
                        continue
                    elif i != 0 and num == 0:
                        dfs(N - 1, K, L, i)
                    else:
                        if abs(num % 10 - i) == K:
                            dfs(N - 1, K, L, num * 10 + i)

        l = []
        if N == 0:
            return [0]
        elif N == 1:
            l.append(0)
        dfs(N, K, l, 0)
        return l


