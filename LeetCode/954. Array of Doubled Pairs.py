class Solution(object):
    def canReorderDoubled(self, A):
        import collections
        count = collections.Counter(A)
        print(sorted(A, key = abs))
        for x in sorted(A, key = abs):
            if count[x] == 0: continue
            if count[2*x] == 0: return False
            count[x] -= 1
            count[2*x] -= 1
        return True

solution = Solution()
print(solution.canReorderDoubled([-2,4,2,-4]))