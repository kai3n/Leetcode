# Time limit Solution 1
class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [i for i in range(1, n + 1)]
        permutations = []

        def helper(p):
            if len(p) == len(nums):
                permutations.append(p)
                return
            else:
                for i in nums:
                    if str(i) not in p:
                        helper(p + str(i))

        helper("")
        return permutations[k - 1]

# Time limit Solution 2

class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [str(i) for i in range(1, n + 1)]
        permutations = []

        def helper(p, n):
            if len(p) == 0:
                permutations.append(n)
                return
            else:
                for i in range(len(p)):
                    helper(p[:i] + p[i + 1:], n + p[i])

        helper(nums, "")
        return permutations[k - 1]

# AC
class Solution:
    def getPermutation(self, n, k):
        import math
        res, nums = "", [i for i in range(1, n + 1)]
        k -= 1
        while n:
            n -= 1
            index, k = divmod(k, math.factorial(n))
            res += str(nums.pop(index))
        return res
