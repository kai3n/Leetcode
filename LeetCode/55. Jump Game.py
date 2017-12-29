class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if 0 not in nums:
            return True
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False

        for i in range(1, len(nums)):
            if nums[i] == 0:
                j = i - 1
                f = False
                if i == len(nums) - 1:
                    while j >= 0:
                        if (i - j) - nums[j] <= 0:
                            f = True
                            break
                        j -= 1
                else:
                    while j >= 0:
                        if (i - j) - nums[j] < 0:
                            f = True
                            break
                        j -= 1
                if not f:
                    return False

        return True
