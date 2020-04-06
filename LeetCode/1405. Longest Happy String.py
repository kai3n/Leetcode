class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        res = ""
        count = 0
        heap = []
        if a != 0:
            heapq.heappush(heap, (-a, "a"))
        if b != 0:
            heapq.heappush(heap, (-b, "b"))
        if c != 0:
            heapq.heappush(heap, (-c, "c"))

        while heap:
            if len(heap) == 1:
                num1, letter1 = heapq.heappop(heap)
                if num1 + 2 < 0:
                    res += letter1 + letter1
                    break
                res += letter1
            else:
                num1, letter1 = heapq.heappop(heap)
                num2, letter2 = heapq.heappop(heap)
                if num1 <= num2 - 1:
                    res += letter1 + letter1
                    if num1 + 2 < 0:
                        heapq.heappush(heap, (num1 + 2, letter1))
                    res += letter2
                    if num2 + 1 < 0:
                        heapq.heappush(heap, (num2 + 1, letter2))
                else:
                    res += letter1 + letter2
                    if num1 + 1 < 0:
                        heapq.heappush(heap, (num1 + 1, letter1))
                    if num2 + 1 < 0:
                        heapq.heappush(heap, (num2 + 1, letter2))
        return res


