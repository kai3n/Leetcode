class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [0 for _ in range(n+1)]
        G[0] = G[1] = 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]
        return G[n]

import math
# Catalan Number  (2n)!/((n+1)!*n!)

def numTrees(self, n):
    return math.factorial(2*n)/(math.factorial(n)*math.factorial(n+1))
