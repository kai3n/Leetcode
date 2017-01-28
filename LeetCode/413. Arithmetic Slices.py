class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        cnt = 0
        sum = 0
        for i in range(len(A)-2):
            if A[i+1] - A[i] == A[i+2] - A[i+1]:
                cnt += 1
                sum += cnt
            else:
                cnt = 0
        return sum



A = [3, -1, -5, -9]
test = Solution()
print(test.numberOfArithmeticSlices(A))