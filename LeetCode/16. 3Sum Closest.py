class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        closest = float("inf")
        res = 0
        nums.sort()
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            while left < right:
                if abs(nums[i] + nums[left] + nums[right] - target) < closest:
                    closest = abs(nums[i] + nums[left] + nums[right] - target)
                    res = nums[i] + nums[left] + nums[right]
                if nums[i] + nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        return res