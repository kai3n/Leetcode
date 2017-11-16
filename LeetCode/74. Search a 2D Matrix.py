class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        arr = []
        for i in range(len(matrix)):
            arr.append(matrix[i][0])

        def binary_search(arr, target):
            first = 0
            last = len(arr) - 1
            while first <= last:
                mid = (first + last) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] > target:
                    last = mid - 1
                else:
                    first = mid + 1
            return last

        row_idx = binary_search(arr, target)
        col_idx = binary_search(matrix[row_idx], target)

        return matrix[row_idx][col_idx] == target