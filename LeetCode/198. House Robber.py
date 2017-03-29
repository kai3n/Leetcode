class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            opt = [-1] * len(nums)
            opt[0] = nums[0]
            for i in range(1, len(nums)):
                if i-2 >= 0:
                    opt[i] = max(opt[i-2] + nums[i], opt[i-1])
                else:
                    opt[i] = max(nums[0], nums[1])
            return opt[len(nums)-1]
        else:
            return 0

testcase = [1,5,1,3,6,2,8]
testcase = []
#testcase = [1]
test = Solution()
print(test.rob(testcase))  # must be 19.