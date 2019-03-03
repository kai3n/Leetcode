class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        zero_list = []
        max_len = 0
        A = [0] + A + [0]
        K += 2
        for i in range(len(A)):
            if A[i] == 0:
                zero_list.append(i)
        for i in range(K-1, len(zero_list)):
            max_len = max(max_len, zero_list[i]-zero_list[i-K+1]+1)
        return max_len-2 if len(zero_list) >= K+2 else len(A)-2