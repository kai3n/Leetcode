#time limit code
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        l = len(nums)
        b = [bin(i)[2:].zfill(l) for i in range(2**l)]
        cnt = 0
        for a in b:
            sum = 0
            for i in range(l):
                if a[i] == "1":
                    sum += nums[i]
                else:
                    sum -= nums[i]
            if sum == S:
                cnt += 1
        return cnt





nums=[1, 1, 1, 1, 3]
S = 3
test = Solution()
print(test.findTargetSumWays(nums, S))
