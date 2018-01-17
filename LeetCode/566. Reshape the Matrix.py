class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        if len(nums) * len(nums[0]) != r * c:
            return nums

        res = [[0] * c for _ in range(r)]
        l = []
        k = 0
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                l.append(nums[i][j])
        for i in range(r):
            for j in range(c):
                res[i][j] = l[k]
                k += 1
        return res