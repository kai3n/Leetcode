class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def helper(start, target):
            if target < 0:
                return
            elif target == 0:
                return True
            else:
                for i in range(start, len(nums)):
                    if helper(i + 1, target - nums[i]):
                        return True
                return False

        return False if sum(nums) % 2 else helper(0, sum(nums) / 2)
