class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        for i in range(len(nums)):
            if d.get(target-nums[i]) is not None:
                return [d.get(target-nums[i]), i]
            else:
                d[nums[i]] = i