class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        import heapq

        heap = []

        for stone in stones:
            heapq.heappush(heap, (-stone, stone))
        while len(heap) > 1:
            first_max = heapq.heappop(heap)[1]
            second_max = heapq.heappop(heap)[1]
            if first_max != second_max:
                heapq.heappush(heap, (second_max - first_max, first_max - second_max))
        return heap[0][1] if heap else 0