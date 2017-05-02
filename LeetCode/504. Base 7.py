class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        isNegative = False
        r = ""
        if num < 0:
            isNegative = True
            num = abs(num)
        if num == 0:
            return "0"

        while num != 0:
            r += str(num % 7)
            num -= num % 7
            num //= 7
        return r[::-1] if isNegative is False else "-" + r[::-1]

test = Solution()
print(test.convertToBase7(100))
print(test.convertToBase7(98))
print(test.convertToBase7(-7))
print(test.convertToBase7(0))

"""
def convertTo7(self, num):
    if num < 0: return '-' + self.convertTo7(-num)
    if num < 7: return str(num)
    return self.convertTo7(num // 7) + str(num % 7)
"""
