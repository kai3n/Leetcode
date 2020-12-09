class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        res = 0
        for num in nums:
            if k - num in d:
                d[k - num] -= 1
                if d[k - num] == 0:
                    del d[k - num]
                res += 1
            else:
                d[num] += 1
        return res
