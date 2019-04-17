class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd_list = [x for x in A if x % 2 == 1]
        even_list = [x for x in A if x % 2 == 0]
        A[::2] = even_list
        A[1::2] = odd_list
        return A