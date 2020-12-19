class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        sub_total = 0
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(total - nums[i]*len(nums))
            else:
                l_sum = i*nums[i] - sub_total
                r_sum = (total - sub_total - nums[i]) - nums[i]*(len(nums) - i - 1)
                res.append(l_sum + r_sum)
            sub_total += nums[i]
        return res
