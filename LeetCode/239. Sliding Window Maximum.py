class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        if not nums:
            return res

        for i in range(len(nums) - k + 1):
            res.append(max(nums[i:i + k]))
        return res

# So difficult to come up with this idea...
def maxSlidingWindow(nums, k):
    from collections import deque
    d = deque()
    out = []
    for i, n in enumerate(nums):
        while d and nums[d[-1]] < n:
            d.pop()
        d += i,
        if d[0] == i - k:
            d.popleft()
        if i >= k - 1:
            out += nums[d[0]],
    return out

nums = [1,3,-1,-3,5,3,6,7]
k = 3

print(maxSlidingWindow(nums, k))