class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False

        min_step1 = nums[0]
        min_step2 = float('inf')

        for i in range(1, len(nums)):
            if nums[i] > min_step1:
                if nums[i] > min_step2:
                    return True
                min_step2 = nums[i]
            else:
                min_step1 = nums[i]
        return False
