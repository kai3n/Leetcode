class Solution(object):
    def canPartition(self, nums):
        cache = set()
        def helper(start, target):
            if (start, target) in cache:
                return False
            if target < 0:
                return
            elif target == 0:
                return True
            else:
                for i in range(start, len(nums)):
                    if helper(i+1, target-nums[i]):
                        return True
                cache.add((start, target))
                return False

        return False if sum(nums)%2 else helper(0, sum(nums)/2)