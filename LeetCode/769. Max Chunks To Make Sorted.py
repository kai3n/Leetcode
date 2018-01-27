class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if not arr:
            return 0

        sorted_arr = sorted(arr)
        idx_dict = dict()

        for i, v in enumerate(sorted_arr):
            idx_dict[v] = i

        pivot = idx_dict[arr[0]]
        count = 0

        for i in range(len(arr)):
            if i > pivot:
                count += 1
                pivot = idx_dict[arr[i]]
            if pivot < idx_dict[arr[i]]:
                pivot = idx_dict[arr[i]]
        count += 1
        return count
