class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        pq = []
        for num in nums:
            heapq.heappush(pq, -num * 2 if num % 2 else -num)
        res = float('inf')
        min_val = -max(pq)
        while len(pq) == len(nums):
            num = -heapq.heappop(pq)
            res = min(res, num - min_val)
            if num % 2 == 0:
                min_val = min(min_val, num // 2)
                heapq.heappush(pq, -num // 2)
        return res
