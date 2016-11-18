class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False

        numDict = dict()

        for i in nums:
            if numDict.get(i,0) == 0:
                numDict[i] = 1
            else:
                numDict[i] += 1

        for i in numDict.keys():
            if numDict[i] > 1:
                return True
        return False

test = Solution()
print(test.containsDuplicate([2,2]))


"""
class Solution(object):
def containsDuplicate(self, nums):
    '''
    :type nums: List[int]
    :rtype: bool
    '''
    return len(nums) != len(set(nums))
"""
