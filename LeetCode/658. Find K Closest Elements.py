class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        first = 0
        last = len(arr) - k
        while first < last:
            mid = (first+last)//2
            if x-arr[mid] > arr[mid+k]-x:
                first = mid + 1
            else:
                last = mid
        return arr[first:first+k]


"""
    return sorted(sorted(arr, key=lambda val: abs(val - x))[:k])
"""
