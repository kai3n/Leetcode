class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        b = bin(n)[2:]
        for i in range(1, len(b)):
            if not (int(b[i]) ^ int(b[i-1])):
                return False
        return True