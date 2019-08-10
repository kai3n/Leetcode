class Solution:
    def stoneGameII(self, piles):
        cache = {}
        n = len(piles)
        def cal(piles, M):
            p = str(len(piles)) + "-" + str(M)
            if p in cache:
                return cache[p]
            tot = sum(piles)
            if len(piles) <= 2*M: return tot
            num = tot
            for x in range(1, 2*M+1):
                num = min(num, cal(piles[x:], max(x, M)))
            ans = tot - num
            cache[p] = ans
            return ans
        return cal(piles, 1)