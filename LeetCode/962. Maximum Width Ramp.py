class Solution(object):
    # def maxWidthRamp(self, A):
    #     ans = 0
    #     m = float('inf')
    #     for i in sorted(range(len(A)), key = A.__getitem__):
    #         print(i)
    #         ans = max(ans, i - m)
    #         m = min(m, i)
    #     return ans

    def maxWidthRamp(self, A):
        s = []
        res = 0
        for i, a in enumerate(A):
            if not s or A[s[-1]] > a:
                s.append(i)
        print(s)
        for j in range(len(A))[::-1]:
            while s and A[s[-1]] <= A[j]:
                res = max(res, j - s.pop())
        return res

solution = Solution()
print(solution.maxWidthRamp([6,0,8,2,1,5]))
