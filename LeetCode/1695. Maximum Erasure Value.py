class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s = set()
        max_score = 0
        cur_score = 0
        l = r = 0
        
        while l < len(nums) and r < len(nums):
            if nums[r] not in s:
                s.add(nums[r])
                cur_score += nums[r]
                max_score = max(max_score, cur_score)
                r += 1
            else:
                while nums[l] != nums[r]:
                    s.remove(nums[l])
                    cur_score -= nums[l]
                    l += 1
                s.remove(nums[l])
                cur_score -= nums[l]
                l += 1
        return max_score
