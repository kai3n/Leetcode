class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False
        if num == 1:
            return False
        import math
        dividers = [1]
        for i in range(1, int(math.ceil(math.sqrt(num)))):
            if num % i == 0 and num != num // i:
                dividers.append(i)
                dividers.append(num // i)

        if sum(dividers) == num:
            return True
        return False

input = 28
test = Solution()
print(test.checkPerfectNumber(input))