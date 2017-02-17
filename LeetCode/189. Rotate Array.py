class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        cur = len(nums) - k % len(nums)
        nums[:] = nums[cur:] + nums[:cur]


test = Solution()
print(test.rotate([10,1,2,3,4,5,6,7,9,4,5],3))
