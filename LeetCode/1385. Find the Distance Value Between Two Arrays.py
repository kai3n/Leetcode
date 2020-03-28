class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        arr2.sort()
        def is_valid(val):
            l = 0
            r = len(arr2)-1
            while l <= r:
                mid = (l + r) // 2
                if abs(arr2[mid] - val) <= d or arr2[mid] == val:
                    return False
                elif arr2[mid] > val:
                    r = mid - 1
                else:
                    l = mid + 1
            return True
        return sum(is_valid(val) for val in arr1)