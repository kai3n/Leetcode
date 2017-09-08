# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(nums):
            if not nums:
                return None
            if len(nums) == 1:
                return TreeNode(nums[0])
            first = 0
            last = len(nums)-1
            mid = (first + last) // 2
            root = TreeNode(nums[mid])
            root.left = helper(nums[first:mid])
            root.right = helper(nums[mid+1:last+1])
            return root
        return helper(nums)

test = Solution()
test.sortedArrayToBST([1,2,3,4,5,6,7,8])

# another person's solution
class Solution:
    # @param num, a list of integers
    # @return a tree node
    # 12:37
    def sortedArrayToBST(self, num):
        if not num:
            return None

        mid = len(num) // 2

        root = TreeNode(num[mid])
        root.left = self.sortedArrayToBST(num[:mid])
        root.right = self.sortedArrayToBST(num[mid+1:])

        return root

