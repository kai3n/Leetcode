class Solution(object):
    def sumOfDigits(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return 0 if sum(map(int, list(str(min(A))))) % 2 else 1