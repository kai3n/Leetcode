class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        res = 0
        arr2.sort()
        for i in range(len(arr1)):
            j = bisect.bisect_left(arr2, arr1[i])
            if j == len(arr2):
                if abs(arr1[i]-arr2[j-1]) > d:
                    res += 1
            elif arr1[i] == arr2[j]:
                continue
            elif j == 0 and abs(arr1[i]-arr2[j]) > d:
                res += 1
            elif abs(arr1[i]-arr2[j]) > d and j-1 >= 0 and abs(arr1[i]-arr2[j-1]) > d:
                res += 1
        return res