class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = -1
        c = Counter(arr)
        for k, v in c.items():
            if k == v and k > res:
                res = k
        return res