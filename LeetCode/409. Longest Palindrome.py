class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        flag = 0
        sum = 0
        for ele, cnt in Counter(s).items():
            if cnt % 2 == 1 and cnt > 1:
                flag = 1
                sum += cnt-1
            elif cnt % 2 == 1:
                flag = 1
            else:
                sum += cnt
        return sum + flag


test = Solution()
print(test.longestPalindrome('abccccdd'))