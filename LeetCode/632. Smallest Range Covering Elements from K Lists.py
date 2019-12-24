import heapq


class Solution:
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        heap = [(List[0], index, 0) for index, List in
                enumerate(nums)]  # First element of each list with list number and index of the element in each list
        heapq.heapify(heap)  # to get the min value from all the elements of each list

        max_val = max([List[0] for List in nums])  # To get the max value for the range
        smallest_range = -1e9, 1e9  # max and min for the range

        while heap:
            min_val, list_index, num_index = heapq.heappop(
                heap)  # get the min value, the list its from and the index it is at in the particular list

            if max_val - min_val < smallest_range[1] - smallest_range[
                0]:  # To find the smallest difference which will be the range
                smallest_range = min_val, max_val

            if num_index + 1 == len(nums[list_index]):  # once any one of the list is exhausted, return the range
                return smallest_range

            next_num = nums[list_index][num_index + 1]  # To get the next element from the list that has the min value

            max_val = max(max_val, next_num)
            heapq.heappush(heap, (next_num, list_index, num_index + 1))