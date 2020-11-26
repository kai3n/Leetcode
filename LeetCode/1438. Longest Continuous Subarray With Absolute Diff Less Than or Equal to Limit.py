class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        min_deque = deque()
        max_deque = deque()
        l = r = ans = 0
        
        while r < len(nums):
            while min_deque and nums[min_deque[-1]] >= nums[r]:
                min_deque.pop()
            while max_deque and nums[max_deque[-1]] <= nums[r]:
                max_deque.pop()
                
            min_deque.append(r)
            max_deque.append(r)
            
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                l += 1
                if l > min_deque[0]:
                    min_deque.popleft()
                if l > max_deque[0]:
                    max_deque.popleft()
                    
            ans = max(ans, r - l + 1)
            r += 1
        return ans
