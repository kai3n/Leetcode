class Solution(object):
    def transformArray(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        is_changed = True
        arr2 = arr[:]

        while is_changed:
            is_changed = False
            for i in range(1, len(arr) - 1):
                if arr[i - 1] > arr[i] and arr[i + 1] > arr[i]:
                    arr2[i] = arr[i] + 1
                    is_changed = True
                elif arr[i - 1] < arr[i] and arr[i + 1] < arr[i]:
                    arr2[i] = arr[i] - 1
                    is_changed = True
            arr = arr2[:]
        return arr