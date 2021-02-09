class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(a for a, c in Counter(nums).items() if c == 1)
