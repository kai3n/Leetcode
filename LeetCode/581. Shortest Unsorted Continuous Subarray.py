class Solution(object):
    def findUnsortedSubarray(self, A):
        B = sorted(A)
        if A == B: return 0
        for i in range(len(A)):
            if A[i] != B[i]: break
        for j in range(len(A) - 1, -1, -1):
            if A[j] != B[j]: break
        return j - i + 1




input = [2, 6, 4, 8, 10, 9, 15]
input2 = [1, 2, 3, 4]
input3 = [1, 3, 2, 2, 2]
input4 = [1, 2, 3, 3, 3]
input5 = [1,3,2,3,3]
input5 = [1,2,3,5,4]

test = Solution()
print(test.findUnsortedSubarray(input))
print(test.findUnsortedSubarray(input2))
print(test.findUnsortedSubarray(input3))
print(test.findUnsortedSubarray(input4))
print(test.findUnsortedSubarray(input5))