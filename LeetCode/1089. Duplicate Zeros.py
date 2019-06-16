class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        queue = []
        for i in range(len(arr)):
            if arr[i] == 0:
                if queue:
                    arr[i] = queue.pop(0)
                    queue.append(0)
                queue.append(0)
            else:
                if queue:
                    queue.append(arr[i])
                    arr[i] = queue.pop(0)
        print(arr)