class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        c = Counter(nums)
        l = [[key, val] for key, val in c.items()]
        heapq.heapify(l)
        while l:
            i = 0
            arr = []
            while i < k:
                if l:
                    arr.append(heapq.heappop(l))
                else:
                    return False
                i += 1
                
            if len(arr) != k:
                return False
                
            for j in range(1, len(arr)):
                if arr[j-1][0] + 1 != arr[j][0]:
                    return False
                
            for h in range(len(arr)):
                if arr[h][1] - 1 != 0:
                    heapq.heappush(l, [arr[h][0], arr[h][1]-1])
        return True
        
        
