class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        A.sort()
        B.sort()
        a_sum = sum(A)
        b_sum = sum(B)
        diff = a_sum - b_sum

        def helper(v, diff, arr):
            start = 0
            last = len(arr) - 1
            while start <= last:
                mid = (start + last) / 2
                if v - arr[mid] == diff / 2:
                    return mid
                elif v - arr[mid] > diff / 2:
                    start = mid + 1
                else:
                    last = mid - 1
            return -1

        for i in range(len(A)):
            r = helper(A[i], diff, B)
            if r != -1:
                return [A[i], B[r]]


class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        dif = (sum(A) - sum(B)) / 2
        A = set(A)
        for b in set(B):
            if dif + b in A:
                return [dif + b, b]

