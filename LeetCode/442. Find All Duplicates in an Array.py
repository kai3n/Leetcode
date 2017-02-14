class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = dict()
        ret = list()
        for i in nums:
            if d.get(i,0) == 0:
                d[i] = 1
            else:
                d[i] += 1

        for k, v in d.items():
            if v == 2:
                ret.append(k)
        return ret