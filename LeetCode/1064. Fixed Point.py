class Solution(object):
    def fixedPoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in range(len(A)):
            if A[i] == i:
                return i
        return -1


class Solution(object):
    def fixedPoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left = 0
        right = len(A) - 1

        while left <= right:
            mid = (left + right) / 2
            if A[mid] == mid:
                return mid
            elif A[mid] > mid:
                right = mid - 1
            else:
                left = mid + 1
        return -1