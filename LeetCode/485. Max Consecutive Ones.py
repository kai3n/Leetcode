class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxVal = 0
        i = 0
        begin = 0
        end = 0
        nums.append(0)

        while i < len(nums):
            if nums[i] == 1:
                begin = i
                while nums[i] == 1:
                    i += 1
                end = i
                if end - begin > maxVal:
                    maxVal = end - begin
            i += 1
        return maxVal

test = Solution()
print(test.findMaxConsecutiveOnes([1,1,0,1,1,1]))

#another solution
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        cnt = 0
        ans = 0
        for num in nums:
            if num == 1:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 0
        return ans




