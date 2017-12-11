class Solution:
    def subarraySum(self, nums, k):
        sums = {0: 1}
        count = cur_sum = 0

        for n in nums:
            cur_sum += n
            count += sums.get(cur_sum - k, 0)
            sums[cur_sum] = sums.get(cur_sum, 0) + 1
        print(sums)
        return count