class Solution(object):
    def mctFromLeafValues(self, arr: List[int]) -> int:
        self.memo = {}
        def dp(i,j):
            if j<=i:
                return 0
            if (i,j) not in self.memo:
                res = float('inf')
                for k in range(i+1,j+1):
                    res = min(dp(i,k-1)+dp(k,j)+max(arr[i:k])*max(arr[k:j+1]),res)
                self.memo[(i,j)] = res
            return self.memo[(i,j)]
        return dp(0,len(arr)-1)
