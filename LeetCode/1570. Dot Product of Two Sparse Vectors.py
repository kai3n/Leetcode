class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.idx_set = set()
        for i in range(len(nums)):
            if nums[i]:
                self.idx_set.add(i)
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        res = 0
        for i in self.idx_set.intersection(vec.idx_set):
            res += self.nums[i]*vec.nums[i]
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
