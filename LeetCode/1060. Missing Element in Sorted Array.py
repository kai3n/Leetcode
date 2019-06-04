class Solution:
    def missingElement(self, nums, k):
        missCount = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1] + 1:
                missCountPre = missCount
                missCount += nums[i] - nums[i - 1] - 1
                if missCount >= k:
                    return nums[i - 1] + (k - missCountPre)
        return nums[-1] + (k - missCount)