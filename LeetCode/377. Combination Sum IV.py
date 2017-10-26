class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = [0] * (target + 1)
        res[0] = 1
        for i in range(1, target+1):
            for x in nums:
                if i >= x:
                    res[i] += res[i-x]
        return res[target]

test = Solution()
test.combinationSum4([1,2,3],4)