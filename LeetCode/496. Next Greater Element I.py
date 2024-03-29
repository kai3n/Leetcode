class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = [-1]*len(nums1)
        for i in range(len(nums1)):
            target_index = nums2.index(nums1[i])
            for j in range(target_index+1, len(nums2)):
                if nums2[j] > nums1[i]:
                    res[i] = nums2[j]
                    break
        return res


class Solution:
    def nextGreaterElement(self, findNums, nums):
        st, d = [], {}
        for n in nums:
            while st and st[-1] < n:
                d[st.pop()] = n
            st.append(n)

        return [d.get(x, -1) for x in findNums]