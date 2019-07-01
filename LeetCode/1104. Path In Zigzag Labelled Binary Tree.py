class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        res = []
        while label != 1:
            res.append(label)
            label /= 2
        res.append(label)
        for i in range(len(res)):
            if i % 2:
                v = 2**(len(res)-1-i) + 2**(len(res)-1-i+1) - 1
                res[i] = v - res[i]
        return res[::-1]