class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.res = 0
        def helper(nums, prev):
            for i in range(len(nums)):
                xor_val = nums[i] ^ prev
                self.res += xor_val
                helper(nums[i+1:], xor_val)
        helper(nums, 0)
        return self.res