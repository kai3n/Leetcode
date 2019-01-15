class Solution(object):
    def maxWidthRamp(self, A):
        ans = 0
        m = float('inf')
        for i in sorted(range(len(A)), key = A.__getitem__):
            print(i)
            ans = max(ans, i - m)
            m = min(m, i)
        return ans

solution = Solution()
print(solution.maxWidthRamp([6,0,8,2,1,5]))
