class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        import math
        times = math.ceil(float(len(B)) / float(len(A)))
        for i in range(2):
          if B in (A * (times + i)):
            return times + i
        return -1

