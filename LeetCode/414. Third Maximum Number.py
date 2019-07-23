class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = []
        for i in range(len(nums)):
            if len(l) >= 3:
                break
            if nums[i] in l:
                continue
            l.append(nums[i])
        l.sort()
        if len(l) < 3:
            return max(l)
        for i in range(2, len(nums)):
            if nums[i] in l or nums[i] < l[0]:
                continue
            elif l[0] < nums[i] < l[1]:
                l = [nums[i], l[1], l[2]]
            elif l[1] < nums[i] < l[2]:
                l = [l[1], nums[i], l[2]]
            else:
                l = [l[1], l[2], nums[i]]
        return l[0]
                
                
