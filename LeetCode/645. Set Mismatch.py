class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        for num in nums:
            if d.get(num) is None:
                d[num] = 1
            else:
                d[num] += 1

        twice = -1
        missing = -1
        for i in range(1, len(nums) + 1):
            if d.get(i) is None:
                missing = i
            else:
                if d.get(i) == 2:
                    twice = i
        return [twice, missing]
