# Time limit Soluton
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
