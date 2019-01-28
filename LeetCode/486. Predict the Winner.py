from collections import defaultdict


class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def winner(nums, s, e, memo):
            if s == e:
                return nums[s]
            if memo[s][e]:
                return memo[s][e]
            a = nums[s] - winner(nums, s + 1, e, memo)
            b = nums[e] - winner(nums, s, e - 1, memo)
            memo[s][e] = max(a, b)
            return memo[s][e]

        memo = defaultdict(lambda: defaultdict(int))
        return winner(nums, 0, len(nums) - 1, memo) >= 0