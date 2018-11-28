class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        return self.findKth(A, B, l // 2) if l % 2 == 1 else (self.findKth(A, B, l // 2 - 1) + self.findKth(A, B,
                                                                                                            l // 2)) / 2.0

    def findKth(self, A, B, k):
        if len(A) > len(B):
            A, B = B, A
        if not A:
            return B[k]
        if k == len(A) + len(B) - 1:
            return max(A[-1], B[-1])
        i = len(A) // 2
        j = k - i
        if A[i] > B[j]:
            # Here I assume it is O(1) to get A[:i] and B[j:]. In python, it's not but in cpp it is.
            print("A[:i]",A[:i])
            print("B[j:]", B[j:])
            print("i",i)
            print("j", j)
            print()
            return self.findKth(A[:i], B[j:], i)
        else:
            return self.findKth(A[i:], B[:j], j)


a = [1,2,12,13,14]
b = [3,4,5,6,7,8,9]

s = Solution()
print(s.findMedianSortedArrays(a, b))