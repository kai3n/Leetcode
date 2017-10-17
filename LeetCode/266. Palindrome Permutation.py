class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        from collections import defaultdict

        d = defaultdict(int)
        for i in s:
            d[i] += 1
        c = 0
        for k, v in d.items():
            if v % 2:
                c += 1
        if c > 1:
            return False
        return True




# a = "code"  # False
# b = "aab"  # True
# c = "carerac" # True
#
# test = Solution()
# print(test.canPermutePalindrome(a))
# print(test.canPermutePalindrome(b))
# print(test.canPermutePalindrome(c))


